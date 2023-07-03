import sys, os
from local import constants
from src.gui import omniverse_main
from src.gui.login_widget import Ui_Form as LoginUI
from src.gui.tool_bar_widget import Ui_Form as ToolBarUI
from src.gui.user_creation_widget import Ui_Form as UserCreationUI

import importlib.resources
from datetime import datetime
from src.data.data_manager import DataManager

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QPixmap, QIcon, QImage, QTextCursor
from PyQt6.QtCore import QTimer, Qt

from src.audio.audio_manager import AudioManager

from src.art.art_manager import ArtManager

from src.llms.llm_manager import LLMManager
from langchain.callbacks.base import BaseCallbackManager
from src.gui.streaming_browser_out import StreamingBrowserCallbackHandler


TITLE = "Omniverse"
VERSION = "0.0.2"
FRAMES_PER_SECOND = 66

class Omniverse(QtWidgets.QMainWindow, omniverse_main.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Omniverse, self).__init__(parent)
        QtWidgets.QMainWindow.__init__(self, parent=parent)
        self.setupUi(self)
        self.setWindowTitle(f"{TITLE} {VERSION}")

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
        self.main_graphics_view.advance(delta_time)
  
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
        # if self.tts_checkbox.isChecked():
        #     self.tts_manager.play_speech_async(self.current_response)
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
        self.main_graphics_view.present_mode = True
        self.main_graphics_view.draw_mode = not self.main_graphics_view.present_mode
        self.main_graphics_view.code_mode = not self.main_graphics_view.present_mode
        self.toolbar_ui.draw_button.setChecked(self.main_graphics_view.draw_mode)
        self.toolbar_ui.present_button.setChecked(self.main_graphics_view.present_mode)
        self.toolbar_ui.code_button.setChecked(self.main_graphics_view.code_mode)
        self.centtral_stacked_widget.setCurrentIndex(0)

    def set_draw_mode(self):
        self.toolbar_ui.mode_tools_stacked_widget.setCurrentIndex(1)
        self.main_graphics_view.draw_mode = True
        self.main_graphics_view.present_mode = not self.main_graphics_view.draw_mode
        self.main_graphics_view.code_mode = not self.main_graphics_view.draw_mode
        self.toolbar_ui.draw_button.setChecked(self.main_graphics_view.draw_mode)
        self.toolbar_ui.present_button.setChecked(self.main_graphics_view.present_mode)
        self.toolbar_ui.code_button.setChecked(self.main_graphics_view.code_mode)        
        self.centtral_stacked_widget.setCurrentIndex(0)     
    
    def set_code_mode(self):
        self.toolbar_ui.mode_tools_stacked_widget.setCurrentIndex(2)
        self.main_graphics_view.code_mode = True
        self.main_graphics_view.present_mode = not self.main_graphics_view.code_mode
        self.main_graphics_view.draw_mode = not self.main_graphics_view.code_mode
        self.toolbar_ui.code_button.setChecked(self.main_graphics_view.code_mode)
        self.toolbar_ui.present_button.setChecked(self.main_graphics_view.present_mode)
        self.toolbar_ui.draw_button.setChecked(self.main_graphics_view.draw_mode)        
        self.centtral_stacked_widget.setCurrentIndex(1)
    
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
       
    def initialize_gui(self):
        # Setup the application icon
        icon_data = importlib.resources.read_binary("resources.icons", "application-icon.ico")
        icon_image = QImage.fromData(icon_data)
        self.application_icon_pixmap = QPixmap.fromImage(icon_image)
        self.setWindowIcon(QIcon(self.application_icon_pixmap))

        # Setup the various widgets
        
        self.toolbar_ui.setupUi(self.toolbar_widget)
        self.toolBar.addWidget(self.toolbar_widget)
        self.toolBar.setMovable(False)
        self.toolBar.setFloatable(False)

        self.login_ui.setupUi(self.login_widget)
        self.login_widget.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
        self.login_widget.setWindowIcon(QIcon(self.application_icon_pixmap))
        self.login_widget.show()

        self.user_creation_ui.setupUi(self.user_creation_widget)
        # We need to set it so that the widget has no minimize or maximize buttons
        self.user_creation_widget.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
        self.user_creation_widget.setWindowIcon(QIcon(self.application_icon_pixmap))
        self.user_creation_widget.show()

        # Setup the dynamic components

        tts_on_button_icon_data = importlib.resources.read_binary("resources.icons", "button-tts-on.ico")
        tts_on_button_icon_image = QImage.fromData(tts_on_button_icon_data)
        self.tts_on_button_icon_pixmap = QPixmap.fromImage(tts_on_button_icon_image)

        tts_off_button_icon_data = importlib.resources.read_binary("resources.icons", "button-tts-off.ico")
        tts_off_button_icon_image = QImage.fromData(tts_off_button_icon_data)
        self.tts_off_button_icon_pixmap = QPixmap.fromImage(tts_off_button_icon_image)
        self.tts_mode_button.setIcon(QIcon(self.tts_off_button_icon_pixmap))

        stt_on_button_icon_data = importlib.resources.read_binary("resources.icons", "button-stt-on.ico")
        stt_on_button_icon_image = QImage.fromData(stt_on_button_icon_data)
        self.stt_on_button_icon_pixmap = QPixmap.fromImage(stt_on_button_icon_image)

        stt_off_button_icon_data = importlib.resources.read_binary("resources.icons", "button-stt-off.ico")
        stt_off_button_icon_image = QImage.fromData(stt_off_button_icon_data)
        self.stt_off_button_icon_pixmap = QPixmap.fromImage(stt_off_button_icon_image)
        self.stt_mode_button.setIcon(QIcon(self.stt_off_button_icon_pixmap))

        stt_on_button_icon_data = importlib.resources.read_binary("resources.icons", "button-stt-on.ico")
        stt_on_button_icon_image = QImage.fromData(stt_on_button_icon_data)
        self.stt_on_button_icon_pixmap = QPixmap.fromImage(stt_on_button_icon_image)

        user_button_icon_data = importlib.resources.read_binary("resources.icons", "button-user.ico")
        user_button_icon_image = QImage.fromData(user_button_icon_data)
        self.user_button_icon_pixmap = QPixmap.fromImage(user_button_icon_image)
        self.toolbar_ui.user_button.setIcon(QIcon(self.user_button_icon_pixmap))
        
        # Setup static components

        # Setup static toolbar components
        present_button_icon_data = importlib.resources.read_binary("resources.icons", "mode-present.ico")
        present_button_icon_image = QImage.fromData(present_button_icon_data)
        self.toolbar_ui.present_button.setIcon(QIcon(QPixmap.fromImage(present_button_icon_image)))

        draw_button_icon_data = importlib.resources.read_binary("resources.icons", "mode-draw.ico")
        draw_button_icon_image = QImage.fromData(draw_button_icon_data)
        self.toolbar_ui.draw_button.setIcon(QIcon(QPixmap.fromImage(draw_button_icon_image)))

        code_button_icon_data = importlib.resources.read_binary("resources.icons", "mode-code.ico")
        code_button_icon_image = QImage.fromData(code_button_icon_data)
        self.toolbar_ui.code_button.setIcon(QIcon(QPixmap.fromImage(code_button_icon_image)))

        pencil_button_icon_data = importlib.resources.read_binary("resources.icons", "tool-pencil.ico")
        pencil_button_icon_image = QImage.fromData(pencil_button_icon_data)
        self.toolbar_ui.pencil_button.setIcon(QIcon(QPixmap.fromImage(pencil_button_icon_image)))

        erase_button_icon_data = importlib.resources.read_binary("resources.icons", "tool-eraser.ico")
        erase_button_icon_image = QImage.fromData(erase_button_icon_data)
        self.toolbar_ui.erase_button.setIcon(QIcon(QPixmap.fromImage(erase_button_icon_image)))
        
        line_button_icon_data = importlib.resources.read_binary("resources.icons", "tool-line.ico")
        line_button_icon_image = QImage.fromData(line_button_icon_data)
        self.toolbar_ui.line_button.setIcon(QIcon(QPixmap.fromImage(line_button_icon_image)))
        
        ellipse_button_icon_data = importlib.resources.read_binary("resources.icons", "tool-circle.ico")
        ellipse_button_icon_image = QImage.fromData(ellipse_button_icon_data)
        self.toolbar_ui.ellipse_button.setIcon(QIcon(QPixmap.fromImage(ellipse_button_icon_image)))

        rectangle_button_icon_data = importlib.resources.read_binary("resources.icons", "tool-square.ico")
        rectangle_button_icon_image = QImage.fromData(rectangle_button_icon_data)
        self.toolbar_ui.rectangle_button.setIcon(QIcon(QPixmap.fromImage(rectangle_button_icon_image)))

        undo_button_icon_data = importlib.resources.read_binary("resources.icons", "button-undo.ico")
        undo_button_icon_image = QImage.fromData(undo_button_icon_data)
        self.toolbar_ui.undo_button.setIcon(QIcon(QPixmap.fromImage(undo_button_icon_image)))

        redo_button_icon_data = importlib.resources.read_binary("resources.icons", "button-redo.ico")
        redo_button_icon_image = QImage.fromData(redo_button_icon_data)
        self.toolbar_ui.redo_button.setIcon(QIcon(QPixmap.fromImage(redo_button_icon_image)))

        new_button_icon_data = importlib.resources.read_binary("resources.icons", "button-new.ico")
        new_button_icon_image = QImage.fromData(new_button_icon_data)
        self.toolbar_ui.new_button.setIcon(QIcon(QPixmap.fromImage(new_button_icon_image)))

        open_button_icon_data = importlib.resources.read_binary("resources.icons", "button-open.ico")
        open_button_icon_image = QImage.fromData(open_button_icon_data)
        self.toolbar_ui.open_button.setIcon(QIcon(QPixmap.fromImage(open_button_icon_image)))

        save_button_icon_data = importlib.resources.read_binary("resources.icons", "button-save.ico")
        save_button_icon_image = QImage.fromData(save_button_icon_data)
        self.toolbar_ui.save_button.setIcon(QIcon(QPixmap.fromImage(save_button_icon_image)))

        # Setup static login widget components
        github_icon_data = importlib.resources.read_binary("resources.icons", "github-icon.ico")
        github_icon_image = QImage.fromData(github_icon_data)
        self.github_icon_pixmap = QPixmap.fromImage(github_icon_image)
        self.login_ui.github_button.setIcon(QIcon(self.github_icon_pixmap))

        discord_icon_data = importlib.resources.read_binary("resources.icons", "discord-icon.ico")
        discord_icon_image = QImage.fromData(discord_icon_data)
        self.discord_icon_pixmap = QPixmap.fromImage(discord_icon_image)
        self.login_ui.discord_button.setIcon(QIcon(self.discord_icon_pixmap))

        twitter_icon_data = importlib.resources.read_binary("resources.icons", "twitter-icon.ico")
        twitter_icon_image = QImage.fromData(twitter_icon_data)
        self.twitter_icon_pixmap = QPixmap.fromImage(twitter_icon_image)
        self.login_ui.twitter_button.setIcon(QIcon(self.twitter_icon_pixmap))

        generate_text_button_icon_data = importlib.resources.read_binary("resources.icons", "button-generate-text.ico")
        generate_text_button_icon_image = QImage.fromData(generate_text_button_icon_data)
        self.generate_text_button.setIcon(QIcon(QPixmap.fromImage(generate_text_button_icon_image)))

        generate_image_button_icon_data = importlib.resources.read_binary("resources.icons", "button-generate-image.ico")
        generate_image_button_icon_image = QImage.fromData(generate_image_button_icon_data)
        self.generate_image_button.setIcon(QIcon(QPixmap.fromImage(generate_image_button_icon_image)))

        # Connect signals to methods
        self.main_graphics_view.undoAvailable.connect(self.toolbar_ui.undo_button.setEnabled)
        self.main_graphics_view.redoAvailable.connect(self.toolbar_ui.redo_button.setEnabled)
        self.tts_mode_button.clicked.connect(self.toggle_tts_mode)
        self.stt_mode_button.clicked.connect(self.toggle_stt_mode)
        self.generate_text_button.clicked.connect(self.generate_response)
        self.generate_image_button.clicked.connect(self.generate_image)
        self.toolbar_ui.present_button.clicked.connect(self.set_present_mode)
        self.toolbar_ui.draw_button.clicked.connect(self.set_draw_mode)
        self.toolbar_ui.code_button.clicked.connect(self.set_code_mode)
        self.toolbar_ui.pencil_button.clicked.connect(self.main_graphics_view.set_pencil_tool)
        self.toolbar_ui.erase_button.clicked.connect(self.main_graphics_view.set_erase_tool)
        self.toolbar_ui.line_button.clicked.connect(self.main_graphics_view.set_line_tool)
        self.toolbar_ui.ellipse_button.clicked.connect(self.main_graphics_view.set_ellipse_tool)
        self.toolbar_ui.rectangle_button.clicked.connect(self.main_graphics_view.set_rectangle_tool)
        self.toolbar_ui.undo_button.clicked.connect(self.main_graphics_view.undo)
        self.toolbar_ui.redo_button.clicked.connect(self.main_graphics_view.redo)
        self.toolbar_ui.new_button.clicked.connect(self.main_graphics_view.clear)
        self.toolbar_ui.stroke_color_button.color_changed.connect(self.main_graphics_view.set_tool_color)        
        self.toolbar_ui.stroke_width_spin_box.valueChanged.connect(self.main_graphics_view.set_stroke_width)
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
    