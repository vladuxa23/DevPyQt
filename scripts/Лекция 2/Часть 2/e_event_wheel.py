"""
Перехват и обработка события вращения колесика мыши
"""

from PySide6 import QtWidgets, QtGui


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

    def wheelEvent(self, event: QtGui.QWheelEvent) -> None:
        """
        Событие вращения колесика мышки

        :param event: QtGui.QWheelEvent
        :return: None
        """

        print(event.angleDelta())


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
