# Скрипт создания таблиц БД в SQLite
import sqlite3
from sqlite3 import Error

path = r"test1_mysql.db3"


def create_connection(path):
    """ Функция подключения к БД """
    connection = None
    try:
        connection = sqlite3.connect(path)
        connection.execute("PRAGMA foreign_keys = ON")   # по умолчанию в SQLite ключи отключены для отладки
        print("Connection to SQLite DB successful!")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


def execute_query(connection, query):
    """
    Функция выполняет сформированные запросы и делает коммит в базу.

    :connection: установленное соединение с БД
    :query:      содержит запрос SQL
    """
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print(f"Next Query executed successfully: {query}")
    except Error as e:
        print(f"The error '{e}' occurred")


#1 создание таблицы с типами приказов
create_orders_type_table = """
CREATE TABLE IF NOT EXISTS TypeOrder (
  TOid INTEGER PRIMARY KEY AUTOINCREMENT,
  TOtype NVARCHAR(7) NOT NULL CHECK (TOtype IN ('Зачислить', 'Уволить', 'Поставить', 'Снять'))           --тип приказа
  --TOtype NVARCHAR(7) NOT NULL CHECK (TOtype IN ('Create', 'Close', 'Accept', 'Dismiss', 'In', 'Out'))  --тип приказа
 );
"""

#2 создание таблицы с приказами
create_orders_table = """
CREATE TABLE IF NOT EXISTS Orders (
  Ordid INTEGER PRIMARY KEY AUTOINCREMENT, 
  Onumber TEXT UNIQUE NOT NULL CHECK (Onumber !='' and length (Onumber) <= 7),       --номер приказа
  Odate DATE DEFAULT CURRENT_DATE,                                                   --дата приказа
  Oname NVARCHAR(20) NOT NULL CHECK (Oname !='' and length (Oname) <= 20),           --фамилия подписавшего
  Otype INTEGER NOT NULL,                                                            --внешний ключ на тип приказа 
  CONSTRAINT orders_typeorder_fk                                         
  FOREIGN KEY (Otype) REFERENCES TypeOrder (TOid) ON DELETE RESTRICT 
);
"""

#3 создание таблицы подразделение
create_table_department = """
CREATE TABLE IF NOT EXISTS Department (
  Depid INTEGER PRIMARY KEY AUTOINCREMENT,
  Dname NVARCHAR(100) UNIQUE NOT NULL CHECK (length (Dname) <= 100),              --название подразделения
  Headname NVARCHAR(100) NULL CHECK (length (Headname) <= 100),                   --название головного
  Chief NVARCHAR(50) NOT NULL CHECK (length (Chief) <= 50),                      --фамилия начальника
  PhoneChief NVARCHAR(20) NOT NULL UNIQUE CHECK (PhoneChief !='' and length (PhoneChief) <= 20)                       
); 
"""

#4 создание таблицы сотрудников
create_employee_table = """
CREATE TABLE IF NOT EXISTS Employee (
  Empid INTEGER PRIMARY KEY AUTOINCREMENT,
  Firstname NVARCHAR(50) NOT NULL CHECK (length (firstname) <= 50),                  --имя сотрудника
  Lastname NVARCHAR(50) NOT NULL CHECK (length (lastname) <= 50),                    --фамилия сотрудника
  Borndate DATE DEFAULT NULL,                                                        --дата рождения
  Address NVARCHAR(100) NOT NULL CHECK (length (Address) <= 100),                    --адрес
  Phone NVARCHAR(20) NOT NULL UNIQUE CHECK (Phone !='' and length (Phone) <= 20),    --телефон  
  AcceptOrder NVARCHAR(30) NOT NULL CHECK (length (AcceptOrder) <= 30),              --номер приказа принятия 'Accept'
  DismissOrder NVARCHAR(30) DEFAULT NULL CHECK (length (DismissOrder) <= 30),        --номер приказа увольнения 'Dismiss'
  EmpOrdid INTEGER NOT NULL,                                                         --внешний ключ на приказ
  CONSTRAINT employee_orders_fk
  FOREIGN KEY (EmpOrdid) REFERENCES Orders (Ordid) ON DELETE RESTRICT 
);
"""

#5 создание таблицы справочник должностей
# create_catalog_position_table = """
# CREATE TABLE IF NOT EXISTS CatalogPosition (
#   CatPosid INTEGER PRIMARY KEY AUTOINCREMENT,
#   PositionName NVARCHAR(40) NOT NULL CHECK (length (PositionName) <= 40),               --должность
#   MinSalary MONEY NOT NULL CHECK (MinSalary > 0),                                       --минимальный оклад
#   MaxSalary MONEY NOT NULL,                                                             --максимальный оклад
#   CONSTRAINT ch_catalog_position_money CHECK (MaxSalary >= MinSalary)
# );
# """

#6 создание таблицы закрепленная должность
create_position_table = """
CREATE TABLE IF NOT EXISTS Positions (
  Posid INTEGER PRIMARY KEY AUTOINCREMENT,
  InOrder NVARCHAR(30) NOT NULL CHECK (length (InOrder) <= 30),                           --приказ на постановку на должность
  OutOrder NVARCHAR(30) DEFAULT NULL CHECK (length (OutOrder) <= 30),                     --приказ снятия с должности
  PositionName NVARCHAR(40) NOT NULL CHECK (length (PositionName) <= 40),                 --должность
  Bet FLOAT CHECK (Bet >= 0.5 AND Bet <= 2) NOT NULL,                                     --ставка зарплаты конкр сотрудника
  Salary INTEGER NOT NULL,                                                                --зарплата конкр сотрудника    
  --SumSalary FLOAT AS (Bet * Salary) NOT NULL, --stored хранит, этот нет                 --высиляемый столбец ЗП
  SumSalary FLOAT NOT NULL, 
  PosOrdid INTEGER NOT NULL,                                                              --внешний ключ на приказ
  CONSTRAINT position_orders_fk
  FOREIGN KEY (PosOrdid) REFERENCES Orders (Ordid) ON DELETE RESTRICT 
);
"""

# 7 связывающая таблица расстановки сотрудников по подразделениям с должностями
create_ranking_table = """
CREATE TABLE IF NOT EXISTS Ranking (
  Rankid INTEGER PRIMARY KEY AUTOINCREMENT,
  REmpid INTEGER NOT NULL,                              --связываем с табл Employee
  RDepid INTEGER NOT NULL,                              --связываем с табл Department
  RPosid INTEGER NOT NULL,                               --связываем с табл Position
  CONSTRAINT ranking_employee_fk
  FOREIGN KEY (REmpid) REFERENCES Employee (Empid) ON DELETE CASCADE,
  CONSTRAINT ranking_department_fk
  FOREIGN KEY (RDepid) REFERENCES Department (Depid) ON DELETE CASCADE,
  CONSTRAINT ranking_position_fk
  FOREIGN KEY (RPosid) REFERENCES Positions (Posid) ON DELETE CASCADE
);
"""

if __name__ == "__main__":

    con1 = create_connection(path)

    execute_query(con1, create_orders_type_table)               #1
    execute_query(con1, create_orders_table)                    #2
    execute_query(con1, create_table_department)                #3
    execute_query(con1, create_employee_table)                  #4
    # execute_query(con1, create_catalog_position_table)          #5
    execute_query(con1, create_position_table)                  #6
    execute_query(con1, create_ranking_table)                   #7

