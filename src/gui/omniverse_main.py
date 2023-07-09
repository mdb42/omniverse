# Form implementation generated from reading ui file 'src\gui\omniverse_main.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(832, 553)
        self.main_widget = QtWidgets.QWidget(parent=MainWindow)
        self.main_widget.setObjectName("main_widget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.main_widget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.main_splitter = QtWidgets.QSplitter(parent=self.main_widget)
        self.main_splitter.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.main_splitter.setObjectName("main_splitter")
        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.main_splitter)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.controls_layout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.controls_layout.setContentsMargins(0, 0, 0, 0)
        self.controls_layout.setObjectName("controls_layout")
        self.controls_stacked_widget = QtWidgets.QStackedWidget(parent=self.gridLayoutWidget)
        self.controls_stacked_widget.setObjectName("controls_stacked_widget")
        self.presentation_controls_page = QtWidgets.QWidget()
        self.presentation_controls_page.setObjectName("presentation_controls_page")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.presentation_controls_page)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.presentation_controls_layout = QtWidgets.QGridLayout()
        self.presentation_controls_layout.setObjectName("presentation_controls_layout")
        self.gridLayout_6.addLayout(self.presentation_controls_layout, 0, 0, 1, 1)
        self.controls_stacked_widget.addWidget(self.presentation_controls_page)
        self.canvas_controls_page = QtWidgets.QWidget()
        self.canvas_controls_page.setObjectName("canvas_controls_page")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.canvas_controls_page)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.canvas_controls_layout = QtWidgets.QGridLayout()
        self.canvas_controls_layout.setObjectName("canvas_controls_layout")
        self.gridLayout_14.addLayout(self.canvas_controls_layout, 0, 0, 1, 1)
        self.controls_stacked_widget.addWidget(self.canvas_controls_page)
        self.blueprint_controls_page = QtWidgets.QWidget()
        self.blueprint_controls_page.setObjectName("blueprint_controls_page")
        self.gridLayout_20 = QtWidgets.QGridLayout(self.blueprint_controls_page)
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.blueprint_controls_layout = QtWidgets.QGridLayout()
        self.blueprint_controls_layout.setObjectName("blueprint_controls_layout")
        self.gridLayout_20.addLayout(self.blueprint_controls_layout, 0, 0, 1, 1)
        self.controls_stacked_widget.addWidget(self.blueprint_controls_page)
        self.controls_layout.addWidget(self.controls_stacked_widget, 0, 0, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(parent=self.main_splitter)
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.displays_layout = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.displays_layout.setContentsMargins(0, 0, 0, 0)
        self.displays_layout.setObjectName("displays_layout")
        self.displays_stacked_widget = QtWidgets.QStackedWidget(parent=self.gridLayoutWidget_2)
        self.displays_stacked_widget.setObjectName("displays_stacked_widget")
        self.presentation_view_page = QtWidgets.QWidget()
        self.presentation_view_page.setObjectName("presentation_view_page")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.presentation_view_page)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.presentation_view_layout = QtWidgets.QGridLayout()
        self.presentation_view_layout.setObjectName("presentation_view_layout")
        self.gridLayout_8.addLayout(self.presentation_view_layout, 0, 0, 1, 1)
        self.displays_stacked_widget.addWidget(self.presentation_view_page)
        self.canvas_view_page = QtWidgets.QWidget()
        self.canvas_view_page.setObjectName("canvas_view_page")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.canvas_view_page)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.canvas_view_layout = QtWidgets.QGridLayout()
        self.canvas_view_layout.setObjectName("canvas_view_layout")
        self.gridLayout_15.addLayout(self.canvas_view_layout, 0, 0, 1, 1)
        self.displays_stacked_widget.addWidget(self.canvas_view_page)
        self.blueprint_view_page = QtWidgets.QWidget()
        self.blueprint_view_page.setObjectName("blueprint_view_page")
        self.gridLayout_21 = QtWidgets.QGridLayout(self.blueprint_view_page)
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.blueprint_view_layout = QtWidgets.QGridLayout()
        self.blueprint_view_layout.setObjectName("blueprint_view_layout")
        self.gridLayout_21.addLayout(self.blueprint_view_layout, 0, 0, 1, 1)
        self.displays_stacked_widget.addWidget(self.blueprint_view_page)
        self.displays_layout.addWidget(self.displays_stacked_widget, 0, 0, 1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(parent=self.main_splitter)
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.chat_layout = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.chat_layout.setContentsMargins(0, 0, 0, 0)
        self.chat_layout.setObjectName("chat_layout")
        self.chat_stacked_widget = QtWidgets.QStackedWidget(parent=self.gridLayoutWidget_3)
        self.chat_stacked_widget.setObjectName("chat_stacked_widget")
        self.chat_interface_page = QtWidgets.QWidget()
        self.chat_interface_page.setObjectName("chat_interface_page")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.chat_interface_page)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.chat_interface_layout = QtWidgets.QGridLayout()
        self.chat_interface_layout.setObjectName("chat_interface_layout")
        self.gridLayout_10.addLayout(self.chat_interface_layout, 0, 0, 1, 1)
        self.chat_stacked_widget.addWidget(self.chat_interface_page)
        self.chat_test_page = QtWidgets.QWidget()
        self.chat_test_page.setObjectName("chat_test_page")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.chat_test_page)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.chat_test_layout = QtWidgets.QGridLayout()
        self.chat_test_layout.setObjectName("chat_test_layout")
        self.gridLayout_16.addLayout(self.chat_test_layout, 0, 0, 1, 1)
        self.chat_stacked_widget.addWidget(self.chat_test_page)
        self.chat_layout.addWidget(self.chat_stacked_widget, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.main_splitter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.main_widget)
        self.menu_bar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 832, 21))
        self.menu_bar.setObjectName("menu_bar")
        self.menu_file = QtWidgets.QMenu(parent=self.menu_bar)
        self.menu_file.setObjectName("menu_file")
        self.menu_edit = QtWidgets.QMenu(parent=self.menu_bar)
        self.menu_edit.setObjectName("menu_edit")
        self.menu_view = QtWidgets.QMenu(parent=self.menu_bar)
        self.menu_view.setObjectName("menu_view")
        self.menu_settings = QtWidgets.QMenu(parent=self.menu_bar)
        self.menu_settings.setObjectName("menu_settings")
        self.menu_window = QtWidgets.QMenu(parent=self.menu_bar)
        self.menu_window.setObjectName("menu_window")
        self.menu_help = QtWidgets.QMenu(parent=self.menu_bar)
        self.menu_help.setObjectName("menu_help")
        MainWindow.setMenuBar(self.menu_bar)
        self.status_bar = QtWidgets.QStatusBar(parent=MainWindow)
        self.status_bar.setObjectName("status_bar")
        MainWindow.setStatusBar(self.status_bar)
        self.tool_bar = QtWidgets.QToolBar(parent=MainWindow)
        self.tool_bar.setObjectName("tool_bar")
        MainWindow.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.tool_bar)
        self.action_about = QtGui.QAction(parent=MainWindow)
        self.action_about.setObjectName("action_about")
        self.menu_help.addAction(self.action_about)
        self.menu_bar.addAction(self.menu_file.menuAction())
        self.menu_bar.addAction(self.menu_edit.menuAction())
        self.menu_bar.addAction(self.menu_view.menuAction())
        self.menu_bar.addAction(self.menu_settings.menuAction())
        self.menu_bar.addAction(self.menu_window.menuAction())
        self.menu_bar.addAction(self.menu_help.menuAction())

        self.retranslateUi(MainWindow)
        self.chat_stacked_widget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menu_file.setTitle(_translate("MainWindow", "File"))
        self.menu_edit.setTitle(_translate("MainWindow", "Edit"))
        self.menu_view.setTitle(_translate("MainWindow", "View"))
        self.menu_settings.setTitle(_translate("MainWindow", "Settings"))
        self.menu_window.setTitle(_translate("MainWindow", "Window"))
        self.menu_help.setTitle(_translate("MainWindow", "Help"))
        self.tool_bar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.action_about.setText(_translate("MainWindow", "About"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())