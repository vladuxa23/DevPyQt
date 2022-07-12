import time

import requests

from PySide2 import QtWidgets, QtCore, QtGui

from ui import res
from ui.zachet import Ui_Form
from ui.login import Ui_FormLogin
from ui.details import Ui_FormDetails
from ui.put import Ui_FormPut


class DjangoWebQt(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.current_item = None
        self.list_todo = None

        res.qInitResources()
        self.setWindowIcon(QtGui.QIcon(QtGui.QPixmap(":/ico/icon.ico")))

        self.url = 'http://127.0.0.1:8000'

        self.initUi()

    def initUi(self):
        self.setWindowTitle("Работа с БД через API")
        self.setMinimumSize(965, 600)
        self.child_window = Login()
        self.ui.pushButtonGet.clicked.connect(self.onPushButtonNoteGetAll)
        self.ui.pushButtonLogin.clicked.connect(self.onPushButtonLogin)
        self.ui.pushButtonLogOut.clicked.connect(self.onPushButtonLogOut)
        self.ui.comboBox.addItems(['Активно', 'Отложено', 'Выполнено'])
        self.ui.create_todo.clicked.connect(self.postToDo)
        self.child_window.user[str].connect(self.setUserName)
        self.ui.pushButtonLogOut.setEnabled(False)
        self.ui.pushButtonDetails.setEnabled(False)
        self.ui.pushButtonDelete.setEnabled(False)
        self.ui.pushButtonPut.setEnabled(False)
        self.ui.tableView.clicked.connect(self.clicked_table)
        self.ui.pushButtonDelete.clicked.connect(self.onPushButtonNoteDelete)
        self.detail_window = DetailsWindow()
        self.ui.pushButtonDetails.clicked.connect(self.onPushButtonNoteDetail)
        self.put_window = PutWindow()
        self.ui.pushButtonPut.clicked.connect(self.onPushButtonNotePut)
        self.loadGUI()

    def loadGUI(self):
        splash = QtWidgets.QSplashScreen(QtGui.QPixmap(":/logo/load_gui.jpg").scaled(300, 300))
        splash.show()
        time.sleep(1)
        splash.finish(self)
        self.show()

    def clicked_table(self, item: QtCore.QModelIndex):
        self.ui.pushButtonDelete.setEnabled(True)
        self.ui.pushButtonDetails.setEnabled(True)
        self.ui.pushButtonPut.setEnabled(True)
        self.current_item = item.row()

    def onPushButtonNoteDelete(self):
        try:
            id_todo = self.list_todo[self.current_item]["id"]
            resp = requests.delete(
                f"{self.url}/api/v1/todo/{id_todo}/",
                headers={'Authorization': "token {}".format(self.child_window.token)}
            )

            if resp.status_code == 200:
                self.onPushButtonNoteGetAll()

            elif resp.status_code == 401:
                QtWidgets.QMessageBox.warning(
                    self,
                    "Внимание", "Нужно авторизоваться в системе",
                    QtWidgets.QMessageBox.Yes
                )
            elif resp.status_code == 403:
                QtWidgets.QMessageBox.warning(
                    self,
                    "Внимание", "Заметку может удалить только автор",
                    QtWidgets.QMessageBox.Yes
                )
            else:
                QtWidgets.QMessageBox.warning(
                    self,
                    "Внимание", "Что-то пошло не так, повторите попытку",
                    QtWidgets.QMessageBox.Yes
                )
        except requests.exceptions.ConnectionError:
            QtWidgets.QMessageBox.warning(
                self,
                "Внимание", "Нет соединения с сервером!",
                QtWidgets.QMessageBox.Yes
            )
        self.onPushButtonNoteGetAll()

    def onPushButtonNoteDetail(self):
        id_todo = self.list_todo[self.current_item]["id"]

        resp = requests.get(
            f"{self.url}/api/v1/todo/{id_todo}/",
            headers={'Authorization': "token {}".format(self.child_window.token)}
        )
        todo = resp.json()
        self.detail_window.ui.lineEdit_author.setText(todo["author"])
        self.detail_window.ui.lineEdit_title.setText(todo["title"])
        self.detail_window.ui.textEdit_message.setText(todo["message"])
        self.detail_window.ui.lineEdit_deadline.setText(todo["deadline"])
        self.detail_window.ui.lineEdit_createdate.setText(todo["create_at"])
        self.detail_window.ui.lineEdit_updatedate.setText(todo["update_at"])
        self.detail_window.ui.lineEdit_status.setText(todo["status"])

        if todo["public"] == False:
            self.detail_window.ui.checkBox_public.setChecked(False)
        else:
            self.detail_window.ui.checkBox_public.setChecked(True)

        if todo["importance"] == False:
            self.detail_window.ui.checkBox_importance.setChecked(False)
        else:
            self.detail_window.ui.checkBox_importance.setChecked(True)

        self.detail_window.show()

    def onPushButtonNotePut(self):
        id_todo = self.list_todo[self.current_item]["id"]
        resp = requests.get(
            f"{self.url}/api/v1/todo/{id_todo}/",
            headers={'Authorization': "token {}".format(self.child_window.token)}
        )
        todo = resp.json()
        dict_status = {
            "Active": 0,
            "Delayed": 1,
            "Finish": 2
        }

        self.put_window.ui.lineEdit_author.setText(todo["author"])
        self.put_window.ui.lineEdit_title.setText(todo["title"])
        self.put_window.ui.textEdit_message.setText(todo["message"])
        # self.put_window.ui.dateTimeEdit.setDateTime(todo["deadline"])
        self.put_window.ui.lineEdit_createdate.setText(todo["create_at"])
        self.put_window.ui.lineEdit_updatedate.setText(todo["update_at"])
        self.put_window.ui.comboBox_status.setCurrentIndex(dict_status[todo["status"]])

        if todo["public"] == False:
            self.put_window.ui.checkBox_public.setChecked(False)
        else:
            self.put_window.ui.checkBox_public.setChecked(True)

        if todo["importance"] == False:
            self.put_window.ui.checkBox_importance.setChecked(False)
        else:
            self.put_window.ui.checkBox_importance.setChecked(True)

        self.put_window.current_id = id_todo
        self.put_window.put_token = self.child_window.token
        self.put_window.show()

    def onPushButtonLogOut(self):
        reply = QtWidgets.QMessageBox.question(self,
                                               'Выход', 'Вы действительно хотите выйти?',
                                               QtWidgets.QMessageBox.Yes,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            self.ui.label_user.clear()
            self.child_window.token = None
            self.ui.pushButtonLogOut.setEnabled(False)
            self.ui.pushButtonLogin.setEnabled(True)
            self.ui.tableView.setModel(None)
            self.ui.pushButtonDelete.setEnabled(False)
            self.ui.pushButtonDetails.setEnabled(False)
            self.ui.pushButtonPut.setEnabled(False)
            self.list_todo = None
            self.current_item = None

    def setUserName(self, user):
        self.put_window.put_token = self.child_window.token
        self.ui.label_user.setText(user)
        self.ui.pushButtonLogOut.setEnabled(True)
        self.ui.pushButtonLogin.setEnabled(False)

    def onPushButtonNoteGetAll(self):
        try:
            resp = requests.get(
                f"{self.url}/api/v1/todo/",
                headers={'Authorization': "token {}".format(self.child_window.token)}
            )

            if resp.status_code == 200:
                self.list_todo = resp.json()
                headers = ["Автор", "Название", "Текст задания", "Крайний срок"]
                stm = QtGui.QStandardItemModel()
                stm.setHorizontalHeaderLabels(headers)

                key_dict = ["author", "title", "message", "deadline"]

                for row in range(len(self.list_todo)):
                    for i in range(len(headers)):
                        stm.setItem(row, i, QtGui.QStandardItem(str(self.list_todo[row][key_dict[i]])))

                self.ui.tableView.setModel(stm)

            elif resp.status_code == 401:
                QtWidgets.QMessageBox.warning(
                    self,
                    "Внимание", "Нужно авторизоваться в системе, чтобы получить список всех дел",
                    QtWidgets.QMessageBox.Yes
                )
            else:
                QtWidgets.QMessageBox.warning(
                    self,
                    "Внимание", "Что-то пошло не так, повторите попытку",
                    QtWidgets.QMessageBox.Yes
                )
        except requests.exceptions.ConnectionError:
            QtWidgets.QMessageBox.warning(
                self,
                "Внимание", "Нет соединения с сервером!",
                QtWidgets.QMessageBox.Yes
            )

    def postToDo(self):

        title = self.ui.lineEdit.text()
        message = self.ui.textEdit.toPlainText()

        if self.ui.checkBox.isChecked():
            public = True
        else:
            public = False

        if self.ui.checkBox_2.isChecked():
            importance = True
        else:
            importance = False

        dict_status = {
            "Активно": "Active",
            "Отложено": "Delayed",
            "Выполнено": "Finish"
        }

        status = dict_status[self.ui.comboBox.currentText()]

        deadline = self.ui.dateTimeEdit.dateTime().toString("yyyy-MM-ddTHH:mm:ss")

        dict_todo = dict(
            title=title,
            message=message,
            public=public,
            importance=importance,
            status=status,
            deadline=deadline
        )
        try:
            request = requests.post(
                f"{self.url}/api/v1/todo/",
                json=dict_todo,
                headers={'Authorization': "token {}".format(self.child_window.token)}
            )
            print(request.status_code)
            if request.status_code == 200:
                QtWidgets.QMessageBox.warning(self, "Внимание", "Вы создали новое дело!", QtWidgets.QMessageBox.Yes)
                self.ui.lineEdit.clear()
                self.ui.textEdit.clear()

            if request.status_code == 401:
                QtWidgets.QMessageBox.warning(
                    self,
                    "Внимание", "Дело не создано, нужно авторизоваться в системе!",
                    QtWidgets.QMessageBox.Yes
                )
        except requests.exceptions.ConnectionError:
            QtWidgets.QMessageBox.warning(
                self,
                "Внимание", "Нет соединения с сервером!",
                QtWidgets.QMessageBox.Yes
            )

    def onPushButtonLogin(self):
        self.child_window.show()

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        reply = QtWidgets.QMessageBox.question(self,
                                               'Закрыть окно?', 'Вы хотите закрыть окно?',
                                               QtWidgets.QMessageBox.Yes,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


class Login(QtWidgets.QWidget):
    token = None
    user = QtCore.Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_FormLogin()
        self.ui.setupUi(self)

        res.qInitResources()
        self.setWindowIcon(QtGui.QIcon(QtGui.QPixmap(":/ico/icon.ico")))

        self.initUi()

    def initUi(self):
        self.setWindowTitle("Авторизация")
        self.ui.pushButtonLogin.clicked.connect(self.onPushButtonLogin)

    def onPushButtonLogin(self):
        try:
            username = self.ui.lineEdit.text()
            password = self.ui.lineEdit_2.text()
            dict_login = dict(username=username, password=password)
            request = requests.post(f"http://127.0.0.1:8000/api/v1/login/", json=dict_login)

            if request.status_code == 200:
                QtWidgets.QMessageBox.warning(self, "Поздравляем", "Вы вошли в систему!")
                self.token = request.json()['token']
                self.user.emit(dict_login["username"])
                self.ui.lineEdit.clear()
                self.ui.lineEdit_2.clear()
                self.close()
            else:
                QtWidgets.QMessageBox.warning(self, "Внимание", "Данные введены неправильно!")
                self.ui.lineEdit.clear()
                self.ui.lineEdit_2.clear()
        except requests.exceptions.ConnectionError:
            QtWidgets.QMessageBox.warning(
                self,
                "Внимание", "Нет соединения с сервером!",
                QtWidgets.QMessageBox.Yes
            )

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
        event.accept()


class DetailsWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_FormDetails()
        self.ui.setupUi(self)

        res.qInitResources()
        self.setWindowIcon(QtGui.QIcon(QtGui.QPixmap(":/ico/icon.ico")))

        self.initUi()

    def initUi(self):
        self.setWindowTitle("Подробности дела")
        self.setMinimumSize(600, 400)


class PutWindow(QtWidgets.QWidget):
    update = QtCore.Signal()
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_FormPut()
        self.ui.setupUi(self)

        self.url = 'http://127.0.0.1:8000'
        self.current_id = None
        self.put_token = None

        res.qInitResources()
        self.setWindowIcon(QtGui.QIcon(QtGui.QPixmap(":/ico/icon.ico")))

        self.initUi()

    def initUi(self):
        self.setWindowTitle("Обновить дело")
        self.setMinimumSize(600, 400)
        self.ui.comboBox_status.addItems(['Активно', 'Отложено', 'Выполнено'])
        self.ui.pushButtonPut.clicked.connect(self.onPushButtonPut)

    def onPushButtonPut(self):
        title = self.ui.lineEdit_title.text()
        message = self.ui.textEdit_message.toPlainText()

        if self.ui.checkBox_public.isChecked():
            public = True
        else:
            public = False

        if self.ui.checkBox_importance.isChecked():
            importance = True
        else:
            importance = False

        dict_status = {
            "Активно": "Active",
            "Отложено": "Delayed",
            "Выполнено": "Finish"
        }

        status = dict_status[self.ui.comboBox_status.currentText()]

        deadline = self.ui.dateTimeEdit.dateTime().toString("yyyy-MM-ddTHH:mm:ss")

        dict_todo = dict(
            title=title,
            message=message,
            public=public,
            importance=importance,
            status=status,
            deadline=deadline
        )

        try:
            request = requests.patch(
                f"{self.url}/api/v1/todo/{self.current_id}/",
                headers={'Authorization': "token {}".format(self.put_token)},
                data=dict_todo
            )

            if request.status_code == 200:
                reply = QtWidgets.QMessageBox.warning(self, "Внимание", "Вы обновили дело!", QtWidgets.QMessageBox.Yes)
                if reply == QtWidgets.QMessageBox.Yes:
                    self.close()

            if request.status_code == 401:
                QtWidgets.QMessageBox.warning(
                    self,
                    "Внимание",
                    "Дело не создано, нужно авторизоваться в системе!",
                    QtWidgets.QMessageBox.Yes
                )

            if request.status_code == 403:
                QtWidgets.QMessageBox.warning(
                    self,"Ошибка",
                    f"{request.json()}",
                    QtWidgets.QMessageBox.Yes
                )

        except requests.exceptions.ConnectionError:
            QtWidgets.QMessageBox.warning(
                self,
                "Внимание",
                "Нет соединения с сервером!",
                QtWidgets.QMessageBox.Yes
            )


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myapp = DjangoWebQt()
    myapp.show()

    app.exec_()
