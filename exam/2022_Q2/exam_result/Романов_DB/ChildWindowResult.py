from PySide2 import QtWidgets, QtCore, QtSql
from ui.FormAddResult import Ui_Form

from ErrorsAndInsert import create_connection, execute_query_result

path = r"test1_mysql.db3"


class ChildResult(QtWidgets.QWidget):
    """ Класс описывает дочернее окно для добавления нового сотрудника"""
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.initUi()

        self.initReadEmployee()
        self.initReadDepartment()
        self.initReadPositions()
        self.set_connection()

    def initUi(self):
        self.setWindowTitle("Общая расстановка")

        # Signals
        self.ui.pushButton.clicked.connect(self.addPositionData)

        # Slot
    def addPositionData(self):
        """ Функция устанавливает расстановку  """
        model_empl = self.ui.tableView.model()
        index_empl = model_empl.index(self.ui.tableView.currentIndex().row(), 0)  # выбор столбца с id записи в Employee
        emp_record = index_empl.data(0)                                           # номер записи выделеного приказа

        model_dep = self.ui.tableView_2.model()                                   # выбор столбца с id записи в Departm
        index_dep = model_dep.index(self.ui.tableView_2.currentIndex().row(), 0)  # выбор столбца с номером записи
        dep_record = index_dep.data(0)

        model_pos = self.ui.tableView_3.model()                                   # выбор столбца с id записи в Position
        index_pos = model_pos.index(self.ui.tableView_3.currentIndex().row(), 0)  # выбор столбца с номером записи
        pos_record = index_pos.data(0)

        print(emp_record, dep_record, pos_record)

        # добавляем данные в табл Ranking
        connection = create_connection(path)
        execute_query_result(connection, emp_record, dep_record, pos_record)

    def initReadEmployee(self):
        """ Отображает данные из табл Employee на tableView"""
        self.model_emp = QtSql.QSqlTableModel()
        self.model_emp.setTable('Employee')
        self.model_emp.select()

        self.model_emp.setHeaderData(0, QtCore.Qt.Horizontal, "id")
        self.model_emp.setHeaderData(1, QtCore.Qt.Horizontal, "Имя")
        self.model_emp.setHeaderData(2, QtCore.Qt.Horizontal, "Фамилия")
        self.model_emp.setHeaderData(3, QtCore.Qt.Horizontal, "Дата Рождения")

        self.ui.tableView.setModel(self.model_emp)
        self.ui.tableView.setSortingEnabled(True)
        # self.ui.tableView.setColumnHidden(0, True)     # скрыть id в релизе !!!!!!!!!
        self.ui.tableView.setColumnHidden(4, True)
        self.ui.tableView.setColumnHidden(5, True)
        self.ui.tableView.setColumnHidden(6, True)
        self.ui.tableView.setColumnHidden(7, True)
        self.ui.tableView.setColumnHidden(8, True)
        self.ui.tableView.horizontalHeader().setSectionsMovable(True)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

    def initReadDepartment(self):
        """ Отображает данные из табл Department на tableView_2 """
        self.model_dep = QtSql.QSqlTableModel()
        self.model_dep.setTable('Department')
        self.model_dep.select()

        self.model_dep.setHeaderData(0, QtCore.Qt.Horizontal, "id")
        self.model_dep.setHeaderData(1, QtCore.Qt.Horizontal, "Отдел")
        self.model_dep.setHeaderData(2, QtCore.Qt.Horizontal, "Организация")

        self.ui.tableView_2.setModel(self.model_dep)
        self.ui.tableView_2.setSortingEnabled(True)
        # self.ui.tableView_2.setColumnHidden(0, True)     # скрыть id в релизе
        self.ui.tableView_2.setColumnHidden(3, True)
        self.ui.tableView_2.setColumnHidden(4, True)
        self.ui.tableView_2.horizontalHeader().setSectionsMovable(True)
        self.ui.tableView_2.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

    def initReadPositions(self):
        """ Отображает данные из табл Positions на tableView_3 """
        self.model_pos = QtSql.QSqlTableModel()
        self.model_pos.setTable('Positions')
        self.model_pos.select()

        self.model_pos.setHeaderData(0, QtCore.Qt.Horizontal, "id")
        self.model_pos.setHeaderData(1, QtCore.Qt.Horizontal, "Приказ постановки")
        self.model_pos.setHeaderData(2, QtCore.Qt.Horizontal, "Должность")

        self.ui.tableView_3.setModel(self.model_pos)
        self.ui.tableView_3.setSortingEnabled(True)
        # self.ui.tableView_3.setColumnHidden(0, True)     # скрыть id в релизе
        self.ui.tableView_3.setColumnHidden(2, True)
        self.ui.tableView_3.setColumnHidden(4, True)
        self.ui.tableView_3.setColumnHidden(5, True)
        self.ui.tableView_3.setColumnHidden(6, True)
        self.ui.tableView_3.setColumnHidden(7, True)
        self.ui.tableView_3.horizontalHeader().setSectionsMovable(True)
        self.ui.tableView_3.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

    def set_connection(self):
        """ Соединение с БД """
        self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName(path)
        if not self.db.open():
            print("Database Error: %s" % self.db.lastError().databaseText())


