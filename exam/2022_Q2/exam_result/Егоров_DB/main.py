import pyodbc
from PySide2 import QtWidgets, QtGui

from ui.GetInfo_form import Ui_Form


class AppForDB(QtWidgets.QWidget):
    """Создание конструктора класса приложения, для выполнения поискового запроса о авиа рейсах"""

    def __init__(self, parent=None):
        super().__init__(parent)  # ссылка на родительский объект с помощью метода super

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.resize(1200, 800)
        self.setWindowTitle("Поиск информации о рейсе")

        self.initUi()
        self.initDB()
        # self.initTableViewModel()
        # self.ChangeStartPoint()
        # self.ChangeFinishPoint()

    def initUi(self):
        pass
        self.ui.pushButton.clicked.connect(self.initTableViewModel)  # Подключение кнопки из Ui формы

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        """Метод выводит предупреждающую информацию при попытке закрытия диалогового окна"""
        reply = QtWidgets.QMessageBox.question(self,
                                               'Поиск информации о рейсах',
                                               'Вы действительно хотите закрыть приложение?',
                                               QtWidgets.QMessageBox.Yes,
                                               QtWidgets.QMessageBox.No)

    def initDB(self):
        """Метод для инициализации подключения к базе данных
        :param - server - адрес сервера;
        :param - database - имя базы данных;
        :param - user имя пользователя для авторизации;
        :param - password - пароль к user для авторизации на сервере;
        """
        server = 'vpngw.avalon.ru'
        database = 'DevDB2022_EVGEGO'
        user = 'tsqllogin'
        password = 'Pa$$w0rd'
        self.con = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server}; SERVER=' + server
            + ';DATABASE=' + database + ';UID=' + user + ';PWD=' + password)  # инициализация объекта подключения
        self.cursor = self.con.cursor()  # объект курсора осуществления для забросов в БД

        # self.cursor.execute("SELECT * FROM FlySales.RouteDetails") # тест
        # request = self.cursor.fetchall()
        # print(request)

    def initTableViewModel(self):
        """Метод для данных передачи и вывода данных, получаемых из запроса от БД в приложение
                """
        sim = QtGui.QStandardItemModel()  # Модель, содержит данные в двумерном представлении
        self.cursor.execute(f"SELECT StartPoint, FinishPoint, TravelTime, TotalDistance"
                            f" FROM DevDB2022_EVGEGO.FlySales.RouteDetails  "
                            f"WHERE StartPoint LIKE '%{self.ui.lineEdit_2.text()}%' "
                            f"AND FinishPoint LIKE '%{self.ui.lineEdit_4.text()}%'")

        # f"WHERE D.StartPoint "
        # f"LIKE ' % {self.ui.lineEdit_2.text()}% ' ")
        # f"AND D.FinishPoint LIKE ' % {self.ui.lineEdit_4.text()}%'")

        lst = self.cursor.fetchall()
        print(lst) # Тестовый вывод данных в консоль, если запрос к БД неверный, в консоль выводится пустой список []

        for elem in lst:  # Передача данных в модель, формирование элементов колонок таблицы приложения
            item1 = QtGui.QStandardItem(str(elem[0]))
            item2 = QtGui.QStandardItem(str(elem[1]))
            item3 = QtGui.QStandardItem(str(elem[2]))
            item4 = QtGui.QStandardItem(str(elem[3]))

            sim.appendRow([item1, item2, item3, item4])
        sim.setHorizontalHeaderLabels(['Start point', 'Finish point', 'Total time', 'Total distance'])
        # установка наименования таблицы приложения

        self.ui.tableView.setModel(sim)
        # self.ui.pushButton.clicked.connect(self.)

        self.ui.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)  # Выделение строки
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)  # Выделение столбца


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myapp = AppForDB()
    myapp.show()

    app.exec_()
