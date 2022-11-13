import sys
from PySide2 import QtWidgets  # Импорт класса, который содержит элементы окна


class MyFirstWindow(QtWidgets.QWidget):  # Наследуемся от QWidget

    def __init__(self, parent=None):  # Создаем конструктор класса
        super().__init__(parent)  # Передаем конструктору ссылку на родительский компонент

        self.initUi()

    def initUi(self):
        main_layout = QtWidgets.QVBoxLayout()

        btn = QtWidgets.QPushButton("Кнопка")
        lbl = QtWidgets.QLabel("Текст")

        main_layout.addWidget(btn)
        main_layout.addWidget(lbl)

        self.setLayout(main_layout)


if __name__ == "__main__":
    app = QtWidgets.QApplication()  # Создаем  объект приложения

    myWindow = MyFirstWindow()  # Создаём объект окна
    myWindow.show()  # Показываем окно

    sys.exit(app.exec_())  # Запускает бесконечный цикл выполнения приложения
