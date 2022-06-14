from PySide2 import QtCore, QtWidgets, QtGui


class _Bar(QtWidgets.QWidget):

    clickedValue = QtCore.Signal(int)

    def __init__(self, steps, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                           QtWidgets.QSizePolicy.MinimumExpanding)

        if isinstance(steps, list):
            self.n_steps = len(steps)
            self.steps = steps

        elif isinstance(steps, int):
            self.n_steps = steps
            self.steps = ["green"] * steps

        else:
            raise TypeError("steps must be list or int")

        self._bar_solid_percent = 0.8
        self._background_color = QtGui.QColor("gray")
        self._padding = 4.0

    def paintEvent(self, event: QtGui.QPaintEvent) -> None:
        painter = QtGui.QPainter(self)

        brush = QtGui.QBrush()
        brush.setColor(self._background_color)
        brush.setStyle(QtCore.Qt.SolidPattern)
        rect = QtCore.QRect(0, 0, painter.device().width(), painter.device().height())
        painter.fillRect(rect, brush)

        parent = self.parent()
        vmin, vmax = parent.minimum(), parent.maximum()
        value = parent.value()

        d_height = painter.device().height() - (self._padding * 2)
        d_width = painter.device().width() - (self._padding * 2)

        step_size = d_height / self.n_steps
        bar_height = step_size * self._bar_solid_percent
        bar_spacer = step_size * (1 - self._bar_solid_percent) / 2

        pc = (value - vmin) / (vmax - vmin)
        n_steps_to_draw = int(pc * self.n_steps)

        for n in range(n_steps_to_draw):
            brush.setColor(QtGui.QColor(self.steps[n]))
            rect = QtCore.QRect(self._padding,
                                self._padding + d_height - ((n + 1) * step_size) + bar_spacer,
                                d_width,
                                bar_height)
            painter.fillRect(rect, brush)

        painter.end()

    def sizeHint(self) -> QtCore.QSize:
        return QtCore.QSize(40, 120)

    def _triggered_refresh(self):
        self.update()

    def _calculate_clicked_value(self, e):
        parent = self.parent()
        vmin, vmax = parent.minimum(), parent.maximum()
        d_height = self.size().height() + (self._padding * 2)
        step_size = d_height / self.n_steps
        click_y = e.y() - self._padding - step_size / 2
        pc = (d_height - click_y) / d_height
        value = vmin + pc * (vmax - vmin)
        self.clickedValue.emit(value)

    def mouseMoveEvent(self, event: QtGui.QMouseEvent) -> None:
        self._calculate_clicked_value(event)

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        self._calculate_clicked_value(event)


class PowerBar(QtWidgets.QWidget):

    colorChanged = QtCore.Signal()

    def __init__(self, steps=10, *args, **kwargs):
        super(PowerBar, self).__init__(*args, **kwargs)

        self._bar = _Bar(steps)

        self._dial = QtWidgets.QDial()
        self._dial.setNotchesVisible(True)
        self._dial.setWrapping(False)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self._bar)
        layout.addWidget(self._dial)
        self.setLayout(layout)

        self._dial.valueChanged.connect(self._bar._triggered_refresh)
        self._bar.clickedValue.connect(self._dial.setValue)

    def __getattr__(self, item):
        if item in self.__dict__:
            return self[item]

        return getattr(self._dial, item)

    def setColor(self, color):
        self._bar.steps = [color] * self._bar.n_steps
        self._bar.update()

    def setColors(self, colors):
        self._bar.n_steps = len(colors)
        self._bar.steps = colors
        self._bar.update()

    def setBarPadding(self, i):
        self._bar._padding = int(i)
        self._bar.update()

    def setBarSolidPercent(self, f):
        self._bar._bar_solid_percent = float(f)
        self._bar.update()

    def setBackgroundColor(self, color):
        self._bar._background_color = QtGui.QColor(color)
        self._bar.update()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    volume = PowerBar()
    volume.show()
    app.exec_()
