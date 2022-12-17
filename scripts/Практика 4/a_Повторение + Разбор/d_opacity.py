from PySide6 import QtWidgets, QtCore, QtGui


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # Удаление titleBar
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # Установка прозрачного фона

        # добавление эффекта тени
        # self.shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        # self.shadow.setBlurRadius(10)
        # self.shadow.setXOffset(0)
        # self.shadow.setYOffset(0)
        # self.shadow.setColor(QtGui.QColor(0, 0, 0, 120))
        # self.setGraphicsEffect(self.shadow)
        label = QtWidgets.QLabel()
        label.setPixmap(QtGui.QPixmap('64.png'))
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(QtWidgets.QPushButton("123156"))

        self.setLayout(layout)


        # self.setStyleSheet('border: 5px solid black; background-image: "64.png"')


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
