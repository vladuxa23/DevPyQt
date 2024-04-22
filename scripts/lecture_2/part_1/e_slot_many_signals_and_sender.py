"""
Подключение нескольких сигналов к одному слоту
"""

from PySide6 import QtWidgets


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()
        self.initSignals()

        self.counter = 0

    def initUi(self) -> None:
        """
        Доинициализация Ui

        :return: None
        """

        self.setFixedSize(200, 200)

        self.button1 = QtWidgets.QPushButton("1")
        self.button2 = QtWidgets.QPushButton("2")

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)

        self.setLayout(layout)

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """

        self.button1.clicked.connect(self.print_button_text)
        self.button2.clicked.connect(self.print_button_text)

    def print_button_text(self) -> None:
        """
        Метод для печати текста

        :return: None
        """

        widget_link = self.sender()
        widget_link.setText(str(self.counter))
        self.counter += 1
        print(widget_link)
        print(widget_link.text())


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myapp = Window()
    myapp.show()

    app.exec()
