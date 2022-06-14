import sys
from PySide2 import QtCore, QtWidgets  # Импорт класса, который содержит элементы окна


class MyFirstWindow(QtWidgets.QWidget):  # Наследуемся от QMainWindow

    def __init__(self, parent=None):                 # Создаем конструктор класса
        super().__init__(parent)  # Передаем конструктору ссылку на родительский компонент

        v_layout = QtWidgets.QVBoxLayout()

        date_edit = QtWidgets.QDateEdit()
        date_time_edit = QtWidgets.QDateTimeEdit()

        date_edit.setDate(QtCore.QDate.currentDate())
        print(QtCore.QDate.currentDate())
        date_time_edit.setDateTime(QtCore.QDateTime.currentDateTime())

        v_layout.addWidget(date_edit)
        v_layout.addWidget(date_time_edit)

        self.setLayout(v_layout)


if __name__ == "__main__":
    app = QtWidgets.QApplication()  # Создаем  объект приложения
    # app = QtWidgets.QApplication(sys.argv)  # Если PyQt

    myWindow = MyFirstWindow()  # Создаём объект окна
    myWindow.show()  # Показываем окно

    sys.exit(app.exec_())  # Если exit, то код дальше не исполняется

