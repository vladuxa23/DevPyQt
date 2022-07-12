import pyodbc

from PySide2 import QtCore, QtWidgets
from PySide2.QtSql import QSqlTableModel, QSqlQuery, QSqlDatabase

from ui import SQL_mainWindows

from settings import *
from version import VERSION


class MySQLViewerForm(QtWidgets.QMainWindow):
    """Класс простого внешнего подключения к SQL серверу,
    поддерживает подключение через QODBC"""

    def __init__(self, parent=None):
        super(MySQLViewerForm, self).__init__(parent)
        self.ui = SQL_mainWindows.Ui_MainWindow()
        self.ui.setupUi(self)

        self.driver_name = ""
        self.server_name = ""
        self.port = ""
        self.db_name = ""

        self.sql_login = None
        self.sql_pass = None

        self.connection_str = ""

        self.connection = None

        self.model = QSqlTableModel()


        self.init_cred_form()

        self.ui.exit_action.triggered.connect(self.closeEvent)
        self.ui.radio_windows_authentication.toggled.connect(self.change_to_auth)
        self.ui.button_connect.clicked.connect(self.connect_to_DB)
        self.ui.button_show_table.clicked.connect(self.show_requested_table)
        self.ui.about_action.triggered.connect(self.about_info_show)

    def init_cred_form(self):
        """Инициализация значения контролов на основе файла settings.py"""
        self.ui.lineEdit_driver.setText(CON_DRV)
        self.ui.lineEdit_server_address.setText(SERV)
        self.ui.lineEdit_database_name.setText(CON_DATABASE)
        self.ui.lineEdit_login.setText(USER_LOGIN)
        self.ui.lineEdit_password.setText(USR_PASS)
        self.ui.spinBox_server_port.setValue(CON_PORT)

        self.ui.radio_sql_authentication.setChecked(True)
        self.ui.lineEdit_login.setEnabled(True)
        self.ui.lineEdit_password.setEnabled(True)

    def push_info(self, messageStr):
        """отправка сообщения пользователю, текст сообщения в messageStr"""

        QtWidgets.QMessageBox.information(self,
                                          "Ошибка в настройках подключения",
                                          messageStr,
                                          QtWidgets.QMessageBox.Ok)
        return

    def validate_connection_settings(self,
                                     driver_name: str,
                                     server_name: str,
                                     port: str,
                                     db_name: str,
                                     sql_login=None,
                                     sql_pass=None) -> bool:
        """проверка заполненности значений контролов на форме"""

        check_ok = True

        if not server_name:
            self.push_info("Не указано имя сервера")
            check_ok = False
        if check_ok and not driver_name:
            self.push_info("Не указан драйвер")
            check_ok = False
        if check_ok and port == "0":
            self.push_info("Не указан порт")
            check_ok = False
        if check_ok and not db_name:
            self.push_info("Не указано имя базы данных")
            check_ok = False
        if check_ok and sql_login is not None and not sql_login:
            self.push_info("Не указано имя пользователя для подключения к БД")
            check_ok = False
        if check_ok and sql_login is not None and not sql_pass:
            self.push_info("Не указан пароль пользователя для подключения к БД")
            check_ok = False

        return check_ok

    def setSQLPartEnabled(self, lst: list):
        """инициализация части интефейса на подключения к БД
        на вход передается список таблиц считанный из БД сервера """

        self.ui.groupBox_database_browser.setEnabled(bool(lst))

        if bool(lst):
            self.ui.comboBox_table_name.addItems(lst)
            self.ui.button_show_table.setText(QtCore.QCoreApplication.translate("MainWindow",
                                                                                u"\u041e\u0442\u043e\u0431\u0440\u0430\u0437\u0438\u0442\u044c\u0020\u043f\u0435\u0440\u0432\u044b\u0435\u0020\u0031\u0030\u0030\u0020\u0437\u0430\u043f\u0438\u0441\u0435\u0439", None))
        else:
            self.ui.comboBox_table_name.clear()
            self.ui.button_show_table.setText(QtCore.QCoreApplication.translate("MainWindow",
                                                                      u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435",
                                                                      None))
            self.ui.comboBox_table_name.setFixedSize(120, 20)
        return

    # Декоратор слота просто для того чтобы найти событийность в коде
    @QtCore.Slot()
    def connect_to_DB(self):
        """функция подключения к БД значения подключения берутся из контролов формы"""

        if self.ui.button_connect.text() == "Отключиться":
            self.ui.button_connect.setText(QtCore.QCoreApplication.translate("MainWindow",
                                                                             u"\u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0438\u0442\u044c\u0441\u044f",
                                                                             None))
            self.connection.close()
            self.setSQLPartEnabled([])
            return

        self.driver_name = self.ui.lineEdit_driver.text()
        self.server_name = self.ui.lineEdit_server_address.text()
        self.port = self.ui.spinBox_server_port.text()
        self.db_name = self.ui.lineEdit_database_name.text()

        self.sql_login = None
        self.sql_pass = None

        is_windows_auth = self.ui.radio_windows_authentication.isChecked()

        if not is_windows_auth:
            self.sql_login: str = self.ui.lineEdit_login.text()
            self.sql_pass = self.ui.lineEdit_password.text()

        if not self.validate_connection_settings(self.driver_name,
                                                 self.server_name,
                                                 self.port,
                                                 self.db_name,
                                                 self.sql_login,
                                                 self.sql_pass):
            return

        if is_windows_auth:
            self.connection_str = f"DRIVER={self.driver_name};Server={self.server_name};Database={self.db_name};Trusted_Connection=yes;"
        else:
            self.connection_str = f"DRIVER={self.driver_name};Server={self.server_name};Port={self.port};Database={self.db_name};UID={self.sql_login};PWD={self.sql_pass}"

        self.connection = pyodbc.connect(self.connection_str)

        # Если вдруг коннект не работает попытаемся выдать ошибку
        if not self.connection:
            QtWidgets.QMessageBox.critical(
                None,
                "Критическая ошибка",
                f"Ошибка подключения на сервере: {SERV} к БД: {CON_DATABASE} \n {self.connection}"
            )
            return

        if cursor := self.connection.cursor():

            cursor.execute("SELECT [TABLE_SCHEMA],[TABLE_NAME] FROM information_schema.tables "
                           "WHERE TABLE_TYPE = 'BASE Table' ORDER BY TABLE_SCHEMA, TABLE_NAME ")

            records = cursor.fetchall()
            cursor.close()
            lst = [f"{row[0]}.{row[1]}" for row in records]
            val = len(max(lst, key=len))
            self.ui.comboBox_table_name.setFixedSize(val*6, 20)

            self.ui.button_connect.setText("Отключиться")

            self.setSQLPartEnabled(lst)

    def show_requested_table(self):
        """отображения на tableView выбранной таблицы, отображается только первый 100 строк """
        if self.connection is None:
            return

        db = QSqlDatabase.addDatabase('QODBC')
        db.setDatabaseName(self.connection_str)
        db.open()

        qry = QSqlQuery(db)

        # формируем запрос к выбранной таблице
        qry.prepare(f'SELECT TOP 100 * FROM {self.ui.comboBox_table_name.currentText()}')
        qry.exec_()

        self.model.setQuery(qry)
        self.ui.tableView_database_table.setModel(self.model)
        self.ui.tableView_database_table.horizontalHeader().setSectionsMovable(True)
        self.ui.tableView_database_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

    def change_to_auth(self):
        """событие смена метода аутентификации, меняются значения контролов"""

        auth_methods = self.ui.groupBox_authentication.findChildren(QtWidgets.QRadioButton)
        for auth_method in auth_methods:
            if auth_method.isChecked():
                if auth_method.text() == "Windows authentication":
                    self.ui.lineEdit_login.setEnabled(False)
                    self.ui.lineEdit_login.setText("")
                    self.ui.lineEdit_password.setEnabled(False)
                    self.ui.lineEdit_password.setText("")
                    self.setSQLPartEnabled([])

                else:
                    self.ui.lineEdit_login.setEnabled(True)
                    self.ui.lineEdit_login.setText(USER_LOGIN)
                    self.ui.lineEdit_password.setEnabled(True)
                    self.ui.lineEdit_password.setText(USR_PASS)

    def closeEvent(self, event):
        """Закрытие формы возможно из двух мест меню и по кнопке"""

        called_from_menu = self.sender() is not None and self.sender().objectName() == "exit_action"

        reply = QtWidgets.QMessageBox.question(self, "Закрыть приложение",
                                               "Закрыть приложение?",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if called_from_menu:
            if reply == QtWidgets.QMessageBox.Yes:
                if self.connection:
                    self.connection.close()
                app.exit()
        elif reply == QtWidgets.QMessageBox.Yes:
            if self.connection:
                self.connection.close()
            event.accept()
        else:
            event.ignore()

    def about_info_show(self):
        """информация о программе"""

        QtWidgets.QMessageBox.information(self, "О программе",
                            f"Внешний SQL обозреватель. Версия {VERSION}")


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myapp = MySQLViewerForm()
    myapp.show()

    app.exec_()
