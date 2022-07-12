from PySide2 import QtCore, QtWidgets, QtGui
import requests
from requests.auth import HTTPBasicAuth

from ui.form.Notes_client_design_form import Ui_MainWindow as Form
from ui.ico import my_res


class Note_Form(QtWidgets.QMainWindow):
    def __init__(self, parent=None) -> None:
        super(Note_Form, self).__init__(parent)
        self.ui = Form()
        self.ui.setupUi(self)

        # атрибут для сохранения логина и пароля пользователя
        self.login = None
        self.password = None

        self.initUi()
        self.initWindows()

    def initUi(self) -> None:
        self.setFixedSize(800, 800)
        # добавление иконки
        my_res.qInitResources()
        self.setWindowIcon(QtGui.QIcon(QtGui.QPixmap(":/ico/ico/atom-browser.ico")))
        # изменение стиля
        with open("ui/themes/darkstyle.qss") as f:
            self.setStyleSheet(f.read())

        self.ui.comboBox_importance.addItems(["False", "True"])
        self.ui.comboBox_importance_filter.addItems(["False", "True"])
        self.ui.comboBox_importance_filter.setEnabled(False)
        self.ui.comboBox_condition.addItems(["Активно", "Отложено", "Выполнено"])
        self.ui.comboBox_note_pk.addItems(self.get_id_list())

        # сигналы
        self.ui.pushButton_get_all_notes.clicked.connect(self.loadTable)
        self.ui.pushButton.clicked.connect(self.postNote)
        self.ui.pushButton_login.clicked.connect(self.open_child_window)
        self.ui.pushButton_note_pk.clicked.connect(self.loadTable)

        self.ui.checkBox_filter.stateChanged.connect(self.filter_activate)

        self.pbdelete = PushButtonDelegate()
        self.pbdelete.clicked.connect(self.deleteNote)

    def initWindows(self) -> None:
        """
        Инициализация дочернего окна
        """
        self.child_window = DroppedWindow()
        self.child_window.send_data.connect(self.setLoginPass)

    def open_child_window(self) -> None:
        """
        вызов дочернего окна
        """
        self.child_window.show()

    def get_id_list(self) -> list:
        """
        Формирует актуальный список ID всех записей из базы данных для динамического заполнения/обновления comboBox_note_pk
        :return: список имеющихся в базе id
        """
        response = requests.get("http://127.0.0.1:8000/notes/")
        output = response.json()

        return [str(output[i]["id"]) for i in range(len(output))]

    # слоты

    def filter_activate(self) -> None:
        """При наличии галочки в checkBox_filter активирует фильтр и
        блокирует кнопку получения одной записи и наоборот"""

        if self.ui.checkBox_filter.isChecked() == True:
            self.ui.comboBox_importance_filter.setEnabled(True)
            self.ui.pushButton_note_pk.setEnabled(False)
        else:
            self.ui.comboBox_importance_filter.setEnabled(False)
            self.ui.pushButton_note_pk.setEnabled(True)

    def postNote(self) -> None:
        """
        Метод POST
        :return: None
        """
        if self.login and self.password:
            auth = HTTPBasicAuth(self.login, self.password)
        else:
            self.open_child_window()

        condition_index = {
            "Активно": 1,
            "Отложено": 2,
            "Выполнено": 3,
        }

        data = {
            "title": self.ui.lineEdit_title.text(),
            "message": self.ui.lineEdit_massage.text(),
            "importance": self.ui.comboBox_importance.currentText(),
            "condition": condition_index[self.ui.comboBox_condition.currentText()],
        }

        response = requests.post("http://127.0.0.1:8000/notes/", auth=auth, json=data)
        if response.status_code == 403:
            self.ui.labe_window_output.setStyleSheet("color: red")
            self.ui.labe_window_output.setText("Неверные логин или пароль !!!")
            self.open_child_window()

        if response.status_code == 201:
            self.ui.comboBox_note_pk.clear()
            self.ui.comboBox_note_pk.addItems(self.get_id_list())
            self.ui.labe_window_output.setStyleSheet("color: darkgreen")
            self.ui.labe_window_output.setText("Запись опубликована")
            self.loadTable(pk=str(self.get_id_list()[-1]))
            print(response.status_code)

            self.ui.lineEdit_title.clear()
            self.ui.lineEdit_massage.clear()

        if response.status_code == 400:
            self.ui.labe_window_output.setStyleSheet("color: red")
            self.ui.labe_window_output.setText("Проверьте, заполнены ли все поля")

    def setLoginPass(self, emit: tuple) -> None:
        """
        Записывает лоиг и пароль, пришедшие из дочернего окна
        :param emit: сигнал из дочернего окна
        :return: None
        """
        self.login = emit[0]
        self.password = emit[1]
        self.child_window.close()

        print(self.login, self.password)

    def loadTable(self, pk: str = None) -> None:
        """
        Создает и заполняет таблицу с результатами, вызывая метод GET
        :param pk:
        :return: None
        """
        headers = ["id", "title", "message", "importance", "condition", "author", "delete"]

        stm = QtGui.QStandardItemModel()
        stm.setHorizontalHeaderLabels(headers)

        if self.sender() == self.ui.pushButton_get_all_notes or self.sender() == self.deleteNote:
            if self.ui.checkBox_filter.isChecked():
                response = requests.get(
                    f"http://127.0.0.1:8000/notes/filter/?importance={self.ui.comboBox_importance_filter.currentText()}")
                self.ui.labe_window_output.setStyleSheet("color: darkgreen")
                self.ui.labe_window_output.setText("Результат:")
            else:
                response = requests.get("http://127.0.0.1:8000/notes/")
                self.ui.labe_window_output.setStyleSheet("color: darkgreen")
                self.ui.labe_window_output.setText("Результат:")

        else:
            if self.login and self.password:
                auth = HTTPBasicAuth(self.login, self.password)
            else:
                self.open_child_window()
            if not pk:
                pk = (self.ui.comboBox_note_pk.currentText())
            response = requests.get(f"http://127.0.0.1:8000/notes/{pk}", auth=auth)
            self.ui.labe_window_output.setStyleSheet("color: darkgreen")
            self.ui.labe_window_output.setText("Результат:")

        if response.status_code == 403:
            self.ui.labe_window_output.setStyleSheet("color: red")
            self.ui.labe_window_output.setText("Неверные логин или пароль !!!")
            self.open_child_window()

        output = response.json()
        print(response.json(), response.status_code)

        data = [x for x in output]

        for row in range(len(data)):
            stm.setItem(row, 0, QtGui.QStandardItem(str(data[row]["id"])))
            stm.setItem(row, 1, QtGui.QStandardItem(data[row]["title"]))
            stm.setItem(row, 2, QtGui.QStandardItem(data[row]["message"]))
            stm.setItem(row, 3, QtGui.QStandardItem(str(data[row]["importance"])))
            stm.setItem(row, 4, QtGui.QStandardItem(str(data[row]["condition"])))
            stm.setItem(row, 5, QtGui.QStandardItem(data[row]["author"]))
            stm.setItem(row, 6, QtGui.QStandardItem(""))

        self.ui.tableView_output.setModel(stm)
        self.ui.tableView_output.setItemDelegateForColumn(6, self.pbdelete)


    def deleteNote(self, push_row) -> None:
        """
        Метод DELETE
        :param push_row: сигнал из кнопки делегата PushButtonDelegate
        :return: None
        """
        # row = push_row.row()
        if self.login and self.password:
            auth = HTTPBasicAuth(self.login, self.password)
        else:
            self.open_child_window()

        model: QtGui.QStandardItemModel = self.ui.tableView_output.model()
        row_data = model.item(push_row.row(), 0)
        id = row_data.data(0)
        author = row_data.data(5)


        # response = requests.get("http://127.0.0.1:8000/notes/")
        # pk_to_del = response.json()[row]["id"]
        if author != self.login:
            self.ui.labe_window_output.setStyleSheet("color: red")
            self.ui.labe_window_output.setText("Вы не можете удалять чужие записи !!!")

        response = requests.delete(f"http://127.0.0.1:8000/notes/{id}", auth=auth)

        if response.status_code == 200:
            self.ui.comboBox_note_pk.clear()
            self.ui.comboBox_note_pk.addItems(self.get_id_list())
            self.ui.labe_window_output.setStyleSheet("color: lightgreen")
            self.ui.labe_window_output.setText(f"Запись с 'id' {id} удалена")
            # self.loadTable()

        print(response.status_code)


