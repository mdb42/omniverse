from collections import deque
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPixmap, QImage, QCursor, QPainter, QPainterPath, QPen, QColor
from PyQt6.QtWidgets import QGraphicsScene, QStyleOptionGraphicsItem, QGraphicsRectItem, QGraphicsEllipseItem, QGraphicsLineItem, QGraphicsPathItem
from PyQt6.QtCore import Qt, QRectF, QLineF
import importlib.resources

# Constants
SCENE_RECT_MULTIPLE = 2
ZOOM_LIMIT = 5

class PresentationView(QtWidgets.QGraphicsView):
    animating = True
    undoAvailable = QtCore.pyqtSignal(bool)
    redoAvailable = QtCore.pyqtSignal(bool)
    processing_click = False

    def __init__(self):
        super().__init__()       
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.setMouseTracking(True)
        self.blueprint_scene = QGraphicsScene()
        self.background_color = QColor(200, 200, 200, 255)        
        self.setScene(self.blueprint_scene)
        self.scene().setBackgroundBrush(self.background_color)
        self.reset_scene_rect()
        self.setViewportUpdateMode(QtWidgets.QGraphicsView.ViewportUpdateMode.FullViewportUpdate)
        self.zoom = 0 
  
    def mousePressEvent(self, event):
        pass
    
    def mouseMoveEvent(self, event):
        pass

    def mouseReleaseEvent(self, event):
        pass

    def wheelEvent(self, event):
        """
        Handle mouse wheel events for zooming in and out.
        """
       
        if event.angleDelta().y() > 0:
            factor = 1.25
            self.zoom += 1
        else:
            factor = 0.8
            self.zoom -= 1
        if self.zoom > -ZOOM_LIMIT and self.zoom < ZOOM_LIMIT:
            self.scale(factor, factor)
        else:
            self.zoom = max(min(self.zoom, ZOOM_LIMIT), -ZOOM_LIMIT)

        # Just ensuring zoom level is within limits
        self.zoom = max(min(self.zoom, ZOOM_LIMIT), -ZOOM_LIMIT)

    def reset_zoom(self):
        current_zoom = self.transform().m11()
        factor = 1 / current_zoom
        self.scale(factor, factor)
        self.zoom = 0

    def reset_transformations(self):
        self.setTransform(QtGui.QTransform())
    
    def reset_translation(self):
        self.translate(-self.sceneRect().x(), -self.sceneRect().y())
    
    def move_to_center(self):
        self.centerOn(0, 0)

    def reset_scene_rect(self):
        initial_scene_rect = QtCore.QRectF(
            -2 * SCENE_RECT_MULTIPLE * self.width(),
            -2 * SCENE_RECT_MULTIPLE * self.height(),
            4 * SCENE_RECT_MULTIPLE * self.width(),
            4 * SCENE_RECT_MULTIPLE * self.height()
        )
        self.blueprint_scene.setSceneRect(initial_scene_rect)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.reset_scene_rect()
    
    def advance(self, dt: float):
        self.scene().advance()



