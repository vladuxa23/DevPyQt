import sys

from PySide6 import QtCore, QtWidgets, QtGui
from random_word import RandomWords


class WindowModels(QtWidgets.QWidget):

    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        self.random_words = RandomWords()  # API для генерации рандомных слов

        self.initUi()

    def initUi(self) -> None:
        """
        Доинициализация Ui

        :return:
        """

        # Установка ограниченй размера окна
        self.setMinimumSize(500, 700)
        self.setMaximumSize(500, 700)
        # Аналог
        # self.setFixedSize(500, 700)

        # виджеты
        self.comboBox = QtWidgets.QComboBox()
        self.comboBox.setModel(self.getStringListProxyModel())

        self.listView = QtWidgets.QListView()
        self.listView.setModel(self.getStringListModel())

        self.tableView = QtWidgets.QTableView()
        self.tableView.setModel(self.getTableModel())
        self.tableView.resizeColumnsToContents()  # Нежелательно делать для большого количества данных

        self.treeView = QtWidgets.QTreeView()
        self.treeView.setModel(self.getTreeModel())

        self.columnView = QtWidgets.QColumnView()
        self.columnView.setModel(self.getTreeModel())

        # компоновка
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.comboBox)
        layout.addWidget(self.listView)
        layout.addWidget(self.tableView)
        layout.addWidget(self.treeView)
        layout.addWidget(self.columnView)

        self.setLayout(layout)

    # Методы инициализации моделей
    def getStringListModel(self) -> QtCore.QStringListModel:
        """
        Получение модели представляющей массив строк

        :return: QStringListModel
        """

        lst = self.random_words.get_random_words()[:]
        return QtCore.QStringListModel(lst)

    def getStringListProxyModel(self) -> QtCore.QSortFilterProxyModel:
        """
        Получение прокси модели для QStringListModel

        :return: QSortFilterProxyModel
        """

        proxy = QtCore.QSortFilterProxyModel()
        proxy.setSourceModel(self.getStringListModel())
        proxy.setFilterWildcard("????")

        return proxy

    def getTableModel(self) -> QtGui.QStandardItemModel:
        """
        Получение стандартной двумерной модели (для QTableView)

        :return: QStandardItemModel
        """

        model = QtGui.QStandardItemModel()
        lst = self.random_words.get_random_words()

        for row, elem in enumerate(lst):
            item1 = QtGui.QStandardItem(str(row + 10))
            item2 = QtGui.QStandardItem(lst[row])
            model.appendRow([item1, item2])
        model.setHorizontalHeaderLabels(["№ п/п", "Слово"])

        return model

    def getTreeModel(self) -> QtGui.QStandardItemModel:
        """
        Получение стандартной двумерной модели (для QTreeView)

        :return: QStandardItemModel
        """

        model = QtGui.QStandardItemModel()

        parent_1 = QtGui.QStandardItem("QAbstractItemView")
        parent_2 = QtGui.QStandardItem("Базовый класс")

        child_1 = QtGui.QStandardItem("QListView")
        child_2 = QtGui.QStandardItem("Список")

        parent_1.appendRow([child_1, child_2])

        child_1 = QtGui.QStandardItem("QTableView")
        child_2 = QtGui.QStandardItem("Таблица")

        parent_1.appendRow([child_1, child_2])

        child_1 = QtGui.QStandardItem("QTreeView")
        child_2 = QtGui.QStandardItem("Иерархический список")

        parent_1.appendRow([child_1, child_2])

        model.appendRow([parent_1, parent_2])
        model.setHorizontalHeaderLabels(["Класс", "Описание"])

        return model


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    myWindow = WindowModels()
    myWindow.show()

    app.exec_()
