from abc import ABC, abstractmethod
from PyQt6.QtWidgets import QGraphicsItem
from PyQt6.QtGui import QCursor, QPixmap, QImage
from src.gui.modes.tool_base import ToolBase
from PyQt6.QtCore import Qt
from importlib.resources import files
from PyQt6 import QtCore


class CanvasToolBase(ToolBase, ABC):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.name = kwargs.get('name', "Canvas Tool Base")
        self.cursor = kwargs.get('cursor', None)
        self.icon_filename = kwargs.get('icon_filename', None)

        self.pixmap = kwargs.get('pixmap', None)
        self.item = kwargs.get('item', None)
        self.intersecting_items = kwargs.get('intersecting_items', [])
        self.commit_on_drag = kwargs.get('commit_on_drag', False)

        self.cursor_filename = kwargs.get('cursor_filename', self.icon_filename)
        self.cursor_hot_x = kwargs.get('cursor_hot_x', 0)
        self.cursor_hot_y = kwargs.get('cursor_hot_y', 0)
        self.cursor = self.load_cursor(self.cursor_filename, self.cursor_hot_x, self.cursor_hot_y)  
        
        self.persistent_cursor = kwargs.get('persistent_cursor', True)
        self.origin = kwargs.get('origin', None)
        self.position = kwargs.get('position', None)

        

    @abstractmethod
    def get_item(self, *args, **kwargs) -> QGraphicsItem:
        self.origin = kwargs.get('origin')
        self.intersecting_items = kwargs.get('intersecting_items')
        self.pixmap = kwargs.get('pixmap')
        pass

    @abstractmethod
    def drag(self, *args, **kwargs):
        self.position = kwargs.get('position')
        self.intersecting_items = kwargs.get('intersecting_items')
        pass

    def load_cursor(self, resource, hot_x, hot_y):
        cursor_size = 18
        resource_path = files("resources.icons") / resource
        with open(resource_path, 'rb') as file:
            cursor_data = file.read()
        cursor_image = QImage.fromData(cursor_data).scaled(cursor_size, cursor_size, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        return QCursor(QPixmap.fromImage(cursor_image), hot_x, hot_y)

    


