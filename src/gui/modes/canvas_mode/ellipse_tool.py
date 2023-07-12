from src.gui.modes.canvas_mode.canvas_tool_base import CanvasToolBase
from PyQt6.QtWidgets import QGraphicsEllipseItem
from PyQt6.QtCore import QRectF

class EllipseTool(CanvasToolBase):
    def __init__(self):
        super().__init__(name = "Ellipse Tool", 
                            icon_filename = "tool-circle.ico", 
                            cursor_filename = "tool-misc.ico", 
                            cursor_hot_x = 8,
                            cursor_hot_y = 8,
                            persistent_cursor = False)
        self.persistent_cursor = False
        self.cursor = self.load_cursor("tool-misc.ico", 8, 8)

    def get_item(self, *args, **kwargs) -> QGraphicsEllipseItem:
        super().get_item(**kwargs)
        self.item = QGraphicsEllipseItem(self.origin.x(), self.origin.y(), 0, 0)
        return self.item
    
    def drag(self, *args, **kwargs):
        super().drag(**kwargs)
        ellipse = QRectF(self.origin, self.position)
        ellipse = ellipse.normalized()
        self.item.setRect(ellipse)
    
    