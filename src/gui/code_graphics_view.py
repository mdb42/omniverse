from collections import deque
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPixmap, QImage, QCursor, QPainter, QPainterPath, QPen, QColor
from PyQt6.QtWidgets import QGraphicsScene, QStyleOptionGraphicsItem, QGraphicsRectItem, QGraphicsEllipseItem, QGraphicsLineItem, QGraphicsPathItem
from PyQt6.QtCore import Qt, QRectF, QLineF
import importlib.resources

# Constants
SCENE_RECT_MULTIPLE = 2
ZOOM_LIMIT = 5

class CodeGraphicsView(QtWidgets.QGraphicsView):
    present_mode = True
    draw_mode = False    
    code_mode = False

    animating = True
    undoAvailable = QtCore.pyqtSignal(bool)
    redoAvailable = QtCore.pyqtSignal(bool)
    processing_click = False

    def __init__(self, parent):
        super().__init__(parent)       
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)        
        self.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)    
        self.setMouseTracking(True)

        
        self.code_scene = QGraphicsScene()
        self.background_color = QColor(200, 200, 200, 0)
        self.code_scene.setBackgroundBrush(self.background_color)
        self.setScene(self.code_scene)
        self.reset_scene_rect()
        self.setViewportUpdateMode(QtWidgets.QGraphicsView.ViewportUpdateMode.FullViewportUpdate)

        
        # Go ahead and paint the background
        self.tool_color = QColor(0, 0, 0)        
        self.stroke_width = 1
        self.zoom = 0

        self.tool_index = 0
        self.tools = ["Pencil", "Eraser", "Line", "Ellipse", "Rectangle"]
        self.cursors = self.generate_tool_cursors(self.tools)

        self._mouse_press_start_pos = None
        self.last_mouse_pos = None        
        self.current_path = None
        self.current_path_item = None
        self.current_rect_item = None
        self.rect_start_point = None
        self.ellipse_start_point = None
        self.current_ellipse_item = None
        self.drawn_items = deque()
        self.undo_stack = deque()
        self.redo_stack = deque()    

    def generate_tool_cursors(self, tools):
        cursor_size = 18

        pencil_cursor_icon_data = importlib.resources.read_binary("resources.icons", "tool-pencil.ico")
        pencil_cursor_icon_image = QImage.fromData(pencil_cursor_icon_data).scaled(cursor_size, cursor_size, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        pencil_cursor = QCursor(QPixmap.fromImage(pencil_cursor_icon_image), 1, 17)

        eraser_cursor_icon_data = importlib.resources.read_binary("resources.icons", "tool-eraser.ico")
        eraser_cursor_icon_image = QImage.fromData(eraser_cursor_icon_data).scaled(cursor_size, cursor_size, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        eraser_cursor = QCursor(QPixmap.fromImage(eraser_cursor_icon_image), 8, 13)

        misc_cursor_icon_data = importlib.resources.read_binary("resources.icons", "tool-misc.ico")
        misc_cursor_icon_image = QImage.fromData(misc_cursor_icon_data).scaled(cursor_size, cursor_size, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        misc_cursor = QCursor(QPixmap.fromImage(misc_cursor_icon_image), 8, 8)

        cursors = []

        for tool in tools:
            if tool == "Pencil":
                cursors.append(pencil_cursor)
            elif tool == "Eraser":
                cursors.append(eraser_cursor)
            else:
                cursors.append(misc_cursor)            
        
        return cursors

        
    def mousePressEvent(self, event):
        if not self.processing_click:
            self.processing_click = True
            if self.draw_mode:
                self.drawModeMousePressEvent(event)
            else:
                self.presentationModeMousePressEvent(event)
    
    def mouseMoveEvent(self, event):
        if self.draw_mode:
            self.drawModeMouseMoveEvent(event)
        else:
            self.presentationModeMouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if self.draw_mode:
            self.drawModeMouseReleaseEvent(event)
        else:
            self.presentationModeMouseReleaseEvent(event)
        self.processing_click = False

    def drawModeMousePressEvent(self, event):
        self.setCursor(self.cursors[self.tool_index])

        if self.tools[self.tool_index] == "Pencil":
            if event.button() == QtCore.Qt.MouseButton.LeftButton:
                self.pencil_tool_action(event)
        elif self.tools[self.tool_index] == "Eraser":
            if event.button() == QtCore.Qt.MouseButton.LeftButton:
                self.eraser_tool_action(event)
        elif self.tools[self.tool_index] == "Rectangle":
            if event.button() == QtCore.Qt.MouseButton.LeftButton:
                self.rectangle_tool_action(event)
        elif self.tools[self.tool_index] == "Ellipse":
            if event.button() == QtCore.Qt.MouseButton.LeftButton:
                self.ellipse_tool_action(event)
        elif self.tools[self.tool_index] == "Line":
            if event.button() == QtCore.Qt.MouseButton.LeftButton:
                self.line_tool_action(event)

    def drawModeMouseMoveEvent(self, event):
        if self.tools[self.tool_index] == "Pencil" or self.tools[self.tool_index] == "Eraser" or self.tools[self.tool_index] == "A Plus":
            self.setCursor(self.cursors[self.tool_index])
        elif event.buttons() & QtCore.Qt.MouseButton.LeftButton:
            self.setCursor(self.cursors[self.tool_index])
        else:
            self.setCursor(Qt.CursorShape.ArrowCursor)

        if self.tools[self.tool_index] == "Pencil":
            if event.buttons() & QtCore.Qt.MouseButton.LeftButton and self.current_path and self.current_path_item:
                self.current_path.lineTo(self.mapToScene(event.pos()))
                self.current_path_item.setPath(self.current_path)
        elif self.tools[self.tool_index] == "Rectangle":
            if event.buttons() & QtCore.Qt.MouseButton.LeftButton and self.rect_start_point is not None:
                current_point = self.mapToScene(event.pos())
                rect = QRectF(self.rect_start_point, current_point)
                rect = rect.normalized()  
                self.current_rect_item.setRect(rect)
        elif self.tools[self.tool_index] == "Ellipse":
            if event.buttons() & QtCore.Qt.MouseButton.LeftButton and self.ellipse_start_pos is not None:
                current_point = self.mapToScene(event.pos())
                ellipse = QRectF(self.ellipse_start_pos, current_point)
                ellipse = ellipse.normalized()
                self.current_ellipse_item.setRect(ellipse)
        elif self.tools[self.tool_index] == "Line":
            if event.buttons() & QtCore.Qt.MouseButton.LeftButton and self.line_start_point is not None:
                current_point = self.mapToScene(event.pos())
                self.current_line.setLine(QLineF(self.line_start_point, current_point))
        elif self.tools[self.tool_index] == "Eraser":
            if event.buttons() & QtCore.Qt.MouseButton.LeftButton:
                self.eraser_tool_action(event)
                self.undoAvailable.emit(len(self.undo_stack) > 0)
                self.redoAvailable.emit(len(self.redo_stack) > 0)

    def drawModeMouseReleaseEvent(self, event):
        if self.tools[self.tool_index] == "Pencil" or self.tools[self.tool_index] == "Eraser" or self.tools[self.tool_index] == "A Plus":
            self.setCursor(self.cursors[self.tool_index])
        else:
            self.setCursor(Qt.CursorShape.ArrowCursor)

        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            if self.tools[self.tool_index] == "Pencil":
                if self.current_path_item:
                    self.undo_stack.append({"item": self.current_path_item, "action": "drawn"})
                    self.redo_stack.clear()
                    self.current_path = None
                    self.current_path_item = None
            elif self.tools[self.tool_index] == "Rectangle":
                if self.current_rect_item:
                    self.undo_stack.append({"item": self.current_rect_item, "action": "drawn"})
                    self.redo_stack.clear()
                    self.rect_start_point = None
                    self.current_rect_item = None
            elif self.tools[self.tool_index] == "Ellipse":
                if self.current_ellipse_item:
                    self.undo_stack.append({"item": self.current_ellipse_item, "action": "drawn"})
                    self.redo_stack.clear()
                    self.ellipse_start_pos = None
                    self.current_ellipse_item = None
            elif self.tools[self.tool_index] == "Line":
                if self.current_line:
                    self.undo_stack.append({"item": self.current_line, "action": "drawn"})
                    self.redo_stack.clear()
                    self.line_start_point = None
                    self.current_line = None
            self.undoAvailable.emit(len(self.undo_stack) > 0)
            self.redoAvailable.emit(len(self.redo_stack) > 0)
            
    def pencil_tool_action(self, event):
        self.current_path = QPainterPath()
        self.current_path.moveTo(self.mapToScene(event.pos()))
        offset_position = self.mapToScene(event.pos()) + QtCore.QPointF(1, 1)
        self.current_path.lineTo(offset_position)
        self.current_path_item = QGraphicsPathItem(self.current_path)
        scale_factor = self.transform().m11()
        adjusted_width = (self.stroke_width + 1) / scale_factor
        self.current_path_item.setPen(QPen(self.tool_color, adjusted_width))
        self.code_scene.addItem(self.current_path_item)
        self.drawn_items.append(self.current_path_item)
        self.redo_stack.clear()
        self.current_path_item_index = len(self.drawn_items) - 1
    
    
    def rectangle_tool_action(self, event):
        self.rect_start_point = self.mapToScene(event.pos())
        self.current_rect_item = QGraphicsRectItem()
        scale_factor = self.transform().m11()
        adjusted_width = (self.stroke_width + 1) / scale_factor
        self.current_rect_item.setPen(QPen(self.tool_color, adjusted_width))
        self.code_scene.addItem(self.current_rect_item)
        self.drawn_items.append(self.current_rect_item)
        self.redo_stack.clear()
        self.current_path_item_index = len(self.drawn_items) - 1

    def ellipse_tool_action(self, event):
        self.current_ellipse_item = QGraphicsEllipseItem(0, 0, 0, 0)
        scale_factor = self.transform().m11()
        adjusted_width = (self.stroke_width + 1) / scale_factor
        self.current_ellipse_item.setPen(QPen(self.tool_color, adjusted_width))
        self.ellipse_start_pos = self.mapToScene(event.pos())
        self.code_scene.addItem(self.current_ellipse_item)
        self.drawn_items.append(self.current_ellipse_item)
        self.redo_stack.clear()
        self.current_path_item_index = len(self.drawn_items) - 1

    def line_tool_action(self, event):
        self.line_start_point = self.mapToScene(event.pos())
        scale_factor = self.transform().m11()
        adjusted_width = (self.stroke_width + 1) / scale_factor
        self.current_line = QGraphicsLineItem(QLineF(self.line_start_point, self.line_start_point))        
        self.current_line.setPen(QPen(self.tool_color, adjusted_width))
        self.code_scene.addItem(self.current_line)
        self.drawn_items.append(self.current_line)
        self.redo_stack.clear()
        self.current_path_item_index = len(self.drawn_items) - 1
   
    def eraser_tool_action(self, event):
        items_at_pos = self.items(event.pos())

        for item_to_remove in items_at_pos:
            if item_to_remove in self.drawn_items:
                should_erase = self.shouldEraseItem(item_to_remove, self.mapToScene(event.pos()))
                print(f"Should erase: {should_erase}")
                if should_erase:
                    self.code_scene.removeItem(item_to_remove)
                    self.drawn_items.remove(item_to_remove)
                    self.undo_stack.append({"item": item_to_remove, "action": "erased"})
                    self.redo_stack.clear()
                    print(f"erased item: {item_to_remove}")
                    break  # Stop after erasing one item
            else:
                print("No items at position")

    def itemToPixmap(self, item):
        rect = item.boundingRect()
        pixmap = QPixmap(int(rect.width()), int(rect.height()))
        pixmap.fill(QColor(255, 0, 0, 0))  # fill pixmap with red

        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing, False)
        painter.setTransform(item.transform())  # set the painter's transform matrix
        painter.translate(-rect.x(), -rect.y())
        item.paint(painter, QStyleOptionGraphicsItem(), None)
        painter.end()

        return pixmap

    def shouldEraseItem(self, item, erase_pos):
        """
        Determine whether a QGraphicsItem should be erased based on a QPixmap
        representation of the item and an erase position.
        """
        # Convert the item to a QPixmap
        pixmap = self.itemToPixmap(item)

        # Adjust the erase position to be relative to the item's bounding rect
        adjusted_erase_pos = erase_pos - item.boundingRect().topLeft()

        # Map the adjusted erase position from scene coordinates to item coordinates
        mapped_pos = item.mapFromScene(adjusted_erase_pos)

        # Check if the mapped position is within the pixmap's bounds
        if 0 <= mapped_pos.x() < pixmap.width() and 0 <= mapped_pos.y() < pixmap.height():
            # Get the color of the pixel at the mapped position
            color = pixmap.toImage().pixelColor(mapped_pos.toPoint())

            # Return True if the pixel is not transparent
            return color.alpha() > 0

        # If the mapped position is out of bounds, return False
        return False
    
    def undo(self):
        if self.undo_stack:
            action_to_undo = self.undo_stack.pop()
            self.undoAvailable.emit(len(self.undo_stack) > 0)
            self.redoAvailable.emit(True)
            if action_to_undo["action"] == "drawn":
                self.code_scene.removeItem(action_to_undo["item"])
                # Only remove from drawn_items if the action was "drawn"
                self.drawn_items.remove(action_to_undo["item"])
                self.redo_stack.append({"item": action_to_undo["item"], "action": "drawn"})
            elif action_to_undo["action"] == "erased":
                self.code_scene.addItem(action_to_undo["item"])
                # Add back to drawn_items if the action was "erased"
                self.drawn_items.append(action_to_undo["item"])
                self.redo_stack.append({"item": action_to_undo["item"], "action": "erased"})

    def redo(self):
        if self.redo_stack:
            action_to_redo = self.redo_stack.pop()
            self.redoAvailable.emit(len(self.redo_stack) > 0)
            self.undoAvailable.emit(True)
            if action_to_redo["action"] == "drawn":
                self.code_scene.addItem(action_to_redo["item"])
                # Add back to drawn_items if the action was "drawn"
                self.drawn_items.append(action_to_redo["item"])
                self.undo_stack.append({"item": action_to_redo["item"], "action": "drawn"})
            elif action_to_redo["action"] == "erased":
                self.code_scene.removeItem(action_to_redo["item"])
                # Only remove from drawn_items if the action was "erased"
                self.drawn_items.remove(action_to_redo["item"])
                self.undo_stack.append({"item": action_to_redo["item"], "action": "erased"})
 
    def reset_undo_redo_stacks(self):
        """
        Reset the undo and redo stacks.
        """
        self.undo_stack.clear()
        self.redo_stack.clear()

    def presentationModeMousePressEvent(self, event):
        """ 
        Handle mouse press events in presentation mode.
        """
        self.setCursor(Qt.CursorShape.ArrowCursor)
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self.last_mouse_pos = event.pos()

    def presentationModeMouseMoveEvent(self, event):
        """
        Handle mouse move events in presentation mode.
        """
        self.setCursor(Qt.CursorShape.ArrowCursor)
        if event.buttons() & QtCore.Qt.MouseButton.LeftButton and self.last_mouse_pos is not None:
            diff = event.pos() - self.last_mouse_pos
            self.horizontalScrollBar().setValue(self.horizontalScrollBar().value() - diff.x())
            self.verticalScrollBar().setValue(self.verticalScrollBar().value() - diff.y())
            self.last_mouse_pos = event.pos()

    def presentationModeMouseReleaseEvent(self, event):
        """
        Handle mouse release events in presentation mode.
        """
        self.setCursor(Qt.CursorShape.ArrowCursor)
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self.last_mouse_pos = None

    def wheelEvent(self, event):
        """
        Handle mouse wheel events for zooming in and out.
        """
        if not self.draw_mode:
            if event.angleDelta().y() > 0:
                factor = 1.25
                self.zoom += 1
            else:
                factor = 0.8
                self.zoom -= 1
            if self.zoom > -ZOOM_LIMIT and self.zoom < ZOOM_LIMIT:
                self.scale(factor, factor)
            else:
                self.zoom = max(min(self.zoom, ZOOM_LIMIT), -ZOOM_LIMIT)

        # Just ensuring zoom level is within limits
        self.zoom = max(min(self.zoom, ZOOM_LIMIT), -ZOOM_LIMIT)

    def reset_zoom(self):
        current_zoom = self.transform().m11()
        factor = 1 / current_zoom
        self.scale(factor, factor)
        self.zoom = 0

    def reset_transformations(self):
        self.setTransform(QtGui.QTransform())
    
    def reset_translation(self):
        self.translate(-self.sceneRect().x(), -self.sceneRect().y())
    
    def move_to_center(self):
        self.centerOn(0, 0)

    def reset_scene_rect(self):
        initial_scene_rect = QtCore.QRectF(
            -2 * SCENE_RECT_MULTIPLE * self.width(),
            -2 * SCENE_RECT_MULTIPLE * self.height(),
            4 * SCENE_RECT_MULTIPLE * self.width(),
            4 * SCENE_RECT_MULTIPLE * self.height()
        )
        self.code_scene.setSceneRect(initial_scene_rect)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.reset_scene_rect()

    def clear(self):
        self.code_scene.clear()
        self.drawn_items = deque()
        self.undo_stack = deque()
        self.redo_stack = deque()
        self.current_path = None
        self.current_path_item = None
        self.undoAvailable.emit(len(self.undo_stack) > 0)
        self.redoAvailable.emit(len(self.redo_stack) > 0)
        self.reset_scene_rect()
        self.reset_zoom()
        self.reset_undo_redo_stacks()
        self.reset_transformations()
        self.reset_translation()
        self.move_to_center()

    def set_tool_color(self, color):
        self.tool_color = color
        
    def set_stroke_width(self, width):
        self.stroke_width = width

    def set_pencil_tool(self):
        self.tool_index = 0
    
    def set_erase_tool(self):
        self.tool_index = 1
    
    def set_line_tool(self):
        self.tool_index = 2
    
    def set_ellipse_tool(self):
        self.tool_index = 3
    
    def set_rectangle_tool(self):
        self.tool_index = 4
    
    def set_color(self, color):
        self.tool_color = color
    
    def set_draw_mode(self):
        self.draw_mode = True
        self.present_mode = False
    
    def set_present_mode(self):
        self.draw_mode = False
        self.present_mode = True
    
    def advance(self, dt: float):
        self.code_scene.advance()



