from PySide2 import QtCore, QtWidgets, QtSql
import sys

"""
Создаем 3 таблицы:
-------------------------------------------------------------------------------------------------
1. Главная таблица orders, которая содержит информацию о заказах. Включает следующие поля:
id - первичный ключ, автоинкремент, тип данных int
date - дата заказа, тип данных date
client - код клиента, тип данных int. Связан с таблицей 'clients'
name - название заказа (виды работ), тип данных text
price - цена заказа, тип данных float
master - код исполнителя, тип данных int. Связан с таблицей 'masters'
complete - заказ выполнен / не выполнен, тип данных bool
paid - заказ оплачен / не оплачен, тип данных bool
-------------------------------------------------------------------------------------------------
2. Таблица 'clients', которая содержит информацию о клиентах. Включает следующие поля:
id - первичный ключ, автоинкремент, тип данных int. Через этот ключ связан с главной таблицей 'orders'
name - название клиента, тип данных text
email - электронная почта клиента, тип данных text
phone - телефон клиента, тип данных text 
about - описание клиента, тип данных text
-------------------------------------------------------------------------------------------------
3. Таблица 'masters', которая содержит информацию об исполнителях. Включает следующие поля:
id - первичный ключ, автоинкремент, тип данных int. Через этот ключ связан с главной таблицей 'orders'
name - имя исполнителя, тип данных text
email - электронная почта исполнителя, тип данных text
Данная функция выполняется только в том случае, если какая-то из этих таблиц отсутствует, тогда она создается заново.
"""


def create_tables():
    query = QtSql.QSqlQuery()
    if 'orders' not in db.tables():
        query.exec("create table orders(id integer primary key autoincrement,"
                   "date date,"
                   "client int,"
                   "name text,"
                   "price float,"
                   "master int,"
                   "complete bool,"
                   "paid bool)")
    if 'clients' not in db.tables():
        query.exec("create table clients(id integer primary key autoincrement,"
                   "name text,"
                   "email text,"
                   "phone text,"
                   "about text) ")
    if 'masters' not in db.tables():
        query.exec("create table masters(id integer primary key autoincrement,"
                   "name text,"
                   "email text) ")


# функция добавления записи в таблицу 'orders'
def addRecord():
    stm.insertRow(stm.rowCount())


# функция добавления запис в таблицу 'masters'
def addMaster():
    stm2.insertRow(stm2.rowCount())


# функция добавления запис в таблицу 'clients'
def addClient():
    stm3.insertRow(stm3.rowCount())


# функция удаления записи из таблицы 'orders'
def delRecord():
    stm.removeRow(tv.currentIndex().row())
    stm.select()


# функция удаления записи из таблицы 'masters'
def delMaster():
    stm2.removeRow(tv2.currentIndex().row())
    stm2.select()


# функция удаления записи из таблицы 'clients'
def delClient():
    stm3.removeRow(tv3.currentIndex().row())
    stm3.select()


# функция открытия окна для редактирования списка исполнителей
def editMasters():
    window2.show()


# функция открытия окна для редактирования списка клиентов
def editClients():
    window3.show()


app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Реестр заказов")
# соединяемся с базой данных, задаем имя базы даннх и открываем ее
db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
db.setDatabaseName('my_orders.sqlite')
db.open()
# создаем модель
stm = QtSql.QSqlRelationalTableModel(parent=window)
stm.setTable('orders')
# задаем для поля категории связь с таблицами клиентов и исполнителей
stm.setRelation(2, QtSql.QSqlRelation('clients', 'id', 'name'))
stm.setRelation(5, QtSql.QSqlRelation('masters', 'id', 'name'))
stm.select()
# задаем название столбцов таблицы с помощью цикла и списка
a = ['Номер', 'Дата', 'Клиент', 'Название заказа', 'Цена', 'Исполнитель', 'Выполнен', 'Оплачен']
for i in range(8):
    stm.setHeaderData(i, QtCore.Qt.Horizontal, a[i])
# задаем для таблицы созданную модель
vbox = QtWidgets.QVBoxLayout()
tv = QtWidgets.QTableView()
tv.setModel(stm)
# использование связанных делегатов для вывода списков
tv.setItemDelegateForColumn(2, QtSql.QSqlRelationalDelegate(tv))
tv.setItemDelegateForColumn(5, QtSql.QSqlRelationalDelegate(tv))
# скрываем первый столбец, содержащий id
tv.hideColumn(0)
# задаем ширину столбцов с помощью цикла и списка
a = [50, 100, 200, 300, 50, 100, 70, 70]
for i in range(8):
    tv.setColumnWidth(i, a[i])
