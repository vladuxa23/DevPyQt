"""
Подключение одного сигнала к нескольким слотам
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

        self.pushButton = QtWidgets.QPushButton("Выполнить функцию")
        self.pushButton.setCheckable(True)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.pushButton)

        self.setLayout(layout)

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """

        self.pushButton.clicked.connect(lambda x: print(x))
        self.pushButton.clicked.connect(self.onPushButtonClicked)

    def onPushButtonClicked(self, checked) -> None:
        """
        Действие при нажатии на кнопку

        :param checked: состояние кнопки
        :return: None
        """

        print(self.pushButton.isChecked())  # + можно получить состояние с помощью метода
        print("Статус кнопки", checked)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
