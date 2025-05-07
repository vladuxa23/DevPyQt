"""
Реализация программу взаимодействия виджетов друг с другом:
Форма для приложения (ui/d_eventfilter_settings_form.ui)

Программа должна обладать следующим функционалом:

1. Добавить для dial возможность установки значений кнопками клавиатуры(+ и -),
   выводить новые значения в консоль

2. Соединить между собой QDial, QSlider, QLCDNumber
   (изменение значения в одном, изменяет значения в других)

3. Для QLCDNumber сделать отображение в различных системах счисления (oct, hex, bin, dec),
   изменять формат отображаемого значения в зависимости от выбранного в comboBox параметра.

4. Сохранять значение выбранного в comboBox режима отображения
   и значение LCDNumber в QSettings, при перезапуске программы выводить
   в него соответствующие значения
"""

from PySide6 import QtWidgets, QtCore


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        l = QtWidgets.QVBoxLayout()

        self.lcd_modes = {
            "hex": QtWidgets.QLCDNumber.Mode.Hex,
            "dec": QtWidgets.QLCDNumber.Mode.Dec,
            "oct": QtWidgets.QLCDNumber.Mode.Oct,
            "bin": QtWidgets.QLCDNumber.Mode.Bin,
        }

        self.dial = QtWidgets.QDial()
        self.dial.valueChanged.connect(self.onValueChanged)
        self.dial.installEventFilter(self)
        self.lcd = QtWidgets.QLCDNumber()
        self.lcd.display(14)
        self.lcd.setMinimumHeight(60)
        self.slider = QtWidgets.QSlider()
        self.slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.slider.valueChanged.connect(self.onValueChanged)
        self.cb = QtWidgets.QComboBox()
        self.cb.addItems(list(self.lcd_modes.keys()))
        self.cb.currentTextChanged.connect(lambda mode: self.lcd.setMode(self.lcd_modes[mode]))

        l.addWidget(self.dial)
        l.addWidget(self.lcd)
        l.addWidget(self.slider)
        l.addWidget(self.cb)

        self.setLayout(l)

    def onValueChanged(self, value):
        self.dial.setValue(value)
        self.slider.setValue(value)


    def eventFilter(self, watched, event):
        if watched == self.dial and event.type() == QtCore.QEvent.Type.KeyPress:
            if event.key() == QtCore.Qt.Key.Key_Minus:
                self.dial.setValue(self.dial.value() - 1)
            elif event.key() == QtCore.Qt.Key.Key_Plus:
                self.dial.setValue(self.dial.value() + 1)
        
        return super().eventFilter(watched, event)

if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