class DroppedWindow(QtWidgets.QWidget):
    """Дочернее окно для авторизации"""
    send_data = QtCore.Signal(tuple)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()

    def initUi(self) -> None:
        self.setFixedSize(600, 400)
        self.setWindowTitle("Окно авторизации")

        with open("ui/themes/darkstyle.qss") as f:
            self.setStyleSheet(f.read())

        self.lineEditLogin = QtWidgets.QLineEdit()
        self.lineEditLogin.setObjectName("Логин")

        self.lineEditPass = QtWidgets.QLineEdit()
        self.lineEditPass.setObjectName("Пароль")

        pb = QtWidgets.QPushButton("LOG IN")
        pb.clicked.connect(self.setSignal)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.lineEditLogin)
        layout.addWidget(self.lineEditPass)
        layout.addWidget(pb)

        self.setLayout(layout)

    def setSignal(self) -> None:
        """инициализация сигнала в основное окно"""
        self.send_data.emit((self.lineEditLogin.text(), self.lineEditPass.text()))

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        """при нажатии на кнопку Enter (вместо pb_login) вызывается слот setSignal"""
        if event.key() == 16777220:
            # if event.text() == "/n":
            self.setSignal()


class PushButtonDelegate(QtWidgets.QStyledItemDelegate):
    """
    Кнопка-делегат удаления записи внутри виджета TableView
    """
    clicked = QtCore.Signal(QtCore.QModelIndex)

    def createEditor(self, parent, option, index):
        button = QtWidgets.QPushButton(parent)

        button.clicked.connect(lambda *args, ix=index: self.clicked.emit(ix))

        return button

    def setEditorData(self, editor, index):
        editor.setText("Удалить")


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myapp = Note_Form()
    myapp.show()

    app.exec_()
