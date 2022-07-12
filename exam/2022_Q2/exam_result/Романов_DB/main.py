import sys
import CreateTables
from PySide2 import QtWidgets, QtGui, QtCore, QtSql
from ui.KadrPrikaz_2 import Ui_Form
from ErrorsAndInsert import create_connection, execute_query_orders
from ChildWindowEmployee import ChildAddEmployee
from ChildWindowAddPosition import ChildAddPositions
from ChildWindowResult import ChildResult


path = r"test1_mysql.db3"


class Form(QtWidgets.QWidget):
    """ Главная форма """
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initUi()

        self.initSQLModelReadOrders()
        self.initSQLModelShowEmployee()
        self.initSQLModelShowPositions()
        self.initSQLModelShowResult()

    def initUi(self):
        self.setWindowTitle("Простейший учёт приказов-сотрудников-должностей")

        # Tab1 - создаем группу кнопок и устанавливаем id для удобства обращения к БД
        self.button_group = None
        self.button_group = QtWidgets.QButtonGroup()
        self.button_group.addButton(self.ui.radioButton, 1)
        self.button_group.addButton(self.ui.radioButton_2, 2)
        self.button_group.addButton(self.ui.radioButton_3, 3)
        self.button_group.addButton(self.ui.radioButton_4, 4)

        # Tab1 - signals приказы
        self.button_group.buttonClicked.connect(self.radioButtonSelectToggled)          # выбор выделенной radioButton
        self.ui.pushButton.clicked.connect(self.initSQLModelAddOrders)                  # добавление приказа
        self.ui.pushButton_2.clicked.connect(self.initSQLModelReadOrders)               # отображение приказов из БД
        self.ui.pushButton_3.clicked.connect(self.initSQLModelDeleteOrders)             # удаление приказа

        # Tab2 - signals сотрудники
        self.ui.pushButton_4.clicked.connect(self.initSQLModelAddEmployee)
        self.ui.pushButton_5.clicked.connect(self.initSQLModelDeleteEmployee)

        # Tab3 - signals должности
        self.ui.pushButton_6.clicked.connect(self.initSQLModelAddPositions)

        # Tab4 - signals расстановка
        self.ui.pushButton_7.clicked.connect(self.initSQLModelAddResult)
        self.ui.pushButton_8.clicked.connect(self.initSQLModelDeleteResult)

    # Tab1 - slots
    def radioButtonSelectToggled(self):
        """ Метод определяет выбранную radioButton в button_group и ее id """
        # print(button)
        self.tmp_radio_number = None
        self.tmp_radio_number = self.button_group.checkedId()
        print(self.tmp_radio_number)

    def initSQLModelAddOrders(self):
        """ Метод добавляет приказ в БД """
        number_order = self.ui.lineEdit_3.text()                    # считываем введенный приказ
        sername_chief = self.ui.lineEdit_2.text()                   # считываем введенную Фамилию
        number_radio = self.tmp_radio_number                        # считываем id выделенной radioButton

        print(number_order, sername_chief, number_radio)
        connection = create_connection(path)                        # соединяемся с БД
        execute_query_orders(connection, number_order, sername_chief, number_radio)
        self.initSQLModelReadOrders()

    def initSQLModelReadOrders(self):
        """ Метод читает данные из таблицы приказов по соответствующему запросу """

        help_dict = {                               # для красивовго отображения типа приказа
                     1: "Зачислить",
                     2: "Уволить",
                     3: "Поставить",
                     4: "Снять"
                    }

        query_read_from_orders = """SELECT Otype, Onumber, Odate, Oname FROM Orders"""

        self.connection = CreateTables.create_connection(path)
        self.cursor = self.connection.cursor()
        self.cursor.execute(query_read_from_orders)
        data = self.cursor.fetchall()
        #print(data)

        model = QtGui.QStandardItemModel()
        headers = ["Тип приказа", "Номер", "Дата", "Фамилия"]
        model.setHorizontalHeaderLabels(headers)

        for i in range(len(data)):
            for j in range(len(headers)):
                model.setItem(i, j, QtGui.QStandardItem(str(data[i][j])))
                if j == 0:
                   print(data[i][0])
                   #print(help_dict.get(2))
                   model.setItem(i, j, QtGui.QStandardItem(str(help_dict.get(data[i][0]))))

        self.ui.tableView.setModel(model)
        # self.ui.tableView.setColumnHidden(0, True)
        self.ui.tableView.setSortingEnabled(True)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

    def initSQLModelDeleteOrders(self):
        """ Удаление приказа по его номеру """
        model = self.ui.tableView.model()
        index = model.index(self.ui.tableView.currentIndex().row(), 1)     # выбор столбца с номером приказа
        order_number = index.data(0)                                       # выбор номера по которому удалять
        #print(index, order_number)
        query_delete_from_orders = f"DELETE FROM Orders WHERE Onumber = '{order_number}'"

        self.cursor.execute(query_delete_from_orders)
        model.removeRow(index.row())
        self.connection.commit()

    # Tab 2 - slots
    def initSQLModelShowEmployee(self):
        """ Функция показывает занесенных в базу Employee сотрудников"""
        self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName(path)
        if not self.db.open():
            print("Database Error: %s" % self.db.lastError().databaseText())

        self.model = QtSql.QSqlRelationalTableModel()
        self.model.setTable('Employee')
        self.model.setRelation(8, QtSql.QSqlRelation("Orders", "Ordid", "Onumber"))
        #self.model.setRelation(7, QtSql.QSqlRelation("Orders", "Ordid", "Onumber"))

        self.model.select()
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "id")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Имя")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Фамилия")
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, "Дата Рождения")
        self.model.setHeaderData(4, QtCore.Qt.Horizontal, "Адрес регистрации")
        self.model.setHeaderData(5, QtCore.Qt.Horizontal, "Телефон")
        self.model.setHeaderData(6, QtCore.Qt.Horizontal, "Приказ на зачисление")   # напрямую
        self.model.setHeaderData(7, QtCore.Qt.Horizontal, "Приказ на увольнение")
        self.model.setHeaderData(8, QtCore.Qt.Horizontal, "Приказ на зачисление")   # через id - relation

        self.ui.tableView_2.setModel(self.model)
        self.ui.tableView_2.setSortingEnabled(True)
        self.ui.tableView_2.setStyleSheet("QTableView { selection-color: yellow; selection-background-color: green; }")
        self.ui.tableView_2.setColumnHidden(0, True)
        self.ui.tableView_2.setColumnHidden(6, True)
        self.ui.tableView_2.horizontalHeader().setSectionsMovable(True)
        self.ui.tableView_2.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        #self.ui.tableView_2.setItemDelegateForColumn(8, NoEditDelegate())         # делегат на связный не назначать!
        self.ui.tableView_2.setItemDelegateForColumn(6, NoEditDelegate())
        self.ui.tableView_2.setItemDelegateForColumn(1, NoEditDelegate())

    def initSQLModelAddEmployee(self):
        """ Добавление нового сотрудника в новом окне"""
        self.childWindow = ChildAddEmployee()
        self.childWindow.show()

        # index = self.model.rowCount()
        # self.model.insertRows(index, 1)
        # # self.model.setData(self.model.index(index, 1), self.ui.lineEdit.text())
        # # self.model.setData(self.model.index(index, 2), self.ui.lineEdit_2.text())
        # # self.model.setData(self.model.index(index, 4), self.ui.lineEdit_3.text())
        # # self.model.setData(self.model.index(index, 3), self.ui.dateEdit.text())
        # self.model.submitAll()

    def initSQLModelDeleteEmployee(self):
        """ Удаление выделенного сотрудника из таблицы """
        if not self.db.open():
            print("Database Error: %s" % self.db.lastError().databaseText())
            #print(100)
        if self.ui.tableView_2.currentIndex().row() > -1:
            self.model.removeRow(self.ui.tableView_2.currentIndex().row())
            self.initSQLModelShowEmployee()
        else:
            QtWidgets.QMessageBox.question(self, 'Message', "Please select a row would you like to delete",
                                           QtWidgets.QMessageBox.Ok)

    # Tab3 - Slots
    def initSQLModelAddPositions(self):
        """ Посчтановка сотрудника на должность """
        self.childWindowPos = ChildAddPositions()
        self.childWindowPos.show()

    def initSQLModelShowPositions(self):
        """ Функция показывает занесенных в базу Positions данные """
        self.dbnew = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.dbnew.setDatabaseName(path)
        if not self.dbnew.open():
            print("Database Error: %s" % self.dbnew.lastError().databaseText())

        self.model_position = QtSql.QSqlRelationalTableModel()
        self.model_position.setTable('Positions')
        #self.model.setRelation(8, QtSql.QSqlRelation("Orders", "Ordid", "Onumber"))
        #self.model.setRelation(7, QtSql.QSqlRelation("Orders", "Ordid", "Onumber"))

        self.model_position.select()
        self.model_position.setHeaderData(0, QtCore.Qt.Horizontal, "id")
        self.model_position.setHeaderData(1, QtCore.Qt.Horizontal, "Приказ постановка")
        self.model_position.setHeaderData(2, QtCore.Qt.Horizontal, "Приказ снятие")
        self.model_position.setHeaderData(3, QtCore.Qt.Horizontal, "Должность")
        self.model_position.setHeaderData(4, QtCore.Qt.Horizontal, "Ставка")
        self.model_position.setHeaderData(5, QtCore.Qt.Horizontal, "Оклад")
        self.model_position.setHeaderData(6, QtCore.Qt.Horizontal, "Зарплата")
        self.model_position.setHeaderData(7, QtCore.Qt.Horizontal, "FK_id")   # id for relation

        self.ui.tableView_3.setModel(self.model_position)
        self.ui.tableView_3.setSortingEnabled(True)
        self.ui.tableView_3.setStyleSheet("QTableView { selection-color: yellow; selection-background-color: green; }")
        self.ui.tableView_3.setColumnHidden(0, True)
        self.ui.tableView_3.setColumnHidden(7, True)
        self.ui.tableView_3.horizontalHeader().setSectionsMovable(True)
        self.ui.tableView_3.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui.tableView_3.setItemDelegateForColumn(1, NoEditDelegate())
        #self.ui.tableView_3.setItemDelegateForColumn(7, NoEditDelegate())   # делегат на связный не назначать!

    # Tab4 - Slot
    def initSQLModelAddResult(self):
        """ Вызов дочернего окна формирования расстановки """
        self.childWindowRes = ChildResult()
        self.childWindowRes.show()

    def initSQLModelShowResult(self):
        #pass
        """ Функция показывает расстановку занесенную в табл Ranking """
        query_read_from_results = """SELECT E.Firstname, E.Lastname, E.Phone, D.Headname, D.Dname,
                                            P.PositionName, P.InOrder, P.SumSalary 
                                     FROM
                                        Employee AS E, Department AS D, Positions AS P, Ranking AS R 
                                     WHERE
                                        E.Empid = R.REmpid AND D.Depid = R.RDepid AND P.Posid = R.RPosid 
"""
        self.connection = CreateTables.create_connection(path)
        self.cursor = self.connection.cursor()
        self.cursor.execute(query_read_from_results)
        data = self.cursor.fetchall()
        # print(data)

        model_result = QtGui.QStandardItemModel()
        headers = ["Имя", "Фамилия", "Телефон", "Организация", "Отдел", "Должность",
                   "Приказ постановки", "Зарплата"]
        model_result.setHorizontalHeaderLabels(headers)

        for i in range(len(data)):
            for j in range(len(headers)):
                model_result.setItem(i, j, QtGui.QStandardItem(str(data[i][j])))

        self.ui.tableView_4.setModel(model_result)
        # self.ui.tableView.setColumnHidden(0, True)
        self.ui.tableView_4.setSortingEnabled(True)
        self.ui.tableView_4.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

    def initSQLModelDeleteResult(self):
        """ Удаление расстановки по выделенному номеру """
        model_del_res = self.ui.tableView_4.model()
        index = model_del_res.index(self.ui.tableView_4.currentIndex().row(), 1)     # выбор строки с номером приказа
        order_number = index.data(0)                                                 # выбор номера по которому удалять
        print(index, order_number)
        query_delete_from_result = f"DELETE FROM Ranking WHERE Rankid= '{order_number}'"

        self.cursor.execute(query_delete_from_result)
        model_del_res.removeRow(index.row())
        self.connection.commit()

    # События окон
    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        """ Функция закрытие дочернего окна при закрытии главного с подтверждением """
        reply = QtWidgets.QMessageBox.question(self, "Закрытие программы",
                                               "Закрыть все окна?",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            self.childWindow.close()
            self.childWindowPos.close()
            self.childWindowRes.close()
            event.accept()
        else:
            event.ignore()

    def event(self, event: QtCore.QEvent):   # QtGui.QCloseEvent
        """ Функция обновления полей """
        if event.type() == QtCore.QEvent.WindowUnblocked:
            self.initSQLModelShowEmployee()
            self.initSQLModelShowPositions()
            self.initSQLModelShowResult()

        return QtWidgets.QWidget.event(self, event)


class NoEditDelegate(QtWidgets.QStyledItemDelegate):
    """ Класс для запрета редактирования на столбцы """
    def __init__(self):
        super(NoEditDelegate, self).__init__()

    def createEditor(self, parent: QtWidgets.QWidget, option: QtWidgets.QStyleOptionViewItem,
                     index: QtCore.QModelIndex) -> QtWidgets.QWidget:
        return 0


if __name__ == "__main__":
    app = QtWidgets.QApplication()  # Создаем  объект приложения
    myWindow = Form()               # Создаём объект окна
    myWindow.show()                 # Показываем окно
    sys.exit(app.exec_())           # Если exit, то код дальше не исполняется
