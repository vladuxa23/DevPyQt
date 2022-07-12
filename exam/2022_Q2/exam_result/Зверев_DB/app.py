from PySide2 import QtWidgets, QtGui
from PySide2.QtWidgets import QMessageBox
from ui import Myapp
import pyodbc
from datetime import datetime


class Myapps(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Myapp.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.dateEdit_2.setDate(datetime.now())

        self.connectDB()

        self.maintablewiget()
        self.initCombobox()
        self.initTableview()
        self.initPodrazdelenie()
        self.ininTableviewSotrudnikList(sort=None)
        self.ininTableviewSotrudnikList2(sort=None)
        self.ui.dateEdit.dateChanged.connect(self.maintablewiget)
        self.ui.dateEdit_2.dateChanged.connect(self.maintablewiget)
        self.ui.pushButton.clicked.connect(self.addSotrudnik)
        self.ui.pushButton_3.clicked.connect(self.addOtdela)
        self.ui.pushButton_5.clicked.connect(self.addDolznost)
        self.ui.pushButton_6.clicked.connect(self.dellDolznost)
        self.ui.pushButton_4.clicked.connect(self.dellPodrazdelenie)
        self.ui.lineEdit_7.textChanged.connect(self.sorted)
        self.ui.pushButton_2.clicked.connect(self.uvolnenie)
        self.ui.lineEdit_11.textChanged.connect(self.sorted2)
        self.ui.pushButton_7.clicked.connect(self.perevod)

    def connectDB(self):
        server = 'tcp:vpngw.avalon.ru'
        database = 'DEVDB2022_EVGZVE'
        username = 'tsqllogin'
        password = 'Pa$$w0rd'

        self.conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
        self.cursor = self.conn.cursor()

    def maintablewiget(self):
        data1 = self.ui.dateEdit.dateTime().toString('yyyy-MM-dd')
        data2 = self.ui.dateEdit_2.dateTime().toString('yyyy-MM-dd')

        print(data1, data2)
        values = (f'{data1}', f'{data2}')
        self.cursor.execute("SELECT DB.idPricaza, DB.data_prikaza, (NZ.Name_naznaceniy), "
                            "LTRIM(RTRIM(SO.Lname))+ ' '+LTRIM(RTRIM(SO.Fname)) FROM dbo.DBPricazi AS DB "
                            "INNER JOIN dbo.Naznacenie AS NZ ON DB.idNaznaceniy = NZ.id "
                            "INNER JOIN dbo.SotrudnikiList AS SO ON DB.idSotrudnicaPodpis = SO.idSotrudnika "
                            "WHERE data_prikaza BETWEEN ? AND ? ORDER BY DB.idPricaza DESC", values)
        lst = self.cursor.fetchall()
        sim = QtGui.QStandardItemModel()
        for elem in lst:
            item1 = QtGui.QStandardItem(str(elem[0]))
            item2 = QtGui.QStandardItem(str(elem[1]))
            item3 = QtGui.QStandardItem(str(elem[2]))
            item4 = QtGui.QStandardItem(str(elem[3]))

            sim.appendRow([item1, item2, item3, item4])
        sim.setHorizontalHeaderLabels(["№Приказа", "Дата приказа", "Вид приказа", "Подписал"])
        self.ui.tableView_4.setModel(sim)
        self.ui.tableView_4.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.ui.tableView_4.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

    def initCombobox(self):
        self.ui.comboBox.clear()
        self.ui.comboBox_11.clear()
        self.ui.comboBox_4.clear()
        self.ui.comboBox_10.clear()
        self.ui.comboBox_5.clear()
        self.ui.comboBox_9.clear()
        self.ui.comboBox_2.clear()

        self.ui.comboBox.addItems(" ")
        self.ui.comboBox_11.addItems(" ")
        self.ui.comboBox_4.addItems(" ")
        self.ui.comboBox_10.addItems(" ")
        self.ui.comboBox_5.addItems(" ")
        self.ui.comboBox_9.addItems(" ")
        self.ui.comboBox_2.addItems(" ")

        self.cursor.execute("SELECT LTRIM(RTRIM(NamePodrazdeleniy)) "
                            "FROM dbo.StrukturaPredpriytiy WHERE idPricazaUprozneniy IS NULL")
        lst = self.cursor.fetchall()
        for i in lst:
            self.ui.comboBox.addItems(list(i))
            self.ui.comboBox_11.addItems(list(i))
            self.ui.comboBox_4.addItems(list(i))
            self.ui.comboBox_10.addItems(list(i))

        self.cursor.execute("SELECT LTRIM(RTRIM(NameDoljnosti)) "
                            "FROM dbo.SpisocDoljnostei")
        lst2 = self.cursor.fetchall()
        for i in lst2:
            self.ui.comboBox_5.addItems(list(i))
            self.ui.comboBox_9.addItems(list(i))
            self.ui.comboBox_2.addItems(list(i))

    def initTableview(self):
        self.cursor.execute("SELECT LTRIM(RTRIM(NameDoljnosti)), "
                            "LTRIM(RTRIM(MinOklad)), LTRIM(RTRIM(MaxOklad))"
                            " FROM dbo.SpisocDoljnostei")
        lst = self.cursor.fetchall()
        sim = QtGui.QStandardItemModel()
        for elem in lst:
            item1 = QtGui.QStandardItem(str(elem[0]))
            item2 = QtGui.QStandardItem(str(elem[1]))
            item3 = QtGui.QStandardItem(str(elem[2]))
            sim.appendRow([item1, item2, item3])

        sim.setHorizontalHeaderLabels(["Должность", "Минимальный оклад", "Максимальный оклад"])
        self.ui.tableView_3.setModel(sim)
        self.ui.tableView_3.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.ui.tableView_3.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

    def TableviewSotrudnikList(self, sort):

        if sort == None:
            self.cursor.execute("SELECT idSotrudnika, LTRIM(RTRIM(Lname)), LTRIM(RTRIM(Fname)), "
                            "LTRIM(RTRIM(Otchestvo)),DataRojdeniy, AdresRegistracii, Telefon, Mail "
                            "FROM dbo.SotrudnikiList WHERE idPricazaUvolneniy IS NULL ")
        else:

            self.cursor.execute("SELECT idSotrudnika, LTRIM(RTRIM(Lname)), LTRIM(RTRIM(Fname)), "
                                "LTRIM(RTRIM(Otchestvo)),DataRojdeniy, AdresRegistracii, Telefon, Mail "
                                "FROM dbo.SotrudnikiList WHERE idPricazaUvolneniy IS NULL AND idSotrudnika = ?", sort)

        lst = self.cursor.fetchall()
        sim = QtGui.QStandardItemModel()
        for elem in lst:
            item1 = QtGui.QStandardItem(str(elem[0]))
            item2 = QtGui.QStandardItem(str(elem[1]))
            item3 = QtGui.QStandardItem(str(elem[2]))
            item4 = QtGui.QStandardItem(str(elem[3]))
            item5 = QtGui.QStandardItem(str(elem[4]))
            item6 = QtGui.QStandardItem(str(elem[5]))
            item7 = QtGui.QStandardItem(str(elem[6]))
            item8 = QtGui.QStandardItem(str(elem[7]))
            sim.appendRow([item1, item2, item3, item4, item5, item6, item7, item8])
            sim.setHorizontalHeaderLabels(["ID", "Фамилия", "Имя", "Отчество",
                                           "Дата рождения", "Адрес регистрации",
                                           "Телефон", "Email"])
        return sim

    def ininTableviewSotrudnikList(self, sort):

        sim = self.TableviewSotrudnikList(sort)
        self.ui.tableView_2.setModel(sim)
        self.ui.tableView_2.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.ui.tableView_2.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

    def ininTableviewSotrudnikList2(self, sort):
        sim = self.TableviewSotrudnikList(sort)
        self.ui.tableView.setModel(sim)
        self.ui.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

    def initPodrazdelenie(self):
        self.cursor.execute("SELECT  SP.NamePodrazdeleniy, COUNT(idSotrudnika)  "
                            "FROM dbo.ShtatnoeRaspisanie AS SR INNER JOIN dbo.StrukturaPredpriytiy AS SP "
                            "ON SR.idPodrazdeleniy = SP.idPodrazdeleniy  GROUP BY SP.NamePodrazdeleniy")
        lst = self.cursor.fetchall()
        sim = QtGui.QStandardItemModel()
        for elem in lst:
            item1 = QtGui.QStandardItem(str(elem[0]))
            item2 = QtGui.QStandardItem(str(elem[1]))
            sim.appendRow([item1, item2])
            sim.setHorizontalHeaderLabels(["Наименование отдела ", "Кол-во сотрудников"])
        self.ui.tableView_5.setModel(sim)
        self.ui.tableView_5.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.ui.tableView_5.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

    def addSotrudnik(self):

        if self.ui.lineEdit.text() == '':
            QMessageBox.warning(self, '', "Не заполнена строка Фамилия")
            return
        if self.ui.lineEdit_2.text() == '':
            QMessageBox.warning(self, '', "Не заполнена строка Имя")
            return
        if self.ui.lineEdit_4.text() == '':
            QMessageBox.warning(self, '', "Не заполнена строка Адрес")
            return
        if self.ui.lineEdit_5.text() == '':
            QMessageBox.warning(self, '', "Не заполнена строка Телефон")
            return
        if self.ui.comboBox.currentIndex() == 0:
            QMessageBox.warning(self, '', "Не выбран отдел")
            return
        if self.ui.comboBox_2.currentIndex() == 0:
            QMessageBox.warning(self, '', "Не выбрана должность")
            return

        self.cursor.execute("SELECT MAX(idPricaza) "
                            "FROM dbo.DBPricazi")
        lst = self.cursor.fetchone()

        self.cursor.execute("SELECT MAX(idSotrudnika) "
                            "FROM dbo.SotrudnikiList")
        lst2 = self.cursor.fetchone()

        values = (lst[0]+1, f'{datetime.now().date()}', 1, 1)
        values1 = (lst2[0]+1, f'{self.ui.lineEdit.text()}',
                   f'{self.ui.lineEdit_2.text()}', f'{self.ui.lineEdit_3.text()}',
                   f'{self.ui.dateEdit_3.dateTime().toString("yyyy-MM-dd")}',
                   f'{self.ui.lineEdit_4.text()}', f'{self.ui.lineEdit_5.text()}',
                   f'{self.ui.lineEdit_6.text()}', lst[0]+1)

        values2 = (lst2[0]+1, self.ui.comboBox.currentIndex(), self.ui.comboBox_2.currentIndex(), 100, lst[0]+1, None)
        self.cursor.execute("INSERT INTO dbo.DBPricazi (idPricaza, data_prikaza, "
                            "idNaznaceniy, idSotrudnicaPodpis) VALUES (?,?,?,?)", values)

        self.cursor.execute("INSERT INTO [dbo].[SotrudnikiList] ("
                            "[idSotrudnika],[Lname],[Fname],[Otchestvo],"
                            "[DataRojdeniy],[AdresRegistracii],"
                            "[Telefon],[Mail],[idPricazaPriema]) VALUES (?,?,?,?,?,?,?,?,?)", values1)

        self.cursor.execute("INSERT INTO dbo.ShtatnoeRaspisanie ("
                            "[idSotrudnika],[idPodrazdeleniy],[idDoljnosti],"
                            "[Stavka_Procenti],[idPrikazaNaznaceniy],[idPricazaSnytiys])"
                            " VALUES (?,?,?,?,?,?)", values2)

        QMessageBox.about(self, 'Прием на работу',
                          f'{self.ui.lineEdit.text()} {self.ui.lineEdit_2.text()} {self.ui.lineEdit_3.text()} Добавлен в базу')
        self.cursor.commit()

        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_3.clear()
        self.ui.lineEdit_4.clear()
        self.ui.lineEdit_5.clear()
        self.ui.lineEdit_6.clear()
        self.ui.comboBox.setCurrentIndex(0)
        self.ui.comboBox_2.setCurrentIndex(0)
        self.ininTableviewSotrudnikList(None)
        self.initTableview()

    def addOtdela(self):

        if self.ui.lineEdit_8.text() == '':
            QMessageBox.warning(self, 'Ошибка', "Не указан отдел")
            return
        self.cursor.execute("SELECT idPodrazdeleniy "
                            "FROM dbo.StrukturaPredpriytiy "
                            "WHERE NamePodrazdeleniy = ?",
                            self.ui.lineEdit_8.text())
        lst = self.cursor.fetchone()

        if lst is not None:
            QMessageBox.warning(self, 'Ошибка', "Такой отдел уже есть")
            return
        self.cursor.execute("SELECT MAX(idPricaza) "
                            "FROM dbo.DBPricazi")
        lst3 = self.cursor.fetchone()
        values = (lst3[0] + 1, f'{datetime.now().date()}', 3, 1)

        self.cursor.execute("INSERT INTO dbo.DBPricazi (idPricaza, data_prikaza, "
                            "idNaznaceniy, idSotrudnicaPodpis) VALUES (?,?,?,?)", values)

        self.cursor.execute("SELECT MAX(idPodrazdeleniy) "
                            "FROM dbo.StrukturaPredpriytiy")
        lst1 = self.cursor.fetchone()
        if self.ui.comboBox_11.currentIndex() == 0:
            lst2 = None
        else:
            self.cursor.execute("SELECT idPodrazdeleniy "
                                "FROM dbo.StrukturaPredpriytiy "
                                "WHERE NamePodrazdeleniy = ?",
                                self.ui.comboBox_11.currentText())
            a= self.cursor.fetchone()
            lst2 = a[0]

        values1 = (lst1[0] + 1, f'{self.ui.lineEdit_8.text()}', lst2, lst3[0] + 1, None)

        self.cursor.execute("INSERT INTO dbo.StrukturaPredpriytiy ("
                            "idPodrazdeleniy, NamePodrazdeleniy, idRukPodrazdeleniy, "
                            "idPricazaSozdaniy, idPricazaUprozneniy) VALUES (?,?,?,?,?)", values1)
        QMessageBox.about(self, 'Создан',
                          f'{self.ui.lineEdit_8.text()}  Добавлен в базу')
        self.cursor.commit()
        self.ui.lineEdit_8.clear()
        self.ui.comboBox_11.setCurrentIndex(0)
        self.initCombobox()
        self.maintablewiget()

    def addDolznost(self):
        if self.ui.lineEdit_9.text() == '':
            QMessageBox.warning(self, 'Ошибка', "Укажите должность")
            return

        self.cursor.execute("SELECT idDoljnosti "
                            "FROM dbo.SpisocDoljnostei "
                            "WHERE NameDoljnosti = ?",
                            self.ui.lineEdit_9.text())
        lst = self.cursor.fetchone()

        if lst is not None:
            QMessageBox.warning(self, 'Ошибка', "Такая должность уже есть")
            return

        if self.ui.lineEdit_10.text() == '':
            QMessageBox.warning(self, 'Ошибка', "Минимальная ставка не указана")
            return

        if self.ui.lineEdit_12.text() == '':
            QMessageBox.warning(self, 'Ошибка', "Максимальная ставка не указана")
            return

        if self.testFloat(self.ui.lineEdit_10.text()) and self.testFloat(self.ui.lineEdit_12.text()) == False:
            QMessageBox.warning(self, 'Ошибка', "Максимальная или минимальная ставка не является числом")
            return

        if float(self.ui.lineEdit_10.text()) >= float(self.ui.lineEdit_12.text()):
            QMessageBox.warning(self, 'Ошибка', "Максимальная ставка должна быть больше")
            return
        self.cursor.execute("SELECT MAX(idDoljnosti) "
                            "FROM dbo.SpisocDoljnostei ")
        lst1 = self.cursor.fetchone()
        values = (lst1[0]+1, self.ui.lineEdit_9.text(),
                  float(self.ui.lineEdit_10.text()),
                  float(self.ui.lineEdit_12.text()))

        self.cursor.execute("INSERT INTO dbo.SpisocDoljnostei (idDoljnosti, "
                            "NameDoljnosti, MinOklad, MaxOklad)VALUES (?,?,?,?)", values)
        QMessageBox.about(self, 'Создан',
                          f'{self.ui.lineEdit_9.text()} должность добавлена в базу')
        self.cursor.commit()
        self.ui.lineEdit_9.clear()
        self.ui.lineEdit_10.clear()
        self.ui.lineEdit_12.clear()
        self.initCombobox()
        self.initTableview()

    def dellDolznost(self):

        if self.ui.comboBox_5.currentText() == " ":
            QMessageBox.warning(self, 'Ошибка', "Не выбрана должность")
            return
        values = (self.ui.comboBox_5.currentText())
        self.cursor.execute("SELECT idSotrudnika "
                            "FROM dbo.ShtatnoeRaspisanie "
                            "WHERE idDoljnosti = (SELECT idDoljnosti "
                            "FROM dbo.SpisocDoljnostei WHERE NameDoljnosti = ?)", values)
        lst1 = self.cursor.fetchall()
        if len(lst1) > 0:
            QMessageBox.warning(self, 'Ошибка', f"На данной должности работают {len(lst1)} сотрудников")
            return
        self.cursor.execute("DELETE FROM dbo.SpisocDoljnostei WHERE NameDoljnosti = ?", values)
        QMessageBox.about(self, 'удаление', f'{values} должность удалена')
        self.cursor.commit()
        self.initCombobox()
        self.initTableview()

    def dellPodrazdelenie(self):
        if self.ui.comboBox_4.currentText() == " ":
            QMessageBox.warning(self, 'Ошибка', "Не выбрано подразделение")
            return
        values = (self.ui.comboBox_4.currentText())
        self.cursor.execute("SELECT idSotrudnika "
                            "FROM dbo.ShtatnoeRaspisanie "
                            "WHERE idPodrazdeleniy = (SELECT idPodrazdeleniy "
                            "FROM dbo.StrukturaPredpriytiy WHERE NamePodrazdeleniy = ?)", values)
        lst1 = self.cursor.fetchall()
        if len(lst1) > 0:
            QMessageBox.warning(self, 'Ошибка', f"В данном подразделении работает {len(lst1)} сотрудников")
            return
        self.cursor.execute("SELECT MAX(idPricaza) "
                            "FROM dbo.DBPricazi")
        lst = self.cursor.fetchone()
        values1 = (lst[0] + 1, f'{datetime.now().date()}', 4, 1)
        values2 = (lst[0] + 1, values)
        self.cursor.execute("INSERT INTO dbo.DBPricazi (idPricaza, data_prikaza, "
                            "idNaznaceniy, idSotrudnicaPodpis) VALUES (?,?,?,?)", values1)

        self.cursor.execute("SELECT idPodrazdeleniy, idRukPodrazdeleniy "
                            "FROM dbo.StrukturaPredpriytiy WHERE NamePodrazdeleniy = ?", values)
        lst2 = self.cursor.fetchone()
        values4 = (lst2[0])
        print(values4)
        self.cursor.execute("SELECT idPodrazdeleniy FROM dbo.StrukturaPredpriytiy "
                            "WHERE idRukPodrazdeleniy = ?", values4)
        lst3 = self.cursor.fetchall()

        for i in lst3:
            values3 = (lst2[1], i[0])
            self.cursor.execute("UPDATE dbo.StrukturaPredpriytiy SET idRukPodrazdeleniy = ? "
                                "WHERE idPodrazdeleniy = ?", values3)
            self.cursor.commit()
        self.cursor.execute("UPDATE dbo.StrukturaPredpriytiy "
                            "SET idPricazaUprozneniy =? WHERE NamePodrazdeleniy = ?", values2)
        QMessageBox.about(self, 'удаление', f'{values} упразднено')
        self.cursor.commit()
        self.initCombobox()
        self.maintablewiget()
        self.initPodrazdelenie()

    def sorted(self):
        a = self.ui.lineEdit_7.text()
        if a == '':
            self.ininTableviewSotrudnikList2(None)
            return
        if self.ui.comboBox_3.currentIndex() == 0:
            if self.testInt(a) == False:
                QMessageBox.warning(self, 'Ошибка', f"ID должна быть целым числом")
                return
            else:
                self.ininTableviewSotrudnikList2(int(a))

    def sorted2(self):
        a = self.ui.lineEdit_11.text()
        if a == '':
            self.ininTableviewSotrudnikList(None)
            return
        if self.ui.comboBox_6.currentIndex() == 0:
            if self.testInt(a) == False:
                QMessageBox.warning(self, 'Ошибка', f"ID должна быть целым числом")
                return
            else:
                self.ininTableviewSotrudnikList(int(a))


    def uvolnenie(self):
        values = self.ui.lineEdit_11.text()
        if values == '':
            QMessageBox.warning(self, 'Ошибка', f"не указан ID")
            return
        if self.ui.comboBox_6.currentIndex() == 0:
            if self.testInt(values) == False:
                QMessageBox.warning(self, 'Ошибка', f"ID должна быть целым числом")
                return
            else:
                self.cursor.execute("SELECT MAX(idPricaza) "
                                    "FROM dbo.DBPricazi")
                lst = self.cursor.fetchone()
                values1 = (lst[0] + 1, f'{datetime.now().date()}', 2, 1)
                values2 = (lst[0]+1, int(values))
                self.cursor.execute("INSERT INTO dbo.DBPricazi (idPricaza, data_prikaza, "
                                    "idNaznaceniy, idSotrudnicaPodpis) VALUES (?,?,?,?)", values1)

                self.cursor.execute("UPDATE dbo.ShtatnoeRaspisanie "
                                    "SET idPricazaSnytiys =? WHERE idSotrudnika =?", values2)

                self.cursor.execute("UPDATE dbo.SotrudnikiList "
                                    "SET idPricazaUvolneniy =? WHERE idSotrudnika =? ", values2)
                self.cursor.commit()
                QMessageBox.about(self, 'увольнение', f'Сотрудник уволен')
                self.ui.lineEdit_7.clear()
                self.ininTableviewSotrudnikList2(None)
                self.maintablewiget()
                self.initPodrazdelenie()

    def perevod(self):
        values = self.ui.lineEdit_11.text()
        if values == '':
            QMessageBox.warning(self, 'Ошибка', f"не указан ID")
            return
        if self.ui.comboBox_10.currentIndex() ==0:
            QMessageBox.warning(self, 'Ошибка', f"Не выбран отдел назначения")
            return
        if self.ui.comboBox_9.currentIndex() == 0:
            QMessageBox.warning(self, 'Ошибка', f"Не выбрана должность")
            return
        if self.ui.comboBox_3.currentIndex() == 0:
            if self.testInt(values) == False:
                QMessageBox.warning(self, 'Ошибка', f"ID должна быть целым числом")
                return
            else:
                self.cursor.execute("SELECT MAX(idPricaza) "
                                    "FROM dbo.DBPricazi")
                lst = self.cursor.fetchone()
                values1 = (lst[0] + 1, f'{datetime.now().date()}', 2, 1)
                values2 = (lst[0] + 1, int(values))
                self.cursor.execute("INSERT INTO dbo.DBPricazi (idPricaza, data_prikaza, "
                                    "idNaznaceniy, idSotrudnicaPodpis) VALUES (?,?,?,?)", values1)

                self.cursor.execute("UPDATE dbo.ShtatnoeRaspisanie "
                                    "SET idPricazaSnytiys =? WHERE idSotrudnika =?", values2)

                self.cursor.execute("SELECT idPodrazdeleniy FROM dbo.StrukturaPredpriytiy "
                                    "WHERE NamePodrazdeleniy = ?",
                                    self.ui.comboBox_10.currentText())
                lst1 = self.cursor.fetchone()
                self.cursor.execute("SELECT idDoljnosti FROM dbo.SpisocDoljnostei "
                                    "WHERE NameDoljnosti = ?", self.ui.comboBox_9.currentText())
                lst2 = self.cursor.fetchone()
                values3 = (int(values), lst1[0], lst2[0], 100, lst[0] + 1, None)
                print(values3)
                self.cursor.execute(
                    "INSERT INTO  dbo.ShtatnoeRaspisanie (idSotrudnika, idPodrazdeleniy, idDoljnosti, Stavka_Procenti, idPrikazaNaznaceniy, idPricazaSnytiys) VALUES (?,?,?,?,?,?)", values3)
                self.cursor.commit()
                QMessageBox.about(self, 'увольнение', f'Сотрудник переведен')
                self.ui.lineEdit_7.clear()
                self.ininTableviewSotrudnikList(None)
                self.initCombobox()
                self.maintablewiget()
                self.initPodrazdelenie()
                self.initTableview()

    def testFloat(self, a):
        try:
            float(a)
            return True
        except ValueError:
            return False

    def testInt(self, a):
        try:
            int(a)
            return True
        except ValueError:
            return False


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myapp = Myapps()
    myapp.show()

    app.exec_()
