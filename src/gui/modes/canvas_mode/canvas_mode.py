from src.gui.modes.mode_base import AbstractMode
from src.gui.modes.canvas_mode.canvas_view import CanvasView
from src.gui.modes.canvas_mode.canvas_controls_widget import Ui_Form as CanvasControlUI
from src.gui.modes.canvas_mode.pencil_tool import PencilTool, PencilTool
from src.gui.modes.canvas_mode.eraser_tool import EraserTool
from src.gui.modes.canvas_mode.line_tool import LineTool
from src.gui.modes.canvas_mode.ellipse_tool import EllipseTool
from src.gui.modes.canvas_mode.rect_tool import RectTool
from src.gui.modes.canvas_mode.image_tool import ImageTool
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import Qt
from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtWidgets import QHBoxLayout, QGridLayout, QToolButton, QPushButton, QWidget
from src.gui.components.color_button import ColorButton

#QButton?
from PyQt6.QtWidgets import QButtonGroup, QPushButton



class CanvasMode(AbstractMode):
    def __init__(self, parent):   
        super().__init__(parent=parent,
                         description="Canvas Mode", 
                         icon_filename="mode-canvas.ico",
                         display= CanvasView(),
                         control_ui= CanvasControlUI())
        
        # Create the file tool bar
        self.file_tool_bar = QtWidgets.QToolBar(self.parent)
        self.file_tool_button_group = QButtonGroup()
        self.new_button = QPushButton()
        self.open_button = QPushButton()
        self.save_button = QPushButton()
        self.file_tool_button_group.addButton(self.new_button)
        self.file_tool_button_group.addButton(self.open_button)
        self.file_tool_button_group.addButton(self.save_button)

        self.file_tool_bar.setFloatable(False)
        self.file_tool_bar.setOrientation(Qt.Orientation.Horizontal)
        self.file_tool_bar.setHidden(False)
        self.file_tool_bar.setContentsMargins(2,2,2,2)

        self.new_button.setIcon(QIcon(self.load_icon("button-new.ico")))
        self.new_button.setToolTip("Clear Canvas")
        self.new_button.setFixedSize(32, 32)
        self.new_button.clicked.connect(self.display.clear)
        self.file_tool_bar.addWidget(self.new_button)

        self.open_button.setIcon(QIcon(self.load_icon("button-open.ico")))
        self.open_button.setToolTip("Open Image")
        self.open_button.setFixedSize(32, 32)
        self.open_button.setContentsMargins(2,2,2,2)
        self.file_tool_bar.addWidget(self.open_button)

        self.save_button.setIcon(QIcon(self.load_icon("button-save.ico")))
        self.save_button.setToolTip("Save Image")
        self.save_button.setFixedSize(32, 32)
        self.save_button.setContentsMargins(2,2,2,2)
        self.file_tool_bar.addWidget(self.save_button)

        # Create the settings tool bar
        self.settings_tool_bar = QtWidgets.QToolBar(self.parent)
        # The settings tool bar has other things besides buttons, so we need to use a layout
        self.settings_tool_bar_layout = QHBoxLayout()
        self.settings_tool_bar_layout.setContentsMargins(2, 2, 2, 2)
        self.settings_tool_bar_layout.setSpacing(2)
        self.settings_tool_bar_widget = QWidget()
        self.settings_tool_bar_widget.setLayout(self.settings_tool_bar_layout)
        self.settings_tool_bar.addWidget(self.settings_tool_bar_widget)

        self.settings_tool_button_group = QButtonGroup()
        self.fill_color_button = ColorButton()
        self.stroke_color_button = ColorButton()
        self.stroke_width_spin_box = QtWidgets.QSpinBox()
        self.settings_tool_button_group.addButton(self.fill_color_button)
        self.settings_tool_button_group.addButton(self.stroke_color_button)
        self.settings_tool_bar_widget.layout().addWidget(self.fill_color_button)
        self.settings_tool_bar_widget.layout().addWidget(self.stroke_color_button)
        self.settings_tool_bar_widget.layout().addWidget(self.stroke_width_spin_box)
        
        self.settings_tool_bar.setFloatable(False)
        self.settings_tool_bar.setOrientation(Qt.Orientation.Horizontal)
        self.settings_tool_bar.setHidden(False)
        # self.settings_tool_bar.setContentsMargins(2,2,2,2)

        self.fill_color_button.color_changed.connect(self.display.set_tool_color)
        self.fill_color_button.set_color(QtGui.QColor(255, 255, 255))
        self.fill_color_button.setFixedSize(32, 32)
        self.fill_color_button.setContentsMargins(0,0,0,0)

        self.stroke_color_button.color_changed.connect(self.display.set_tool_color)
        self.stroke_color_button.set_color(QtGui.QColor(0, 0, 0))
        self.stroke_color_button.setFixedSize(32, 32)
        self.stroke_color_button.setContentsMargins(0,0,0,0)

        self.stroke_width_spin_box.setRange(1, 10)
        self.stroke_width_spin_box.setValue(1)
        self.stroke_width_spin_box.setFixedSize(50, 32)
        self.stroke_width_spin_box.setContentsMargins(0,0,0,0)
        self.stroke_width_spin_box.valueChanged.connect(self.display.set_stroke_width)

        # Create the display tool bar
        self.display_tool_bar = QtWidgets.QToolBar(self.parent)
        self.display_tool_button_group = QButtonGroup()
        self.pencil_button = QPushButton()
        self.eraser_button = QPushButton()
        self.rect_button = QPushButton()
        self.ellipse_button = QPushButton()
        self.line_button = QPushButton()
        self.image_button = QPushButton()
        self.display_tool_button_group.addButton(self.pencil_button)
        self.display_tool_button_group.addButton(self.eraser_button)
        self.display_tool_button_group.addButton(self.rect_button)
        self.display_tool_button_group.addButton(self.ellipse_button)
        self.display_tool_button_group.addButton(self.line_button)
        self.display_tool_button_group.addButton(self.image_button)
        self.display_tool_button_group.setExclusive(True)

        self.display_tool_bar.setFloatable(False)
        self.display_tool_bar.setContentsMargins(2,2,2,2)
        self.display_tool_bar.setOrientation(Qt.Orientation.Horizontal)
        self.display_tool_bar.setHidden(False)

        self.pencil_button.setIcon(QIcon(self.load_icon("tool-pencil.ico")))
        self.pencil_button.setToolTip("Pencil Tool")
        self.pencil_button.setFixedSize(32, 32)
        self.pencil_button.setContentsMargins(2,2,2,2)
        self.pencil_button.clicked.connect(self.display.set_pencil_tool)
        self.pencil_button.setCheckable(True)
        self.pencil_button.setChecked(True)
        self.display_tool_bar.addWidget(self.pencil_button)
        
        self.eraser_button.setIcon(QIcon(self.load_icon("tool-eraser.ico")))
        self.eraser_button.setToolTip("Eraser Tool")
        self.eraser_button.setFixedSize(32, 32)
        self.eraser_button.setContentsMargins(2,2,2,2)
        self.eraser_button.clicked.connect(self.display.set_erase_tool)
        self.eraser_button.setCheckable(True)
        self.display_tool_bar.addWidget(self.eraser_button)

        self.rect_button.setIcon(QIcon(self.load_icon("tool-square.ico")))
        self.rect_button.setToolTip("Rectangle Tool")
        self.rect_button.setFixedSize(32, 32)
        self.rect_button.setContentsMargins(2,2,2,2)
        self.rect_button.clicked.connect(self.display.set_rectangle_tool)
        self.rect_button.setCheckable(True)
        self.display_tool_bar.addWidget(self.rect_button)

        self.ellipse_button.setIcon(QIcon(self.load_icon("tool-circle.ico")))
        self.ellipse_button.setToolTip("Ellipse Tool")
        self.ellipse_button.setFixedSize(32, 32)
        self.ellipse_button.setContentsMargins(2,2,2,2)
        self.ellipse_button.clicked.connect(self.display.set_ellipse_tool)
        self.ellipse_button.setCheckable(True)
        self.display_tool_bar.addWidget(self.ellipse_button)

        self.line_button.setIcon(QIcon(self.load_icon("tool-line.ico")))
        self.line_button.setToolTip("Line Tool")
        self.line_button.setFixedSize(32, 32)
        self.line_button.setContentsMargins(2,2,2,2)
        self.line_button.clicked.connect(self.display.set_line_tool)
        self.line_button.setCheckable(True)
        self.display_tool_bar.addWidget(self.line_button)
        
        self.image_button.setIcon(QIcon(self.load_icon("tool-image.ico")))
        self.image_button.setToolTip("Image Tool")
        self.image_button.setFixedSize(32, 32)
        self.image_button.setContentsMargins(2,2,2,2)
        self.image_button.clicked.connect(self.display.set_image_tool)
        self.image_button.setCheckable(True)
        self.display_tool_bar.addWidget(self.image_button)

        # Create the edit tool bar
        self.edit_tool_bar = QtWidgets.QToolBar(self.parent)
        self.edit_tool_button_group = QButtonGroup()
        self.undo_button = QPushButton()
        self.redo_button = QPushButton()
        self.edit_tool_button_group.addButton(self.undo_button)
        self.edit_tool_button_group.addButton(self.redo_button)

        self.edit_tool_bar.setFloatable(False)
        self.edit_tool_bar.setContentsMargins(2,2,2,2)
        self.edit_tool_bar.setOrientation(Qt.Orientation.Horizontal)
        self.edit_tool_bar.setHidden(False)

        self.undo_button.setIcon(QIcon(self.load_icon("button-undo.ico")))
        self.undo_button.setToolTip("Undo")
        self.undo_button.setFixedSize(32, 32)
        self.undo_button.setContentsMargins(2,2,2,2)
        self.undo_button.clicked.connect(self.display.undo)
        self.display.undoAvailable.connect(self.undo_button.setEnabled)
        self.undo_button.setEnabled(False)
        self.edit_tool_bar.addWidget(self.undo_button)

        self.redo_button.setIcon(QIcon(self.load_icon("button-redo.ico")))
        self.redo_button.setToolTip("Redo")
        self.redo_button.setFixedSize(32, 32)
        self.redo_button.setContentsMargins(2,2,2,2)    
        self.redo_button.clicked.connect(self.display.redo)
        self.display.redoAvailable.connect(self.redo_button.setEnabled)
        self.redo_button.setEnabled(False)
        self.edit_tool_bar.addWidget(self.redo_button)

        self.tool_bars = { 
            "File": self.file_tool_bar,
            "Settings": self.settings_tool_bar,
            "Display": self.display_tool_bar,
            "Edit": self.edit_tool_bar,
        }
        
    def set_mode(self):
        pass

        
