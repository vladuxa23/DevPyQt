"""
Создание окна на основе QWidget
"""
import os

from PySide6 import QtWidgets, QtGui

from conf import ROOT_FOLDER


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        self.setWindowTitle('MyFirstWindow')
        self.setWindowIcon(QtGui.QIcon(os.path.join(ROOT_FOLDER, 'static', 'images', 'python.png')))
        self.setGeometry(500, 400, 250, 350)

        print(self.pos())
        print(self.size())
        print(self.frameGeometry())
        print(self.width(), self.height())

        self.setMinimumHeight(100)
        self.setMinimumWidth(200)

        self.setMaximumSize(600, 800)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
