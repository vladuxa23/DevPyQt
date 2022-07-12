import random
import sys
import json

import psycopg2
import ui.crud_design
from PySide2 import QtWidgets, QtGui


class Form(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = ui.crud_design.Ui_MainWindow()
        self.ui.setupUi(self)

        self.initSQLModel()

        self.initSignals()

    def initSignals(self):
        self.ui.pushButtonAdd.clicked.connect(self.onPushButtonAddClicked)
        self.ui.pushButtonDel.clicked.connect(self.onPushButtonDelClicked)

    def initSQLModel(self):

        self.con = psycopg2.connect("dbname=demo user=postgres")
        self.cur = self.con.cursor()

        self.cur.execute("SELECT ticket_no, passenger_name, contact_data "
                         "FROM bookings.tickets "
                         "LIMIT 10000")
        data = self.cur.fetchall()

        model = QtGui.QStandardItemModel()
        headers = ["Ticket #", "Passengers", "Phone", "E-mail"]
        model.setHorizontalHeaderLabels(headers)

        for i in range(len(data)):
            for j in range(3):
                model.setItem(i, j, QtGui.QStandardItem(str(data[i][j])))
                if j == 2:
                    model.setItem(i, j, QtGui.QStandardItem(str(data[i][2].get("phone", ""))))
                    model.setItem(i, j + 1, QtGui.QStandardItem(str(data[i][2].get("email", ""))))

        self.ui.tableView.setModel(model)
        # self.ui.tableView.setColumnHidden(0, True)
        self.ui.tableView.setSortingEnabled(True)

        self.ui.tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

    def onPushButtonAddClicked(self):
        model = self.ui.tableView.model()
        ticket_no = random.randint(1005433102927, 2005433102927)
        print(ticket_no)
        name = f"{self.ui.lineEdit.text()} {self.ui.lineEdit_2.text()}"
        phone = {"phone": self.ui.lineEdit_3.text()}
        book_ref = random.randint(100000, 999999)
        passenger_id = f"{random.randint(1000, 9999)} {random.randint(100000, 999999)}"

        self.cur.execute(f"INSERT INTO bookings.bookings (book_ref, book_date, total_amount)"
                         f" VALUES ({book_ref}, NOW(), 12000)")

        self.cur.execute(f"INSERT INTO bookings.tickets (ticket_no, book_ref, passenger_name, contact_data, passenger_id)"
                         f"VALUES ({ticket_no}, {book_ref},'{name}', '{json.dumps(phone)}', '{passenger_id}')")
        model.insertRow(0)
        model.setItem(0, 0, QtGui.QStandardItem(str(ticket_no)))
        model.setItem(0, 1, QtGui.QStandardItem(name))
        model.setItem(0, 2, QtGui.QStandardItem(self.ui.lineEdit_3.text()))
        self.con.commit()

    def onPushButtonDelClicked(self):
        model = self.ui.tableView.model()
        index = model.index(self.ui.tableView.currentIndex().row(), 0)
        ticket_no = index.data(0)
        print(ticket_no)

        self.cur.execute(f"DELETE FROM bookings.boarding_passes WHERE ticket_no='{ticket_no}'")
        self.cur.execute(f"DELETE FROM bookings.ticket_flights WHERE ticket_no='{ticket_no}'")
        self.cur.execute(f"DELETE FROM bookings.tickets WHERE ticket_no='{ticket_no}'")

        model.removeRow(index.row())
        self.con.commit()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    frm = Form()
    frm.show()
    sys.exit(app.exec_())
