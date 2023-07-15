from gui.components.chat_interface_widget import Ui_Form as ChatInterfaceWidget
from src import utils
from local import constants
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
import webbrowser
from importlib.resources import files
from PyQt6 import QtCore, QtGui, QtWidgets

tts_clicked_signal = QtCore.pyqtSignal(bool)
stt_clicked_signal = QtCore.pyqtSignal(bool)
generate_text_clicked_signal = QtCore.pyqtSignal(bool)
generate_image_clicked_signal = QtCore.pyqtSignal(bool)

class ChatInterface(ChatInterfaceWidget):
    def __init__(self, parent) -> None:
        super().__init__()
        self.setupUi(parent)
        self.tts_on_button_icon_pixmap = utils.load_icon("button-tts-on.ico")
        self.tts_off_button_icon_pixmap = utils.load_icon("button-tts-off.ico")
        self.stt_on_button_icon_pixmap = utils.load_icon("button-stt-on.ico")
        self.stt_off_button_icon_pixmap = utils.load_icon("button-stt-off.ico")
        self.tts_button.setIcon(QIcon(self.tts_off_button_icon_pixmap))
        self.stt_button.setIcon(QIcon(self.stt_off_button_icon_pixmap))
        self.generate_text_button.setIcon(QIcon(utils.load_icon("button-generate-text.ico")))
        self.generate_image_button.setIcon(QIcon(utils.load_icon("button-generate-image.ico")))
        