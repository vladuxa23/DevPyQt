"""
Работа с виджетами даты и времени
"""

from PySide6 import QtCore, QtWidgets


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        print(QtCore.QDate.currentDate())  # Текущая дата в формате Qt

        date_edit = QtWidgets.QDateEdit()  # Создаем виджет для редактирования даты
        date_edit.setDate(QtCore.QDate.currentDate())  # Установка текущей даты в QDateEdit

        date_time_edit = QtWidgets.QDateTimeEdit()  # Создаем виджет для редактирования даты и времени
        date_time_edit.setDateTime(
            QtCore.QDateTime.currentDateTime()
        )  # Установка текущей даты и времени в QDateTimeEdit
        date_time_edit.setCalendarPopup(True)  # Включение выпадающего календаря в QDateTimeEdit

        v_layout = QtWidgets.QVBoxLayout()  # Создаем вертикальный layout
        v_layout.addWidget(date_edit)  # Добавление QDateEdit в layout
        v_layout.addWidget(date_time_edit)  # Добавление QDateTimeEdit в layout

        # Устанавливаем layout для окна
        self.setLayout(v_layout)  # Установка layout для окна


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
