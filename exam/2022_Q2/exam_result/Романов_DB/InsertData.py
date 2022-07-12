# Скрипт начального наполнения таблиц БД тестовыми данными
import sys
from PySide2.QtSql import QSqlDatabase, QSqlQuery

path = r"test1_mysql.db3"


# Создаем соединение с БД
connection = QSqlDatabase.addDatabase("QSQLITE")
connection.setDatabaseName(path)

if not connection.open():
    print("Database Error: %s" % connection.lastError().databaseText())
    sys.exit(1)

query = QSqlQuery()
query.exec_("PRAGMA foreign_keys = ON;")   # !!!!!!!!!!!! ОБЯЗАТЕЛЬНО ДЛЯ РАБОТЫ FOREIGN KEY

# Добавляем типы приказов в табл TypeOrder
if not query.exec_(f"""INSERT INTO TypeOrder (TOtype) 
                VALUES ('Зачислить'),('Уволить'),('Поставить'),('Снять')"""):
    print("*************Error: insert TypeOrder:", query.lastError().text())
print("Success: insert TypeOrder")

# добавляем в таблицу Orders 6 приказов (2 зачислить, 2 поставить, 1 уволить, 1 снять)
if not query.exec_(f"""INSERT INTO Orders (Onumber, Oname, Odate, Otype)
                VALUES ('501', 'Williams', '01.03.2022', '1'),('503', 'Williams', '01.03.2022', '1'), --2 зачислить
                       ('610', 'Иванов', '03.05.2022', '3'),('611', 'Иванов', '03.05.2022', '3'),     --2 поставить
                       ('399', 'Семонов', '11.08.2022', '2'),('807', 'Семенов', '21.10.2022', '4')    --1 уволить и 1 снять  
"""):
    print("*************Error: insert Orders:", query.lastError().text())
print("Success: insert Orders")

# добавляем в таблицу Employee 3 сотрудников
if not query.exec_(f"""INSERT INTO Employee (Firstname, Lastname, Borndate, AcceptOrder, Address, Phone, EmpOrdid)
                VALUES ('Олег', 'Андреев', '01.03.1987', '501', 'Москва, Измайлова пр. 7-10', '+79213333333', '1'),   
                       ('Петр', 'Бочкин', '01.10.1977', '503', 'СПб, Невский 15-47', '+79051111111', '2'),
                       ('Илья', 'Кучкин', '22.02.1973', '503', 'Курск, Заоблачная 10-1', '+79045557791', '2')
"""):
    print("*************Error: insert Employee:", query.lastError().text())
print("Success: insert Employee")

if not query.exec_(f"""INSERT INTO Department (Dname, Headname, Chief, PhoneChief)
                VALUES ('Сварочный цех', 'ПАО Логово', 'Смирнов А.А.', '+79213333333'),   
                       ('Малярный цех', 'ПАО Логово', 'Иванов И.И.', '+79214444444'),
                       ('Конструкторское бюро', 'ПАО Логово', 'Сумкин И.И.', '+79215555555')
"""):
    print("*************Error: insert Department:", query.lastError().text())
print("Success: insert Department")

# добавляем в таблицу Position 3 сотрудников
if not query.exec_(f"""INSERT INTO Positions (InOrder, OutOrder, PositionName, Bet, Salary, SumSalary, PosOrdid)
                VALUES ('610', NULL, 'Сварщик', '1.5', '500', '750', '3'),   
                       ('611', NULL, 'Маляр', '1.8', '400', '720', '4')
                       --('610', NULL, 'Сварщик', '1.5', '500', '3'),   
                       --('611', NULL, 'Маляр', '1.8', '400', '4'),
                       --('503', '807', 'Чертежник', '1.9', '700', '6')
"""):
    print("*************Error: insert Positions:", query.lastError().text())
print("Success: insert Positions")

# добавляем в таблицу Ranking 1 расстановку
if not query.exec_(f"""INSERT INTO Ranking (REmpid, RDepid, RPosid)
                VALUES ('3', '1', '1')   
"""):
    print("*************Error: insert Ranking:", query.lastError().text())
print("Success: insert Ranking")