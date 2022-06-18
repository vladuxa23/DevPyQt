import sys
from PySide2 import QtWidgets, QtCore, QtGui  # Импорт класса, который содержит элементы окна
from LectionRepeatForm import Ui_Form

class RepeatLesson(QtWidgets.QWidget):  # Наследуемся от QWidget

    def __init__(self, parent=None):  # Создаем конструктор класса
        super().__init__(parent)  # Передаем конструктору ссылку на родительский компонент

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.initUi()

    def initUi(self):
        self.setWindowTitle("Моя программа")

        self.ui.pushButton.clicked.connect(self.onPushButtonClicked)
        self.ui.lineEditSource.textChanged.connect(self.onPushButtonClicked)

    def onPushButtonClicked(self):
        # print(self.sender())
        source_text = self.ui.lineEditSource.text()
        self.ui.lineEditResult.setText(source_text[::-1])

    def event(self, event:QtCore.QEvent) -> bool:
        if event.type() == QtCore.QEvent.Move:
            print(event.pos().x(), event.pos().y())

        return QtWidgets.QWidget.event(self, event)

    def closeEvent(self, event:QtGui.QCloseEvent) -> None:
        print("Пока")





if __name__ == "__main__":
    app = QtWidgets.QApplication()  # Создаем  объект приложения
    # app = QtWidgets.QApplication(sys.argv)  # Если PyQt

    myWindow = RepeatLesson()  # Создаём объект окна
    myWindow.show()  # Показываем окно

    sys.exit(app.exec_())  # Если exit, то код дальше не исполняется

