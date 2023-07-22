# Form implementation generated from reading ui file 'gui\components\user_creation_widget.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(320, 341)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(1, 1, 1, 1)
        self.gridLayout.setSpacing(1)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalFrame = QtWidgets.QFrame(parent=Form)
        self.verticalFrame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.verticalFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.verticalFrame.setObjectName("verticalFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_3.setSpacing(1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(5, 5, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.welcome_label = QtWidgets.QLabel(parent=self.verticalFrame)
        self.welcome_label.setMinimumSize(QtCore.QSize(0, 32))
        self.welcome_label.setMaximumSize(QtCore.QSize(16777215, 32))
        self.welcome_label.setBaseSize(QtCore.QSize(0, 32))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.welcome_label.setFont(font)
        self.welcome_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.welcome_label.setObjectName("welcome_label")
        self.verticalLayout_2.addWidget(self.welcome_label)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.feedback_label = QtWidgets.QLabel(parent=self.verticalFrame)
        self.feedback_label.setText("")
        self.feedback_label.setObjectName("feedback_label")
        self.horizontalLayout_4.addWidget(self.feedback_label)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.user_creation_vitals_widget = QtWidgets.QFrame(parent=self.verticalFrame)
        self.user_creation_vitals_widget.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.user_creation_vitals_widget.setObjectName("user_creation_vitals_widget")
        self.formLayout = QtWidgets.QFormLayout(self.user_creation_vitals_widget)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.formLayout.setContentsMargins(1, -1, 1, 0)
        self.formLayout.setSpacing(1)
        self.formLayout.setObjectName("formLayout")
        self.name_line_edit = QtWidgets.QLineEdit(parent=self.user_creation_vitals_widget)
        self.name_line_edit.setMinimumSize(QtCore.QSize(128, 0))
        self.name_line_edit.setMaximumSize(QtCore.QSize(128, 16777215))
        self.name_line_edit.setBaseSize(QtCore.QSize(128, 0))
        self.name_line_edit.setObjectName("name_line_edit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.name_line_edit)
        self.name_label = QtWidgets.QLabel(parent=self.user_creation_vitals_widget)
        self.name_label.setObjectName("name_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.name_label)
        self.password_label = QtWidgets.QLabel(parent=self.user_creation_vitals_widget)
        self.password_label.setObjectName("password_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.password_label)
        self.password_line_edit = QtWidgets.QLineEdit(parent=self.user_creation_vitals_widget)
        self.password_line_edit.setMinimumSize(QtCore.QSize(128, 0))
        self.password_line_edit.setMaximumSize(QtCore.QSize(128, 16777215))
        self.password_line_edit.setBaseSize(QtCore.QSize(128, 0))
        self.password_line_edit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.password_line_edit.setObjectName("password_line_edit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.password_line_edit)
        self.confirm_label = QtWidgets.QLabel(parent=self.user_creation_vitals_widget)
        self.confirm_label.setObjectName("confirm_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.confirm_label)
        self.confirm_line_edit = QtWidgets.QLineEdit(parent=self.user_creation_vitals_widget)
        self.confirm_line_edit.setMinimumSize(QtCore.QSize(128, 0))
        self.confirm_line_edit.setMaximumSize(QtCore.QSize(128, 16777215))
        self.confirm_line_edit.setBaseSize(QtCore.QSize(128, 0))
        self.confirm_line_edit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.confirm_line_edit.setObjectName("confirm_line_edit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.confirm_line_edit)
        self.verticalLayout_6.addWidget(self.user_creation_vitals_widget)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.verticalLayout_2.addLayout(self.verticalLayout_6)
        spacerItem3 = QtWidgets.QSpacerItem(5, 5, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem4 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.api_key_label = QtWidgets.QLabel(parent=self.verticalFrame)
        self.api_key_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.api_key_label.setObjectName("api_key_label")
        self.verticalLayout_3.addWidget(self.api_key_label)
        self.api_key_line_edit = QtWidgets.QLineEdit(parent=self.verticalFrame)
        self.api_key_line_edit.setMinimumSize(QtCore.QSize(180, 0))
        self.api_key_line_edit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.api_key_line_edit.setObjectName("api_key_line_edit")
        self.verticalLayout_3.addWidget(self.api_key_line_edit)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        spacerItem5 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.key_instruction_label_1 = QtWidgets.QLabel(parent=self.verticalFrame)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.key_instruction_label_1.setFont(font)
        self.key_instruction_label_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.key_instruction_label_1.setObjectName("key_instruction_label_1")
        self.verticalLayout_2.addWidget(self.key_instruction_label_1)
        self.key_instruction_label_2 = QtWidgets.QLabel(parent=self.verticalFrame)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.key_instruction_label_2.setFont(font)
        self.key_instruction_label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.key_instruction_label_2.setObjectName("key_instruction_label_2")
        self.verticalLayout_2.addWidget(self.key_instruction_label_2)
        spacerItem6 = QtWidgets.QSpacerItem(5, 5, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem6)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.key_question_label = QtWidgets.QLabel(parent=self.verticalFrame)
        self.key_question_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.key_question_label.setObjectName("key_question_label")
        self.verticalLayout_4.addWidget(self.key_question_label)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem7)
        self.get_api_key_button = QtWidgets.QPushButton(parent=self.verticalFrame)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.get_api_key_button.setFont(font)
        self.get_api_key_button.setFlat(True)
        self.get_api_key_button.setObjectName("get_api_key_button")
        self.horizontalLayout_7.addWidget(self.get_api_key_button)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem8)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.verticalLayout_2.addLayout(self.verticalLayout_4)
        spacerItem9 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem9)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        spacerItem10 = QtWidgets.QSpacerItem(5, 5, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem10)
        self.horizontalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem11 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem11)
        self.cancel_button = QtWidgets.QPushButton(parent=self.verticalFrame)
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout_2.addWidget(self.cancel_button)
        self.confirm_button = QtWidgets.QPushButton(parent=self.verticalFrame)
        self.confirm_button.setObjectName("confirm_button")
        self.horizontalLayout_2.addWidget(self.confirm_button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout.addWidget(self.verticalFrame, 0, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "User Creation"))
        self.welcome_label.setText(_translate("Form", "Welcome to the Omniverse"))
        self.name_label.setText(_translate("Form", "Name:"))
        self.password_label.setText(_translate("Form", "Password:"))
        self.confirm_label.setText(_translate("Form", "Confirm:"))
        self.api_key_label.setText(_translate("Form", "OpenAI API Key:"))
        self.key_instruction_label_1.setText(_translate("Form", "Most of the features in this application"))
        self.key_instruction_label_2.setText(_translate("Form", "require an API key to function."))
        self.key_question_label.setText(_translate("Form", "Don\'t have an API key?"))
        self.get_api_key_button.setText(_translate("Form", "Get one here"))
        self.cancel_button.setText(_translate("Form", "Cancel"))
        self.confirm_button.setText(_translate("Form", "Confirm"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
