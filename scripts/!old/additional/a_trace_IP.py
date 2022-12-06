import subprocess
import sys
from PySide2 import QtWidgets  # Импорт класса, который содержит элементы окна


class MyFirstWindow(QtWidgets.QWidget):  # Наследуемся от QMainWindow

    def __init__(self, parent=None):  # Создаем конструктор класса
        super().__init__(parent)  # Передаем конструктору ссылку на родительский компонент

        self.initUi()

    def initUi(self):

        btn = QtWidgets.QPushButton("Кнопка")
        btn.clicked.connect(self.onPBClicked)

        btn.setDefault(True)

        self.plTE = QtWidgets.QPlainTextEdit()

        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addWidget(btn)
        main_layout.addWidget(self.plTE)

        self.setLayout(main_layout)

    def onPBClicked(self):
        cmd_command = "tracert 95.161.217.249"
        # cmd_command = "ping 192.168.58.58 -n 1"
        pr = subprocess.Popen(cmd_command, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        stdout, stderr = pr.communicate()

        self.plTE.setPlainText(stdout.decode("cp866", "ignore"))


if __name__ == "__main__":
    app = QtWidgets.QApplication()  # Создаем  объект приложения
    # app = QtWidgets.QApplication(sys.argv)  # Если PyQt

    myWindow = MyFirstWindow()  # Создаём объект окна
    myWindow.show()  # Показываем окно

    sys.exit(app.exec_())  # Если exit, то код дальше не исполняется

