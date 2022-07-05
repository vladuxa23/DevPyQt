import sys
from PySide2 import QtWidgets, QtCore, QtGui  # Импорт класса, который содержит элементы окна
from mirror_window_design import Ui_Form


class RepeatLesson(QtWidgets.QWidget):  # Наследуемся от QWidget

    def __init__(self, parent=None):  # Создаем конструктор класса
        super().__init__(parent)  # Передаем конструктору ссылку на родительский компонент

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.initUi()

    def initUi(self):
        self.setWindowTitle("Моя программа")
        self.ui.pushButton.setText("Очистить")

        self.ui.pushButton.clicked.connect(self.clear_lineedit)
        self.ui.lineEditSource.textChanged.connect(self.mirror_text)

    def mirror_text(self):
        print(self.sender().objectName())
        src_text = self.ui.lineEditSource.text()
        self.ui.lineEditResult.setText(src_text[::-1])

    def clear_lineedit(self):
        self.ui.lineEditSource.setText("")
        self.ui.lineEditResult.setText("")

    def event(self, event:QtCore.QEvent) -> bool:
        print(event.type())
        if event.type() == QtCore.QEvent.Move:
            print(self.pos())

        return QtWidgets.QWidget.event(self, event)

    def closeEvent(self, event:QtGui.QCloseEvent) -> None:
        print("Пока")

        return QtWidgets.QWidget.closeEvent(self, event)


if __name__ == "__main__":
    app = QtWidgets.QApplication()  # Создаем  объект приложения
    # app = QtWidgets.QApplication(sys.argv)  # Если PyQt

    myWindow = RepeatLesson()  # Создаём объект окна
    myWindow.show()  # Показываем окно

    sys.exit(app.exec_())  # Если exit, то код дальше не исполняется

