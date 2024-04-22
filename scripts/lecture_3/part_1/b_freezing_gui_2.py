"""
Демонстрация 'падения' приложения из-за обработки событий в основном потоке
"""

import time

from PySide6 import QtWidgets, QtCore


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()

    def initUi(self) -> None:
        """
        Инициализация Ui

        :return: None
        """

        self.plainTextEdit = QtWidgets.QPlainTextEdit()

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.plainTextEdit)

        self.setLayout(layout)

    def event(self, event: QtCore.QEvent) -> bool:
        print(time.ctime(), event)
        self.plainTextEdit.appendPlainText(str(event))


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
