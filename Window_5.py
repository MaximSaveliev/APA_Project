# Form implementation generated from reading ui file 'Window_5.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Window_5(object):
    def setupUi(self, Window_5):
        Window_5.setObjectName("Window_5")
        Window_5.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Window_5.setWindowIcon(icon)
        Window_5.setStyleSheet("background-color: rgb(245, 248, 250);\n"
"color: rgb(20, 23, 26);")
        self.backButton = QtWidgets.QPushButton(Window_5)
        self.backButton.setGeometry(QtCore.QRect(50, 520, 50, 50))
        self.backButton.setMinimumSize(QtCore.QSize(50, 50))
        self.backButton.setMaximumSize(QtCore.QSize(50, 50))
        self.backButton.setBaseSize(QtCore.QSize(50, 50))
        self.backButton.setFocusPolicy(QtCore.Qt.FocusPolicy.ClickFocus)
        self.backButton.setStyleSheet("#backButton\n"
"{\n"
"color: #fff;\n"
"border-radius: 10%;\n"
"font-size: 24px;\n"
"font-weight: bold;\n"
"background-color: rgb(29, 161,242);\n"
"}\n"
"#backButton:hover\n"
"{\n"
"background-color: rgb(50, 119, 194);\n"
"}")
        self.backButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Icons/arrow-left.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.backButton.setIcon(icon1)
        self.backButton.setIconSize(QtCore.QSize(28, 28))
        self.backButton.setObjectName("backButton")
        self.downloadButton = QtWidgets.QPushButton(Window_5)
        self.downloadButton.setGeometry(QtCore.QRect(175, 15, 112, 30))
        self.downloadButton.setStyleSheet("#downloadButton\n"
"{\n"
"color: #fff;\n"
"border-radius: 10%;\n"
"font-size: 14px;\n"
"font-family: \'Roboto\', sans-serif;\n"
"font-weight: bold;\n"
"background-color: rgb(29, 161,242);\n"
"}\n"
"#downloadButton:hover\n"
"{\n"
"background-color: rgb(50, 119, 194);\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Icons/download.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.downloadButton.setIcon(icon2)
        self.downloadButton.setIconSize(QtCore.QSize(12, 12))
        self.downloadButton.setObjectName("downloadButton")
        self.uploadButton = QtWidgets.QPushButton(Window_5)
        self.uploadButton.setGeometry(QtCore.QRect(30, 15, 115, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(1)
        font.setBold(True)
        self.uploadButton.setFont(font)
        self.uploadButton.setStyleSheet("#uploadButton\n"
"{\n"
"color: #fff;\n"
"border-radius: 10%;\n"
"font-size: 14px;\n"
"font-family: \'Roboto\', sans-serif;\n"
"font-weight: bold;\n"
"background-color: rgb(29, 161,242);\n"
"}\n"
"#uploadButton:hover\n"
"{\n"
"background-color: rgb(50, 119, 194);\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Icons/upload.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.uploadButton.setIcon(icon3)
        self.uploadButton.setIconSize(QtCore.QSize(12, 12))
        self.uploadButton.setDefault(False)
        self.uploadButton.setFlat(False)
        self.uploadButton.setObjectName("uploadButton")
        self.realTimeButton = QtWidgets.QPushButton(Window_5)
        self.realTimeButton.setGeometry(QtCore.QRect(317, 15, 112, 30))
        self.realTimeButton.setStyleSheet("#realTimeButton\n"
"{\n"
"color: #fff;\n"
"border-radius: 10%;\n"
"font-size: 14px;\n"
"font-family: \'Roboto\', sans-serif;\n"
"font-weight: bold;\n"
"background-color: rgb(29, 161,242);\n"
"}\n"
"#realTimeButton:hover\n"
"{\n"
"background-color: rgb(50, 119, 194);\n"
"}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Icons/person-video.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.realTimeButton.setIcon(icon4)
        self.realTimeButton.setIconSize(QtCore.QSize(12, 12))
        self.realTimeButton.setObjectName("realTimeButton")

        self.retranslateUi(Window_5)
        QtCore.QMetaObject.connectSlotsByName(Window_5)

    def retranslateUi(self, Window_5):
        _translate = QtCore.QCoreApplication.translate
        Window_5.setWindowTitle(_translate("Window_5", "Object Detection"))
        self.backButton.setToolTip(_translate("Window_5", "Go Back"))
        self.downloadButton.setText(_translate("Window_5", " Download"))
        self.uploadButton.setText(_translate("Window_5", " Upload File"))
        self.realTimeButton.setText(_translate("Window_5", " Real Time"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Window_5 = QtWidgets.QDialog()
    ui = Ui_Window_5()
    ui.setupUi(Window_5)
    Window_5.show()
    sys.exit(app.exec())
