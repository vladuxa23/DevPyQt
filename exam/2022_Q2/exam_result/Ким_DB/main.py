import sys
import pyodbc

from PySide2 import QtWidgets, QtSql, QtCore, QtGui
from PySide2.QtSql import QSqlQuery

from ui.pageCases1 import Ui_WindowCases
from ui.page_1 import Ui_MainWindow
from ui.emp import Ui_MainWindowEmp
# from ui.newEmp import Ui_MainWindowNewEmp


"""Начальная страница приложения. Позволяет выбрать представление информации в виде судебных дел либо сотрудников"""


class Page1(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # self.casesThread = CasesThread()
        # self.empThread = EmpThread()


        # self.ui.pushButtonCases.clicked.connect(self.casesThread.start)
        self.ui.pushButtonCases.clicked.connect(self.onPushButtonCasesClicked)
        self.ui.pushButtonEmp.clicked.connect(self.onPushButtonEmpClicked)


    """Кнопки на начальной странице приложения "Дела", "Сотрудники" """

    def onPushButtonCasesClicked(self):
        self.cases = Cases()
        self.cases.show()

    def onPushButtonEmpClicked(self):
        self.emp = Employees()
        self.emp.show()

    """Переопределение события закрытия окна"""

    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self, "Закрыть окно?",
                                               "Вы действительно хотите закрыть окно?",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


# class CasesThread(QtCore.QThread):
#     casesSignal = QtCore.Signal(bool)
#
#     def run(self):
#         self.status = True
#         while self.status:
#             self.cases = Cases()
#             self.cases.show()
#             self.casesSignal.emit(self.cases.isEnabled())
#             if not self.cases.isEnabled():
#                 break


"""Представление судебных дел"""


class Cases(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initDB()

        self.ui = Ui_WindowCases()
        self.ui.setupUi(self)

        self.initTVModelCases()

        self.ui.pushButtonSave.clicked.connect(self.onPushButtonSaveClicked)
        self.ui.pushButtonDel.clicked.connect(self.onPushButtonDelClicked)

        self.ui.addRow.triggered.connect(self.addRowTriggered)
        self.ui.addColumn.triggered.connect(self.addColumnTriggered)

        # self.model = QtSql.QSqlRelationalTableModel()
        # self.model.setTable('litigation.cases')
        # self.model.setRelation(3, QtSql.QSqlRelation('litigation.tasks', 'CaseID', 'TaskDateTime'))
        # self.model.select()
        # self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)

    """Подключение к БД"""

    def initDB(self):
        server = 'vpngw.avalon.ru'
        db = 'DevDB2022_KimAY'
        user = 'tsqllogin'
        pasw = 'Pa$$w0rd'
        self.con = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server}; '
            'SERVER=' + server +
            ';DATABASE=' + db +
            ';UID=' + user +
            ';PWD=' + pasw)
        self.cursor = self.con.cursor()

    """Создание модели для отображения данных о судебных делах из БД в tableView"""

    def initTVModelCases(self):
        # создание модели
        self.sim = QtGui.QStandardItemModel()

        # запрос данных из БД
        self.cursor.execute('SELECT DISTINCT LC.CaseNumber, LC.Court, PP.PersonName, LC.Claims, LT.TaskDateTime, SE.LastName '
                            'FROM litigation.cases as LC '
                            'LEFT JOIN parties.case_participants as PCP '
                            'ON LC.id = PCP.CaseID '
                            'LEFT JOIN parties.persons as PP '
                            'ON PCP.PersonID = PP.id '
                            'LEFT JOIN staff.employees as SE '
                            'ON LC.DoerID = SE.id '
                            'JOIN litigation.tasks as LT '
                            'on LC.id = LT.CaseID')
        data = self.cursor.fetchall()
        # print(data)

        # передача данных в модель
        for elem in data:
            item1 = QtGui.QStandardItem(str(elem[0]))
            item2 = QtGui.QStandardItem(str(elem[1]))
            item3 = QtGui.QStandardItem(str(elem[2]))
            item4 = QtGui.QStandardItem(str(elem[3]))
            item5 = QtGui.QStandardItem(str(elem[4]))
            item6 = QtGui.QStandardItem(str(elem[5]))
            self.sim.appendRow([item1, item2, item3, item4, item5, item6])

        # установление заголовков столбцов модели
        self.sim.setHorizontalHeaderLabels(['Номер дела', 'Суд', 'Истец', 'Требования', 'Дата заседания', 'Исполнитель'])

        # установка модели на tableView
        self.ui.tableViewCases.setModel(self.sim)

        # выделение строк и столбцов цветом
        # self.ui.tableViewCases.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.ui.tableViewCases.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectColumns)

        # установка размеров столбцов
        self.ui.tableViewCases.setColumnWidth(0, 80)
        self.ui.tableViewCases.setColumnWidth(1, 200)
        self.ui.tableViewCases.setColumnWidth(2, 150)
        self.ui.tableViewCases.setColumnWidth(3, 200)
        self.ui.tableViewCases.resizeRowsToContents()
        # setAligment(QtCore.Qt.AlignHCenter)

        # self.ui.tableViewCases.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        # установка ширины основного окна
        self.centralWidget().setMinimumWidth(self.setMinWidthCW())

    def setMinWidthCW(self):
        min_width_cw = 50
        for i in range(self.sim.columnCount()):
            min_width_cw += self.ui.tableViewCases.columnWidth(i)
        return min_width_cw

    def onPushButtonSaveClicked(self):
        index = self.ui.tableViewCases.currentIndex()
        print(index)
        value = self.sim.itemData(index)[0]
        self.sim.setData(index, value)
        self.sim.submit()
        print(value)
        # self.ui.tableViewCases.update()

        self.cursor.execute("UPDATE litigation.cases"
                            f"SET Court = '{str(value)}'")
        self.cursor.commit()
        self.con.commit()

    def onPushButtonDelClicked(self):
        reply = QtWidgets.QMessageBox.question(self, 'Удалить строку?',
                                       "Вы действительно хотите удалить строку?",
                                       QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                       QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            self.sim.removeRow(self.ui.tableViewCases.currentIndex().row())


    # слоты для меню
    @QtCore.Slot()
    def addRowTriggered(self):
        self.sim.insertRow(self.sim.rowCount(), [])

    @QtCore.Slot()
    def addColumnTriggered(self):
        self.sim.insertColumn(self.sim.rowCount(), [])
        self.centralWidget().setMinimumWidth(self.setMinWidthCW())

    """Переопределение события закрытия окна"""
    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self, "Закрыть окно?",
                                               "Вы действительно хотите закрыть окно?",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


"""Представление сотрудников"""


class Employees(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_MainWindowEmp()
        self.ui.setupUi(self)

        self.initDB()

        self.initTVModelEmp()

        # self.NewEmp = NewEmp()

        self.ui.pushbuttonAddRow.clicked.connect(self.onPushButtonAddRow)
        self.ui.pushbuttonAddColumn.clicked.connect(self.onPushButtonAddColumn)
        self.ui.pushbuttonDelRow.clicked.connect(self.onPushButtonDelRow)
        self.ui.pushbuttonDelColumn.clicked.connect(self.onPushButtonDelColumn)

        # self.ui.actionSave.triggered.connect(self.saveTriggered)
        # self.ui.ActionCopy.triggered.connect(self.copyTriggered)

    """Подключение к БД"""

    def initDB(self):
        server = 'vpngw.avalon.ru'
        db = 'DevDB2022_KimAY'
        user = 'tsqllogin'
        pasw = 'Pa$$w0rd'
        self.con = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server}; '
            'SERVER=' + server +
            ';DATABASE=' + db +
            ';UID=' + user +
            ';PWD=' + pasw)
        self.cursor = self.con.cursor()

    """Создание модели для отображения данных о сотрудниках из БД в tableView"""

    def initTVModelEmp(self):
        # создание модели
        self.simE = QtGui.QStandardItemModel()

        # запрос данных из БД
        self.cursor.execute('SELECT * FROM staff.employees')
        data = self.cursor.fetchall()
        # print(data)

        # передача данных в модель
        for elem in data:
            item1 = QtGui.QStandardItem(str(elem[0]))
            item2 = QtGui.QStandardItem(str(elem[1]))
            item3 = QtGui.QStandardItem(str(elem[2]))
            item4 = QtGui.QStandardItem(str(elem[3]))
            self.simE.appendRow([item1, item2, item3, item4])

        # установление заголовков столбцов модели
        self.simE.setHorizontalHeaderLabels(['№', 'Фамилия', 'Имя', 'Должность'])

        # установка модели на tableView
        self.ui.tableViewEmp.setModel(self.simE)

        # выделение строки
        self.ui.tableViewEmp.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        self.ui.tableViewEmp.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        # установка размеров столбцов
        self.ui.tableViewEmp.resizeRowsToContents()

        # скрываем первый столбец
        self.ui.tableViewEmp.setColumnHidden(0, True)
        # setAligment(QtCore.Qt.AlignHCenter)

        # установка ширины основного окна
        self.centralWidget().setMinimumWidth(self.setMinWidthCW())

        self.ui.pushButtonSave.clicked.connect(self.onPushButtonSaveClicked)

        self.pr_model = QtCore.QSortFilterProxyModel()
        self.pr_model.setSourceModel(self.simE)

        self.ui.lineEditFilterLastname.textChanged.connect(self.setFilterLastName)

        self.ui.lineEditFilterName.textChanged.connect(self.setFilterName)

        self.ui.lineEditFilterPosition.textChanged.connect(self.setFilterPosition)

        # pr_model.setFilterKeyColumn(1)
        # self.ui.lineEditFilterLastname.textChanged.connect(pr_model.setFilterRegExp)
        # pr_model.setFilterKeyColumn(2)
        # self.ui.lineEditFilterName.textChanged.connect(pr_model.setFilterRegExp)
        # pr_model.setFilterKeyColumn(3)
        # self.ui.lineEditFilterPosition.textChanged.connect(pr_model.setFilterRegExp)
        # self.ui.tableViewEmp.setModel(pr_model)

    def setMinWidthCW(self):
        min_width_cw = 200
        for i in range(self.simE.columnCount()):
            min_width_cw += self.ui.tableViewEmp.columnWidth(i)
        return min_width_cw

    def setFilterLastName(self):
        self.ui.lineEditFilterLastname.textChanged.connect(self.pr_model.setFilterRegExp)
        self.pr_model.setFilterKeyColumn(1)
        self.ui.tableViewEmp.setModel(self.pr_model)

    def setFilterName(self):
        self.ui.lineEditFilterName.textChanged.connect(self.pr_model.setFilterRegExp)
        self.pr_model.setFilterKeyColumn(2)
        self.ui.tableViewEmp.setModel(self.pr_model)

    def setFilterPosition(self):
        self.ui.lineEditFilterPosition.textChanged.connect(self.pr_model.setFilterRegExp)
        self.pr_model.setFilterKeyColumn(3)
        self.ui.tableViewEmp.setModel(self.pr_model)



    # def (self, event: QtGui.QMouseEvent) -> None:
    #     print(event.type())
    #     pr_model = QtCore.QSortFilterProxyModel()
    #     pr_model.setSourceModel(self.simE)
    #
    #     # if event.button() == self.ui.lineEditFilterLastname:
    #     pr_model.setFilterKeyColumn(1)
    #     self.ui.lineEditFilterLastname.textChanged.connect(pr_model.setFilterRegExp)
    #     self.ui.tableViewEmp.setModel(pr_model)

        # pr_model.setFilterKeyColumn(2)
        # self.ui.lineEditFilterName.textChanged.connect(pr_model.setFilterRegExp)

        # pr_model.setFilterKeyColumn(3)
        # self.ui.lineEditFilterPosition.textChanged.connect(pr_model.setFilterRegExp)

    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self, "Закрыть окно?",
                                               "Вы действительно хотите закрыть окно?",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def onPushButtonSaveClicked(self):
        index = self.ui.tableViewEmp.currentIndex()
        print(index)

        value = self.simE.itemData(index)
        print(value)
        self.simE.setData(index, value)
        self.simE.submit()

        # self.ui.tableViewCases.update()

        self.cursor.execute("UPDATE [staff].[employees]"
                            f"SET FirstName = '{str(value)}'")
        self.cursor.commit()
        self.con.commit()


    def onPushButtonAddRow(self):
        self.simE.insertRow(self.simE.rowCount(), [])
        # self.NewEmp.show()

        # self.windowNewEmp = NewEmp()
        # self.windowNewEmp.show()
        # self.simE.insertRow(self.simE.rowCount(), [])

    def saveData(self, lastname, name, position):
        index = self.simE.rowCount()
        self.simE.setData(self.simE.index(index, 1), lastname)
        self.simE.setData(self.simE.index(index, 2), name)
        self.simE.setData(self.simE.index(index, 3), position)

    def onPushButtonAddColumn(self):
        self.simE.insertColumn(self.simE.columnCount(), [])
        self.centralWidget().setMinimumWidth(self.setMinWidthCW())

    def onPushButtonDelRow(self):
        self.simE.removeRow(self.ui.tableViewEmp.currentIndex().row())

    def onPushButtonDelColumn(self):
        print(self.ui.tableViewEmp.currentIndex().column())
        self.simE.removeColumn(self.ui.tableViewEmp.currentIndex().column())

    """Переопределение события закрытия окна"""

    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self, "Закрыть окно?",
                                               "Вы действительно хотите закрыть окно?",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    # def onPushButtonSaveClicked(self):
    #     index = self.ui.tableViewEmp.currentIndex()
    #     value = self.simE.itemData(index)[0]
    #     self.simE.setData(index, value)
    #     self.simE.submit()
    #     print(value)
    #     # self.ui.tableViewCases.update()
    #     self.cursor.execute('UPDATE litigation.cases'
    #                         f'SET Court = {str(value)}')
    #     self.cursor.commit()
    #     self.con.commit()
    #

    # # слоты для меню
    # @QtCore.Slot()
    # def addRowTriggered(self):
    #     self.simE.insertRow(self.simE.rowCount(), [])
    #
    # @QtCore.Slot()
    # def addColumnTriggered(self):
    #     self.simE.insertColumn(self.simE.rowCount(), [])


