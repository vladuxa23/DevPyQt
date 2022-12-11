"""
Демонстрация применения флагов Qt.WindowType
"""

from PySide6 import QtCore, QtWidgets


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Неизменяемое окно
        # self.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint)

        # Неизменяемое окно без рамок
        # self.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint | QtCore.Qt.FramelessWindowHint)

        # Окно со строкой заголовка
        self.setWindowFlags(QtCore.Qt.WindowTitleHint)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myWindow = Window()
    myWindow.show()

    app.exec()
