"""
Работа с классом QSettings (сохранение простых типов)
"""

from PySide6 import QtWidgets, QtCore, QtGui


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.settings = QtCore.QSettings("MyDataCard")

        self.initUI()
        self.loadData()
        self.initSignals()

    def initUI(self) -> None:
        """
        Доинициализация Ui

        :return: None
        """

        # labels
        self.labelName = QtWidgets.QLabel("Имя")
        self.labelName.setMinimumWidth(50)

        self.labelSurname = QtWidgets.QLabel("Фамилия")
        self.labelSurname.setMinimumWidth(50)

        # lineedits
        self.lineEditName = QtWidgets.QLineEdit()
        self.lineEditSurname = QtWidgets.QLineEdit()

        # checkbox
        self.checkBox = QtWidgets.QCheckBox("Сохранять настройки")

        # pushbuttons
        self.pushButtonShowPath = QtWidgets.QPushButton("Показать путь к настройкам")
        self.pushButtonClearSettings = QtWidgets.QPushButton("Очистить настройки")

        # layouts
        layoutHName = QtWidgets.QHBoxLayout()
        layoutHName.addWidget(self.labelName)
        layoutHName.addWidget(self.lineEditName)
        layoutHSurname = QtWidgets.QHBoxLayout()
        layoutHSurname.addWidget(self.labelSurname)
        layoutHSurname.addWidget(self.lineEditSurname)

        layoutVMain = QtWidgets.QVBoxLayout()
        layoutVMain.addLayout(layoutHName)
        layoutVMain.addLayout(layoutHSurname)
        layoutVMain.addWidget(self.pushButtonShowPath)
        layoutVMain.addWidget(self.pushButtonClearSettings)
        layoutVMain.addWidget(self.checkBox)

        self.setLayout(layoutVMain)

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """

        self.pushButtonShowPath.clicked.connect(self.showSettingsPath)
        self.pushButtonClearSettings.clicked.connect(self.cleanSettingsPath)

    def loadData(self) -> None:
        """
        Загрузка данных в Ui

        :return: None
        """

        self.lineEditName.setText(self.settings.value("Name", ""))
        self.lineEditSurname.setText(self.settings.value("Surname", ""))

        data = self.settings.value("CheckState")
        self.checkBox.setCheckState(self.settings.value("CheckState"))
        # if self.settings.value("CheckState") == "true":
        #     self.checkBox.setCheckState(QtCore.Qt.Checked)
        # else:
        #     self.checkBox.setCheckState(QtCore.Qt.Unchecked)

    def showSettingsPath(self) -> None:
        """
        Показ пути хранения настроек

        :return: None
        """

        QtWidgets.QMessageBox.about(self, "Путь", self.settings.fileName())

    def cleanSettingsPath(self) -> None:
        """
        Очистка данных QSettings

        :return: None
        """

        self.settings.clear()
        print(self.settings.allKeys())

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        """
        Событие закрытия окна

        :param event: QtGui.QCloseEvent
        :return: None
        """

        if self.checkBox.isChecked():
            self.settings.setValue("Name", self.lineEditName.text())
            self.settings.setValue("Surname", self.lineEditSurname.text())
            self.settings.setValue("CheckState", self.checkBox.checkState())
        else:
            self.settings.setValue("CheckState", self.checkBox.checkState())


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    windows = Window()
    windows.show()

    app.exec()
