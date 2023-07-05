import sys, os
from local import constants
from src.gui import omniverse_window
from src.gui.windows.login_window import Ui_Form as LoginUI
from src.gui.windows.user_creation_window import Ui_Form as UserCreationUI
from src.gui.components.tool_bar_widget import Ui_Form as ToolBarUI

from importlib.resources import files
from datetime import datetime
from src.data.data_manager import DataManager

"""
Short Term:
TODO: Create a full startup sequence that logs in a user or creates a new user, removing reliance on /local directory.
TODO: Create a full shutdown sequence that saves all data and logs out the user if "Stay Online" setting not selected.
TODO: Fix the LLM Manager's preprocessing functions.
TODO: Implement brush fills for the main graphic's view's draw mode shape tools.
TODO: Merge existing Present Mode and Draw Mode to be managed with more mouse events and gestures.
TODO: Repurpose Present Mode for displaying simulation spaces like tabletop games and virtual worlds.
TODO: Start developing QGraphicsItemGroups for LLM related widgets in the new code graphics view.

Long Term:
TODO: Build alternate chat interface with responses presented discretely for easier feedbacks.
TODO: Create methods for saving and loading the view, model, or session.
TODO: Redevelop the LLM Manager to manage multiple AI personae with dynamic prompt grounding.
TODO: Implement more life-like voices to improve Text-to-Speech.
TODO: Implement OpenAI's Whisper API for Speech-to-Text.

"""

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QPixmap, QIcon, QImage, QTextCursor
from PyQt6.QtCore import QTimer, Qt

from src.audio.audio_manager import AudioManager

from src.art.art_manager import ArtManager

from src.llms.llm_manager import LLMManager
from langchain.callbacks.base import BaseCallbackManager
from src.gui.callbacks.streaming_browser_out import StreamingBrowserCallbackHandler
from src.gui.canvas_view.canvas_view import CanvasView
from src.gui.code_view.code_view import CodeView


TITLE = "Omniverse"
VERSION = "0.0.3"
FRAMES_PER_SECOND = 66

