import subprocess
import sys
from PySide2 import QtWidgets, QtGui, QtCore  # Импорт класса, который содержит элементы окна
import pyodbc
from PySide2.QtCore import QSortFilterProxyModel, QRegExp, Qt


class MyFirstWindow(QtWidgets.QWidget):  # Наследуемся от QMainWindow

    def __init__(self, parent=None):  # Создаем конструктор класса
        super().__init__(parent)  # Передаем конструктору ссылку на родительский компонент

        self.initDB()

        self.initUi()

        self.initTableViewModel()

        self.initListViewModel()

    def initUi(self):
        self.resize(1000, 600)

        # self.lineEditFilter1 = QtWidgets.QLineEdit()
        # self.lineEditFilter2 = QtWidgets.QLineEdit()


        self.tableView = QtWidgets.QTableView()

        self.listView = QtWidgets.QListView()

        l = QtWidgets.QVBoxLayout()
        # l.addWidget(self.lineEditFilter1)
        # l.addWidget(self.lineEditFilter2)
        l.addWidget(self.tableView)
        # l.addWidget(self.listView)

        self.setLayout(l)

    def initTableViewModel(self):
        sim = QtGui.QStandardItemModel()

        self.cursor.execute("SELECT * FROM HumanResources.Department")
        lst = self.cursor.fetchall()

        for elem in lst:
            item1 = QtGui.QStandardItem(str(elem[0]))
            item2 = QtGui.QStandardItem(str(elem[1]))
            item3 = QtGui.QStandardItem(str(elem[2]))
            item4 = QtGui.QStandardItem(str(elem[3]))
            sim.appendRow([item1, item2, item3, item4])

        sim.setHorizontalHeaderLabels(["№ п/п", "Имя", "Группа", "Изменен"])


        self.tableView.setModel(sim)

        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        # self.tableView.selectionModel().currentChanged.connect(self.cellChanged)

        self.tableView.clicked.connect(self.onTableViewPressed)
        # self.tableView.installEventFilter(self)
        
        #
        #
        # pr_model = CustomSortFilterProxyModel()
        # pr_model.setSourceModel(sim)
        # pr_model.setFilterKeyColumn(1)
        # pr_model.setFilterKeyColumn(2)
        #
        #
        # self.lineEditFilter1.textChanged.connect(lambda text:
        #                        pr_model.setFilterByColumn(QRegExp(text, Qt.CaseSensitive, QRegExp.FixedString), 1))
        #
        # self.lineEditFilter2.textChanged.connect(lambda text:
        #                                          pr_model.setFilterByColumn(
        #                                              QRegExp(text, Qt.CaseSensitive, QRegExp.FixedString), 2))
    
    # def eventFilter(self, watched:QtCore.QObject, event:QtCore.QEvent) -> bool:
    #     print(watched)
    #     print(event.type())
    #     # if isinstance(watched, QtWidgets.QTableView) and event.type() == QtCore.QEvent.Type.MouseButtonPress:
    #     #     print(123)
    #
    #     return super(MyFirstWindow, self).eventFilter(watched, event)
        
    
    def onTableViewPressed(self, row):
        print(self.tableView.selectionModel().selectedRows())

    def initListViewModel(self):

        self.cursor.execute("SELECT name FROM HumanResources.Department")
        lst = self.cursor.fetchall()
        lst = [x[0] for x in lst]

        lsm = QtCore.QStringListModel(lst)

        self.listView.setModel(lsm)

    def initDB(self):
        server = 'tcp:vpngw.avalon.ru'
        database = 'AdventureWorks'
        username = 'tsqllogin'
        password = 'Pa$$w0rd'

        self.conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
        self.cursor = self.conn.cursor()

    def cellChanged(self, index):
        print(index.row())
        print(index.column())
        print(index.data(0))

#
# class CustomSortFilterProxyModel(QSortFilterProxyModel):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.filters = {}
#
#     def setFilterByColumn(self, regex, column):
#         self.filters[column] = regex
#         self.invalidateFilter()
#
#     def filterAcceptsRow(self, source_row:int, source_parent:QtCore.QModelIndex) -> bool:
#         results = []
#         for key, regex in self.filters.items():
#             text = ''
#             ix = self.sourceModel().index(source_row, key, source_parent)
#             if ix.isValid():
#                 text = self.sourceModel().data(ix, Qt.DisplayRole)
#
#                 if text is None:
#                     text = ''
#             results.append(regex.match(text))


if __name__ == "__main__":
    app = QtWidgets.QApplication()  # Создаем  объект приложения
    # app = QtWidgets.QApplication(sys.argv)  # Если PyQt

    myWindow = MyFirstWindow()  # Создаём объект окна
    myWindow.show()  # Показываем окно

    sys.exit(app.exec_())  # Если exit, то код дальше не исполняется

