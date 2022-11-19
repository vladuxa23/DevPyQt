"""
Подключение слота к сигналу, который является статическим методом
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

        self.setWindowTitle("Калькулятор")

        labelA = QtWidgets.QLabel("Число A")
        labelB = QtWidgets.QLabel("Число B")

        self.lineEditA = QtWidgets.QLineEdit()
        self.lineEditB = QtWidgets.QLineEdit()

        self.pushButtonSum = QtWidgets.QPushButton("Сложить")
        self.pushButtonSub = QtWidgets.QPushButton("Вычесть")

        layoutInputs = QtWidgets.QHBoxLayout()
        layoutInputs.addWidget(labelA)
        layoutInputs.addWidget(self.lineEditA)
        layoutInputs.addWidget(labelB)
        layoutInputs.addWidget(self.lineEditB)

        layoutButtons = QtWidgets.QHBoxLayout()
        layoutButtons.addWidget(self.pushButtonSum)
        layoutButtons.addWidget(self.pushButtonSub)

        layoutMain = QtWidgets.QVBoxLayout()
        layoutMain.addLayout(layoutInputs)
        layoutMain.addLayout(layoutButtons)

        self.setLayout(layoutMain)

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """

        self.pushButtonSum.clicked.connect(self.calc_sum)

    @staticmethod
    def calc_sum(a: float | int, b: float | int) -> float | int:
        """
        Суммирование двух чисел

        :param a: число a
        :param b: число b
        :return: сумма a и b
        """

        print(a + b)

        return a + b

    @staticmethod
    def calc_sub(a: float | int, b: float | int) -> float | int:
        """
        Разность двух чисел

        :param a: число a
        :param b: число b
        :return: разность a и b
        """

        print(a - b)

        return a - b


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
