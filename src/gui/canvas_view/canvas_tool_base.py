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
        self.colliding_items = []
        self.commit_on_drag = False

    @abc.abstractmethod
    def get_item(self, *args, **kwargs) -> QGraphicsItem:
        self.origin = kwargs.get('origin')
        self.colliding_items = kwargs.get('colliding_items')
        pass

    @abc.abstractmethod
    def drag(self, *args, **kwargs):
        self.position = kwargs.get('position')
        self.colliding_items = kwargs.get('colliding_items')
        pass


