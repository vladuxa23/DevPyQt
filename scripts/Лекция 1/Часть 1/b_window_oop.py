"""
Создание простого окна в ООП стиле
"""

from PySide6 import QtWidgets


class MyFirstWindow(QtWidgets.QWidget):  # Наследование от QWidget
    def __init__(self, parent=None) -> None:  # Создание конструктор класса
        super().__init__(parent)  # Передача конструктору ссылки на родительский виджет

        # Добавление виджетов/донастройка (опционально)
        self.initUi()

    def initUi(self) -> None:
        """
        Доинициализация Ui

        :return: None
        """

        main_layout = QtWidgets.QVBoxLayout()

        btn = QtWidgets.QPushButton("Кнопка")
        lbl = QtWidgets.QLabel("Текст")

        main_layout.addWidget(btn)
        main_layout.addWidget(lbl)

        self.setLayout(main_layout)


if __name__ == "__main__":
    app = QtWidgets.QApplication()  # Создание объекта приложения

    window = MyFirstWindow()  # Создание объекта окна
    window.show()  # Показ окна

    app.exec()  # Забуск бесконечного цикла приложения (событий)
