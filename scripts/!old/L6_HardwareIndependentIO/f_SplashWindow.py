import time
from PySide2 import QtCore, QtWidgets, QtGui

from scripts.res import MyResources


class MySpalsh(QtWidgets.QSplashScreen):

    def mousePressEvent(self, arg__1):
        pass


class MySpalshExample(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        MyResources.qInitResources()

        self.pushButton = QtWidgets.QPushButton("Работа ведись!")
        # self.pushButton.setIcon(QtGui.QIcon("./res/ui/img/Word.ico"))
        self.pushButton.setIcon(QtGui.QIcon(":/ico/img/Word.ico"))
        self.setCentralWidget(self.pushButton)

        self.loadGUI()
        # self.show()

    def loadGUI(self):
        splash = QtWidgets.QSplashScreen(QtGui.QPixmap(":/graphics/img/pyside_logo.png"))
        # splash = MySpalsh(QtGui.QPixmap(":/graphics/img/pyside_logo.png"))
        splash.showMessage("Загрузка данных...     0%", QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom, QtCore.Qt.white)
        splash.show()

        for _ in range(100):
            time.sleep(0.05)
            if (_ % 10) == 0:
                splash.showMessage(f"Загрузка данных...     {_}%", QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter, QtCore.Qt.white)

        splash.finish(self)
        self.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication()
    myapp = MySpalshExample()

    app.exec_()
