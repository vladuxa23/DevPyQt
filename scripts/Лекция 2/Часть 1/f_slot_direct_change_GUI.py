"""
Подключение сигнала к методу изменения состояния GUI
"""

from PySide6 import QtWidgets


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()
        self.initSignals()

    def initUi(self) -> None:
        """
        Доинициализация Ui

        :return: None
        """

        self.lineEdit = QtWidgets.QLineEdit()

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.lineEdit)

        self.setLayout(layout)

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """

        self.lineEdit.textChanged.connect(self.setWindowTitle)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
