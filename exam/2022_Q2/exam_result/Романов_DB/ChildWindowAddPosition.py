from PySide2 import QtWidgets, QtCore, QtSql
from ui.FormAddPositions import Ui_Form        # форма добавления сотрудника

from ErrorsAndInsert import create_connection, execute_query_positions
path = r"test1_mysql.db3"


class ChildAddPositions(QtWidgets.QWidget):
    """ Класс описывает дочернее окно для добавления нового сотрудника"""
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.initUi()
        self.initSQLModelReadOrders_2()

    def initUi(self):
        self.setWindowTitle("Постановка на должность")

        # Signals
        self.ui.pushButton.clicked.connect(self.addPositionData)

        # Slot
    def addPositionData(self):
        """ Функция добавляет должноть """
        pos_name = self.ui.lineEdit_3.text()                   # получаем должность
        pos_bet = self.ui.doubleSpinBox.value()                # если text() число через запятую, value() через точку
        pos_salary = self.ui.spinBox.text()                    # получаем оклад
        sum_salary = pos_bet * int(pos_salary)                 # ПРОБЛЕМА МОДЕЛИ и ВЫЧИСЛЯЕМОГО СТОЛБЦА БД)

        model = self.ui.tableView.model()
        index = model.index(self.ui.tableView.currentIndex().row(), 1)  # выбор столбца с номером приказа
        index1 = model.index(self.ui.tableView.currentIndex().row(), 0) # выбор столбца с номером записи

        order_number = index.data(0)                                    # номер выделенного приказа
        order_record = index1.data(0)                                   # номер записи выделеного приказа

        print(pos_name, pos_bet, pos_salary, order_number, order_record)

        # добавляем данные в табл Positions
        connection = create_connection(path)
        execute_query_positions(connection, order_number, pos_name, pos_bet, pos_salary, sum_salary, order_record)


    def initSQLModelReadOrders_2(self):
        """ Функция читает приказы "Поставить" из таблицы Orders через модель QSqlRelationalTableModel """
        self.connection = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.connection.setDatabaseName(path)
        if not self.connection.open():
            print("Database Error: %s" % self.connection.lastError().databaseText())
            print(400)

        self.model = QtSql.QSqlRelationalTableModel()
        self.model.setTable('Orders')
        self.model.setFilter("Otype IN (3)")                   # отбираем приказы на "зачислить" и "уволить"
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

