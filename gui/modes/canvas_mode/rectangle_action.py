from gui.modes.canvas_mode.draw_action_base import DrawActionBase
from PyQt6.QtWidgets import QGraphicsRectItem
from PyQt6.QtCore import QRectF

class RectangleAction(DrawActionBase):
    def __init__(self, *args, **kwargs):
        super().__init__(name = "Rectangle Tool", 
                         icon_filename = "tool-rectangle.ico", 
                         persistent_cursor = False, 
                         cursor_filename = "tool-misc.ico", 
                         cursor_hot_x = 8, 
                         cursor_hot_y = 8,
                         *args,
                         **kwargs)

    def get_item(self, *args, **kwargs) -> QGraphicsRectItem:
        super().get_item(**kwargs)
        self.item = QGraphicsRectItem(self.origin.x(), self.origin.y(), 0, 0)
        return self.item     
    
    def drag(self, *args, **kwargs):
        super().drag(**kwargs)
        rect = QRectF(self.origin, self.position)
        rect = rect.normalized()  
        self.item.setRect(rect)
    
    