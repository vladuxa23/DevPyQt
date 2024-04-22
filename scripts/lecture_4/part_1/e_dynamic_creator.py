"""
Демонстрация динамического создания виджетов
"""

from PySide6 import QtWidgets
from random_word import RandomWords


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.randomWords = RandomWords()

        self.initUi()
        self.initSignals()

    def initUi(self) -> None:
        """
        Инициализация Ui

        :return: None
        """

        self.pushButtonAddLineEdit = QtWidgets.QPushButton("Добавить lineEdit")
        self.pushButtonAddComboBox = QtWidgets.QPushButton("Добавить comboBox")

        self.layout_dynamic = QtWidgets.QVBoxLayout()

        for i in range(5):
            self.layout_dynamic.addWidget(self.createLineEdit())

        layout = QtWidgets.QVBoxLayout()
        layout.addLayout(self.layout_dynamic)
        layout.addSpacerItem(QtWidgets.QSpacerItem(
            10, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        )
        layout.addWidget(self.pushButtonAddLineEdit)
        layout.addWidget(self.pushButtonAddComboBox)

        self.setLayout(layout)

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """

        self.pushButtonAddLineEdit.clicked.connect(
            lambda: self.layout_dynamic.addWidget(self.createLineEdit())
        )

        self.pushButtonAddComboBox.clicked.connect(
            lambda: self.layout_dynamic.addWidget(self.createComboBox())
        )

    def createLineEdit(self) -> QtWidgets.QLineEdit:
        """
        Создание QLineEdit

        :return: QtWidgets.QLineEdit
        """

        lineEdit = QtWidgets.QLineEdit()
        lineEdit.setObjectName(f"lineEdit_{self.layout_dynamic.count()}")
        lineEdit.textChanged.connect(lambda: print(lineEdit.objectName(), lineEdit.text()))
        lineEdit.setPlaceholderText(lineEdit.objectName())

        return lineEdit

    def createComboBox(self) -> QtWidgets.QComboBox:
        """
        Создание ComboBox

        :return: QtWidgets.QComboBox
        """

        comboBox = QtWidgets.QComboBox()
        comboBox.setObjectName(f"comboBox_{self.layout_dynamic.count()}")
        comboBox.addItems(self.randomWords.get_random_words())
        comboBox.currentIndexChanged.connect(lambda: print(comboBox.objectName(), comboBox.currentText()))

        return comboBox


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
