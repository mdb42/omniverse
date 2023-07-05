from src.gui.canvas_view.canvas_tool_base import CanvasToolBase
from PyQt6.QtWidgets import QGraphicsRectItem
from PyQt6.QtCore import QRectF

class RectTool(CanvasToolBase):
    def __init__(self, cursor):
        super().__init__("Rectangle", cursor)
        self.persistent_cursor = False

    def get_item(self, *args, **kwargs) -> QGraphicsRectItem:
        super().get_item(**kwargs)
        self.item = QGraphicsRectItem(self.origin.x(), self.origin.y(), 0, 0)
        return self.item     
    
    def drag(self, *args, **kwargs):
        super().drag(**kwargs)
        rect = QRectF(self.origin, self.position)
        rect = rect.normalized()  
        self.item.setRect(rect)
    
    