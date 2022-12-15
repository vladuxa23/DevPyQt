"""
Демонстрация использования списковой модели
"""

from PySide6 import QtCore, QtWidgets
from random_word import RandomWords


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initListModel()
        self.initUi()

    def initUi(self) -> None:
        """
        Инициализация Ui

        :return: None
        """

        self.setFixedSize(500, 700)

        self.comboBox = QtWidgets.QComboBox()
        self.comboBox.setModel(self.listModel)

        self.listView = QtWidgets.QListView()
        self.listView.setModel(self.listModel)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.comboBox)
        layout.addWidget(self.listView)

        self.setLayout(layout)

    def initListModel(self) -> None:
        """
        Инициализация строковой модели данных

        :return: None
        """

        random_word = RandomWords().get_random_words()

        self.listModel = QtCore.QStringListModel(random_word)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myWindow = Window()
    myWindow.show()

    app.exec()