class NewEmp(QtWidgets.QMainWindow):
    addNewEmp = QtCore.Signal(str, str, str)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_MainWindowNewEmp()
        self.ui.setupUi(self)

        #self.Emp = Employees()

        self.ui.pushButtonSave.clicked.connect(self.onPushButtonSaveClicked)

        self.ui.comboBoxPostion.addItems(['партнер', 'советник', 'ст.юрист', 'юрист', 'мл.юрист', 'секретарь', 'курьер'])


    def onPushButtonSaveClicked(self):
        self.addNewEmp.emit(self.ui.lineEditLastName.text(),
                            self.ui.lineEditName.text(),
                            self.ui.comboBoxPostion.itemText(self.ui.comboBoxPostion.currentIndex()))
        self.close()

        # index = self.Emp.simE.rowCount()
        # self.Emp.simE.setData(self.Emp.simE.index(index, 1), self.ui.lineEditLastName.text())
        # self.Emp.simE.setData(self.Emp.simE.index(index, 2), self.ui.lineEditName.text())
        # self.Emp.simE.setData(self.Emp.simE.index(index, 2),self.ui.comboBoxPostion.itemText(self.ui.comboBoxPostion.currentIndex())
        # self.Emp.simE.submit()
        # if not self.ui.lineEditLastName.text():
        #     self.Emp.simE.removeRow(self.simE.rowCount())