# добавляем в вертикальный контейнер только что созданну таблицу
vbox.addWidget(tv)
# создаем горизонтальный контейнер, где будут размещены 4 кнопки в ряд.
hbox = QtWidgets.QHBoxLayout()
# создаем кнопку "Добавить запись"
btnAdd = QtWidgets.QPushButton("&Добавить запись")
btnAdd.clicked.connect(addRecord)
hbox.addWidget(btnAdd)
# создаем кнопку "Удалить запись"
btnDel = QtWidgets.QPushButton("&Удалить запись")
btnDel.clicked.connect(delRecord)
hbox.addWidget(btnDel)
# создаем кнопку "Исполнители", которая открывает окно для редактирования исполнителей
btnMas = QtWidgets.QPushButton("&Исполнители")
btnMas.clicked.connect(editMasters)
hbox.addWidget(btnMas)
# создаем кнопку "Клиенты", которая открывает окно для редактирования клиентов
btnCli = QtWidgets.QPushButton("&Клиенты")
btnCli.clicked.connect(editClients)
hbox.addWidget(btnCli)
# добавляем горизонтальный контейнер с кнопками в вертикальный, под таблицу
vbox.addLayout(hbox)
window.setLayout(vbox)
window.resize(1000, 400)
window.show()

# Создаем второе окно для редактирования списка исполнителей
window2 = QtWidgets.QWidget()
window2.setWindowTitle("Редактировать список исполнителей")
stm2 = QtSql.QSqlRelationalTableModel(parent=window)
stm2.setTable('masters')
stm2.select()
# Задаем название столбцов таблицы с помощью цикла и списка
a = ['Номер', 'Имя', 'E-mail']
for i in range(3):
    stm2.setHeaderData(i, QtCore.Qt.Horizontal, a[i])
vbox2 = QtWidgets.QVBoxLayout()
tv2 = QtWidgets.QTableView()
tv2.setModel(stm2)
tv2.hideColumn(0)
# задаем ширину столбцов с помощью цикла и списка
a = [50, 100, 200]
for i in range(3):
    tv2.setColumnWidth(i, a[i])
vbox2.addWidget(tv2)
hbox = QtWidgets.QHBoxLayout()
btnAdd = QtWidgets.QPushButton("&Добавить Исполнителя")
btnAdd.clicked.connect(addMaster)
hbox.addWidget(btnAdd)
btnDel = QtWidgets.QPushButton("&Удалить Исполнителя")
btnDel.clicked.connect(delMaster)
hbox.addWidget(btnDel)
vbox2.addLayout(hbox)
window2.setLayout(vbox2)
window2.resize(400, 300)

# Создаем третье окно для редактирования списка клиентов
window3 = QtWidgets.QWidget()
window3.setWindowTitle("Редактировать список клиентов")
stm3 = QtSql.QSqlRelationalTableModel(parent=window)
stm3.setTable('clients')
stm3.select()
# Задаем название столбцов таблицы с помощью цикла и списка
a = ['Номер', 'Имя', 'E-mail', 'Телефон', 'Описание']
for i in range(5):
    stm3.setHeaderData(i, QtCore.Qt.Horizontal, a[i])
vbox3 = QtWidgets.QVBoxLayout()
tv3 = QtWidgets.QTableView()
tv3.setModel(stm3)
tv3.hideColumn(0)
# задаем ширину столбцов с помощью цикла и списка
a = [50, 200, 200, 100, 400]
for i in range(5):
    tv3.setColumnWidth(i, a[i])
vbox3.addWidget(tv3)
hbox = QtWidgets.QHBoxLayout()
btnAdd = QtWidgets.QPushButton("&Добавить Клиента")
btnAdd.clicked.connect(addClient)
hbox.addWidget(btnAdd)
btnDel = QtWidgets.QPushButton("&Удалить Клиента")
btnDel.clicked.connect(delClient)
hbox.addWidget(btnDel)
vbox3.addLayout(hbox)
window3.setLayout(vbox3)
window3.resize(1000, 300)

sys.exit(app.exec_())