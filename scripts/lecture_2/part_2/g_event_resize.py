"""
Перехват и обработка события изменения размера окна
"""

from PySide6 import QtWidgets, QtGui


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

    def resizeEvent(self, event: QtGui.QResizeEvent) -> None:
        """
        Событие изменения размера окна

        :param event: QtGui.QResizeEvent
        :return: None
        """

        print(event.size())


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
