import sys
from random_word import RandomWords
from PySide2 import QtCore, QtWidgets, QtGui

# TODO: RandomWords возвращает None

class MyModelsPreview(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.rndWords = RandomWords()
        self.initUi()

    def initUi(self):
        # центральное окно
        centralWidget = QtWidgets.QWidget()
        self.setCentralWidget(centralWidget)

        self.setMinimumSize(500, 700)
        self.setMaximumSize(500, 700)
        # self.setFixedSize(500, 700)
        # модели
        lm = self.createQStringListModel()

        # виджеты
        self.comboBox = QtWidgets.QComboBox()
        proxy1 = QtCore.QSortFilterProxyModel()
        proxy1.setSourceModel(lm)
        proxy1.setFilterWildcard("?????????")
        self.comboBox.setModel(proxy1)

        self.listView = QtWidgets.QListView()
        self.listView.setModel(lm)

        self.tableView = QtWidgets.QTableView()
        self.tableView.setModel(self.createQStandardItemModel())
        self.tableView.resizeColumnsToContents()  # Нежелательно делать для большого количества данных
        self.tableView.selectionModel().currentChanged.connect(self.itemSelectionChanged)

        self.treeView = QtWidgets.QTreeView()
        self.treeView.setModel(self.createQStandardItemModel())

        # self.treeView.setModel(self.createTreeModel())

        self.columnView = QtWidgets.QColumnView()
        md = QtWidgets.QDirModel()
        index = md.index(1, 0)
        print(md.data(index, 0))
        self.columnView.setModel(md)

        # компоновка
        layoutV1 = QtWidgets.QVBoxLayout()
        layoutV1.addWidget(self.comboBox)
        layoutV1.addWidget(self.listView)
        layoutV1.addWidget(self.tableView)
        layoutV1.addWidget(self.treeView)
        layoutV1.addWidget(self.columnView)

        centralWidget.setLayout(layoutV1)

    def itemSelectionChanged(self, item: QtCore.QModelIndex):
        print(item.row())
        print(item.column())

        print(item.data(0))

    def createQStringListModel(self):
        lst = self.rndWords.get_random_words()[:]
        # lst = self.rndWords
        return QtCore.QStringListModel(lst)

    def createQStandardItemModel(self):
        sim = QtGui.QStandardItemModel()
        lst = self.rndWords.get_random_words()
        # lst = self.rndWords
        for row, elem in enumerate(lst):
            item1 = QtGui.QStandardItem(str(row+10))
            item2 = QtGui.QStandardItem(lst[row])
            sim.appendRow([item1, item2])
        sim.setHorizontalHeaderLabels(["№ п/п", "Слово"])

        sim.dataChanged.connect(self.tableViewDataChanged)



        return sim

    def tableViewDataChanged(self, item):
        model = self.tableView.model()
        id_ = model.index(item.row(), 0)
        print()
        print()
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



    def createTreeModel(self):
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


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    myWindow = MyModelsPreview()
    myWindow.show()

    app.exec_()
