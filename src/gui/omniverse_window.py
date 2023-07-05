# Form implementation generated from reading ui file 'src\gui\omniverse_window.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(701, 401)
        self.central_widget = QtWidgets.QWidget(parent=MainWindow)
        self.central_widget.setObjectName("central_widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.central_widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.central_layout = QtWidgets.QGridLayout()
        self.central_layout.setContentsMargins(2, 2, 2, 2)
        self.central_layout.setHorizontalSpacing(2)
        self.central_layout.setVerticalSpacing(0)
        self.central_layout.setObjectName("central_layout")
        self.central_stacked_widget = QtWidgets.QStackedWidget(parent=self.central_widget)
        self.central_stacked_widget.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.central_stacked_widget.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.central_stacked_widget.setObjectName("central_stacked_widget")
        self.main_grid_widget = QtWidgets.QWidget()
        self.main_grid_widget.setObjectName("main_grid_widget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.main_grid_widget)
        self.gridLayout_5.setContentsMargins(1, 1, 1, 1)
        self.gridLayout_5.setSpacing(1)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.central_stacked_widget.addWidget(self.main_grid_widget)
        self.code_view_widget = QtWidgets.QWidget()
        self.code_view_widget.setObjectName("code_view_widget")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.code_view_widget)
        self.gridLayout_8.setContentsMargins(1, 1, 1, 1)
        self.gridLayout_8.setSpacing(1)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.code_view_layout = QtWidgets.QGridLayout()
        self.code_view_layout.setContentsMargins(0, 0, 0, 0)
        self.code_view_layout.setSpacing(0)
        self.code_view_layout.setObjectName("code_view_layout")
        self.code_view_vertical_widget = QtWidgets.QWidget(parent=self.code_view_widget)
        self.code_view_vertical_widget.setObjectName("code_view_vertical_widget")
        self.code_view_vertical_layout = QtWidgets.QVBoxLayout(self.code_view_vertical_widget)
        self.code_view_vertical_layout.setContentsMargins(0, 0, 0, 0)
        self.code_view_vertical_layout.setSpacing(0)
        self.code_view_vertical_layout.setObjectName("code_view_vertical_layout")
        self.browsers_widget = QtWidgets.QWidget(parent=self.code_view_vertical_widget)
        self.browsers_widget.setObjectName("browsers_widget")
        self.code_widget = QtWidgets.QGridLayout(self.browsers_widget)
        self.code_widget.setContentsMargins(0, 0, 0, 0)
        self.code_widget.setSpacing(2)
        self.code_widget.setObjectName("code_widget")
        self.summary_label = QtWidgets.QLabel(parent=self.browsers_widget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.summary_label.setFont(font)
        self.summary_label.setObjectName("summary_label")
        self.code_widget.addWidget(self.summary_label, 2, 1, 1, 1)
        self.summary_browser = QtWidgets.QTextBrowser(parent=self.browsers_widget)
        self.summary_browser.setObjectName("summary_browser")
        self.code_widget.addWidget(self.summary_browser, 3, 1, 1, 1)
        self.knowledge_browser = QtWidgets.QTextBrowser(parent=self.browsers_widget)
        self.knowledge_browser.setObjectName("knowledge_browser")
        self.code_widget.addWidget(self.knowledge_browser, 3, 0, 1, 1)
        self.entity_label = QtWidgets.QLabel(parent=self.browsers_widget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.entity_label.setFont(font)
        self.entity_label.setObjectName("entity_label")
        self.code_widget.addWidget(self.entity_label, 0, 1, 1, 1)
        self.knowledge_label = QtWidgets.QLabel(parent=self.browsers_widget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.knowledge_label.setFont(font)
        self.knowledge_label.setObjectName("knowledge_label")
        self.code_widget.addWidget(self.knowledge_label, 2, 0, 1, 1)
        self.sentiment_browser = QtWidgets.QTextBrowser(parent=self.browsers_widget)
        self.sentiment_browser.setObjectName("sentiment_browser")
        self.code_widget.addWidget(self.sentiment_browser, 1, 0, 1, 1)
        self.sentiment_label = QtWidgets.QLabel(parent=self.browsers_widget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.sentiment_label.setFont(font)
        self.sentiment_label.setObjectName("sentiment_label")
        self.code_widget.addWidget(self.sentiment_label, 0, 0, 1, 1)
        self.entity_browser = QtWidgets.QTextBrowser(parent=self.browsers_widget)
        self.entity_browser.setObjectName("entity_browser")
        self.code_widget.addWidget(self.entity_browser, 1, 1, 1, 1)
        self.code_view_vertical_layout.addWidget(self.browsers_widget)
        self.code_view_layout.addWidget(self.code_view_vertical_widget, 0, 1, 1, 1)
        self.gridLayout_8.addLayout(self.code_view_layout, 0, 0, 1, 1)
        self.central_stacked_widget.addWidget(self.code_view_widget)
        self.central_layout.addWidget(self.central_stacked_widget, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.central_layout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.central_widget)
        self.chat_dockable_widget = QtWidgets.QDockWidget(parent=MainWindow)
        self.chat_dockable_widget.setFeatures(QtWidgets.QDockWidget.DockWidgetFeature.DockWidgetMovable)
        self.chat_dockable_widget.setAllowedAreas(QtCore.Qt.DockWidgetArea.LeftDockWidgetArea|QtCore.Qt.DockWidgetArea.RightDockWidgetArea)
        self.chat_dockable_widget.setObjectName("chat_dockable_widget")
        self.chat_dockable_widget_layout = QtWidgets.QWidget()
        self.chat_dockable_widget_layout.setObjectName("chat_dockable_widget_layout")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.chat_dockable_widget_layout)
        self.gridLayout_3.setContentsMargins(1, 1, 1, 1)
        self.gridLayout_3.setSpacing(1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.chat_stacked_widget = QtWidgets.QStackedWidget(parent=self.chat_dockable_widget_layout)
        self.chat_stacked_widget.setObjectName("chat_stacked_widget")
        self.chat_widget = QtWidgets.QWidget()
        self.chat_widget.setObjectName("chat_widget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.chat_widget)
        self.gridLayout_6.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_6.setSpacing(2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.chat_layout = QtWidgets.QGridLayout()
        self.chat_layout.setContentsMargins(1, 1, 1, 1)
        self.chat_layout.setSpacing(1)
        self.chat_layout.setObjectName("chat_layout")
        self.chat_input_layout = QtWidgets.QHBoxLayout()
        self.chat_input_layout.setContentsMargins(1, 1, 1, 1)
        self.chat_input_layout.setSpacing(1)
        self.chat_input_layout.setObjectName("chat_input_layout")
        self.chat_input_button_panel_1 = QtWidgets.QGridLayout()
        self.chat_input_button_panel_1.setContentsMargins(1, 1, 1, 1)
        self.chat_input_button_panel_1.setSpacing(1)
        self.chat_input_button_panel_1.setObjectName("chat_input_button_panel_1")
        self.stt_mode_button = QtWidgets.QPushButton(parent=self.chat_widget)
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
        self.tts_mode_button = QtWidgets.QPushButton(parent=self.chat_widget)
        self.tts_mode_button.setMinimumSize(QtCore.QSize(32, 32))
        self.tts_mode_button.setMaximumSize(QtCore.QSize(32, 32))
        self.tts_mode_button.setBaseSize(QtCore.QSize(32, 32))
        self.tts_mode_button.setText("")
        self.tts_mode_button.setObjectName("tts_mode_button")
        self.chat_input_button_panel_1.addWidget(self.tts_mode_button, 0, 0, 1, 1)
        self.chat_input_layout.addLayout(self.chat_input_button_panel_1)
        self.input_text_editor = QtWidgets.QTextEdit(parent=self.chat_widget)
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
        self.generate_image_button = QtWidgets.QPushButton(parent=self.chat_widget)
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
        self.generate_text_button = QtWidgets.QPushButton(parent=self.chat_widget)
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
        self.chat_layout.addLayout(self.chat_input_layout, 1, 1, 1, 1)
        self.response_text_browser = QtWidgets.QTextBrowser(parent=self.chat_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.response_text_browser.sizePolicy().hasHeightForWidth())
        self.response_text_browser.setSizePolicy(sizePolicy)
        self.response_text_browser.setMinimumSize(QtCore.QSize(100, 100))
        self.response_text_browser.setObjectName("response_text_browser")
        self.chat_layout.addWidget(self.response_text_browser, 0, 1, 1, 1)
        self.chat_layout.setRowStretch(0, 10)
        self.chat_layout.setRowStretch(1, 1)
        self.gridLayout_6.addLayout(self.chat_layout, 0, 0, 1, 1)
        self.chat_stacked_widget.addWidget(self.chat_widget)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.chat_stacked_widget.addWidget(self.page_2)
        self.gridLayout_3.addWidget(self.chat_stacked_widget, 0, 0, 1, 1)
        self.chat_dockable_widget.setWidget(self.chat_dockable_widget_layout)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.chat_dockable_widget)
        self.toolBar = QtWidgets.QToolBar(parent=MainWindow)
        self.toolBar.setMovable(False)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        self.actionNew = QtGui.QAction(parent=MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtGui.QAction(parent=MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtGui.QAction(parent=MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as = QtGui.QAction(parent=MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")

        self.retranslateUi(MainWindow)
        self.central_stacked_widget.setCurrentIndex(0)
        self.chat_stacked_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Omniverse Window"))
        self.summary_label.setText(_translate("MainWindow", "Summary"))
        self.entity_label.setText(_translate("MainWindow", "Entity"))
        self.knowledge_label.setText(_translate("MainWindow", "Knowledge"))
        self.sentiment_label.setText(_translate("MainWindow", "Sentiment"))
        self.chat_dockable_widget.setWindowTitle(_translate("MainWindow", "Chat"))
        self.stt_mode_button.setToolTip(_translate("MainWindow", "Speech To Text"))
        self.tts_mode_button.setToolTip(_translate("MainWindow", "Text To Speech"))
        self.generate_image_button.setToolTip(_translate("MainWindow", "Generate Image"))
        self.generate_text_button.setToolTip(_translate("MainWindow", "Send To Chat"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_as.setText(_translate("MainWindow", "Save as..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())