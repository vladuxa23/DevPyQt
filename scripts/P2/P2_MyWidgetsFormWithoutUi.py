from PySide2 import QtWidgets, QtCore


class MyWindow(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()

    def initUi(self):

        self.pb_left_top = QtWidgets.QPushButton()
        self.pb_left_top.setText("Лево/верх")
        self.pb_left_top.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                       QtWidgets.QSizePolicy.Policy.Expanding)

        self.pb_right_top = QtWidgets.QPushButton()
        self.pb_right_top.setText("Право/верх")
        self.pb_right_top.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                       QtWidgets.QSizePolicy.Policy.Expanding)

        self.pb_center = QtWidgets.QPushButton()
        self.pb_center.setText("Центр")
        self.pb_center.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                       QtWidgets.QSizePolicy.Policy.Expanding)

        self.pb_left_bottom = QtWidgets.QPushButton()
        self.pb_left_bottom.setText("Лево/низ")
        self.pb_left_bottom.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                       QtWidgets.QSizePolicy.Policy.Expanding)

        self.pb_right_bottom = QtWidgets.QPushButton()
        self.pb_right_bottom.setText("Право/низ")
        self.pb_right_bottom.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                       QtWidgets.QSizePolicy.Policy.Expanding)

        self.pb_get_parameters = QtWidgets.QPushButton()
        self.pb_get_parameters.setText("Получить параметры")

        self.dial = QtWidgets.QDial()

        self.cb_lcd = QtWidgets.QComboBox()
        self.cb_lcd.addItems(["HEX", "DEC", "OCT", "BIN"])

        self.lcd = QtWidgets.QLCDNumber()

        self.slider = QtWidgets.QSlider()
        self.slider.setOrientation(QtCore.Qt.Orientation.Horizontal)

        self.textEdit = QtWidgets.QPlainTextEdit()

        # LAYOUTS

        # pb_layout
        pb_layout = QtWidgets.QVBoxLayout()
        pb_layout_sub_1 = QtWidgets.QHBoxLayout()
        pb_layout_sub_2 = QtWidgets.QHBoxLayout()
        pb_layout_sub_3 = QtWidgets.QHBoxLayout()
        pb_layout_sub_4 = QtWidgets.QHBoxLayout()

        pb_layout_sub_1.addWidget(self.pb_left_top)
        pb_layout_sub_1.addWidget(self.pb_right_top)

        pb_layout_sub_2.addWidget(self.pb_center)

        pb_layout_sub_3.addWidget(self.pb_left_bottom)
        pb_layout_sub_3.addWidget(self.pb_right_bottom)

        pb_layout_sub_4.addWidget(self.pb_get_parameters)

        pb_layout.addLayout(pb_layout_sub_1)
        pb_layout.addLayout(pb_layout_sub_2)
        pb_layout.addLayout(pb_layout_sub_3)
        pb_layout.addLayout(pb_layout_sub_4)
        # /pb_layout

        # lcd_layout
        lcd_layout = QtWidgets.QVBoxLayout()

        lcd_layout.addWidget(self.cb_lcd)
        lcd_layout.addWidget(self.lcd)
        # /lcd_layout

        # lcd_layout_with_dial
        lcd_layout_with_dial = QtWidgets.QHBoxLayout()

        lcd_layout_with_dial.addWidget(self.dial)
        lcd_layout_with_dial.addLayout(lcd_layout)
        # /lcd_layout_with_dial

        # left_bottom_layout
        left_bottom_layout = QtWidgets.QVBoxLayout()

        left_bottom_layout.addLayout(lcd_layout_with_dial)
        left_bottom_layout.addWidget(self.slider)
        # /left_bottom_layout

        # main_layout_left
        main_layout_left = QtWidgets.QVBoxLayout()

        main_layout_left.addLayout(pb_layout)
        main_layout_left.addLayout(left_bottom_layout)
        # /main_layout_left

        # main_layout
        main_layout = QtWidgets.QHBoxLayout()

        main_layout.addLayout(main_layout_left)
        main_layout.addWidget(self.textEdit)
        # main_layout

        self.setLayout(main_layout)


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    win = MyWindow()
    win.show()

    app.exec_()

