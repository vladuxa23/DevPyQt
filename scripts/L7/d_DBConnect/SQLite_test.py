import sys
import time

import ui.crud_design
from PySide2 import QtWidgets, QtCore, QtSql, QtGui


class NoEditDelegate(QtWidgets.QStyledItemDelegate):
    def __init__(self):
        super(NoEditDelegate, self).__init__()

    def createEditor(self, parent: QtWidgets.QWidget, option: QtWidgets.QStyleOptionViewItem, index: QtCore.QModelIndex) -> QtWidgets.QWidget:
        return 0


class EditableSQLModel(QtSql.QSqlTableModel):

    def __init__(self, parent=None):
        super(EditableSQLModel, self).__init__(parent)

    def data(self, item, role):
        if role == QtCore.Qt.DisplayRole:
            if item.column() == 1:
                name = QtSql.QSqlTableModel.data(self, item, QtCore.Qt.DisplayRole)
                # print(name)
                if name == "Вася":
                    name = "Василий"
                return name

        if role == QtCore.Qt.BackgroundRole:
            if item.row() % 2:
                return QtGui.QColor(QtCore.Qt.lightGray)

        return QtSql.QSqlTableModel.data(self, item, role)

    def flags(self, index):
        if index.column() == 2:
            return QtCore.Qt.ItemIsEnabled
        else:
            return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable


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
        self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('fieldlist.db')
        self.model = EditableSQLModel()
        # self.model = QtSql.QSqlTableModel()
        self.model.setTable('field')

        self.model.select()
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "id")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Name")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Surname")
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, "Birthday")
        self.model.setHeaderData(4, QtCore.Qt.Horizontal, "Phone")

        self.ui.tableView.setModel(self.model)
        self.ui.tableView.setColumnHidden(0, True)
        self.ui.tableView.horizontalHeader().setSectionsMovable(True)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui.tableView.setItemDelegateForColumn(4, NoEditDelegate())
        self.ui.lcdNumber.display(self.model.rowCount())

    def onPushButtonAddClicked(self):
        index = self.model.rowCount()
        self.model.insertRows(index, 1)
        self.model.setData(self.model.index(index, 1), self.ui.lineEdit.text())
        self.model.setData(self.model.index(index, 2), self.ui.lineEdit_2.text())
        self.model.setData(self.model.index(index, 4), self.ui.lineEdit_3.text())
        self.model.setData(self.model.index(index, 3), self.ui.dateEdit.text())
        self.model.submitAll()

        self.ui.lcdNumber.display(self.model.rowCount())

    def onPushButtonDelClicked(self):
        if self.ui.tableView.currentIndex().row() > -1:
            self.model.removeRow(self.ui.tableView.currentIndex().row())
            self.model.select()
            self.ui.lcdNumber.display(self.model.rowCount())
        else:
            QtWidgets.QMessageBox.question(self, 'Message', "Please select a row would you like to delete", QtWidgets.QMessageBox.Ok)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    frm = Form()
    frm.show()
    sys.exit(app.exec_())
