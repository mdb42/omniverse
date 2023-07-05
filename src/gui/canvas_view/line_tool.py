from src.gui.canvas_view.canvas_tool_base import CanvasToolBase
from PyQt6.QtWidgets import QGraphicsLineItem
from PyQt6.QtCore import QLineF

class LineTool(CanvasToolBase):
    def __init__(self, cursor):
        super().__init__("Line", cursor)
        self.persistent_cursor = False

    def get_item(self, *args, **kwargs) -> QGraphicsLineItem:
        super().get_item(**kwargs)
        self.item = QGraphicsLineItem(QLineF(self.origin, self.origin))
        return self.item
    
    def drag(self, *args, **kwargs):
        super().drag(**kwargs)
        self.item.setLine(QLineF(self.origin, self.position))
    
    