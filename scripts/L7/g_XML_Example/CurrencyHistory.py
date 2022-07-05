import sys
sys.path.append("../examples/My_Example")
import xml.etree.ElementTree as ET
import requests
from PySide2 import QtWidgets, QtCore, QtGui

# https://cbr.ru/development/SXML/

class CurrencyHistory(QtWidgets.QWidget):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.initUI()
        self.loadData("http://www.cbr.ru/scripts/XML_daily.asp?")

        self.dateEdit.dateChanged.connect(self.refreshData)

        self.comboBoxCurrency.currentTextChanged.connect(lambda: self.labelResult.setText(
            self.currencyDict[self.comboBoxCurrency.currentText()]))

    def initUI(self):
        self.setFixedSize(250, 400)
        self.setWindowTitle("Курс валют")

        labelChooseCurrency = QtWidgets.QLabel("Выберите валюту")
        self.comboBoxCurrency = QtWidgets.QComboBox()
        labelChooseDate = QtWidgets.QLabel("Выберите дату")
        self.dateEdit = QtWidgets.QDateEdit()
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDate(QtCore.QDate.currentDate())

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(25)

        self.labelResult = QtWidgets.QLabel()
        self.labelResult.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.labelResult.setAlignment(QtCore.Qt.AlignCenter)
        self.labelResult.setFont(font)
        self.labelResult.setStyleSheet("color: green")

        layoutV = QtWidgets.QVBoxLayout()
        layoutV.addWidget(labelChooseCurrency)
        layoutV.addWidget(self.comboBoxCurrency)
        layoutV.addWidget(labelChooseDate)
        layoutV.addWidget(self.dateEdit)
        layoutV.addWidget(self.labelResult)

        self.setLayout(layoutV)

    def loadData(self, date):
        getXml = requests.get(date)
        # print(getXml.status_code)
        if getXml.status_code == 200:
            try:
                tree = ET.fromstring(getXml.content)
                currencyName = tree.findall("Valute/Name")
                currencyValue = tree.findall("Valute/Value")
                currencyName = [x.text for x in currencyName]
                currencyValue = [x.text for x in currencyValue]

                self.currencyDict = dict(zip(currencyName, currencyValue))

                self.comboBoxCurrency.blockSignals(True)
                self.comboBoxCurrency.clear()
                self.comboBoxCurrency.addItems(list(self.currencyDict.keys()))
                self.labelResult.setText(self.currencyDict[self.comboBoxCurrency.currentText()])
                self.comboBoxCurrency.blockSignals(False)
            except Exception as err:
                print(err)

    def refreshData(self):
        day = str(self.dateEdit.date().day())
        if len(day) == 1:
            day = "0" + day

        month = str(self.dateEdit.date().month())
        if len(month) == 1:
            month = "0" + month

        year = str(self.dateEdit.date().year())

        query = f'http://www.cbr.ru/scripts/XML_daily.asp?date_req={day}/{month}/{year}'
        # print(query)
        self.loadData(query)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myapp = CurrencyHistory()
    myapp.show()

    app.exec_()
