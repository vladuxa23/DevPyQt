import random

from PySide2 import QtWidgets, QtCore
from ui.forms.P1_QtWidgetsAndWindows_AddUi_design import Ui_MainWindow

# https://doc.qt.io/qtforpython/overviews/stylesheet-examples.html

class MyMainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.initUi()

    def initUi(self):
        pass
        # 1
        # from ui.themes import breeze_resources
        # breeze_resources.qInitResources()
        # file = QtCore.QFile(":/dark.qss")
        # file.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text)
        # stream = QtCore.QTextStream(file)
        # self.setStyleSheet(stream.readAll())

        # 2
        # with open('./ui/themes/Dark.qss', 'r') as f:
        #     self.setStyleSheet(f.read())

        # 3
        # with open('./ui/themes/Lite.qss', 'r') as f:
        #     self.setStyleSheet(f.read())

        # 4
        # with open('./ui/themes/OSX Dark.qss', 'r') as f:
        #     self.setStyleSheet(f.read())

        # 5
        # with open('./ui/themes/OSX Lite.qss', 'r') as f:
        #     self.setStyleSheet(f.read())

        # 6
        # with open('./ui/themes/darkstyle.qss', 'r') as f:
        #     self.setStyleSheet(f.read())

        # 7
        # with open('./ui/themes/Qdarkstyle.qss', 'r') as f:
        #     self.setStyleSheet(f.read())


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = MyMainWindow()
    window.show()

    app.exec_()