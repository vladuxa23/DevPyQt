import sys

from PySide2 import QtWidgets  # Импорт класса, который содержит элементы окна


if __name__ == '__main__':

    app = QtWidgets.QApplication()  # Создаем  объект приложения
    # app = QtWidgets.QApplication(sys.argv)  # Если PyQt

    myWindow = QtWidgets.QWidget()  # Создаём объект окна
    myWindow.setWindowTitle("Моя первая программа на PySide")
    myWindow.resize(300, 150)

    label = QtWidgets.QLabel("<center><strong>!!!ПРИВЕТ!!!</strong></center>")
    #
    btn_close = QtWidgets.QPushButton()
    btn_close.setText("Текст кнопки")
    btn_close.clicked.connect(app.quit())
    btn_close.setObjectName("MyButton")
    #
    v_layout = QtWidgets.QVBoxLayout()
    v_layout.addWidget(label)
    v_layout.addWidget(btn_close)
    #
    myWindow.setLayout(v_layout)
    # print(myWindow.layout())

    myWindow.show()  # Показываем окно

    sys.exit(app.exec_())  # Если exit, то код дальше не исполняется
