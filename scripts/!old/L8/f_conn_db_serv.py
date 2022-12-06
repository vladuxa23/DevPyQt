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

        self.tableView = QtWidgets.QTableView()

        self.listView = QtWidgets.QListView()

        l = QtWidgets.QVBoxLayout()
        l.addWidget(self.tableView)
        l.addWidget(self.listView)

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

        sim.dataChanged.connect(lambda x: print(x))

        self.tableView.setModel(sim)

        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

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


if __name__ == "__main__":
    app = QtWidgets.QApplication()  # Создаем  объект приложения
    # app = QtWidgets.QApplication(sys.argv)  # Если PyQt

    myWindow = MyFirstWindow()  # Создаём объект окна
    myWindow.show()  # Показываем окно

    sys.exit(app.exec_())  # Если exit, то код дальше не исполняется