class Omniverse(QtWidgets.QMainWindow, omniverse_window.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Omniverse, self).__init__(parent)
        QtWidgets.QMainWindow.__init__(self, parent=parent)
        self.setupUi(self)
        self.setWindowTitle(f"{TITLE} {VERSION}")

        self.canvas_view = CanvasView(parent=self)
        self.code_view = CodeView(parent=self)

        self.application_icon_pixmap = QPixmap()
        self.tts_on_button_icon_pixmap = QPixmap()
        self.tts_off_button_icon_pixmap = QPixmap()
        self.stt_on_button_icon_pixmap = QPixmap()
        self.stt_off_button_icon_pixmap = QPixmap()
        self.user_button_icon_pixmap = QPixmap()

        self.toolbar_widget = QtWidgets.QWidget()
        self.toolbar_ui = ToolBarUI()

        self.login_widget = QtWidgets.QWidget()
        self.login_ui = LoginUI()

        self.user_creation_widget = QtWidgets.QWidget()
        self.user_creation_ui = UserCreationUI()

        self.initialize_gui()

        self.data_manager = DataManager(app_name=TITLE, key=constants.ENCRYPTION_KEY)
        os.environ["OPENAI_API_KEY"] = constants.OPENAI_API_KEY

        # Setup session variables
        self.session_start_time = datetime.now()
        self.user_id = constants.DEFAULT_USER_NAME
        self.assistant_id = constants.DEFAULT_AI_NAME
        

        # Setup the language model manager
        self.response_cb = BaseCallbackManager([StreamingBrowserCallbackHandler(self.response_text_browser)])
        self.sentiment_cb = BaseCallbackManager([StreamingBrowserCallbackHandler(self.sentiment_browser)])
        self.entity_cb = BaseCallbackManager([StreamingBrowserCallbackHandler(self.entity_browser)])
        self.knowledge_cb = BaseCallbackManager([StreamingBrowserCallbackHandler(self.knowledge_browser)])
        self.summary_cb = BaseCallbackManager([StreamingBrowserCallbackHandler(self.summary_browser)])

        self.browser_callbacks = {
            "response": self.response_cb,
            "sentiment": self.sentiment_cb,
            "entity": self.entity_cb,
            "knowledge": self.knowledge_cb,
            "summary": self.summary_cb
        }

        self.llm_manager = LLMManager(self.browser_callbacks, self.user_id, self.assistant_id)
        self.current_input = ""
        self.current_response = ""

        # Setup the AI art manager
        self.art_manager = ArtManager()        
        self.current_image = None

        # Setup the audio manager
        self.audio_manager = AudioManager()
        self.audio_manager.play_sound_effect("click")       
        
        # Initialize a QTimer for animation
        self.animation_timer = QTimer(self)
        self.animation_timer.timeout.connect(self.advance)
        self.animation_timer.start(int(1000/FRAMES_PER_SECOND))

    def login(self):
        print("Logging in")

    def twitter_button_clicked(self):
        print("Twitter Button Clicked")
    
    def discord_button_clicked(self):
        print("Discord Button Clicked")
    
    def github_button_clicked(self):
        print("Github Button Clicked")

    def user_button_clicked(self):
        print("User Button Clicked")
    
    def exit_login(self):
        self.login_widget.close()

    def advance(self):
        delta_time = self.animation_timer.interval() / 1000.0
        self.canvas_view.advance(delta_time)
  
    def generate_response(self):
        self.current_input = self.input_text_editor.toPlainText().rstrip()
        self.response_text_browser.append("\n" + str(self.user_id + ": " + self.current_input + "\n"))
        self.input_text_editor.clear()
        self.input_text_editor.setFocus()
        """ Generate a response from the LLM Manager."""
        print("Generating Response")
        self.set_cursor_to_end(self.response_text_browser)
        self.response_text_browser.append(self.assistant_id + ": ")
        self.preprocessing()
        self.current_response = self.llm_manager.generate_response()
        self.postprocessing()
        self.llm_manager.report_tokens()

    def preprocessing(self):
        """ Perform all preprocessing events, ending with the LLM preprocessor."""
        print("Preprocessing Prompt Grounding")
        self.sentiment_browser.clear()
        self.entity_browser.clear()
        QtWidgets.QApplication.processEvents()
        self.llm_manager.preprocessing(self.current_input)

    def postprocessing(self):
        """ Perform all postprocessing events, ending with the LLM postprocessor."""
        print("Postprocessing Model Output")
        if self.audio_manager.tts_flag:
            self.audio_manager.tts_manager.play_speech_async(self.current_response)

        self.summary_browser.clear()
        self.knowledge_browser.clear()
        QtWidgets.QApplication.processEvents()
        print("Going to LLM Manager Post Processing")
        self.llm_manager.postprocessing(self.current_input, self.current_response)
        print("Finished LLM Manager Post Processing")
    
    def set_cursor_to_end(self, browser):
        cursor = browser.textCursor()
        cursor.movePosition(QTextCursor.MoveOperation.End)
        browser.setTextCursor(cursor)
        browser.ensureCursorVisible()
    
    def generate_image(self):
        print("Generating image")

    def set_present_mode(self):
        self.toolbar_ui.mode_tools_stacked_widget.setCurrentIndex(0)
        self.canvas_view.set_present_mode()
        self.toolbar_ui.draw_button.setChecked(self.canvas_view.draw_mode)
        self.toolbar_ui.present_button.setChecked(self.canvas_view.present_mode)
        self.toolbar_ui.code_button.setChecked(self.canvas_view.hidden_mode)
        self.central_stacked_widget.setCurrentIndex(0)

    def set_draw_mode(self):
        self.toolbar_ui.mode_tools_stacked_widget.setCurrentIndex(1)
        self.canvas_view.set_draw_mode()
        self.toolbar_ui.draw_button.setChecked(self.canvas_view.draw_mode)
        self.toolbar_ui.present_button.setChecked(self.canvas_view.present_mode)
        self.toolbar_ui.code_button.setChecked(self.canvas_view.hidden_mode)        
        self.central_stacked_widget.setCurrentIndex(0)     
    
    def set_code_mode(self):
        self.toolbar_ui.mode_tools_stacked_widget.setCurrentIndex(2)
        self.canvas_view.set_hidden_mode()
        self.toolbar_ui.code_button.setChecked(self.canvas_view.hidden_mode)
        self.toolbar_ui.present_button.setChecked(self.canvas_view.present_mode)
        self.toolbar_ui.draw_button.setChecked(self.canvas_view.draw_mode)        
        self.central_stacked_widget.setCurrentIndex(1)
    
    def toggle_tts_mode(self):
        self.audio_manager.tts_flag = not self.audio_manager.tts_flag
        if self.audio_manager.tts_flag:
            self.tts_mode_button.setIcon(QIcon(self.tts_on_button_icon_pixmap))
        else:
            self.tts_mode_button.setIcon(QIcon(self.tts_off_button_icon_pixmap))

    def toggle_stt_mode(self):
        self.audio_manager.stt_flag = not self.audio_manager.stt_flag
        if self.audio_manager.stt_flag:
            self.stt_mode_button.setIcon(QIcon(self.stt_on_button_icon_pixmap))
        else:
            self.stt_mode_button.setIcon(QIcon(self.stt_off_button_icon_pixmap))

    def load_icon(self, package, resource):
        resource_path = files(package) / resource
        with open(resource_path, 'rb') as file:
            icon_data = file.read()
        icon_image = QImage.fromData(icon_data)
        return QPixmap.fromImage(icon_image)


    def initialize_gui(self):

        # Setup the application icon
        self.application_icon_pixmap = self.load_icon("resources.icons", "application-icon.ico")
        self.setWindowIcon(QIcon(self.application_icon_pixmap))
        
        # Add the main graphics view to the main grid widget's layout
        self.main_grid_widget.layout().addWidget(self.canvas_view)
        # We need to ensure the code view is added to the code view vertical widget in the top row, above existing widgets
        self.code_view_vertical_widget.layout().insertWidget(0, self.code_view)
        self.code_view_vertical_widget.layout().setStretch(1, 1)
        #We need to make sure the stretch applies after resizing
        self.code_view_vertical_widget.layout().setStretchFactor(self.code_view, 1)
        
        # Setup the various widgets        
        self.toolbar_ui.setupUi(self.toolbar_widget)
        self.toolbar_ui.fill_color_button.set_color(self.canvas_view.fill_color)
        self.toolBar.addWidget(self.toolbar_widget)
        self.toolBar.setMovable(False)
        self.toolBar.setFloatable(False)

        self.login_ui.setupUi(self.login_widget)
        self.login_widget.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
        self.login_widget.setWindowIcon(QIcon(self.application_icon_pixmap))
        self.login_widget.show()

        self.user_creation_ui.setupUi(self.user_creation_widget)
        self.user_creation_widget.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
        self.user_creation_widget.setWindowIcon(QIcon(self.application_icon_pixmap))
        self.user_creation_widget.show()

        # Setup the dynamic components
        self.tts_on_button_icon_pixmap = self.load_icon("resources.icons", "button-tts-on.ico")
        self.tts_off_button_icon_pixmap = self.load_icon("resources.icons", "button-tts-off.ico")
        self.stt_on_button_icon_pixmap = self.load_icon("resources.icons", "button-stt-on.ico")
        self.stt_off_button_icon_pixmap = self.load_icon("resources.icons", "button-stt-off.ico")
        self.user_button_icon_pixmap = self.load_icon("resources.icons", "button-user.ico")

        # Set the starting icons for the dynamic components
        self.tts_mode_button.setIcon(QIcon(self.tts_off_button_icon_pixmap))
        self.stt_mode_button.setIcon(QIcon(self.stt_off_button_icon_pixmap))
        self.toolbar_ui.user_button.setIcon(QIcon(self.user_button_icon_pixmap))
        
        # Setup static components
        self.generate_text_button.setIcon(QIcon(self.load_icon("resources.icons", "button-generate-text.ico")))
        self.generate_image_button.setIcon(QIcon(self.load_icon("resources.icons", "button-generate-image.ico")))

        # Setup static toolbar components
        self.toolbar_ui.present_button.setIcon(QIcon(self.load_icon("resources.icons", "mode-present.ico")))
        self.toolbar_ui.draw_button.setIcon(QIcon(self.load_icon("resources.icons", "mode-draw.ico")))
        self.toolbar_ui.code_button.setIcon(QIcon(self.load_icon("resources.icons", "mode-code.ico")))
        self.toolbar_ui.pencil_button.setIcon(QIcon(self.load_icon("resources.icons", "tool-pencil.ico")))
        self.toolbar_ui.erase_button.setIcon(QIcon(self.load_icon("resources.icons", "tool-eraser.ico")))
        self.toolbar_ui.line_button.setIcon(QIcon(self.load_icon("resources.icons", "tool-line.ico")))
        self.toolbar_ui.ellipse_button.setIcon(QIcon(self.load_icon("resources.icons", "tool-circle.ico")))
        self.toolbar_ui.rectangle_button.setIcon(QIcon(self.load_icon("resources.icons", "tool-square.ico")))
        self.toolbar_ui.undo_button.setIcon(QIcon(self.load_icon("resources.icons", "button-undo.ico")))
        self.toolbar_ui.redo_button.setIcon(QIcon(self.load_icon("resources.icons", "button-redo.ico")))
        self.toolbar_ui.new_button.setIcon(QIcon(self.load_icon("resources.icons", "button-new.ico")))
        self.toolbar_ui.open_button.setIcon(QIcon(self.load_icon("resources.icons", "button-open.ico")))
        self.toolbar_ui.save_button.setIcon(QIcon(self.load_icon("resources.icons", "button-save.ico")))

        # Setup static login widget components
        self.login_ui.twitter_button.setIcon(QIcon(self.load_icon("resources.icons", "twitter-icon.ico")))
        self.login_ui.discord_button.setIcon(QIcon(self.load_icon("resources.icons", "discord-icon.ico")))
        self.login_ui.github_button.setIcon(QIcon(self.load_icon("resources.icons", "github-icon.ico")))

        # Connect signals to methods
        self.canvas_view.undoAvailable.connect(self.toolbar_ui.undo_button.setEnabled)
        self.canvas_view.redoAvailable.connect(self.toolbar_ui.redo_button.setEnabled)
        self.tts_mode_button.clicked.connect(self.toggle_tts_mode)
        self.stt_mode_button.clicked.connect(self.toggle_stt_mode)
        self.generate_text_button.clicked.connect(self.generate_response)
        self.generate_image_button.clicked.connect(self.generate_image)
        self.toolbar_ui.present_button.clicked.connect(self.set_present_mode)
        self.toolbar_ui.draw_button.clicked.connect(self.set_draw_mode)
        self.toolbar_ui.code_button.clicked.connect(self.set_code_mode)
        self.toolbar_ui.pencil_button.clicked.connect(self.canvas_view.set_pencil_tool)
        self.toolbar_ui.erase_button.clicked.connect(self.canvas_view.set_erase_tool)
        self.toolbar_ui.line_button.clicked.connect(self.canvas_view.set_line_tool)
        self.toolbar_ui.ellipse_button.clicked.connect(self.canvas_view.set_ellipse_tool)
        self.toolbar_ui.rectangle_button.clicked.connect(self.canvas_view.set_rectangle_tool)
        self.toolbar_ui.undo_button.clicked.connect(self.canvas_view.undo)
        self.toolbar_ui.redo_button.clicked.connect(self.canvas_view.redo)
        self.toolbar_ui.new_button.clicked.connect(self.canvas_view.clear)
        self.toolbar_ui.stroke_color_button.color_changed.connect(self.canvas_view.set_tool_color)        
        self.toolbar_ui.stroke_width_spin_box.valueChanged.connect(self.canvas_view.set_stroke_width)
        self.toolbar_ui.user_button.clicked.connect(self.user_button_clicked)
        self.login_ui.github_button.clicked.connect(self.github_button_clicked)
        self.login_ui.discord_button.clicked.connect(self.discord_button_clicked)
        self.login_ui.twitter_button.clicked.connect(self.twitter_button_clicked)
        self.login_ui.login_button.clicked.connect(self.login)
  

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Omniverse()
    window.show()
    sys.exit(app.exec())


    