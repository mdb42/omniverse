# Form implementation generated from reading ui file 'src/gui/omniverse_main.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(688, 433)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setContentsMargins(1, 1, 1, 1)
        self.gridLayout_2.setSpacing(1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.central_layout = QtWidgets.QGridLayout()
        self.central_layout.setContentsMargins(1, 1, 1, 1)
        self.central_layout.setSpacing(1)
        self.central_layout.setObjectName("central_layout")
        self.main_graphics_view = MainGraphicsView(parent=self.centralwidget)
        self.main_graphics_view.setObjectName("main_graphics_view")
        self.central_layout.addWidget(self.main_graphics_view, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.central_layout, 1, 0, 1, 1)
        self.toolbar_widget = QtWidgets.QWidget(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolbar_widget.sizePolicy().hasHeightForWidth())
        self.toolbar_widget.setSizePolicy(sizePolicy)
        self.toolbar_widget.setMinimumSize(QtCore.QSize(440, 40))
        self.toolbar_widget.setMaximumSize(QtCore.QSize(1920, 40))
        self.toolbar_widget.setObjectName("toolbar_widget")
        self.toolbar_layout = QtWidgets.QHBoxLayout(self.toolbar_widget)
        self.toolbar_layout.setContentsMargins(1, 1, 1, 1)
        self.toolbar_layout.setSpacing(1)
        self.toolbar_layout.setObjectName("toolbar_layout")
        self.mode_select_layout = QtWidgets.QHBoxLayout()
        self.mode_select_layout.setContentsMargins(1, 1, 1, 1)
        self.mode_select_layout.setSpacing(1)
        self.mode_select_layout.setObjectName("mode_select_layout")
        self.present_button = QtWidgets.QPushButton(parent=self.toolbar_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.present_button.sizePolicy().hasHeightForWidth())
        self.present_button.setSizePolicy(sizePolicy)
        self.present_button.setMinimumSize(QtCore.QSize(32, 32))
        self.present_button.setMaximumSize(QtCore.QSize(32, 32))
        self.present_button.setText("")
        self.present_button.setCheckable(True)
        self.present_button.setChecked(True)
        self.present_button.setAutoExclusive(True)
        self.present_button.setObjectName("present_button")
        self.mode_select_layout.addWidget(self.present_button)
        self.draw_button = QtWidgets.QPushButton(parent=self.toolbar_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.draw_button.sizePolicy().hasHeightForWidth())
        self.draw_button.setSizePolicy(sizePolicy)
        self.draw_button.setMinimumSize(QtCore.QSize(32, 32))
        self.draw_button.setMaximumSize(QtCore.QSize(32, 32))
        self.draw_button.setText("")
        self.draw_button.setCheckable(True)
        self.draw_button.setChecked(False)
        self.draw_button.setAutoExclusive(True)
        self.draw_button.setObjectName("draw_button")
        self.mode_select_layout.addWidget(self.draw_button)
        self.toolbar_layout.addLayout(self.mode_select_layout)
        self.draw_mode_widget = DrawModeWidget(parent=self.toolbar_widget)
        self.draw_mode_widget.setObjectName("draw_mode_widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.draw_mode_widget)
        self.horizontalLayout_4.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_4.setSpacing(1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.line = QtWidgets.QFrame(parent=self.draw_mode_widget)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_4.addWidget(self.line)
        self.clear_button = QtWidgets.QPushButton(parent=self.draw_mode_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clear_button.sizePolicy().hasHeightForWidth())
        self.clear_button.setSizePolicy(sizePolicy)
        self.clear_button.setMinimumSize(QtCore.QSize(32, 32))
        self.clear_button.setMaximumSize(QtCore.QSize(32, 32))
        self.clear_button.setText("")
        self.clear_button.setObjectName("clear_button")
        self.horizontalLayout_4.addWidget(self.clear_button)
        self.line_1 = QtWidgets.QFrame(parent=self.draw_mode_widget)
        self.line_1.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_1.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_1.setObjectName("line_1")
        self.horizontalLayout_4.addWidget(self.line_1)
        self.tool_customization_layout = QtWidgets.QHBoxLayout()
        self.tool_customization_layout.setContentsMargins(1, 1, 1, 1)
        self.tool_customization_layout.setSpacing(1)
        self.tool_customization_layout.setObjectName("tool_customization_layout")
        self.stroke_color_button = ColorButton(parent=self.draw_mode_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stroke_color_button.sizePolicy().hasHeightForWidth())
        self.stroke_color_button.setSizePolicy(sizePolicy)
        self.stroke_color_button.setMinimumSize(QtCore.QSize(32, 32))
        self.stroke_color_button.setMaximumSize(QtCore.QSize(32, 32))
        self.stroke_color_button.setText("")
        self.stroke_color_button.setObjectName("stroke_color_button")
        self.tool_customization_layout.addWidget(self.stroke_color_button)
        self.stroke_width_spin_box = QtWidgets.QSpinBox(parent=self.draw_mode_widget)
        self.stroke_width_spin_box.setMinimumSize(QtCore.QSize(44, 32))
        self.stroke_width_spin_box.setMaximumSize(QtCore.QSize(16777215, 32))
        self.stroke_width_spin_box.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.stroke_width_spin_box.setMinimum(1)
        self.stroke_width_spin_box.setMaximum(9)
        self.stroke_width_spin_box.setProperty("value", 1)
        self.stroke_width_spin_box.setObjectName("stroke_width_spin_box")
        self.tool_customization_layout.addWidget(self.stroke_width_spin_box)
        self.horizontalLayout_4.addLayout(self.tool_customization_layout)
        self.line_2 = QtWidgets.QFrame(parent=self.draw_mode_widget)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_4.addWidget(self.line_2)
        self.draw_tool_layout = QtWidgets.QHBoxLayout()
        self.draw_tool_layout.setContentsMargins(1, 1, 1, 1)
        self.draw_tool_layout.setSpacing(1)
        self.draw_tool_layout.setObjectName("draw_tool_layout")
        self.pencil_button = QtWidgets.QPushButton(parent=self.draw_mode_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pencil_button.sizePolicy().hasHeightForWidth())
        self.pencil_button.setSizePolicy(sizePolicy)
        self.pencil_button.setMinimumSize(QtCore.QSize(32, 32))
        self.pencil_button.setMaximumSize(QtCore.QSize(32, 32))
        self.pencil_button.setText("")
        self.pencil_button.setCheckable(True)
        self.pencil_button.setChecked(True)
        self.pencil_button.setAutoExclusive(True)
        self.pencil_button.setObjectName("pencil_button")
        self.draw_tool_layout.addWidget(self.pencil_button)
        self.erase_button = QtWidgets.QPushButton(parent=self.draw_mode_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.erase_button.sizePolicy().hasHeightForWidth())
        self.erase_button.setSizePolicy(sizePolicy)
        self.erase_button.setMinimumSize(QtCore.QSize(32, 32))
        self.erase_button.setMaximumSize(QtCore.QSize(32, 32))
        self.erase_button.setText("")
        self.erase_button.setCheckable(True)
        self.erase_button.setAutoExclusive(True)
        self.erase_button.setObjectName("erase_button")
        self.draw_tool_layout.addWidget(self.erase_button)
        self.line_button = QtWidgets.QPushButton(parent=self.draw_mode_widget)
        self.line_button.setMinimumSize(QtCore.QSize(32, 32))
        self.line_button.setMaximumSize(QtCore.QSize(32, 32))
        self.line_button.setText("")
        self.line_button.setCheckable(True)
        self.line_button.setAutoExclusive(True)
        self.line_button.setObjectName("line_button")
        self.draw_tool_layout.addWidget(self.line_button)
        self.ellipse_button = QtWidgets.QPushButton(parent=self.draw_mode_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ellipse_button.sizePolicy().hasHeightForWidth())
        self.ellipse_button.setSizePolicy(sizePolicy)
        self.ellipse_button.setMinimumSize(QtCore.QSize(32, 32))
        self.ellipse_button.setMaximumSize(QtCore.QSize(32, 32))
        self.ellipse_button.setText("")
        self.ellipse_button.setCheckable(True)
        self.ellipse_button.setAutoExclusive(True)
        self.ellipse_button.setObjectName("ellipse_button")
        self.draw_tool_layout.addWidget(self.ellipse_button)
        self.rectangle_button = QtWidgets.QPushButton(parent=self.draw_mode_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rectangle_button.sizePolicy().hasHeightForWidth())
        self.rectangle_button.setSizePolicy(sizePolicy)
        self.rectangle_button.setMinimumSize(QtCore.QSize(32, 32))
        self.rectangle_button.setMaximumSize(QtCore.QSize(32, 32))
        self.rectangle_button.setText("")
        self.rectangle_button.setCheckable(True)
        self.rectangle_button.setAutoExclusive(True)
        self.rectangle_button.setObjectName("rectangle_button")
        self.draw_tool_layout.addWidget(self.rectangle_button)
        self.horizontalLayout_4.addLayout(self.draw_tool_layout)
        self.line_3 = QtWidgets.QFrame(parent=self.draw_mode_widget)
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_4.addWidget(self.line_3)
        self.undo_redo_layout = QtWidgets.QHBoxLayout()
        self.undo_redo_layout.setContentsMargins(1, 1, 1, 1)
        self.undo_redo_layout.setSpacing(1)
        self.undo_redo_layout.setObjectName("undo_redo_layout")
        self.undo_button = QtWidgets.QPushButton(parent=self.draw_mode_widget)
        self.undo_button.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.undo_button.sizePolicy().hasHeightForWidth())
        self.undo_button.setSizePolicy(sizePolicy)
        self.undo_button.setMinimumSize(QtCore.QSize(32, 32))
        self.undo_button.setMaximumSize(QtCore.QSize(32, 32))
        self.undo_button.setText("")
        self.undo_button.setObjectName("undo_button")
        self.undo_redo_layout.addWidget(self.undo_button)
        self.redo_button = QtWidgets.QPushButton(parent=self.draw_mode_widget)
        self.redo_button.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.redo_button.sizePolicy().hasHeightForWidth())
        self.redo_button.setSizePolicy(sizePolicy)
        self.redo_button.setMinimumSize(QtCore.QSize(32, 32))
        self.redo_button.setMaximumSize(QtCore.QSize(32, 32))
        self.redo_button.setText("")
        self.redo_button.setObjectName("redo_button")
        self.undo_redo_layout.addWidget(self.redo_button)
        self.horizontalLayout_4.addLayout(self.undo_redo_layout)
        self.toolbar_layout.addWidget(self.draw_mode_widget)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.toolbar_layout.addItem(spacerItem)
        self.gridLayout_2.addWidget(self.toolbar_widget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.interactions_dockable_widget = QtWidgets.QDockWidget(parent=MainWindow)
        self.interactions_dockable_widget.setFeatures(QtWidgets.QDockWidget.DockWidgetFeature.NoDockWidgetFeatures)
        self.interactions_dockable_widget.setAllowedAreas(QtCore.Qt.DockWidgetArea.BottomDockWidgetArea|QtCore.Qt.DockWidgetArea.LeftDockWidgetArea|QtCore.Qt.DockWidgetArea.RightDockWidgetArea)
        self.interactions_dockable_widget.setObjectName("interactions_dockable_widget")
        self.interactions_widget = QtWidgets.QWidget()
        self.interactions_widget.setObjectName("interactions_widget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.interactions_widget)
        self.gridLayout_3.setContentsMargins(1, 1, 1, 1)
        self.gridLayout_3.setSpacing(1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.interactions_tab_widget = QtWidgets.QTabWidget(parent=self.interactions_widget)
        self.interactions_tab_widget.setObjectName("interactions_tab_widget")
        self.chat_tab = QtWidgets.QWidget()
        self.chat_tab.setObjectName("chat_tab")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.chat_tab)
        self.gridLayout_7.setContentsMargins(1, 1, 1, 1)
        self.gridLayout_7.setSpacing(1)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.chat_layout = QtWidgets.QGridLayout()
        self.chat_layout.setContentsMargins(1, 1, 1, 1)
        self.chat_layout.setSpacing(1)
        self.chat_layout.setObjectName("chat_layout")
        self.response_text_browser = QtWidgets.QTextBrowser(parent=self.chat_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.response_text_browser.sizePolicy().hasHeightForWidth())
        self.response_text_browser.setSizePolicy(sizePolicy)
        self.response_text_browser.setMinimumSize(QtCore.QSize(100, 100))
        self.response_text_browser.setObjectName("response_text_browser")
        self.chat_layout.addWidget(self.response_text_browser, 0, 0, 1, 1)
        self.chat_input_layout = QtWidgets.QHBoxLayout()
        self.chat_input_layout.setContentsMargins(1, 1, 1, 1)
        self.chat_input_layout.setSpacing(1)
        self.chat_input_layout.setObjectName("chat_input_layout")
        self.chat_input_button_panel_1 = QtWidgets.QGridLayout()
        self.chat_input_button_panel_1.setContentsMargins(1, 1, 1, 1)
        self.chat_input_button_panel_1.setSpacing(1)
        self.chat_input_button_panel_1.setObjectName("chat_input_button_panel_1")
        self.stt_mode_button = QtWidgets.QPushButton(parent=self.chat_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stt_mode_button.sizePolicy().hasHeightForWidth())
        self.stt_mode_button.setSizePolicy(sizePolicy)
        self.stt_mode_button.setMinimumSize(QtCore.QSize(32, 32))
        self.stt_mode_button.setMaximumSize(QtCore.QSize(32, 32))
        self.stt_mode_button.setBaseSize(QtCore.QSize(32, 32))
        self.stt_mode_button.setText("")
        self.stt_mode_button.setObjectName("stt_mode_button")
        self.chat_input_button_panel_1.addWidget(self.stt_mode_button, 1, 0, 1, 1)
        self.tts_mode_button = QtWidgets.QPushButton(parent=self.chat_tab)
        self.tts_mode_button.setMinimumSize(QtCore.QSize(32, 32))
        self.tts_mode_button.setMaximumSize(QtCore.QSize(32, 32))
        self.tts_mode_button.setBaseSize(QtCore.QSize(32, 32))
        self.tts_mode_button.setText("")
        self.tts_mode_button.setObjectName("tts_mode_button")
        self.chat_input_button_panel_1.addWidget(self.tts_mode_button, 0, 0, 1, 1)
        self.chat_input_layout.addLayout(self.chat_input_button_panel_1)
        self.input_text_editor = QtWidgets.QTextEdit(parent=self.chat_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.input_text_editor.sizePolicy().hasHeightForWidth())
        self.input_text_editor.setSizePolicy(sizePolicy)
        self.input_text_editor.setMinimumSize(QtCore.QSize(158, 40))
        self.input_text_editor.setObjectName("input_text_editor")
        self.chat_input_layout.addWidget(self.input_text_editor)
        self.chat_input_button_panel_2 = QtWidgets.QGridLayout()
        self.chat_input_button_panel_2.setContentsMargins(1, 1, 1, 1)
        self.chat_input_button_panel_2.setSpacing(1)
        self.chat_input_button_panel_2.setObjectName("chat_input_button_panel_2")
        self.generate_image_button = QtWidgets.QPushButton(parent=self.chat_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.generate_image_button.sizePolicy().hasHeightForWidth())
        self.generate_image_button.setSizePolicy(sizePolicy)
        self.generate_image_button.setMinimumSize(QtCore.QSize(32, 32))
        self.generate_image_button.setMaximumSize(QtCore.QSize(32, 32))
        self.generate_image_button.setBaseSize(QtCore.QSize(32, 32))
        self.generate_image_button.setText("")
        self.generate_image_button.setObjectName("generate_image_button")
        self.chat_input_button_panel_2.addWidget(self.generate_image_button, 2, 0, 1, 1)
        self.generate_text_button = QtWidgets.QPushButton(parent=self.chat_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.generate_text_button.sizePolicy().hasHeightForWidth())
        self.generate_text_button.setSizePolicy(sizePolicy)
        self.generate_text_button.setMinimumSize(QtCore.QSize(32, 32))
        self.generate_text_button.setMaximumSize(QtCore.QSize(32, 32))
        self.generate_text_button.setBaseSize(QtCore.QSize(32, 32))
        self.generate_text_button.setText("")
        self.generate_text_button.setObjectName("generate_text_button")
        self.chat_input_button_panel_2.addWidget(self.generate_text_button, 1, 0, 1, 1)
        self.chat_input_layout.addLayout(self.chat_input_button_panel_2)
        self.chat_layout.addLayout(self.chat_input_layout, 1, 0, 1, 1)
        self.chat_layout.setRowStretch(0, 10)
        self.chat_layout.setRowStretch(1, 1)
        self.gridLayout_7.addLayout(self.chat_layout, 1, 0, 1, 1)
        self.interactions_tab_widget.addTab(self.chat_tab, "")
        self.processes_tab = QtWidgets.QWidget()
        self.processes_tab.setObjectName("processes_tab")
        self.test_tab_layout = QtWidgets.QGridLayout(self.processes_tab)
        self.test_tab_layout.setContentsMargins(1, 1, 1, 1)
        self.test_tab_layout.setSpacing(1)
        self.test_tab_layout.setObjectName("test_tab_layout")
        self.processes_layout = QtWidgets.QGridLayout()
        self.processes_layout.setObjectName("processes_layout")
        self.sentiment_label = QtWidgets.QLabel(parent=self.processes_tab)
        self.sentiment_label.setObjectName("sentiment_label")
        self.processes_layout.addWidget(self.sentiment_label, 0, 0, 1, 1)
        self.sentiment_browser = QtWidgets.QTextBrowser(parent=self.processes_tab)
        self.sentiment_browser.setObjectName("sentiment_browser")
        self.processes_layout.addWidget(self.sentiment_browser, 1, 0, 1, 1)
        self.entity_browser = QtWidgets.QTextBrowser(parent=self.processes_tab)
        self.entity_browser.setObjectName("entity_browser")
        self.processes_layout.addWidget(self.entity_browser, 3, 0, 1, 1)
        self.knowledge_label = QtWidgets.QLabel(parent=self.processes_tab)
        self.knowledge_label.setObjectName("knowledge_label")
        self.processes_layout.addWidget(self.knowledge_label, 4, 0, 1, 1)
        self.summary_browser = QtWidgets.QTextBrowser(parent=self.processes_tab)
        self.summary_browser.setObjectName("summary_browser")
        self.processes_layout.addWidget(self.summary_browser, 7, 0, 1, 1)
        self.entity_label = QtWidgets.QLabel(parent=self.processes_tab)
        self.entity_label.setObjectName("entity_label")
        self.processes_layout.addWidget(self.entity_label, 2, 0, 1, 1)
        self.knowledge_browser = QtWidgets.QTextBrowser(parent=self.processes_tab)
        self.knowledge_browser.setObjectName("knowledge_browser")
        self.processes_layout.addWidget(self.knowledge_browser, 5, 0, 1, 1)
        self.summary_label = QtWidgets.QLabel(parent=self.processes_tab)
        self.summary_label.setObjectName("summary_label")
        self.processes_layout.addWidget(self.summary_label, 6, 0, 1, 1)
        self.test_tab_layout.addLayout(self.processes_layout, 0, 0, 1, 1)
        self.interactions_tab_widget.addTab(self.processes_tab, "")
        self.controls_tab = QtWidgets.QWidget()
        self.controls_tab.setObjectName("controls_tab")
        self.gridLayout = QtWidgets.QGridLayout(self.controls_tab)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.user_name_label_2 = QtWidgets.QLabel(parent=self.controls_tab)
        self.user_name_label_2.setObjectName("user_name_label_2")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.user_name_label_2)
        self.ai_name_label_2 = QtWidgets.QLabel(parent=self.controls_tab)
        self.ai_name_label_2.setObjectName("ai_name_label_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.ai_name_label_2)
        self.user_name_line_edit_2 = QtWidgets.QLineEdit(parent=self.controls_tab)
        self.user_name_line_edit_2.setObjectName("user_name_line_edit_2")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.user_name_line_edit_2)
        self.ai_name_line_edit_2 = QtWidgets.QLineEdit(parent=self.controls_tab)
        self.ai_name_line_edit_2.setObjectName("ai_name_line_edit_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.ai_name_line_edit_2)
        self.verticalLayout_5.addLayout(self.formLayout_2)
        self.language_model_label_2 = QtWidgets.QLabel(parent=self.controls_tab)
        self.language_model_label_2.setObjectName("language_model_label_2")
        self.verticalLayout_5.addWidget(self.language_model_label_2)
        self.language_model_combo_box_2 = QtWidgets.QComboBox(parent=self.controls_tab)
        self.language_model_combo_box_2.setObjectName("language_model_combo_box_2")
        self.verticalLayout_5.addWidget(self.language_model_combo_box_2)
        self.protocol_label_2 = QtWidgets.QLabel(parent=self.controls_tab)
        self.protocol_label_2.setObjectName("protocol_label_2")
        self.verticalLayout_5.addWidget(self.protocol_label_2)
        self.protocol_combo_box_2 = QtWidgets.QComboBox(parent=self.controls_tab)
        self.protocol_combo_box_2.setObjectName("protocol_combo_box_2")
        self.verticalLayout_5.addWidget(self.protocol_combo_box_2)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.temperature_label_2 = QtWidgets.QLabel(parent=self.controls_tab)
        self.temperature_label_2.setObjectName("temperature_label_2")
        self.verticalLayout_6.addWidget(self.temperature_label_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(5, 5, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.temperature_slider_2 = QtWidgets.QSlider(parent=self.controls_tab)
        self.temperature_slider_2.setMaximum(20)
        self.temperature_slider_2.setProperty("value", 1)
        self.temperature_slider_2.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.temperature_slider_2.setObjectName("temperature_slider_2")
        self.horizontalLayout.addWidget(self.temperature_slider_2)
        spacerItem2 = QtWidgets.QSpacerItem(5, 5, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.verticalLayout_5.addLayout(self.verticalLayout_6)
        self.verticalLayout_4.addLayout(self.verticalLayout_5)
        self.gridLayout.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem3, 1, 0, 1, 1)
        self.interactions_tab_widget.addTab(self.controls_tab, "")
        self.gridLayout_3.addWidget(self.interactions_tab_widget, 0, 1, 1, 1)
        self.interactions_dockable_widget.setWidget(self.interactions_widget)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.interactions_dockable_widget)
        self.actionNew = QtGui.QAction(parent=MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtGui.QAction(parent=MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtGui.QAction(parent=MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as = QtGui.QAction(parent=MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")

        self.retranslateUi(MainWindow)
        self.interactions_tab_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.present_button.setToolTip(_translate("MainWindow", "Presentation Mode"))
        self.draw_button.setToolTip(_translate("MainWindow", "Draw Mode"))
        self.clear_button.setToolTip(_translate("MainWindow", "Clear"))
        self.stroke_color_button.setToolTip(_translate("MainWindow", "Stroke Color"))
        self.stroke_width_spin_box.setToolTip(_translate("MainWindow", "Stroke Width"))
        self.pencil_button.setToolTip(_translate("MainWindow", "Pencil Tool"))
        self.erase_button.setToolTip(_translate("MainWindow", "Eraser Tool"))
        self.line_button.setToolTip(_translate("MainWindow", "Line Tool"))
        self.ellipse_button.setToolTip(_translate("MainWindow", "Ellipse Tool"))
        self.rectangle_button.setToolTip(_translate("MainWindow", "Rectangle Tool"))
        self.undo_button.setToolTip(_translate("MainWindow", "Undo"))
        self.redo_button.setToolTip(_translate("MainWindow", "Redo"))
        self.interactions_dockable_widget.setWindowTitle(_translate("MainWindow", "Interactions"))
        self.stt_mode_button.setToolTip(_translate("MainWindow", "Speech To Text"))
        self.tts_mode_button.setToolTip(_translate("MainWindow", "Text To Speech"))
        self.generate_image_button.setToolTip(_translate("MainWindow", "Generate Image"))
        self.generate_text_button.setToolTip(_translate("MainWindow", "Send To Chat"))
        self.interactions_tab_widget.setTabText(self.interactions_tab_widget.indexOf(self.chat_tab), _translate("MainWindow", "Chat"))
        self.sentiment_label.setText(_translate("MainWindow", "Sentiment"))
        self.knowledge_label.setText(_translate("MainWindow", "Knowledge"))
        self.entity_label.setText(_translate("MainWindow", "Entity"))
        self.summary_label.setText(_translate("MainWindow", "Summary"))
        self.interactions_tab_widget.setTabText(self.interactions_tab_widget.indexOf(self.processes_tab), _translate("MainWindow", "Processes"))
        self.user_name_label_2.setText(_translate("MainWindow", "User:"))
        self.ai_name_label_2.setText(_translate("MainWindow", "AI:"))
        self.language_model_label_2.setText(_translate("MainWindow", "Language Model:"))
        self.protocol_label_2.setText(_translate("MainWindow", "Protocol:"))
        self.temperature_label_2.setText(_translate("MainWindow", "Temperature: 0.1"))
        self.interactions_tab_widget.setTabText(self.interactions_tab_widget.indexOf(self.controls_tab), _translate("MainWindow", "Controls"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_as.setText(_translate("MainWindow", "Save as..."))
from src.gui.color_button import ColorButton
from src.gui.draw_mode_widget import DrawModeWidget
from src.gui.main_graphics_view import MainGraphicsView


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
