import sys, webbrowser
from local import constants
from src.gui import omniverse_main
from importlib.resources import files
from src.data.session_manager import SessionManager
from src.audio.audio_manager import AudioManager
from src.art.art_manager import ArtManager
from src.llms.llm_manager import LLMManager
from langchain.callbacks.base import BaseCallbackManager

from src.gui.windows.login_window import Ui_Form as LoginUI
from src.gui.windows.user_creation_window import Ui_Form as UserCreationUI

from src.gui.modes.presentation_mode.presentation_mode import PresentationMode
from src.gui.modes.canvas_mode.canvas_mode import CanvasMode, CanvasView
from src.gui.modes.blueprint_mode.blueprint_mode import BlueprintMode

from src.gui.components.chat_interface_widget import Ui_Form as ChatInterfaceUI
from src.gui.callbacks.streaming_browser_out import StreamingBrowserCallbackHandler

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QPixmap, QIcon, QImage, QTextCursor
from PyQt6.QtCore import QTimer, Qt


TITLE = "Omniverse"
VERSION = "0.0.5"
FRAMES_PER_SECOND = 66

class Omniverse(QtWidgets.QMainWindow, omniverse_main.Ui_MainWindow):
    """This window is the primary interface for the Omniverse application. It allows different
    graphical display objects to be presented in the main window, with two splitter panels:
    one on the left for the control panel, and one on the right for the chat interface.
    The application tracks a mode state, which is used to determine which graphical display
    object is currently being presented in the main window. The mode state also updates the
    control panel and toolbar to reflect the current mode. The chat interface is globally used
    throughout the application, presenting an interactive customizable AI persona that can 
    engage with information gathered from the given display."""
    def __init__(self, parent=None):
        super(Omniverse, self).__init__(parent)
        self.setupUi(self)  
        self.session = SessionManager(app_name=TITLE, key=constants.DEFAULT_ENCRYPTION_KEY)
        self.mode_index = 0  # The index of the current mode
        self.modes = [PresentationMode(parent=self), CanvasMode(parent=self), BlueprintMode(parent=self)]
        
        self.initialize_gui()

        # Initialize a QTimer for continuous constant advancement
        self.frame_timer = QTimer(self)
        self.frame_timer.timeout.connect(self.advance)
        self.frame_timer.start(int(1000/FRAMES_PER_SECOND))

        # Setup the language model manager
        # These callbacks are only for the prototype implementation
        # TODO: Remove these callbacks and replace with a json file defining completion batch sequences
        self.assistant_id = constants.DEFAULT_AI_NAME
        self.browser_callbacks = {
            "response": BaseCallbackManager([StreamingBrowserCallbackHandler(self.chat_interface_ui.chat_output_browser)]),
            "sentiment": BaseCallbackManager([StreamingBrowserCallbackHandler(self.modes[2].control_ui.sentiment_browser)]),
            "entity": BaseCallbackManager([StreamingBrowserCallbackHandler(self.modes[2].control_ui.entity_browser)]),
            "knowledge": BaseCallbackManager([StreamingBrowserCallbackHandler(self.modes[2].control_ui.knowledge_browser)]),
            "summary": BaseCallbackManager([StreamingBrowserCallbackHandler(self.modes[2].control_ui.summary_browser)])
        }

        self.llm_manager = LLMManager(self.browser_callbacks, "Matthew", self.assistant_id)
        self.current_user_prompt = ""
        self.current_generated_response = ""

        # Setup the AI art manager
        self.art_manager = ArtManager()
        self.current_generated_image = None

        # Setup the audio manager
        self.audio = AudioManager()
        self.audio.play_sound_effect("click") # For testing

    def advance(self):
        delta_time = self.frame_timer.interval() / 1000.0
        for test_mode in self.modes:
            test_mode.advance(delta_time)

    def preprocessing(self):
        """ Perform all preprocessing events, ending with the LLM preprocessor."""
        print("*********************************")
        print("* Preprocessing Prompt Grounding")
        print("*********************************")
        self.modes[2].control_ui.sentiment_browser.clear()
        self.modes[2].control_ui.entity_browser.clear()
        QtWidgets.QApplication.processEvents()
        self.llm_manager.preprocessing(self.current_user_prompt)
  
    def generate_response(self):
        self.current_user_prompt = self.chat_interface_ui.chat_input_text_editor.toPlainText().rstrip()
        self.chat_interface_ui.chat_output_browser.append("\n" + str(self.session.current_user_name + ": " + self.current_user_prompt + "\n"))
        self.chat_interface_ui.chat_input_text_editor.clear()
        self.chat_interface_ui.chat_input_text_editor.setFocus()
        print("Generating Response")
        self.set_cursor_to_end(self.chat_interface_ui.chat_output_browser)
        self.chat_interface_ui.chat_output_browser.append(self.assistant_id + ": ")
        self.preprocessing()
        self.current_generated_response = self.llm_manager.generate_response()
        self.postprocessing()
        self.llm_manager.report_tokens()

    def postprocessing(self):
        """ Perform all postprocessing events, ending with the LLM postprocessor."""
        print("Postprocessing Model Output")
        if self.audio.text_to_speech:
            self.audio.play_text_to_speech(self.current_generated_response)
        QtWidgets.QApplication.processEvents()
        print("Going to LLM Manager Post Processing")
        self.llm_manager.postprocessing(self.current_user_prompt, self.current_generated_response)
        print("Finished LLM Manager Post Processing")
    
    def set_cursor_to_end(self, browser):
        # Set the cursor to the end of the browser, preventing the llm from overwriting the chat history
        cursor = browser.textCursor()
        cursor.movePosition(QTextCursor.MoveOperation.End)
        browser.setTextCursor(cursor)
        browser.ensureCursorVisible()
    
    def generate_image(self):
        self.status_bar.showMessage("Generating Image...")
        prompt = self.chat_interface_ui.chat_input_text_editor.toPlainText().rstrip()
        QtWidgets.QApplication.processEvents()
        pixmap = QPixmap()
        pixmap.loadFromData(self.art_manager.generate_image(prompt))
        if not pixmap.isNull():
            self.current_generated_image = pixmap
            for test_mode in self.modes:
                if isinstance(test_mode.display, CanvasView):
                    test_mode.display.subject_pixmap = self.current_generated_image
            self.status_bar.showMessage("Image Generation Complete")
        else:
            self.status_bar.showMessage("Image Generation Failed")

    def toggle_text_to_speech(self):
        self.audio.text_to_speech = not self.audio.text_to_speech
        if self.audio.text_to_speech:
            self.chat_interface_ui.tts_button.setIcon(QIcon(self.tts_on_button_icon_pixmap))
        else:
            self.chat_interface_ui.tts_button.setIcon(QIcon(self.tts_off_button_icon_pixmap))

    def toggle_speech_to_text(self):
        self.audio.speech_to_text = not self.audio.speech_to_text
        if self.audio.speech_to_text:
            self.chat_interface_ui.stt_button.setIcon(QIcon(self.stt_on_button_icon_pixmap))
        else:
            self.chat_interface_ui.stt_button.setIcon(QIcon(self.stt_off_button_icon_pixmap))

    def login_button_clicked(self):
        print("Logging in")

    def twitter_button_clicked(self):
        webbrowser.open(constants.CREATOR_TWITTER_URL)
    
    def discord_button_clicked(self):
        webbrowser.open(constants.DISCORD_URL)
    
    def github_button_clicked(self):
        webbrowser.open(constants.GITHUB_URL)

    def create_new_user_button_clicked(self):
        print("Create New User Clicked")
        self.exit_login()
        self.user_creation_widget.show()
    
    def exit_login(self):
        self.login_widget.close()
    
    def load_icon(self, resource):
        resource_path = files("resources.icons") / resource
        with open(resource_path, 'rb') as file:
            icon_data = file.read()
        icon_image = QImage.fromData(icon_data)
        return QPixmap.fromImage(icon_image)
    
    def set_mode(self):
        self.mode_index = self.mode_selector_button_group.checkedId()
        self.displays_stacked_widget.setCurrentIndex(self.mode_index)
        self.controls_stacked_widget.setCurrentIndex(self.mode_index)
        for mode_index, mode in enumerate(self.modes):
            for tool_bar in mode.get_tool_bars():
                tool_bar.setVisible(mode_index == self.mode_index)

    def setup_window(self):
        self.setWindowTitle(f"{TITLE} {VERSION}")
        self.application_icon_pixmap = self.load_icon("application-icon.ico")
        self.setWindowIcon(QIcon(self.application_icon_pixmap))
        self.main_splitter.setSizes([int(self.width() * 0.20), int(self.width() * 0.50), int(self.width() * 0.30)])

    def create_mode_selector_tool_bar(self):
        self.mode_selector_tool_bar = QtWidgets.QToolBar(self)
        self.mode_selector_tool_bar.setMovable(False)
        self.mode_selector_tool_bar.setFloatable(False)
        self.mode_selector_tool_bar.setOrientation(Qt.Orientation.Horizontal)
        self.mode_selector_tool_bar.setHidden(False)
        self.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.mode_selector_tool_bar)
        self.mode_selector_tool_bar.setFixedHeight(40)

    def add_modes(self):
        self.mode_selection_widget = QtWidgets.QWidget()
        self.mode_selection_layout = QtWidgets.QHBoxLayout()
        self.mode_selection_widget.setLayout(self.mode_selection_layout)
        self.mode_selection_layout.setContentsMargins(2,2,2,2)
        self.mode_selector_button_group = QtWidgets.QButtonGroup()
        self.mode_selector_button_group.setExclusive(True)
        self.mode_selector_button_group.buttonClicked.connect(self.set_mode) 
        self.mode_selector_tool_bar.addWidget(self.mode_selection_widget)

        for mode_index, mode in enumerate(self.modes):
            for tool_bar in mode.get_tool_bars():
                self.addToolBar(Qt.ToolBarArea.TopToolBarArea, tool_bar)

            mode_button = mode.button
            mode_button.setCheckable(True)
            mode_button.setAutoExclusive(True)
            self.mode_selector_button_group.addButton(mode_button, mode_index)
            self.mode_selection_layout.addWidget(mode_button)
            self.mode_selector_tool_bar.addWidget(mode_button)
            if mode_index == self.mode_index:
                mode_button.setChecked(True)  

            self.displays_stacked_widget.addWidget(mode.display)
            self.controls_stacked_widget.addWidget(mode.control_widget)

    def initialize_gui(self):
        """ Initialize the GUI. """
        self.setup_window()
        self.create_mode_selector_tool_bar()
        self.add_modes()
        self.set_mode()

        # Login Window
        self.login_widget = QtWidgets.QWidget()
        self.login_ui = LoginUI()
        self.login_ui.setupUi(self.login_widget)
        self.login_widget.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
        self.login_widget.setWindowIcon(QIcon(self.application_icon_pixmap))
        self.login_ui.twitter_button.setIcon(QIcon(self.load_icon("twitter-icon.ico")))
        self.login_ui.discord_button.setIcon(QIcon(self.load_icon("discord-icon.ico")))
        self.login_ui.github_button.setIcon(QIcon(self.load_icon("github-icon.ico")))
        self.login_ui.github_button.clicked.connect(self.github_button_clicked)
        self.login_ui.discord_button.clicked.connect(self.discord_button_clicked)
        self.login_ui.twitter_button.clicked.connect(self.twitter_button_clicked)
        self.login_ui.create_new_user_button.clicked.connect(self.create_new_user_button_clicked)
        self.login_widget.show() # We'll conditionally initiate this in start() later

        # User Creation Window
        self.user_creation_widget = QtWidgets.QWidget()
        self.user_creation_ui = UserCreationUI()
        self.user_creation_ui.setupUi(self.user_creation_widget)
        self.user_creation_widget.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
        self.user_creation_widget.setWindowIcon(QIcon(self.application_icon_pixmap))

        # Chat interface widget
        self.chat_interface_widget = QtWidgets.QWidget()
        self.chat_interface_ui = ChatInterfaceUI()
        self.chat_interface_ui.setupUi(self.chat_interface_widget)
        self.chat_stacked_widget.addWidget(self.chat_interface_widget)
        self.tts_on_button_icon_pixmap = self.load_icon("button-tts-on.ico")
        self.tts_off_button_icon_pixmap = self.load_icon("button-tts-off.ico")
        self.stt_on_button_icon_pixmap = self.load_icon("button-stt-on.ico")
        self.stt_off_button_icon_pixmap = self.load_icon("button-stt-off.ico")
        self.chat_interface_ui.tts_button.setIcon(QIcon(self.tts_off_button_icon_pixmap))
        self.chat_interface_ui.stt_button.setIcon(QIcon(self.stt_off_button_icon_pixmap))
        self.chat_interface_ui.generate_text_button.setIcon(QIcon(self.load_icon("button-generate-text.ico")))
        self.chat_interface_ui.generate_image_button.setIcon(QIcon(self.load_icon("button-generate-image.ico")))
        self.chat_interface_ui.tts_button.clicked.connect(self.toggle_text_to_speech)
        self.chat_interface_ui.stt_button.clicked.connect(self.toggle_speech_to_text)
        self.chat_interface_ui.generate_text_button.clicked.connect(self.generate_response)
        self.chat_interface_ui.generate_image_button.clicked.connect(self.generate_image)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Omniverse()
    window.show()
    sys.exit(app.exec())


    