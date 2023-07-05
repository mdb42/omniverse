from src.gui.canvas_view.canvas_tool_base import CanvasToolBase
from PyQt6.QtGui import QPainterPath
from PyQt6.QtWidgets import QGraphicsPathItem
from PyQt6 import QtCore

class PencilTool(CanvasToolBase):
    def __init__(self, cursor):
        super().__init__("Pencil", cursor)
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
    