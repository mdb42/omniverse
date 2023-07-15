from gui.modes.canvas_mode.draw_action_base import DrawActionBase
from PyQt6.QtWidgets import QGraphicsEllipseItem
from PyQt6.QtCore import QRectF

class EllipseAction(DrawActionBase):
    def __init__(self, *args, **kwargs):
        super().__init__(name = "Ellipse Tool", 
                            icon_filename = "tool-ellipse.ico", 
                            cursor_filename = "tool-misc.ico", 
                            cursor_hot_x = 8,
                            cursor_hot_y = 8,
                            persistent_cursor = False,
                            *args,
                            **kwargs)

    def get_item(self, *args, **kwargs) -> QGraphicsEllipseItem:
        super().get_item(**kwargs)
        self.item = QGraphicsEllipseItem(self.origin.x(), self.origin.y(), 0, 0)
        return self.item
    
    def drag(self, *args, **kwargs):
        super().drag(**kwargs)
        ellipse = QRectF(self.origin, self.position)
        ellipse = ellipse.normalized()
        self.item.setRect(ellipse)
    
    