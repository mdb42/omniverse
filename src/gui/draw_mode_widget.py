
from PyQt6.QtWidgets import QWidget
class DrawModeWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setVisible(False)
    
    def setVisible(self, visible: bool) -> None:
        return super().setVisible(visible)
    

    