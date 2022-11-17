"""
Создание простого окна в процедунром стиле
"""

from PySide6 import QtWidgets  # Импорт пакета, который содержит виджеты

app = QtWidgets.QApplication()  # Создание  объект приложения
myWindow = QtWidgets.QWidget()  # Создание объект окна

# Добавление виджетов/донастройка (опционально)
# myWindow.setWindowTitle("Моя первая программа на PySide")
# myWindow.resize(300, 150)
#
# label = QtWidgets.QLabel("<center><strong>!!!ПРИВЕТ!!!</strong></center>")
# #
# btn_close = QtWidgets.QPushButton()
# btn_close.setText("Текст кнопки")
# btn_close.clicked.connect(app.quit)
# #
# v_layout = QtWidgets.QVBoxLayout()
# v_layout.addWidget(label)
# v_layout.addWidget(btn_close)
# #
# myWindow.setLayout(v_layout)
# # print(myWindow.layout())

myWindow.show()  # Показ окна
app.exec_()  # Забуск бесконечного цикла приложения (событий)
