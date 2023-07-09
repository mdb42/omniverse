# Form implementation generated from reading ui file 'src\gui\components\chat_interface_widget.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(230, 469)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.chat_interface_layout = QtWidgets.QGridLayout()
        self.chat_interface_layout.setContentsMargins(1, 1, 1, 1)
        self.chat_interface_layout.setSpacing(1)
        self.chat_interface_layout.setObjectName("chat_interface_layout")
        self.chat_input_layout = QtWidgets.QHBoxLayout()
        self.chat_input_layout.setContentsMargins(1, 1, 1, 0)
        self.chat_input_layout.setSpacing(0)
        self.chat_input_layout.setObjectName("chat_input_layout")
        self.chat_audio_button_layout = QtWidgets.QGridLayout()
        self.chat_audio_button_layout.setContentsMargins(1, 1, 1, 1)
        self.chat_audio_button_layout.setSpacing(1)
        self.chat_audio_button_layout.setObjectName("chat_audio_button_layout")
        self.stt_button = QtWidgets.QPushButton(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stt_button.sizePolicy().hasHeightForWidth())
        self.stt_button.setSizePolicy(sizePolicy)
        self.stt_button.setMinimumSize(QtCore.QSize(32, 32))
        self.stt_button.setMaximumSize(QtCore.QSize(32, 32))
        self.stt_button.setBaseSize(QtCore.QSize(32, 32))
        self.stt_button.setText("")
        self.stt_button.setObjectName("stt_button")
        self.chat_audio_button_layout.addWidget(self.stt_button, 1, 0, 1, 1)
        self.tts_button = QtWidgets.QPushButton(parent=Form)
        self.tts_button.setMinimumSize(QtCore.QSize(32, 32))
        self.tts_button.setMaximumSize(QtCore.QSize(32, 32))
        self.tts_button.setBaseSize(QtCore.QSize(32, 32))
        self.tts_button.setText("")
        self.tts_button.setObjectName("tts_button")
        self.chat_audio_button_layout.addWidget(self.tts_button, 0, 0, 1, 1)
        self.chat_input_layout.addLayout(self.chat_audio_button_layout)
        self.chat_input_text_editor = QtWidgets.QTextEdit(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chat_input_text_editor.sizePolicy().hasHeightForWidth())
        self.chat_input_text_editor.setSizePolicy(sizePolicy)
        self.chat_input_text_editor.setMinimumSize(QtCore.QSize(0, 0))
        self.chat_input_text_editor.setBaseSize(QtCore.QSize(158, 0))
        self.chat_input_text_editor.setObjectName("chat_input_text_editor")
        self.chat_input_layout.addWidget(self.chat_input_text_editor)
        self.chat_generation_button_layout = QtWidgets.QGridLayout()
        self.chat_generation_button_layout.setContentsMargins(1, 1, 1, 1)
        self.chat_generation_button_layout.setSpacing(1)
        self.chat_generation_button_layout.setObjectName("chat_generation_button_layout")
        self.generate_image_button = QtWidgets.QPushButton(parent=Form)
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
        self.chat_generation_button_layout.addWidget(self.generate_image_button, 2, 0, 1, 1)
        self.generate_text_button = QtWidgets.QPushButton(parent=Form)
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
        self.chat_generation_button_layout.addWidget(self.generate_text_button, 1, 0, 1, 1)
        self.chat_input_layout.addLayout(self.chat_generation_button_layout)
        self.chat_interface_layout.addLayout(self.chat_input_layout, 1, 1, 1, 1)
        self.chat_output_browser = QtWidgets.QTextBrowser(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.chat_output_browser.sizePolicy().hasHeightForWidth())
        self.chat_output_browser.setSizePolicy(sizePolicy)
        self.chat_output_browser.setMinimumSize(QtCore.QSize(0, 0))
        self.chat_output_browser.setBaseSize(QtCore.QSize(100, 100))
        self.chat_output_browser.setObjectName("chat_output_browser")
        self.chat_interface_layout.addWidget(self.chat_output_browser, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.chat_interface_layout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.stt_button.setToolTip(_translate("Form", "Speech To Text"))
        self.tts_button.setToolTip(_translate("Form", "Text To Speech"))
        self.generate_image_button.setToolTip(_translate("Form", "Generate Image"))
        self.generate_text_button.setToolTip(_translate("Form", "Send To Chat"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())