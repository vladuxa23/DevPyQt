"""
Создание простого окна в процедунром стиле
"""

from PySide6 import QtWidgets  # Импорт пакета, который содержит виджеты

app = QtWidgets.QApplication()  # Создание объекта приложения

myWindow = QtWidgets.QWidget()  # Создание объект окна
myWindow.show()  # Показ окна

app.exec()  # Запуск бесконечного цикла приложения (событий)

print("Приложение закрыто!")
