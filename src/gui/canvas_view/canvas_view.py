from collections import deque
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPixmap, QImage, QCursor, QPen, QColor
from PyQt6.QtWidgets import QGraphicsScene
from PyQt6.QtCore import Qt
from importlib.resources import files
from src.gui.canvas_view.pencil_tool import PencilTool
from src.gui.canvas_view.eraser_tool import EraserTool
from src.gui.canvas_view.line_tool import LineTool
from src.gui.canvas_view.ellipse_tool import EllipseTool
from src.gui.canvas_view.rect_tool import RectTool


# Constants
SCENE_RECT_MULTIPLE = 2
ZOOM_LIMIT = 5

class CanvasView(QtWidgets.QGraphicsView):
    present_mode = True
    draw_mode = False    
    hidden_mode = False

    animating = True

    background_color = QColor(200, 200, 200, 0)
    fill_color = QColor(255, 255, 255, 0)
    stroke_color = QColor(0, 0, 0, 255)        
    stroke_width = 1
    zoom = 0 

    undoAvailable = QtCore.pyqtSignal(bool)
    redoAvailable = QtCore.pyqtSignal(bool)

    processing_left_click = False
    processing_right_click = False
    prev_click_pos = None 

    def __init__(self, parent):
        super().__init__(parent)       
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)        
        self.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)    
        self.setMouseTracking(True)

        self.canvas_scene = QGraphicsScene()        
        self.canvas_scene.setBackgroundBrush(self.background_color)
        self.setScene(self.canvas_scene)
        self.reset_scene_rect()
        self.setViewportUpdateMode(QtWidgets.QGraphicsView.ViewportUpdateMode.FullViewportUpdate)

        self.tools = [PencilTool(self.load_cursor("tool-pencil.ico", 1, 17)), 
                           EraserTool(self.load_cursor("tool-eraser.ico", 8, 13)), 
                           LineTool(self.load_cursor("tool-misc.ico", 8, 8)),
                           EllipseTool(self.load_cursor("tool-misc.ico", 8, 8)), 
                           RectTool(self.load_cursor("tool-misc.ico", 8, 8))]

        self.tool_index = 0
        self.current_item = None

        self.drawn_items = deque()
        self.undo_stack = deque()
        self.redo_stack = deque()
        
        self.canvas_scene.update()
    
    def mousePressEvent(self, event):
        if not self.processing_left_click and not self.processing_right_click:
            self.prev_click_pos = event.pos()
            if event.button() == QtCore.Qt.MouseButton.LeftButton:
                self.processing_left_click = True
                self.leftMousePressEvent(event)
            elif event.button() == QtCore.Qt.MouseButton.RightButton:
                self.processing_right_click = True
                self.rightMousePressEvent(event)
    
    def mouseMoveEvent(self, event):
        if self.processing_left_click:
            self.leftMouseDraggedEvent(event)
        elif self.processing_right_click:
            self.rightMouseDraggedEvent(event)

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self.leftMouseReleaseEvent()
            self.processing_left_click = False
        elif event.button() == QtCore.Qt.MouseButton.RightButton:
            self.rightMouseReleaseEvent(event)
            self.processing_right_click = False
    
    def leftMousePressEvent(self, event):
        if self.draw_mode:
            self.setCursor(self.tools[self.tool_index].cursor)
            self.current_item = self.tools[self.tool_index].get_item(colliding_items=self.items(event.pos()), origin=self.mapToScene(event.pos()))
            if self.tools[self.tool_index].name == "Eraser" and self.current_item:
                self.subtractive_action(self.current_item)
            elif self.current_item:
                self.additive_action(self.current_item)

    def leftMouseDraggedEvent(self, event):
        if self.draw_mode:
            self.setCursor(self.tools[self.tool_index].cursor)
            if self.tools[self.tool_index].commit_on_drag:
                self.leftMousePressEvent(event)
            else:
                self.tools[self.tool_index].drag(position = self.mapToScene(event.pos()))

    def leftMouseReleaseEvent(self):        
        if self.draw_mode:            
            if self.tools[self.tool_index].persistent_cursor:
                self.setCursor(self.tools[self.tool_index].cursor)
            else:
                self.setCursor(Qt.CursorShape.ArrowCursor)

    def additive_action(self, item):        
        adjusted_width = (self.stroke_width + 1) / self.transform().m11()
        self.current_item.setPen(QPen(self.stroke_color, adjusted_width))
        self.canvas_scene.addItem(self.current_item)
        self.drawn_items.append(self.current_item)
        self.undo_stack.append({"item": item, "action": "drawn"})
        self.redo_stack.clear()
        self.undoAvailable.emit(len(self.undo_stack) > 0)
        self.redoAvailable.emit(len(self.redo_stack) > 0)
    
    def subtractive_action(self, item):
        self.canvas_scene.removeItem(item)
        self.drawn_items.remove(item)
        self.undo_stack.append({"item": item, "action": "erased"})
        self.redo_stack.clear()
        self.undoAvailable.emit(len(self.undo_stack) > 0)
        self.redoAvailable.emit(len(self.redo_stack) > 0)

    def undo(self):
        if self.undo_stack:
            action_to_undo = self.undo_stack.pop()
            self.undoAvailable.emit(len(self.undo_stack) > 0)
            self.redoAvailable.emit(True)
            if action_to_undo["action"] == "drawn":
                self.canvas_scene.removeItem(action_to_undo["item"])
                # Only remove from drawn_items if the action was "drawn"
                self.drawn_items.remove(action_to_undo["item"])
                self.redo_stack.append({"item": action_to_undo["item"], "action": "drawn"})
            elif action_to_undo["action"] == "erased":
                self.canvas_scene.addItem(action_to_undo["item"])
                # Add back to drawn_items if the action was "erased"
                self.drawn_items.append(action_to_undo["item"])
                self.redo_stack.append({"item": action_to_undo["item"], "action": "erased"})

    def redo(self):
        if self.redo_stack:
            action_to_redo = self.redo_stack.pop()
            self.redoAvailable.emit(len(self.redo_stack) > 0)
            self.undoAvailable.emit(True)
            if action_to_redo["action"] == "drawn":
                self.canvas_scene.addItem(action_to_redo["item"])
                # Add back to drawn_items if the action was "drawn"
                self.drawn_items.append(action_to_redo["item"])
                self.undo_stack.append({"item": action_to_redo["item"], "action": "drawn"})
            elif action_to_redo["action"] == "erased":
                self.canvas_scene.removeItem(action_to_redo["item"])
                # Only remove from drawn_items if the action was "erased"
                self.drawn_items.remove(action_to_redo["item"])
                self.undo_stack.append({"item": action_to_redo["item"], "action": "erased"})
     
    def rightMousePressEvent(self, event):
        """ 
        Handle mouse press events in presentation mode.
        """
        self.setCursor(Qt.CursorShape.OpenHandCursor)        
        self.prev_click_pos = event.pos()

    def rightMouseDraggedEvent(self, event):
        """
        Handle mouse move events in presentation mode.
        """
        self.setCursor(Qt.CursorShape.OpenHandCursor)        
        diff = event.pos() - self.prev_click_pos
        self.horizontalScrollBar().setValue(self.horizontalScrollBar().value() - diff.x())
        self.verticalScrollBar().setValue(self.verticalScrollBar().value() - diff.y())
        self.prev_click_pos = event.pos()

    def rightMouseReleaseEvent(self, event):
        """
        Handle mouse release events in presentation mode.
        """
        if self.draw_mode:
            if self.tools[self.tool_index].persistent_cursor:
                self.setCursor(self.tools[self.tool_index].cursor)
            else:
                self.setCursor(Qt.CursorShape.ArrowCursor)  

    def reset_undo_redo_stacks(self):
        """
        Reset the undo and redo stacks.
        """
        self.undo_stack.clear()
        self.redo_stack.clear()

    def wheelEvent(self, event):
        """
        Handle mouse wheel events for zooming in and out.
        """        
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
        self.canvas_scene.setSceneRect(initial_scene_rect)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.reset_scene_rect()

    def clear(self):
        self.canvas_scene.clear()
        self.drawn_items = deque()
        self.undo_stack = deque()
        self.redo_stack = deque()
        self.undoAvailable.emit(len(self.undo_stack) > 0)
        self.redoAvailable.emit(len(self.redo_stack) > 0)
        self.reset_scene_rect()
        self.reset_zoom()
        self.reset_undo_redo_stacks()
        self.reset_transformations()
        self.reset_translation()
        self.move_to_center()

    def set_tool_color(self, color):
        self.stroke_color = color
        
    def set_stroke_width(self, width):
        self.stroke_width = width

    def set_pencil_tool(self):
        self.tool_index = 0
        self.setCursor(self.tools[self.tool_index].cursor)
    
    def set_erase_tool(self):
        self.tool_index = 1
        self.setCursor(self.tools[self.tool_index].cursor)
    
    def set_line_tool(self):
        self.tool_index = 2
        self.setCursor(Qt.CursorShape.ArrowCursor)
    
    def set_ellipse_tool(self):
        self.tool_index = 3
        self.setCursor(Qt.CursorShape.ArrowCursor)
    
    def set_rectangle_tool(self):
        self.tool_index = 4
        self.setCursor(Qt.CursorShape.ArrowCursor)
    
    def set_color(self, color):
        self.stroke_color = color
    
    def set_draw_mode(self):
        if self.tools[self.tool_index].persistent_cursor:
            self.setCursor(self.tools[self.tool_index].cursor)
        else:
            self.setCursor(Qt.CursorShape.ArrowCursor)
        self.draw_mode = True
        self.present_mode = False
        self.hidden_mode = False
    
    def set_present_mode(self):
        self.setCursor(Qt.CursorShape.ArrowCursor)
        self.draw_mode = False
        self.present_mode = True
        self.hidden_mode = False
    
    def set_hidden_mode(self):
        self.setCursor(Qt.CursorShape.ArrowCursor)
        self.draw_mode = False
        self.present_mode = False
        self.hidden_mode = True
    
    def advance(self, dt: float):
        self.canvas_scene.advance()

    def load_cursor(self, resource, hot_x, hot_y):
        cursor_size = 18
        resource_path = files("resources.icons") / resource
        with open(resource_path, 'rb') as file:
            icon_data = file.read()
        icon_image = QImage.fromData(icon_data).scaled(cursor_size, cursor_size, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        return QCursor(QPixmap.fromImage(icon_image), hot_x, hot_y)





