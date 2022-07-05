from PySide2 import QtCore, QtWidgets, QtGui
from ui import MyDialogBoxes_design
import time


class MessageBoxes(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = MyDialogBoxes_design.Ui_MainWindow()
        self.ui.setupUi(self)

        self.errorMsg = QtWidgets.QErrorMessage(self)

        self.ui.pushButton_2.clicked.connect(self.onPushButton_2Clicked)
        self.ui.pushButton_3.clicked.connect(self.onPushButton_3Clicked)
        self.ui.pushButton_4.clicked.connect(self.onPushButton_4Clicked)
        self.ui.pushButton_5.clicked.connect(self.onPushButton_5Clicked)
        self.ui.pushButton_6.clicked.connect(self.onPushButton_6Clicked)
        self.ui.pushButton_7.clicked.connect(self.onPushButton_7Clicked)
        self.ui.pushButton_8.clicked.connect(self.onPushButton_8Clicked)
        self.ui.pushButton_9.clicked.connect(self.onPushButton_9Clicked)
        self.ui.pushButton_10.clicked.connect(self.onPushButton_10Clicked)
        self.ui.pushButton_11.clicked.connect(self.onPushButton_11Clicked)
        self.ui.pushButton_12.clicked.connect(self.onPushButton_12Clicked)
        self.ui.pushButton_13.clicked.connect(self.onPushButton_13Clicked)
        self.ui.pushButton_14.clicked.connect(self.onPushButton_14Clicked)
        self.ui.pushButton_15.clicked.connect(self.onPushButton_15Clicked)
        self.ui.pushButton_16.clicked.connect(self.onPushButton_16Clicked)
        self.ui.pushButton_17.clicked.connect(self.onPushButton_17Clicked)
        self.ui.pushButton_18.clicked.connect(self.onPushButton_18Clicked)
        self.ui.pushButton_19.clicked.connect(self.onPushButton_19Clicked)
        self.ui.pushButton_20.clicked.connect(self.onPushButton_20Clicked)
        self.ui.pushButton_21.clicked.connect(self.onPushButton_21Clicked)

    def onPushButton_2Clicked(self):
        QtWidgets.QMessageBox.about(self, "Уведомление", "Обработка выполнена")
        self.ui.textEdit.append("Обработка выполнена")

    def onPushButton_3Clicked(self):
        answers = {QtWidgets.QMessageBox.Yes: "У меня есть компас!", QtWidgets.QMessageBox.Help: "Бежим!!!"}

        answer = QtWidgets.QMessageBox.question(self, "Вопрос", "Ты боишься смерти, Джек Воробей?",
                                                QtWidgets.QMessageBox.Yes,
                                                QtWidgets.QMessageBox.Help)
        self.ui.textEdit.append(answers.get(answer))

    def onPushButton_4Clicked(self):
        QtWidgets.QMessageBox.warning(self, "Предупреждение", "Дальше продолжать опасно", QtWidgets.QMessageBox.Ok)
        self.ui.textEdit.append("Дальше продолжать опасно")

    def onPushButton_5Clicked(self):
        QtWidgets.QMessageBox.critical(self, "Ошибка!!!", "Шеф, всё пропало!", QtWidgets.QMessageBox.Ok)
        self.ui.textEdit.append("Шеф, всё пропало!")

    def onPushButton_6Clicked(self):
        QtWidgets.QMessageBox.aboutQt(self, "О Qt")

    def onPushButton_7Clicked(self):
        text, ok = QtWidgets.QInputDialog.getText(self, "Введите имя", "Как вас зовут?")
        if ok:
            self.ui.textEdit.append(text)

    def onPushButton_8Clicked(self):
        text, ok = QtWidgets.QInputDialog.getInt(self, "Введите число", "Сколько вам лет?")
        if ok:
            self.ui.textEdit.append(str(text))

    def onPushButton_9Clicked(self):
        text, ok = QtWidgets.QInputDialog.getDouble(self, "Введите число", "Какая температура за окном?")
        if ok:
            self.ui.textEdit.append(str(text))

    def onPushButton_10Clicked(self):
        text, ok = QtWidgets.QInputDialog.getItem(self, "Введите число", "Сколько комнат в вашей квартире?",
                                                  ["Студия", "1", "2", "3"], editable=False)
        if ok:
            self.ui.textEdit.append(str(text))

    def onPushButton_11Clicked(self):
        text, ok = QtWidgets.QInputDialog.getMultiLineText(self, "Добавить заметку", "Введите текст заметки")
        if ok:
            self.ui.textEdit.append(text)

    def onPushButton_12Clicked(self):
        dir_ = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку")
        self.ui.textEdit.append(dir_)

    def onPushButton_13Clicked(self):
        # file = QtWidgets.QFileDialog.getOpenFileUrl(self, "Выберите файл")
        # self.ui.textEdit.append(str(file))

        files = QtWidgets.QFileDialog.getOpenFileUrls(self, "Выберите файлы", filter="*.MD *.ui")
        print(files)
        for _ in files[0]:
            print(_)
            self.ui.textEdit.append(str(_))

    def onPushButton_14Clicked(self):
        # file = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите файл")
        # self.ui.textEdit.append(file)

        files = QtWidgets.QFileDialog.getOpenFileNames(self, "Выберите файлы", filter="*.MD *.ui")
        print(files)
        for _ in files[0]:
            print(_)
            self.ui.textEdit.append(_)


    def onPushButton_15Clicked(self):
        file = QtWidgets.QFileDialog.getSaveFileName(self, "Введите название сохраняемого файла")
        print(file[0])
        self.ui.textEdit.append(file[0])

    def onPushButton_16Clicked(self):
        file = QtWidgets.QFileDialog.getSaveFileUrl(self, "Введите название сохраняемого файла")
        print(file[0])
        self.ui.textEdit.append(file[0].toLocalFile())

    def onPushButton_17Clicked(self):
        color = QtWidgets.QColorDialog.getColor(parent=self, title="Выбор цвета")
        self.ui.textEdit.append(str(color.toHsl()))
        self.ui.textEdit.append(str(color.toHsv()))
        self.ui.textEdit.append(str(color.toRgb()))
        self.ui.textEdit.append(str(color.toCmyk()))
        self.ui.textEdit.append(str(color.toTuple()))
        self.ui.textEdit.append(str(color.toExtendedRgb()))

    def onPushButton_18Clicked(self):
        try:
            lst = ["0"]
            lst[1]
        except IndexError as err:

            self.errorMsg.showMessage(str(err))

    def onPushButton_19Clicked(self):
        ok, font = QtWidgets.QFontDialog.getFont(parent=self, title="Выбор шрифта")
        if ok:
            self.ui.textEdit.append(str(font.family()))
            self.ui.textEdit.append(str(font.pointSize()))
            self.ui.textEdit.append(str(font.weight()))
            self.ui.textEdit.append(str(font.italic()))
            self.ui.textEdit.append(str(font.underline()))

    def onPushButton_20Clicked(self):
        pb = QtWidgets.QProgressDialog(self)
        pb.setLabelText("Прогресс")

        pb.setMinimum(0)
        pb.setValue(0)
        pb.setMaximum(100)
        pb.show()

        for i in range(100):
            if pb.wasCanceled():
                break

            pb.setValue(i)
            time.sleep(1)
            QtWidgets.QApplication.processEvents()

    def onPushButton_21Clicked(self):
        dir_ = QtWidgets.QFileDialog.getExistingDirectoryUrl(self, "Выберите папку")
        print(dir_)
        self.ui.textEdit.append(dir_.toString())


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myapp = MessageBoxes()
    myapp.show()

    app.exec_()
