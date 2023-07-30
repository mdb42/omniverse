from gui.components.chat_interface_widget import Ui_Form as ChatInterfaceWidget
from gui import gui_utils
from PyQt6.QtGui import QIcon, QTextCursor
from PyQt6.QtWidgets import QWidget, QTextBrowser, QFileDialog
from PyQt6.QtCore import Qt, pyqtSignal


class ChatInterface(ChatInterfaceWidget):
    """The Chat Interface holds widgets for chat use."""

    def __init__(self, parent) -> None:
        super().__init__()
        self.setupUi(parent)
        self.tts_on_button_icon_pixmap = gui_utils.load_icon("button-tts-on.ico")
        self.tts_off_button_icon_pixmap = gui_utils.load_icon("button-tts-off.ico")
        self.stt_on_button_icon_pixmap = gui_utils.load_icon("button-stt-on.ico")
        self.stt_off_button_icon_pixmap = gui_utils.load_icon("button-stt-off.ico")
        self.tts_button.setIcon(QIcon(self.tts_off_button_icon_pixmap))
        self.stt_button.setIcon(QIcon(self.stt_off_button_icon_pixmap))
        self.generate_text_button.setIcon(QIcon(gui_utils.load_icon("button-generate-text.ico")))
        self.generate_image_button.setIcon(QIcon(gui_utils.load_icon("button-generate-image.ico")))
        self.chat_config_button.setIcon(QIcon(gui_utils.load_icon("button-config.ico")))
        self.chat_config_button.clicked.connect(self.chat_config_button_clicked)
        self.temperature_slider.valueChanged.connect(self.temperature_slider_changed)

    def chat_config_button_clicked(self):
        self.chat_interface_stacked_widget.setCurrentIndex((self.chat_interface_stacked_widget.currentIndex() + 1) % self.chat_interface_stacked_widget.count())
        if self.chat_interface_stacked_widget.currentIndex() == 0:
            self.chat_label.setText("Chat")
        elif self.chat_interface_stacked_widget.currentIndex() == 1:
            self.chat_label.setText("Chat Settings")
        else:
            self.chat_label.setText("Test Chat")

    def populate_personas(self, persona_names):
        self.persona_combo_box.clear()
        for persona in persona_names:
            self.persona_combo_box.addItem(persona)
        self.persona_combo_box.setCurrentIndex(0)
    
    def populate_models(self, model_names):
        self.model_combo_box.clear()
        for model in model_names:
            self.model_combo_box.addItem(model)
        self.model_combo_box.setCurrentIndex(0)
    
    def populate_protocols(self, protocol_names):
        self.protocol_combo_box.clear()
        for protocol in protocol_names:
            self.protocol_combo_box.addItem(protocol)
        self.protocol_combo_box.setCurrentIndex(0)

    def temperature_slider_changed(self, value):
        self.temperature_label.setText(f"Temperature: {value/10}")
    
    def get_user_input(self):
        return self.chat_input_text_editor.toPlainText().rstrip()
    
    def send_user_input_to_chat(self, user_name, responder_name):
        self.set_cursor_to_end(self.chat_output_browser)
        self.chat_output_browser.append("\n" + f"{user_name}: {self.get_user_input()}"+ "\n")
        self.chat_input_text_editor.clear()
        self.chat_input_text_editor.setFocus()
        self.chat_output_browser.append(responder_name + ": ")

    def set_cursor_to_end(self, browser):
        """Set the cursor to the end of the browser, preventing the llm from overwriting the chat history."""
        cursor = browser.textCursor()
        cursor.movePosition(QTextCursor.MoveOperation.End)
        browser.setTextCursor(cursor)
        browser.ensureCursorVisible()

    
    
        

        
