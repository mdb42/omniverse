import abc
from PyQt6.QtWidgets import QGraphicsItem
from PyQt6.QtGui import QCursor

class CanvasToolBase(abc.ABC):
    def __init__(self, name: str, cursor: QCursor):
        self.name = name
        self.cursor = cursor
        self.persistent_cursor = True
        self.origin = None
        self.position = None
        self.item = None
        self.intersecting_items = []
        self.commit_on_drag = False
        self.pixmap = None

    @abc.abstractmethod
    def get_item(self, *args, **kwargs) -> QGraphicsItem:
        self.origin = kwargs.get('origin')
        self.intersecting_items = kwargs.get('intersecting_items')
        self.pixmap = kwargs.get('pixmap')
        pass

    @abc.abstractmethod
    def drag(self, *args, **kwargs):
        self.position = kwargs.get('position')
        self.intersecting_items = kwargs.get('intersecting_items')
        pass


