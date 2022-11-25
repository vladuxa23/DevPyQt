"""
Перехват и обработка события закрытия окна
"""

from PySide6 import QtWidgets, QtGui


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        """
        Событие закрытия окна

        :param event: QtGui.QCloseEvent
        :return: None
        """

        answer = QtWidgets.QMessageBox.question(
            self, "Закрыть окно?", "Вы действительно хотите закрыть окно?"
        )

        if answer == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
