from gui.components.workspace_creation_widget import Ui_Form as WorkspaceCreationWidget
from src import resource_utils
from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6 import QtCore
import base64
import os


class WorkspaceCreationWindow(QtWidgets.QWidget, WorkspaceCreationWidget):
    workspace_created_signal = QtCore.pyqtSignal(bool)
    window_closed_signal = QtCore.pyqtSignal(bool)

    def __init__(self, parent=None):
        super(WorkspaceCreationWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
        self.setWindowIcon(QIcon(resource_utils.load_icon("application-icon.ico")))
        self.setWindowFlag(Qt.WindowType.WindowMinimizeButtonHint, False)
        self.setWindowFlag(Qt.WindowType.WindowMaximizeButtonHint, False)
        self.setFixedSize(self.size())
        self.setWindowModality(Qt.WindowModality.ApplicationModal)

        self.copy_to_clipboard_button.setIcon(QIcon(resource_utils.load_icon("clipboard-icon.ico")))
        self.random_key_button.setIcon(QIcon(resource_utils.load_icon("refresh-icon.ico")))
        self.visibility_on_icon = QIcon(resource_utils.load_icon("visibility-on-icon.ico"))
        
        self.visibility_off_icon = QIcon(resource_utils.load_icon("visibility-off-icon.ico"))
        self.echo_toggle_button.setIcon(self.visibility_off_icon)
        self.continue_button.clicked.connect(self.continue_button_clicked)
        self.random_key_button.clicked.connect(self.random_key_button_clicked)
        self.copy_to_clipboard_button.clicked.connect(self.copy_to_clipboard_button_clicked)
        self.echo_toggle_button.clicked.connect(self.echo_toggle_button_clicked)
        self.key_line_edit.textChanged.connect(self.key_line_edit_changed)
        self.key_line_edit_changed()
    
    def random_key_button_clicked(self):
        self.key_line_edit.setText(self.generate_random_key())
    
    def generate_random_key(self):
        # Generate a 32-byte (256-bit) random key
        key_bytes = os.urandom(32)
        # Base64 encode the key to get a string
        key_b64_string = base64.urlsafe_b64encode(key_bytes).decode('utf-8')
        return key_b64_string



    
    def key_line_edit_changed(self):
        if self.key_line_edit.text() == "":
            self.continue_button.setEnabled(False)
        else:
            self.continue_button.setEnabled(True)

    def copy_to_clipboard_button_clicked(self):
        clipboard = QtWidgets.QApplication.clipboard()
        clipboard.setText(self.key_line_edit.text())

    
    def echo_toggle_button_clicked(self):
        if self.echo_toggle_button.isChecked():
            self.echo_toggle_button.setIcon(self.visibility_on_icon)
            self.echo_toggle_button.setIconSize(QtCore.QSize(16, 15))
            self.key_line_edit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        else:
            self.echo_toggle_button.setIcon(self.visibility_off_icon)
            self.echo_toggle_button.setIconSize(QtCore.QSize(16, 16))
            self.key_line_edit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

    def closeEvent(self, event):
        self.window_closed_signal.emit(True)
        event.accept()

    
    
    def continue_button_clicked(self):
        self.workspace_created_signal.emit(True)

    def get_key(self):
        return self.key_line_edit.text()
    
        
    
        





        



    
