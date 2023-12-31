# Form implementation generated from reading ui file 'gui\components\login_widget.ui'
#
# Created by: PyQt6 UI code generator 6.5.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        Form.resize(319, 190)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setToolTipDuration(-1)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(1, 1, 1, 1)
        self.gridLayout.setHorizontalSpacing(1)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalFrame = QtWidgets.QFrame(parent=Form)
        self.verticalFrame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.verticalFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.verticalFrame.setLineWidth(1)
        self.verticalFrame.setObjectName("verticalFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetFixedSize)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.github_button = QtWidgets.QPushButton(parent=self.verticalFrame)
        self.github_button.setMinimumSize(QtCore.QSize(24, 24))
        self.github_button.setMaximumSize(QtCore.QSize(24, 24))
        self.github_button.setBaseSize(QtCore.QSize(24, 24))
        self.github_button.setText("")
        self.github_button.setObjectName("github_button")
        self.horizontalLayout_2.addWidget(self.github_button)
        self.discord_button = QtWidgets.QPushButton(parent=self.verticalFrame)
        self.discord_button.setMinimumSize(QtCore.QSize(24, 24))
        self.discord_button.setMaximumSize(QtCore.QSize(24, 24))
        self.discord_button.setBaseSize(QtCore.QSize(24, 24))
        self.discord_button.setText("")
        self.discord_button.setObjectName("discord_button")
        self.horizontalLayout_2.addWidget(self.discord_button)
        self.twitter_button = QtWidgets.QPushButton(parent=self.verticalFrame)
        self.twitter_button.setMinimumSize(QtCore.QSize(24, 24))
        self.twitter_button.setMaximumSize(QtCore.QSize(24, 24))
        self.twitter_button.setBaseSize(QtCore.QSize(24, 24))
        self.twitter_button.setText("")
        self.twitter_button.setObjectName("twitter_button")
        self.horizontalLayout_2.addWidget(self.twitter_button)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(5, 5, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        spacerItem1 = QtWidgets.QSpacerItem(5, 5, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.logo_label = QtWidgets.QLabel(parent=self.verticalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo_label.sizePolicy().hasHeightForWidth())
        self.logo_label.setSizePolicy(sizePolicy)
        self.logo_label.setMinimumSize(QtCore.QSize(128, 32))
        self.logo_label.setMaximumSize(QtCore.QSize(32, 32))
        self.logo_label.setBaseSize(QtCore.QSize(32, 32))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.logo_label.setFont(font)
        self.logo_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.logo_label.setObjectName("logo_label")
        self.verticalLayout_4.addWidget(self.logo_label)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(5, 5, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 0, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout_2)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem3 = QtWidgets.QSpacerItem(5, 5, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.formLayout.setSpacing(2)
        self.formLayout.setObjectName("formLayout")
        self.username_label = QtWidgets.QLabel(parent=self.verticalFrame)
        self.username_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.username_label.setObjectName("username_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.username_label)
        self.name_combo_box = QtWidgets.QComboBox(parent=self.verticalFrame)
        self.name_combo_box.setObjectName("name_combo_box")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.name_combo_box)
        self.password_line_edit = QtWidgets.QLineEdit(parent=self.verticalFrame)
        self.password_line_edit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.password_line_edit.setObjectName("password_line_edit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.password_line_edit)
        self.password_label = QtWidgets.QLabel(parent=self.verticalFrame)
        self.password_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.password_label.setObjectName("password_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.password_label)
        self.horizontalLayout_7.addLayout(self.formLayout)
        spacerItem4 = QtWidgets.QSpacerItem(5, 5, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem5 = QtWidgets.QSpacerItem(5, 5, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.remember_me_checkbox = QtWidgets.QCheckBox(parent=self.verticalFrame)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.remember_me_checkbox.setFont(font)
        self.remember_me_checkbox.setObjectName("remember_me_checkbox")
        self.horizontalLayout.addWidget(self.remember_me_checkbox)
        spacerItem6 = QtWidgets.QSpacerItem(5, 5, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem7 = QtWidgets.QSpacerItem(5, 5, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.login_button = QtWidgets.QPushButton(parent=self.verticalFrame)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.login_button.setFont(font)
        self.login_button.setObjectName("login_button")
        self.horizontalLayout_4.addWidget(self.login_button)
        spacerItem8 = QtWidgets.QSpacerItem(5, 5, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem8)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.feedback_label = QtWidgets.QLabel(parent=self.verticalFrame)
        self.feedback_label.setMinimumSize(QtCore.QSize(0, 17))
        self.feedback_label.setMaximumSize(QtCore.QSize(16777215, 17))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setItalic(True)
        self.feedback_label.setFont(font)
        self.feedback_label.setText("")
        self.feedback_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.feedback_label.setObjectName("feedback_label")
        self.verticalLayout.addWidget(self.feedback_label)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem9)
        self.create_new_user_button = QtWidgets.QPushButton(parent=self.verticalFrame)
        font = QtGui.QFont()
        font.setItalic(False)
        font.setUnderline(True)
        self.create_new_user_button.setFont(font)
        self.create_new_user_button.setDefault(False)
        self.create_new_user_button.setFlat(True)
        self.create_new_user_button.setObjectName("create_new_user_button")
        self.horizontalLayout_5.addWidget(self.create_new_user_button)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem10)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.gridLayout.addWidget(self.verticalFrame, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Login"))
        self.github_button.setToolTip(_translate("Form", "Check out the project on Github"))
        self.discord_button.setToolTip(_translate("Form", "Join the Omniverse Discord server"))
        self.twitter_button.setToolTip(_translate("Form", "Contact the creator"))
        self.logo_label.setText(_translate("Form", "Enter the Omniverse"))
        self.username_label.setText(_translate("Form", "Name:"))
        self.password_label.setText(_translate("Form", "Password:"))
        self.remember_me_checkbox.setText(_translate("Form", "Remember Me?"))
        self.login_button.setText(_translate("Form", "Login"))
        self.create_new_user_button.setText(_translate("Form", "Create New User"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
