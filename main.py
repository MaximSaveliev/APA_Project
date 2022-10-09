import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from Main_Window import Ui_MainWindow
from Window_2 import Ui_Window_2
from Window_3 import Ui_Window_3
from Window_4 import Ui_Window_4
from Window_5 import Ui_Window_5



app = QtWidgets.QApplication(sys.argv)


MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()


#logic open other window
def openComputerVisionWindow():
    global Window_2
    Window_2 = QtWidgets.QDialog()
    ui = Ui_Window_2()
    ui.setupUi(Window_2)
    MainWindow.close()
    Window_2.show()


    def openEyeDetectionWindow():
        global Window_3
        Window_3 = QtWidgets.QDialog()
        ui = Ui_Window_3()
        ui.setupUi(Window_3)
        Window_2.close()
        Window_3.show()

        def goBack():
            Window_3.close()
            Window_2.show()

        ui.backButton.clicked.connect(goBack)


    def openColorDetectionWindow():
        global Window_4
        Window_4 = QtWidgets.QDialog()
        ui = Ui_Window_4()
        ui.setupUi(Window_4)
        Window_2.close()
        Window_4.show()

        def goBack():
            Window_4.close()
            Window_2.show()

        ui.backButton.clicked.connect(goBack)


    def openObjectDetectionWindow():
        global Window_5
        Window_5 = QtWidgets.QDialog()
        ui = Ui_Window_5()
        ui.setupUi(Window_5)
        Window_2.close()
        Window_5.show()

        def goBack():
            Window_5.close()
            Window_2.show()

        ui.backButton.clicked.connect(goBack)

    def goBack():
        Window_2.close()
        MainWindow.show()


    ui.backButton.clicked.connect(goBack)
    ui.go_eye_Button.clicked.connect(openEyeDetectionWindow)
    ui.go_color_Button.clicked.connect(openColorDetectionWindow)
    ui.go_object_Button.clicked.connect(openObjectDetectionWindow)


ui.startButton.clicked.connect(openComputerVisionWindow)


sys.exit(app.exec())