"""
Подключение сигнала к методу (слоту) класса
"""

from PySide6 import QtWidgets
from PySide6.QtCore import Slot


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
        labelResult = QtWidgets.QLabel("Результат:")

        self.lineEditA = QtWidgets.QLineEdit()
        self.lineEditB = QtWidgets.QLineEdit()
        self.lineEditResult = QtWidgets.QLineEdit()

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
        layoutMain.addWidget(labelResult)
        layoutMain.addWidget(self.lineEditResult)
        layoutMain.addLayout(layoutButtons)

        self.setLayout(layoutMain)

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """

        self.pushButtonSum.clicked.connect(self.calc_sum)
        self.pushButtonSub.clicked.connect(self.calc_sub)

    def calc_sum(self) -> None:
        """
        Суммирование двух чисел

        :return: None
        """

        a = int(self.lineEditA.text())
        b = int(self.lineEditB.text())

        self.lineEditResult.setText(str(a + b))

    @Slot()
    def calc_sub(self) -> None:
        """
        Разность двух чисел

        :return: None
        """

        a = int(self.lineEditA.text())
        b = int(self.lineEditB.text())

        self.lineEditResult.setText(str(a - b))


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
