from src.gui.modes.canvas_mode.canvas_tool_base import CanvasToolBase
from PyQt6.QtGui import QPainterPath
from PyQt6.QtWidgets import QGraphicsPathItem
from PyQt6 import QtCore
from PyQt6.QtGui import QCursor
from PyQt6.QtCore import Qt

class PencilTool(CanvasToolBase):
    def __init__(self):
        super().__init__(name = "Pencil Tool", icon_filename = "tool-pencil.ico", cursor_hot_x = 1, cursor_hot_y = 17)
        self.path = QPainterPath()
        

    def get_item(self, *args, **kwargs) -> QGraphicsPathItem:
        super().get_item(**kwargs)
        self.path = QPainterPath()
        self.path.moveTo(self.origin)
        self.path.lineTo(self.origin + QtCore.QPointF(1, 1))
        self.item = QGraphicsPathItem(self.path)
        return self.item
    
    def drag(self, *args, **kwargs):
        super().drag(**kwargs)
        self.path.lineTo(self.position)
        self.item.setPath(self.path)
    