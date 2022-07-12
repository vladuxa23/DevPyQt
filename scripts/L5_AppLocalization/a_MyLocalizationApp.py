import sys
from functools import partial
from PySide2 import QtCore, QtWidgets

# https://github.com/thurask/Qt-Linguist/releases/download/20201205/linguist_5.15.2.zip
# lupdate plotWithMPL.py -ts to_en.ts
# lrelease to_en2.ts to_en.qm


class MyTranslateApp(QtWidgets.QMainWindow):
    """Основное окно программы-прототипа для тестирования класса QtCore.Qtranslator"""
    def __init__(self):
        """Функция-конструктор класса, где роисходит инициализация необходимых переменных"""
        super().__init__()
        self.initUI()  # Инициализируем дизайн приложения

        self.QT_TRANSLATIONS_PATH = "C:/Python396/Lib/site-packages/PySide2/translations/"


        self.translator = QtCore.QTranslator(self)  # Инициализируем класс QTranslator, который потребуется для
        # локализации пользовательского текста в самой программе
        self.translatorApp = QtCore.QTranslator(self)  # Инициализируем класс QTranslator, который потребуется для
        # локализации приложения в целом

        self.button_ru.clicked.connect(partial(self.setLocalization, "ru"))  # Устанавливем слот который срабатывает при
        self.button_en.clicked.connect(partial(self.setLocalization, "en"))  # генерации сигнала кнопками button_ru и
        # button_en

    def initUI(self):
        """Функция инициализирует элементы дизайна приложения"""

        cetralWidget = QtWidgets.QWidget()
        self.setCentralWidget(cetralWidget)

        self.setWindowTitle("MyTranslateApp")
        self.setFixedSize(400, 500)

        self.button_ru = QtWidgets.QPushButton("RU")
        self.button_en = QtWidgets.QPushButton("EN")
        self.button_input = QtWidgets.QPushButton("Ввод")

        self.line_edit_name = QtWidgets.QLineEdit()
        self.line_edit_surname = QtWidgets.QLineEdit()

        self.labelName = QtWidgets.QLabel("Имя")
        self.labelName.setMinimumWidth(50)
        self.labelSurname = QtWidgets.QLabel("Фамилия")
        self.labelSurname.setMinimumWidth(50)

        layout_v = QtWidgets.QVBoxLayout()
        layout_h1 = QtWidgets.QHBoxLayout()
        layout_h2 = QtWidgets.QHBoxLayout()
        layout_h3 = QtWidgets.QHBoxLayout()
        layout_h4 = QtWidgets.QHBoxLayout()

        layout_h1.addWidget(self.labelName)
        layout_h1.addWidget(self.line_edit_name)

        layout_h2.addWidget(self.labelSurname)
        layout_h2.addWidget(self.line_edit_surname)

        layout_h3.addWidget(self.button_input)

        layout_h4.addWidget(self.button_ru)
        layout_h4.addWidget(self.button_en)

        layout_v.addLayout(layout_h1)
        layout_v.addLayout(layout_h2)
        layout_v.addLayout(layout_h3)
        layout_v.addLayout(layout_h4)
        layout_v.addItem(QtWidgets.QSpacerItem(1, 1,
                                               QtWidgets.QSizePolicy.Minimum,
                                               QtWidgets.QSizePolicy.Expanding))
        cetralWidget.setLayout(layout_v)

    def changeEvent(self, event):
        """Функция-обработчик событий изменения состояния"""

        if event.type() == QtCore.QEvent.LanguageChange:  # Если "ловим" событие LanguageChange
            self.translateUi()  # Тогда вызываем функцию translateUi()
        super(MyTranslateApp, self).changeEvent(event)  # Отправляем "родителю" новое состояние

    @QtCore.Slot()
    def setLocalization(self, lang):
        """Функция, являющаяся слотом для кнопок button_ru и button_en"""

        self.translator.load(f"translations/to_{lang}")  # Загружаем созданный нами файл qm, можно указывать без расширения
        # self.translator.load(f"{lang}_ver.qm")  # Загружаем созданный нами файл qm, можно указывать без расширения
        self.translatorApp.load(f"{self.QT_TRANSLATIONS_PATH}qtbase_{lang}")  # Загружаем файл qm для ядра нашего
        # приложения, т.е. всех стандартных
        # надписей, к примеру кнопки "Да" -> "Yes"

        QtWidgets.QApplication.instance().installTranslator(self.translator)  # Устанавливаем локализацию окна
        QtWidgets.QApplication.instance().installTranslator(self.translatorApp)  # Устанавливаем локализацию приложения

    def translateUi(self):
        """Обязательная функция для вызова при переводе приложения"""
        # Указываем что текст в элементах подлежит переводу
        self.labelName.setText(QtWidgets.QApplication.translate("MyTranslateApp", "Имя"))
        self.labelSurname.setText(QtWidgets.QApplication.translate("MyTranslateApp", "Фамилия"))
        self.button_input.setText(QtWidgets.QApplication.translate("MyTranslateApp", "Ввод"))
        self.setWindowTitle(QtWidgets.QApplication.translate("MyTranslateApp", "Переводчик"))

    def closeEvent(self, event):
        """Функция-обработчик события закрытия окна"""

        def exit_message_text():
            """Функция  переводит заголовок QtWidgets.QMessageBox.question"""
            return QtWidgets.QApplication.translate("MyTranslateApp", "Вы действительно хотите закрыть программу?")

        def exit_message_title():
            """Функция  переводит текст QtWidgets.QMessageBox.question"""
            return QtWidgets.QApplication.translate("MyTranslateApp", "Выход")

        reply = QtWidgets.QMessageBox.question(self, exit_message_title(),
                                               exit_message_text(),
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyTranslateApp()
    myapp.show()
    sys.exit(app.exec_())
