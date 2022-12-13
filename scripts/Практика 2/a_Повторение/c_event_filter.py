"""
Файл для повторения темы фильтр событий

Напомнить про работу с фильтром событий.

Предлагается создать кликабельный QLabel с текстом "Красивая кнопка",
используя html - теги, покрасить разные части текста на нём в разные цвета
(красивая - красным, кнопка - синим)
"""

from PySide6 import QtWidgets, QtCore


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUi()

    def initUi(self):
        self.lable = QtWidgets.QLabel("Красивая кнопка")
        self.lable.setStyleSheet("border: 3px solid red")
        self.lable.setText("<font color = 'red'>Красивая</font> "
                           "<font color = 'blue'> кнопка</font>")

        self.lable2 = QtWidgets.QLabel("Красивая кнопка 2")
        self.lable2.setStyleSheet("border: 3px solid blue")

        self.lable.installEventFilter(self)
        self.lable2.installEventFilter(self)

        layout = QtWidgets.QHBoxLayout()  # создаем слой
        layout.addWidget(self.lable)  # добавляем на слой элементы(виджеты)
        layout.addWidget(self.lable2)

        self.setLayout(layout)  # устанавливаем слой

    def eventFilter(self, watched: QtCore.QObject, event: QtCore.QEvent) -> bool:
        if watched == self.lable and event.type() == QtCore.QEvent.Type.MouseButtonPress:
            print(event)
            print("Тут можно выполнить любой бэк при нажатии кнопок мыши. Кнопка 1")

        if watched == self.lable2 and event.type() == QtCore.QEvent.Type.Wheel:
            print(event)
            print("Тут можно выполнить любой бэк при прокутке колесиком мыши. Кнопка 2")
            print(self.lable2.setText(f"Красивая кнопка: {event.angleDelta()}"))

        return super(Window, self).eventFilter(watched, event)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
