# Скрипт начального наполнения таблиц БД тестовыми данными
import sys
from PySide2.QtSql import QSqlDatabase, QSqlQuery

CONST_PATH1 = r"test1_mysql.db3"
path = CONST_PATH1

# Создаем соединение с БД
con3 = QSqlDatabase.addDatabase("QSQLITE")
con3.setDatabaseName(path)

if not con3.open():
    print("Database Error: %s" % con3.lastError().databaseText())
    sys.exit(1)

query = QSqlQuery()
query.exec_("PRAGMA foreign_keys = ON;")   # !!!!!!!!!!!! ОБЯЗАТЕЛЬНО ДЛЯ РАБОТЫ АЩКУШПТ ЛУНЫ


# Обновление данных в таблице - рабочие
# query.exec_(f"""UPDATE Orders SET Onumber = 505 where Ordid = 4""");
# аналог рабочий
# query.exec_(f"""UPDATE Orders SET Onumber = '505' where Ordid = '4'""");

# Удаление данных в таблице рабочее
# if not query.exec_(f"""DELETE FROM Orders where Ordid = 6"""):
#     print("Data not deleted")

if not query.exec_(f"""DELETE FROM Orders where Oname = 'Романов'"""):
     print("Data not deleted Orders")
if not query.exec_(f"""DELETE FROM TypeOrder where TOid = 3"""):
    print("Data not deleted TypeOrder")
    if not query.exec_(f"""DELETE FROM TypeOrder where TOid = 1"""):
        print("Data not deleted TypeOrder")
print("Data deleted!")
# def create_connection(path):
#     """ Функция подключения к БД """
#     connection = None
#     try:
#         connection = sqlite3.connect(path)
#         print("Connection to SQLite DB successful")
#     except Error as e:
#         print(f"The error '{e}' occurred")
#
#     return connection
#
#
# def execute_query(connection, query):
#     """ Функция выполняет сформированные запросы и делает коммит в базу"""
#     cursor = connection.cursor()
#     try:
#         cursor.execute(query)
#         connection.commit()
#         print("Query executed successfully")
#     except Error as e:
#         print(f"The error '{e}' occurred")


# #1 создание таблицы с типами приказов
# create_orders_type_table = """
# CREATE TABLE IF NOT EXISTS TypeOrder (
#   TOid INTEGER PRIMARY KEY AUTOINCREMENT,
#   TOtype NVARCHAR(10) NOT NULL CHECK (TOtype IN ('Create', 'Close', 'Accept', 'Dismiss', 'In', 'Out'))  --тип приказа
#  );
# """
#
# #2 создание таблицы с приказами
# create_orders_table = """
# CREATE TABLE IF NOT EXISTS Orders (
#   Ordid INTEGER PRIMARY KEY AUTOINCREMENT,
#   Otype INTEGER NOT NULL,
#   Onumber NVARCHAR(10) UNIQUE NOT NULL,             --номер приказа
#   Odate DATE DEFAULT CURRENT_DATE,                  --дата приказа
#   Oname NVARCHAR(50) NOT NULL,                      --фамилия подписавшего
#   CONSTRAINT orders_typeorder_fk                    --внешний ключ на тип приказа
#   FOREIGN KEY (Otype) REFERENCES TypeOrder (TOid) ON DELETE NO ACTION
# );
# """
#
#
#
# if __name__ == "__main__":
#
#     con1 = create_connection(path)
#
#     execute_query(con1, create_orders_type_table)               #1
#
#
#     cursor = con1.cursor()
#     cursor.fetchall()