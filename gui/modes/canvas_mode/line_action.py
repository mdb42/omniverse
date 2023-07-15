from gui.modes.canvas_mode.draw_action_base import DrawActionBase
from PyQt6.QtWidgets import QGraphicsLineItem
from PyQt6.QtCore import QLineF

class LineAction(DrawActionBase):
    def __init__(self, *args, **kwargs):
        super().__init__(name = "Line Tool", 
                         icon_filename = "tool-line.ico", 
                         cursor_filename = "tool-misc.ico", 
                         persistent_cursor = False, 
                         cursor_hot_x = 8, 
                         cursor_hot_y = 8, 
                         *args,
                         **kwargs)

    def get_item(self, *args, **kwargs) -> QGraphicsLineItem:
        super().get_item(**kwargs)
        self.item = QGraphicsLineItem(QLineF(self.origin, self.origin))
        return self.item
    
    def drag(self, *args, **kwargs):
        super().drag(**kwargs)
        self.item.setLine(QLineF(self.origin, self.position))
    
    