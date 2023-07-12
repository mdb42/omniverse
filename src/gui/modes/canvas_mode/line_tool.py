from src.gui.modes.canvas_mode.canvas_tool_base import CanvasToolBase
from PyQt6.QtWidgets import QGraphicsLineItem
from PyQt6.QtCore import QLineF

class LineTool(CanvasToolBase):
    def __init__(self):
        super().__init__(name = "Line Tool", icon_filename = "tool-line.ico", cursor_filename = "tool-misc.ico", persistent_cursor = False, cursor_hot_x = 8, cursor_hot_y = 8)

    def get_item(self, *args, **kwargs) -> QGraphicsLineItem:
        super().get_item(**kwargs)
        self.item = QGraphicsLineItem(QLineF(self.origin, self.origin))
        return self.item
    
    def drag(self, *args, **kwargs):
        super().drag(**kwargs)
        self.item.setLine(QLineF(self.origin, self.position))
    
    