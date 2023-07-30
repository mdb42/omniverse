# Form implementation generated from reading ui file 'gui\omniverse_main.ui'
#
# Created by: PyQt6 UI code generator 6.5.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 360)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.main_widget = QtWidgets.QWidget(parent=MainWindow)
        self.main_widget.setObjectName("main_widget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.main_widget)
        self.gridLayout_4.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.main_splitter = QtWidgets.QSplitter(parent=self.main_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_splitter.sizePolicy().hasHeightForWidth())
        self.main_splitter.setSizePolicy(sizePolicy)
        self.main_splitter.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.main_splitter.setObjectName("main_splitter")
        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.main_splitter)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.controls_layout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.controls_layout.setContentsMargins(0, 0, 0, 0)
        self.controls_layout.setSpacing(0)
        self.controls_layout.setObjectName("controls_layout")
        self.controls_stacked_widget = QtWidgets.QStackedWidget(parent=self.gridLayoutWidget)
        self.controls_stacked_widget.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.controls_stacked_widget.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.controls_stacked_widget.setObjectName("controls_stacked_widget")
        self.controls_layout.addWidget(self.controls_stacked_widget, 0, 0, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(parent=self.main_splitter)
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.displays_layout = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.displays_layout.setContentsMargins(0, 0, 0, 0)
        self.displays_layout.setSpacing(0)
        self.displays_layout.setObjectName("displays_layout")
        self.displays_stacked_widget = QtWidgets.QStackedWidget(parent=self.gridLayoutWidget_2)
        self.displays_stacked_widget.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.displays_stacked_widget.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.displays_stacked_widget.setObjectName("displays_stacked_widget")
        self.displays_layout.addWidget(self.displays_stacked_widget, 0, 0, 1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(parent=self.main_splitter)
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.chat_layout = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.chat_layout.setContentsMargins(0, 0, 0, 0)
        self.chat_layout.setSpacing(0)
        self.chat_layout.setObjectName("chat_layout")
        self.chat_stacked_widget = QtWidgets.QStackedWidget(parent=self.gridLayoutWidget_3)
        self.chat_stacked_widget.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.chat_stacked_widget.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.chat_stacked_widget.setObjectName("chat_stacked_widget")
        self.chat_layout.addWidget(self.chat_stacked_widget, 1, 0, 1, 1)
        self.gridLayout_4.addWidget(self.main_splitter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.main_widget)
        self.status_bar = QtWidgets.QStatusBar(parent=MainWindow)
        self.status_bar.setObjectName("status_bar")
        MainWindow.setStatusBar(self.status_bar)
        self.action_about = QtGui.QAction(parent=MainWindow)
        self.action_about.setObjectName("action_about")
        self.actionMaximize = QtGui.QAction(parent=MainWindow)
        self.actionMaximize.setObjectName("actionMaximize")
        self.actionRestore = QtGui.QAction(parent=MainWindow)
        self.actionRestore.setObjectName("actionRestore")
        self.actionMinimize = QtGui.QAction(parent=MainWindow)
        self.actionMinimize.setObjectName("actionMinimize")
        self.actionClose = QtGui.QAction(parent=MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.action_dark_mode = QtGui.QAction(parent=MainWindow)
        self.action_dark_mode.setCheckable(True)
        self.action_dark_mode.setObjectName("action_dark_mode")
        self.action_new = QtGui.QAction(parent=MainWindow)
        self.action_new.setObjectName("action_new")
        self.action_open = QtGui.QAction(parent=MainWindow)
        self.action_open.setObjectName("action_open")
        self.action_recent = QtGui.QAction(parent=MainWindow)
        self.action_recent.setObjectName("action_recent")
        self.action_save = QtGui.QAction(parent=MainWindow)
        self.action_save.setObjectName("action_save")
        self.action_save_as = QtGui.QAction(parent=MainWindow)
        self.action_save_as.setObjectName("action_save_as")
        self.action_workspace = QtGui.QAction(parent=MainWindow)
        self.action_workspace.setObjectName("action_workspace")
        self.action_users = QtGui.QAction(parent=MainWindow)
        self.action_users.setObjectName("action_users")
        self.action_developer = QtGui.QAction(parent=MainWindow)
        self.action_developer.setObjectName("action_developer")
        self.action_reset_zoom = QtGui.QAction(parent=MainWindow)
        self.action_reset_zoom.setObjectName("action_reset_zoom")
        self.actionUser_Profile = QtGui.QAction(parent=MainWindow)
        self.actionUser_Profile.setObjectName("actionUser_Profile")

        self.retranslateUi(MainWindow)
        self.displays_stacked_widget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.action_about.setText(_translate("MainWindow", "About"))
        self.actionMaximize.setText(_translate("MainWindow", "Maximize"))
        self.actionRestore.setText(_translate("MainWindow", "Restore"))
        self.actionMinimize.setText(_translate("MainWindow", "Minimize"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.action_dark_mode.setText(_translate("MainWindow", "Dark Mode"))
        self.action_new.setText(_translate("MainWindow", "New"))
        self.action_open.setText(_translate("MainWindow", "Open"))
        self.action_recent.setText(_translate("MainWindow", "Recent"))
        self.action_save.setText(_translate("MainWindow", "Save"))
        self.action_save_as.setText(_translate("MainWindow", "Save as..."))
        self.action_workspace.setText(_translate("MainWindow", "Workspace"))
        self.action_users.setText(_translate("MainWindow", "Users"))
        self.action_developer.setText(_translate("MainWindow", "Developer"))
        self.action_reset_zoom.setText(_translate("MainWindow", "Reset Zoom"))
        self.actionUser_Profile.setText(_translate("MainWindow", "User Profile"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
