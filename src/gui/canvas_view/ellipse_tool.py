from src.gui.canvas_view.canvas_tool_base import CanvasToolBase
from PyQt6.QtWidgets import QGraphicsEllipseItem
from PyQt6.QtCore import QRectF

class EllipseTool(CanvasToolBase):
    def __init__(self, cursor):
        super().__init__("Ellipse", cursor)
        self.persistent_cursor = False

    def get_item(self, *args, **kwargs) -> QGraphicsEllipseItem:
        super().get_item(**kwargs)
        self.item = QGraphicsEllipseItem(self.origin.x(), self.origin.y(), 0, 0)
        return self.item
    
    def drag(self, *args, **kwargs):
        super().drag(**kwargs)
        ellipse = QRectF(self.origin, self.position)
        ellipse = ellipse.normalized()
        self.item.setRect(ellipse)
    
    