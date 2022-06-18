import sys
from PySide2 import QtCore, QtWidgets, QtGui


class DifferentPBColor(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(DifferentPBColor, self).__init__(parent)

        # Настройка label
        label = QtWidgets.QLabel("<font color='#5BC0EB'>Button is </font><font color='#9BC53D'>beautiful</font>")
        label.setAlignment(QtCore.Qt.AlignCenter)
        # Устанавливаем имя объекта, для удобства отслеживания
        label.setObjectName("pb_label")
        # Устанавливаем кастомный слушатель
        label.installEventFilter(self)

        # Настройка компоновки кнопки
        pb_layout = QtWidgets.QVBoxLayout()
        pb_layout.addWidget(label)
        pb_layout.setContentsMargins(0, 0, 0, 0)

        # Настройка кнопки
        pb = QtWidgets.QPushButton()
        pb.setLayout(pb_layout)
        # pb.setStyleSheet("background-color: #404E4D;")

        # Настройка компоновки основного виджета
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(pb)

        # Установка компоновки на виджет
        self.setLayout(layout)

    # Переопределяем слушатель
    def eventFilter(self, watched: QtCore.QObject, event: QtCore.QEvent) -> bool:
        # Отбираем нужный виджет по имени объекта и событие нажатия на него
        if watched.objectName() == 'pb_label' and event.type() == QtCore.QEvent.MouseButtonPress:
            # Запускаем нужный слот
            self.some_slot()

        # Возвращаем event дальше по стеку для основного потока приложения
        return super(DifferentPBColor, self).eventFilter(watched, event)

    # слот с бэком, то что надо сделать
    def some_slot(self):
        print("hello")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    win = DifferentPBColor()
    win.show()

    app.exec_()