# Проверка соединения к БД
# Проверка добавляемых данных в БД

import sys
from PySide2.QtSql import QSqlDatabase, QSqlQuery
from PySide2.QtWidgets import QApplication, QMessageBox

path = r"test1_mysql.db3"


def create_connection(path):
    """ Функция подключения к БД """
    connection = QSqlDatabase.addDatabase("QSQLITE")
    connection.setDatabaseName(path)

    if not connection.open():
        QMessageBox.critical(
            None,
            "App Name - Error!",
            "Database Error - No connection: %s" % connection.lastError().databaseText(),
        )
        sys.exit(1)

    return connection


def execute_query_orders(connection, par1, par2, par3):
    """Функция добавляет данные в таблицу приказов"""

    print(connection.isOpen())
    query = QSqlQuery()
    query.exec_("PRAGMA foreign_keys = ON;")

    if not query.exec_(f"""INSERT INTO Orders (Onumber, Oname, Otype)
                    VALUES ('{par1}', '{par2}', '{par3}')"""):
        QMessageBox.critical(
            None,
            "App Name - Error!",
            "Database Orders Error - Вставляются недопустимые данные!",
        )
        # sys.exit(1)
    else:
        QMessageBox.about(
            None,
            "Успешно",
            "Данные добавлены"
        )

    print("OK - insert Orders by button ")


def execute_query_employee(connection, firstname, lastname, borndate, address, phone, order_number, order_record):
    """Функция добавляет данные в таблицу сотрудников """

    print(connection.isOpen())
    query = QSqlQuery()
    query.exec_("PRAGMA foreign_keys = ON;")

    if not query.exec_(f"""INSERT INTO Employee (Firstname, Lastname, Borndate, Address, Phone, AcceptOrder, EmpOrdid)
                    VALUES ('{firstname}', '{lastname}', '{borndate}', '{address}',
                            '{phone}', '{order_number}', '{order_record}')"""):
        QMessageBox.critical(
            None,
            "App Name - Error!",
            "Database Employee Error - Вставляются недопустимые данные!",
        )
    else:
        QMessageBox.about(
            None,
            "Успешно",
            "Данные добавлены!"
        )

    print("OK - insert Employee by button ")


def execute_query_positions(connection, order_number, pos_name, pos_bet, pos_salary, sum_salary, order_record):
    """Функция добавляет данные в таблицу должностей """

    print(connection.isOpen())
    query = QSqlQuery()
    query.exec_("PRAGMA foreign_keys = ON;")

    if not query.exec_(f"""INSERT INTO Positions (InOrder, PositionName, Bet, Salary, SumSalary, PosOrdid)
                    VALUES ('{order_number}', '{pos_name}', '{pos_bet}', '{pos_salary}', '{sum_salary}',
                            '{order_record}')"""):
        print("*************Error: insert Positions:", query.lastError().text())
        QMessageBox.critical(
            None,
            "App Name - Error!",
            "Database Position Error - Вставляются недопустимые данные!",
        )
    else:
        QMessageBox.about(
            None,
            "Успешно",
            "Данные добавлены!"
        )

    print("OK - insert Position by button ")


def execute_query_result(connection, emp_record, dep_record, pos_record):
    """Функция добавляет данные в таблицу должностей """

    print(connection.isOpen())
    query = QSqlQuery()
    query.exec_("PRAGMA foreign_keys = ON;")

    if not query.exec_(f"""INSERT INTO Ranking (REmpid, RDepid, RPosid)
                    VALUES ('{emp_record}', '{dep_record}', '{pos_record}')"""):
        print("*************Error: insert Ranking:", query.lastError().text())
        QMessageBox.critical(
            None,
            "App Name - Error!",
            "Database Ranking Error - Вставляются недопустимые данные!",
        )
    else:
        QMessageBox.about(
            None,
            "Успешно",
            "Данные добавлены!"
        )

    print("OK - insert Ranking by button ")