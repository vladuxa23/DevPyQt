"""
Демонстрация использования сразу нескольких моделей
"""

from PySide6 import QtCore, QtWidgets, QtGui
from random_word import RandomWords


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.random_words = RandomWords()

        self.initUi()

    def initUi(self) -> None:
        """
        Инициализация Ui

        :return: None
        """

        listModel = self.createQStringListModel()

        self.comboBox = QtWidgets.QComboBox()
        self.comboBox.setModel(listModel)

        self.listView = QtWidgets.QListView()
        self.listView.setModel(listModel)

        self.tableView = QtWidgets.QTableView()
        self.tableView.setModel(self.createQStandardItemModel())
        self.tableView.resizeColumnsToContents()  # Нежелательно делать для большого количества данных
        self.tableView.selectionModel().currentChanged.connect(self.itemSelectionChanged)

        self.treeView = QtWidgets.QTreeView()
        # self.treeView.setModel(self.createQStandardItemModel())
        # ИЛИ
        self.treeView.setModel(self.createTreeModel())

        # компоновка
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.comboBox)
        layout.addWidget(self.listView)
        layout.addWidget(self.tableView)
        layout.addWidget(self.treeView)

        self.setLayout(layout)

    def createQStringListModel(self) -> QtCore.QStringListModel:
        """
        Создание списковой модели

        :return: списковая модель
        """

        lst = self.random_words.get_random_words()
        return QtCore.QStringListModel(lst)

    def createQStandardItemModel(self) -> QtGui.QStandardItemModel:
        """
        Создание двумерной (табличной модели)

        :return: QtGui.QStandardItemModel
        """

        sim = QtGui.QStandardItemModel()
        lst = self.random_words.get_random_words()

        for row, elem in enumerate(lst):
            item1 = QtGui.QStandardItem(str(row + 10))
            item2 = QtGui.QStandardItem(lst[row])
            sim.appendRow([item1, item2])

        sim.setHorizontalHeaderLabels(["№ п/п", "Слово"])
        sim.dataChanged.connect(self.tableViewDataChanged)

        return sim

    def createTreeModel(self) -> QtGui.QStandardItemModel:
        """
        Создание древовидной модели

        :return: QtGui.QStandardItemModel
        """

        sim = QtGui.QStandardItemModel()

        rootItem1 = QtGui.QStandardItem("QAbstractItemView")
        rootItem2 = QtGui.QStandardItem("Базовый класс")

        item1 = QtGui.QStandardItem("QListView")
        item2 = QtGui.QStandardItem("Список")

        rootItem1.appendRow([item1, item2])
        item1 = QtGui.QStandardItem("QTableView")
        item2 = QtGui.QStandardItem("Таблица")
        rootItem1.appendRow([item1, item2])
        item1 = QtGui.QStandardItem("QTreeView")
        item2 = QtGui.QStandardItem("Иерархический список")
        rootItem1.appendRow([item1, item2])
        sim.appendRow([rootItem1, rootItem2])
        sim.setHorizontalHeaderLabels(["Класс", "Описание"])

        return sim

    def itemSelectionChanged(self, item: QtCore.QModelIndex) -> None:
        """
        Действие при выбора элемента

        :param item: элемент
        :return: None
        """

        print(item.row())
        print(item.column())
        print(item.data(0))

    def tableViewDataChanged(self, item) -> None:
        """
        Изменение данных в таблице

        :param item: выбранный элемент
        :return: None
        """

        model = self.tableView.model()
        id_ = model.index(item.row(), 0)
        print()
        print(item.row())
        print(item.column())

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

    myWindow = Window()
    myWindow.show()

    app.exec()
