from src.gui.modes.canvas_mode.canvas_tool_base import CanvasToolBase
from PyQt6.QtWidgets import QGraphicsItem, QStyleOptionGraphicsItem
from PyQt6.QtGui import QPixmap, QPainter, QColor

class EraserTool(CanvasToolBase):
    def __init__(self):
        super().__init__(name = "Eraser", 
                         icon_filename = "tool-eraser.ico", 
                         commit_on_drag = True, 
                         subtractive = True,
                         cursor_hot_x = 8,
                         cursor_hot_y = 13)        

    def get_item(self, *args, **kwargs) -> QGraphicsItem:
        super().get_item(**kwargs)
        self.item = None
        for item in self.intersecting_items:                    
            if self.should_erase_item(item, self.origin):
                self.item = item
                break  # Stop after finding one item
        return self.item
        
    def drag(self, *args, **kwargs):
        super().drag(**kwargs)

    def should_erase_item(self, item, erase_pos):
        """
        Examines the item to verify if the pixel at the erase position is transparent.
        """
        pixmap = self.item_to_pixmap(item)
        adjusted_erase_pos = erase_pos - item.boundingRect().topLeft()
        mapped_pos = item.mapFromScene(adjusted_erase_pos)
        if 0 <= mapped_pos.x() < pixmap.width() and 0 <= mapped_pos.y() < pixmap.height():
            color = pixmap.toImage().pixelColor(mapped_pos.toPoint())
            return color.alpha() > 0
        return False
    
    def item_to_pixmap(self, item):
        """
        Generates and returns a pixmap from the item.
        """
        rect = item.boundingRect()
        pixmap = QPixmap(int(rect.width()), int(rect.height()))
        pixmap.fill(QColor(0, 0, 0, 0))  # set the background to transparent
        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing, False)
        painter.setTransform(item.transform())  # set the painter's transform matrix
        painter.translate(-rect.x(), -rect.y())
        item.paint(painter, QStyleOptionGraphicsItem(), None)
        painter.end()
        return pixmap
    
    