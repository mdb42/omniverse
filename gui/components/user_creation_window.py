from gui.components.user_creation_widget import Ui_Form as UserCreationWidget
from src import resource_utils
from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6 import QtCore


class UserCreationWindow(QtWidgets.QWidget, UserCreationWidget):
    user_created_signal = QtCore.pyqtSignal(bool)
    window_closed_signal = QtCore.pyqtSignal(bool)

    def __init__(self, parent=None, session=None):
        super(UserCreationWindow, self).__init__(parent)
        self.session = session
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
        self.setWindowIcon(QIcon(resource_utils.load_icon("application-icon.ico")))
        self.setWindowFlag(Qt.WindowType.WindowMinimizeButtonHint, False)
        self.setWindowFlag(Qt.WindowType.WindowMaximizeButtonHint, False)
        self.setFixedSize(self.size())
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.cancel_button.clicked.connect(self.cancel_button_clicked)
        self.confirm_button.clicked.connect(self.confirm_button_clicked)
        self.api_key_line_edit.textChanged.connect(self.api_key_line_edit_changed)
        self.confirm_line_edit.textChanged.connect(self.confirm_line_edit_changed)
        self.password_line_edit.textChanged.connect(self.password_line_edit_changed)
        self.name_line_edit.textChanged.connect(self.name_line_edit_changed)
        self.get_api_key_button.clicked.connect(self.get_api_key_button_clicked)

    def name_line_edit_changed(self):
        pass

    def password_line_edit_changed(self):
        pass

    def confirm_line_edit_changed(self):
        pass

    def api_key_line_edit_changed(self):
        pass

    def get_api_key_button_clicked(self):
        pass

    def cancel_button_clicked(self):
        pass

    def confirm_button_clicked(self):
        name = self.name_line_edit.text()
        password = self.password_line_edit.text()
        confirm = self.confirm_line_edit.text()
        api_key = self.api_key_line_edit.text()
        if name == "":
            self.feedback_label.setText("Name cannot be blank.")
            return
        if password == "":
            self.feedback_label.setText("Password cannot be blank.")
            return
        if confirm != password:
            self.feedback_label.setText("Passwords do not match.")
            self.password_line_edit.setText("")
            self.confirm_line_edit.setText("")
            return
        if api_key == "":
            self.feedback_label.setText("API key cannot be blank.")
            return
        if self.session.get_user_by_name(name) is not None:
            self.feedback_label.setText("User already exists.")
            return
        self.session.create_user(name=name, role="User", input_password=password, api_key=api_key)
        self.user_created_signal.emit(True)
        self.name_line_edit.setText("")
        self.password_line_edit.setText("")
        self.confirm_line_edit.setText("")
        self.api_key_line_edit.setText("")
        self.feedback_label.setText("User created successfully.")




        



    
