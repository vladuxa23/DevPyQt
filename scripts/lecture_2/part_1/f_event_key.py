"""
Перехват и обработка события нажатия на клавиатуру
"""

from PySide6 import QtWidgets, QtGui, QtCore


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        """
        Событие нажатия на клавиатуру

        :param event: QtGui.QKeyEvent
        :return: None
        """

        print("#:", event.key(), "-------> text:", event.text())


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
