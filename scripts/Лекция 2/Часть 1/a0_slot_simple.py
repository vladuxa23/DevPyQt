from PySide6 import QtWidgets, QtCore


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()
        self.initSignals()

        QtWidgets.QAbstractButton
        print(self.pushButton.clicked)

    def initUi(self) -> None:
        """
        Доинициализация Ui

        :return: None
        """

        self.pushButton = QtWidgets.QPushButton("Выполнить что-то")

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.pushButton)

        self.setLayout(layout)

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """

        # Указываем, что при нажатии на кнопку,
        # будут выполнены дествия описанные
        # в методе класса onPushButtonClicked
        self.pushButton.clicked.connect(self.onPushButtonClicked)

    @QtCore.Slot()
    def onPushButtonClicked(self):
        print("pushButton was clicked")


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
