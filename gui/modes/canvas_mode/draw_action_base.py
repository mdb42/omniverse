from abc import ABC, abstractmethod
from PyQt6.QtWidgets import QGraphicsItem
from gui.modes.action_base import ActionBase
from src import resource_utils


class DrawActionBase(ActionBase, ABC):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.name = kwargs.get('name', "Canvas Tool Base")
        self.cursor = kwargs.get('cursor', None)
        self.icon_filename = kwargs.get('icon_filename', None)

        self.item = kwargs.get('item', None)
        self.intersecting_items = kwargs.get('intersecting_items', [])
        self.commit_on_drag = kwargs.get('commit_on_drag', False)
        self.fill_enabled = kwargs.get('fill_enabled', False)

        self.cursor_filename = kwargs.get('cursor_filename', self.icon_filename)
        self.cursor_hot_x = kwargs.get('cursor_hot_x', 0)
        self.cursor_hot_y = kwargs.get('cursor_hot_y', 0)
        self.cursor = resource_utils.load_cursor(self.cursor_filename, self.cursor_hot_x, self.cursor_hot_y)  
        
        self.persistent_cursor = kwargs.get('persistent_cursor', True)
        self.origin = kwargs.get('origin', None)
        self.position = kwargs.get('position', None)

        self.button.setCheckable(True)
        self.button.setChecked(False)

        

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


    


