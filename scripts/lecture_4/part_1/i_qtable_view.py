"""
Демонстрация использования табличной модели
"""

import random

from PySide6 import QtCore, QtWidgets, QtGui
from random_word import RandomWords


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initTableModel()
        self.initUi()

    def initUi(self) -> None:
        """
        Инициализация Ui

        :return: None
        """

        self.tableView = QtWidgets.QTableView()
        self.tableView.setModel(self.tableModel)
        self.tableView.resizeColumnsToContents()  # Нежелательно делать для большого количества данных
        self.tableView.selectionModel().currentChanged.connect(self.itemSelectionChanged)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.tableView)

        self.setLayout(layout)

    def initTableModel(self) -> None:
        """
        Инициализация табличной модели

        :return: None
        """

        self.tableModel = QtGui.QStandardItemModel()

        random_words = RandomWords().get_random_words()

        for row, elem in enumerate(random_words):
            item1 = QtGui.QStandardItem(str(row + 10))
            item2 = QtGui.QStandardItem(random_words[row])
            item3 = QtGui.QStandardItem(str(random.randint(0, 220)))
            self.tableModel.appendRow([item1, item2, item3])

        self.tableModel.setHorizontalHeaderLabels(["№ п/п", "Слово", "Значение"])
        self.tableModel.dataChanged.connect(self.tableViewDataChanged)

    def itemSelectionChanged(self, item: QtCore.QModelIndex) -> None:
        """
        Действие при нажатии на элемент в таблице

        :param item: текущий элемент
        :return: None
        """

        print(self.itemSelectionChanged)
        print(item.row())
        print(item.column())

        print(item.data(0))

    def tableViewDataChanged(self, item) -> None:
        """
        Действие при изменении данных в таблице

        :param item: текущий элемент
        :return: None
        """

        print(self.tableViewDataChanged)
        model = self.tableView.model()
        id_ = model.index(item.row(), 0)
        print()
        print()
        print(item.row())
        print(item.column())

        print()
        print(id_.data(0))
        print(item.data(0))

        if item.column() == 1:
            pass
            # do query_1
        elif item.column() == 2:
            pass
            # do query_2
        # back for db


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
