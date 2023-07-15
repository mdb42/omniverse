from gui.modes.mode_base import ModeBase
from gui.modes.canvas_mode.canvas_view import CanvasView
from gui.modes.canvas_mode.canvas_controls_widget import Ui_Form as CanvasControlUI
from PyQt6.QtCore import Qt
from PyQt6 import QtWidgets, QtGui
from PyQt6.QtWidgets import QHBoxLayout, QWidget
from gui.components.color_button import ColorButton
from gui.modes.canvas_mode.open_file_action import OpenFileAction
from gui.modes.canvas_mode.new_file_action import NewFileAction
from gui.modes.canvas_mode.save_file_action import SaveFileAction

from PyQt6.QtWidgets import QButtonGroup, QPushButton

class CanvasMode(ModeBase):
    def __init__(self, parent):   
        super().__init__(parent=parent,
                         name = "Canvas Mode",
                         description="Drawing tools for creating images", 
                         icon_filename="mode-canvas.ico",
                         display= CanvasView(),
                         control_ui= CanvasControlUI())

    def set_mode(self):        
        self.display.set_canvas_mode()
        pass

    def generate_tool_bars(self):
        tool_bars = { 
            "File": self.generate_file_tool_bar(),
            "Settings": self.generate_settings_tool_bar(),
            "Draw": self.generate_draw_tool_bar(self.display.draw_actions),
            "Edit": self.generate_edit_tool_bar(self.display.edit_actions),
        }
        return tool_bars

    def generate_file_tool_bar(self):
        tool_bar = QtWidgets.QToolBar()
        tool_bar.setContentsMargins(2,2,2,2)
        tool_bar.setOrientation(Qt.Orientation.Horizontal)
        self.file_action_button_group = QButtonGroup()
        actions = [NewFileAction(handler=self.new_file_handler), 
                   OpenFileAction(handler=self.open_file_handler), 
                   SaveFileAction(handler=self.save_file_handler)]
        
        for action in actions:
            tool_bar.addWidget(action.button)
            self.file_action_button_group.addButton(action.button)        
        return tool_bar


    def generate_settings_tool_bar(self):
        # Create the settings tool bar
        tool_bar = QtWidgets.QToolBar(self.parent)
        # The settings tool bar has components besides buttons, so we need to use a layout
        tool_bar_layout = QHBoxLayout()
        tool_bar_layout.setContentsMargins(2, 2, 2, 2)
        tool_bar_layout.setSpacing(2)
        tool_bar_widget = QWidget()
        tool_bar_widget.setLayout(tool_bar_layout)
        tool_bar.addWidget(tool_bar_widget)

        self.settings_button_group = QButtonGroup()
        self.fill_color_button = ColorButton()
        self.stroke_color_button = ColorButton()
        self.stroke_width_spin_box = QtWidgets.QSpinBox()
        self.settings_button_group.addButton(self.fill_color_button)
        self.settings_button_group.addButton(self.stroke_color_button)
        tool_bar_widget.layout().addWidget(self.fill_color_button)
        tool_bar_widget.layout().addWidget(self.stroke_color_button)
        tool_bar_widget.layout().addWidget(self.stroke_width_spin_box)
        
        tool_bar.setFloatable(False)
        tool_bar.setOrientation(Qt.Orientation.Horizontal)
        tool_bar.setHidden(False)

        self.fill_color_button.color_changed.connect(self.display.set_fill_color)
        self.fill_color_button.set_color(QtGui.QColor(255, 255, 255, 0))
        self.fill_color_button.setToolTip("Fill Color")

        self.stroke_color_button.color_changed.connect(self.display.set_stroke_color)
        self.stroke_color_button.set_color(QtGui.QColor(0, 0, 0))
        self.stroke_color_button.setToolTip("Stroke Color")

        self.stroke_width_spin_box.setRange(1, 10)
        self.stroke_width_spin_box.setValue(1)
        self.stroke_width_spin_box.setFixedSize(50, 32)
        self.stroke_width_spin_box.setContentsMargins(0,0,0,0)
        self.stroke_width_spin_box.valueChanged.connect(self.display.set_stroke_width)
        self.stroke_width_spin_box.setToolTip("Stroke Width")
        
        return tool_bar

    def generate_draw_tool_bar(self, actions):
        # Generate a toolbar for the display
        tool_bar = QtWidgets.QToolBar()
        tool_bar.setContentsMargins(2,2,2,2)
        tool_bar.setOrientation(Qt.Orientation.Horizontal)
        self.draw_action_button_group = QtWidgets.QButtonGroup()
        self.draw_action_button_group.setExclusive(True)
        self.draw_action_button_group.buttonClicked.connect(self.set_draw_tool)

        for i, action in enumerate(actions):
            tool_bar.addWidget(action.button)
            self.draw_action_button_group.addButton(action.button, i)
            if i==0: action.button.setChecked(True)

        return tool_bar
    
    def generate_edit_tool_bar(self, actions):
        # Create the edit tool bar
        tool_bar = QtWidgets.QToolBar(self.parent)
        self.edit_action_button_group = QButtonGroup()

        tool_bar.setFloatable(False)
        tool_bar.setContentsMargins(2,2,2,2)
        tool_bar.setOrientation(Qt.Orientation.Horizontal)

        for i, action in enumerate(actions):
            self.edit_action_button_group.addButton(action.button, i)
            tool_bar.addWidget(action.button)

        return tool_bar

    def set_draw_tool(self):
        self.display.set_draw_tool(self.draw_action_button_group.checkedId())

    def new_file_handler(self):
        print("New File")
        self.display.clear()
    
    def open_file_handler(self):
        print("Open File")
        file_name = QtWidgets.QFileDialog.getOpenFileName(self.parent, "Open File", "", "Image Files (*.png *.jpg *.bmp)")
        if file_name[0]:
            print("Attempting to open file: ", file_name[0])
        
    def save_file_handler(self):
        print("Save File")
        file_name = QtWidgets.QFileDialog.getSaveFileName(self.parent, "Save File", "", "Image Files (*.png *.jpg *.bmp)")
        if file_name[0]:
            print("Attempting to save file: ", file_name[0])


        
