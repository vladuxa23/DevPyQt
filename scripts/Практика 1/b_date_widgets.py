"""
Работа с виджетами даты и времени
"""

from PySide6 import QtCore, QtWidgets


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()

    def initUi(self) -> None:
        """
        Доинициализация Ui

        :return: None
        """

        print(QtCore.QDate.currentDate())  # Текущее время в формате Qt

        # Создание виджета редактирования даты
        date_edit = QtWidgets.QDateEdit()
        date_edit.setDate(QtCore.QDate.currentDate())

        # Создание виджета редактирования даты и времени
        date_time_edit = QtWidgets.QDateTimeEdit()
        date_time_edit.setDateTime(QtCore.QDateTime.currentDateTime())
        date_time_edit.setCalendarPopup(True)

        v_layout = QtWidgets.QVBoxLayout()
        v_layout.addWidget(date_edit)
        v_layout.addWidget(date_time_edit)

        self.setLayout(v_layout)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