#### ВАРИАНТ С QSL #####
# """"Представление сотрудников"""
# """Переопределение параметров модели"""
#
#
# class EditableSQLModel(QtSql.QSqlTableModel):
#     def __init__(self, parent=None):
#         super(EditableSQLModel, self).__init__(parent)
#
#     def data(self, item, role):
#         if role == QtCore.Qt.BackgroundRole:
#             if item.row() % 2:
#                 return QtGui.QColor(QtCore.Qt.blue)


# class Employees(QtWidgets.QMainWindow):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#
#         self.ui = Ui_MainWindowEmp()
#         self.ui.setupUi(self)
#
#         self.initDB()
#
#         self.initSQLModel()
#
#     """Подключение к БД"""
#
#     def initDB(self):
#         server = 'vpngw.avalon.ru'
#         db = 'DevDB2022_KimAY'
#         user = 'tsqllogin'
#         pasw = 'Pa$$w0rd'
#         self.con = pyodbc.connect(
#             'DRIVER={ODBC Driver 17 for SQL Server}; '
#             'SERVER=' + server +
#             ';DATABASE=' + db +
#             ';UID=' + user +
#             ';PWD=' + pasw)
#         self.cursor = self.con.cursor()
#
#     """Создание модели для отображения данных о сотрудниках из БД в tableView"""
#
#     def initSQLModel(self):
#
#         """создание модели"""
#         self.empModel = EditableSQLModel()
#         # self.empModel = QtSql.QSqlTableModel() - ВАРИАНТ БЕЗ ПЕРЕОПРЕДЕЛЕНИЯ МОДЕЛИ
#         self.empModel.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
#
#         """Подключение к таблице с данными для отображения в модели"""
#         self.empModel.setTable('[staff].[employees]')
#         print(self.cursor.execute('SELECT * from [staff].[employees]').fetchall())
#         self.empModel.select()
#
#         self.empModel.setHeaderData(0, QtCore.Qt.Horizontal, 'id')
#         self.empModel.setHeaderData(1, QtCore.Qt.Horizontal, 'Фамилия')
#         self.empModel.setHeaderData(2, QtCore.Qt.Horizontal, 'Имя')
#         self.empModel.setHeaderData(3, QtCore.Qt.Horizontal, 'Должность')
#
#         self.ui.tableViewEmp.setModel(self.empModel)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myapp = Page1()
    myapp.show()

    app.exec_()