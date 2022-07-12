from PySide2 import QtWidgets, QtCore, QtSql
from ui.FormAddEmployee import Ui_Form        # форма добавления сотрудника

from ErrorsAndInsert import create_connection, execute_query_employee
path = r"test1_mysql.db3"


class ChildAddEmployee(QtWidgets.QWidget):
    """ Класс описывает дочернее окно для добавления нового сотрудника"""
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.initUi()
        self.initSQLModelReadOrders_1()

    def initUi(self):
        self.setWindowTitle("Добавление сотрудника")

        # Signals
        self.ui.pushButton.clicked.connect(self.addEmployeeData)

        # Slot
    def addEmployeeData(self):
        """ Функция добавляет нового сотрудника """
        emp_firstname = self.ui.lineEdit.text()                         # получаем имя
        emp_lastname = self.ui.lineEdit_2.text()                        # получаем Фамилию
        emp_borndate = self.ui.dateEdit.text()                          # получаем дату рождения
        emp_address = self.ui.lineEdit_3.text()                         # получаем адрес
        emp_phone = self.ui.lineEdit_4.text()                           # получаем телефон

        model = self.ui.tableView.model()
        index = model.index(self.ui.tableView.currentIndex().row(), 1)  # выбор столбца с номером приказа
        index1 = model.index(self.ui.tableView.currentIndex().row(), 0) # выбор столбца с номером записи

        order_number = index.data(0)                                    # номер выделенного приказа
        order_record = index1.data(0)                                   # номер записи выделеного приказа

        print(emp_firstname, emp_lastname, emp_borndate, emp_address, emp_phone, order_number, order_record)

        # добавляем данные в табл Employee
        connection = create_connection(path)
        execute_query_employee(connection, emp_firstname, emp_lastname, emp_borndate,
                               emp_address, emp_phone, order_number, order_record)


    def initSQLModelReadOrders_1(self):
        """ Функция читает приказы "зачислить" и "уволить" из таблицы Orders через модель QSqlRelationalTableModel """
        self.connection = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.connection.setDatabaseName(path)
        if not self.connection.open():
            print("Database Error: %s" % self.connection.lastError().databaseText())

        self.model = QtSql.QSqlRelationalTableModel()
        self.model.setTable('Orders')
        self.model.setFilter("Otype = 1")                      # отбираем приказы - IN (1,2) "зачислить" и "уволить"
        self.model.setSort(1, QtCore.Qt.DescendingOrder)       # сортируем по приказу по убыванию
        self.model.setRelation(4, QtSql.QSqlRelation("TypeOrder", "TOid", "TOtype"))   # показываем название по id
        self.model.select()

        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "id")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Номер приказа")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Дата")
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, "Фамилия подписавшего")
        self.model.setHeaderData(4, QtCore.Qt.Horizontal, "Тип приказа")

        self.ui.tableView.setModel(self.model)
        self.ui.tableView.setColumnHidden(0, True)
         #self.ui.tableView.setColumnHidden(6, True)
        self.ui.tableView.horizontalHeader().setSectionsMovable(True)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
