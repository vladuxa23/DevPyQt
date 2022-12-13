"""
Файл для повторения темы сигналов

Напомнить про работу с сигналами и изменением Ui.

Предлагается создать приложение, которое принимает в lineEditInput строку от пользователя,
и при нажатии на pushButtonMirror отображает в lineEditMirror введённую строку в обратном
порядке (задом наперед).
"""

from PySide6 import QtWidgets, QtCore


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()
        self.initSignals()

    def initUi(self) -> None:
        """
        Инициализация Ui
        :return: None
        """

        self.lineEditInput = QtWidgets.QLineEdit()  # строка\поле для ввода
        self.lineEditInput.setPlaceholderText("Введите текст")

        self.lineEditMirror = QtWidgets.QLineEdit()
        self.lineEditMirror.setReadOnly(True)  # только чтение
        # self.lineEditMirror.setEnabled(False)  # серая строка недоступна пользователю, доступна для вывода
        self.lineEditMirror.setPlaceholderText("Текст задом на перед")

        self.pushButton = QtWidgets.QPushButton("Очистить")
        # self.pushButton.setText("Отобразить")  # позволяет установить текст в объект

        layoutLineEdit = QtWidgets.QHBoxLayout()
        layoutLineEdit.addWidget(self.lineEditInput)
        layoutLineEdit.addWidget(self.lineEditMirror)

        layoutMain = QtWidgets.QVBoxLayout()
        layoutMain.addLayout(layoutLineEdit)
        layoutMain.addWidget(self.pushButton)

        self.setLayout(layoutMain)

    def initSignals(self) -> None:
        """
        Инициализация сигнала

        :return: None
        """
        self.pushButton.clicked.connect(lambda: self.lineEditMirror.setText(""))

        # self.lineEditInput.textChanged.connect(
        #     lambda input_text: self.lineEditMirror.setText(input_text[::-1])  # действие при вводе в строку ввода
        # )

        self.lineEditInput.textChanged.connect(self.mirror_text)  # действие при вводе в строку ввода

    def mirror_text(self) -> None:
        """
        Отображение текста задом на перед

        return: None
        """
        input_text = self.lineEditInput.text()  # получение данных из строки ввода пользователем

        if not input_text:
            QtWidgets.QMessageBox.warning(self, "Ошибка",  "Не введен текст!")  # вывод ошибки
            self.lineEditMirror.setText("")
            return

        self.lineEditMirror.setText(input_text[::-1])  # вывод в строку развернутого текста


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
