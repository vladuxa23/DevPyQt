"""
Перехват всех событий
"""

from PySide6 import QtWidgets, QtCore


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

    def event(self, event: QtCore.QEvent) -> bool:
        """
        Перехват всех событий

        :param event: QtCore.QEvent
        :return: bool
        """

        print(event)
        return super().event(event)


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
