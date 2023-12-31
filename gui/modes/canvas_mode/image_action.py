from gui.modes.canvas_mode.draw_action_base import DrawActionBase
from PyQt6.QtWidgets import QGraphicsPixmapItem
from PyQt6 import QtCore

class ImageAction(DrawActionBase):
    def __init__(self, *args, **kwargs):
        super().__init__(name = "Image Tool", 
                         icon_filename = "tool-image.ico",
                         cursor_hot_x = 8,
                         cursor_hot_y = 8,
                         *args,
                         **kwargs)
        
        self.pixmap = kwargs.get('pixmap', None)

    def get_item(self, *args, **kwargs) -> QGraphicsPixmapItem:
        super().get_item(**kwargs)
        print("Attempting to send image item to canvas")
        print(f"ImageTool.get_item() kwargs: {kwargs}")
        if self.pixmap is None:
            return None
        else:
            self.item = QGraphicsPixmapItem(self.pixmap)
            # Let's get the pixmap to be centered on the cursor
            self.item.setPos(self.origin - QtCore.QPointF(self.pixmap.width() / 2, self.pixmap.height() / 2))
            return self.item
    
    def drag(self, *args, **kwargs):
        super().drag(**kwargs)
    