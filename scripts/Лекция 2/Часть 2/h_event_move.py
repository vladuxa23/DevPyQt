"""
Перехват и обработка события изменения положения окна
"""

from PySide6 import QtWidgets, QtGui


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

    def moveEvent(self, event: QtGui.QMoveEvent) -> None:
        """
        Событие изменения положения окна

        :param event: QtGui.QMoveEvent
        :return: None
        """

        print(event.oldPos())
        print(event.pos())
        print()


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
