from PySide2 import QtWidgets, QtCore
from SQLAlchemy_model import addUser, getAllUsers


class ModelPreview(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(ModelPreview, self).__init__(parent)

        self.initUi()
        self.loadUsers()

    def initUi(self):
        pb = QtWidgets.QPushButton("Add user")

        self.list_view_person = QtWidgets.QListView()

        self.plain_text_edit_log = QtWidgets.QPlainTextEdit()

        layout_main = QtWidgets.QVBoxLayout()
        layout_main.addWidget(pb)
        layout_main.addWidget(self.list_view_person)
        layout_main.addWidget(self.plain_text_edit_log)

        self.setLayout(layout_main)

        pb.clicked.connect(self.addNewUser)
        self.list_view_person.clicked.connect(self.getUserInfo)

    def loadUsers(self):
        result = []
        for user in getAllUsers():
            result.append(f"{user.get('name')} {user.get('surname')}")

        sim = QtCore.QStringListModel(result)
        self.list_view_person.setModel(sim)

    def addNewUser(self):
        user = addUser()

        model = self.list_view_person.model()

        new_row = model.rowCount()
        model.insertRow(new_row)
        model.setData(model.index(new_row, 0), f"{user.get('name')} {user.get('surname')}")

    def getUserInfo(self):
        insert_row = self.list_view_person.selectionModel().selectedRows()[0]
        model = self.list_view_person.model()
        name, surname = tuple(model.data(insert_row).split(" "))

        users = getAllUsers()
        for user in users:
            if user.get('name') == name and user.get('surname') == surname:
                self.plain_text_edit_log.\
                    appendPlainText(f"Пользователь: {user.get('name')} {user.get('surname')}\n"
                                    f"Логин:              {user.get('login')}\n"
                                    f"Пароль:            {user.get('password')}\n"
                                    f"E-Mail:               {user.get('email')}\n"
                                    f"Телефон:         {user.get('phone')}\n"
                                    f"Дата рег.:       {user.get('register_time').isoformat()}\n")


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    win = ModelPreview()
    win.show()

    app.exec_()
