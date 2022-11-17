"""
Создание простого кастомного виджета
"""

from PySide6 import QtWidgets


class CustomPushButton(QtWidgets.QPushButton):  # Наследуемся от QPushButton
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

    # Добавление виджетов/донастройка (опционально)
    #     self.initUi()
    #
    # def initUi(self) -> None:
    #     """
    #     Донастройка Ui
    #
    #     :return: None
    #     """
    #
    #     self.setText("Моя кастомная кнопка")


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    my_button = CustomPushButton()
    my_button.show()

    app.exec()
