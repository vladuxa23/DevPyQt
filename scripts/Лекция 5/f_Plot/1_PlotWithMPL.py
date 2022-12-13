import sys
import random
import matplotlib

matplotlib.use('Qt5Agg')

from PySide2 import QtCore, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT
from matplotlib.figure import Figure


class MplCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        fig.set(facecolor="#6272a4")
        self.axes = fig.add_subplot(111)
        self.axes.set(facecolor="#87CEFA")
        super().__init__(fig)


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.initUi()
        self.start_timer()
        # self.update_plot()
        self.move(100, 100)

    def initUi(self):
        self.canvas = MplCanvas(self, width=8, height=5, dpi=100)

        n_data = 100
        self.xdata = list(range(n_data))
        self.ydata = [random.randint(0, 20) for i in range(n_data)]

        toolbar = NavigationToolbar2QT(self.canvas, self)
        toolbar.setObjectName('toolbar')

        label = QtWidgets.QLabel("Max")
        self.spinBoxMax = QtWidgets.QSpinBox()
        self.spinBoxMax.setRange(0, 100)

        paramLayout = QtWidgets.QHBoxLayout()
        paramLayout.addWidget(label)
        paramLayout.addWidget(self.spinBoxMax)
        paramLayout.addStretch(1)

        # SET STYLE
        # title = QtWidgets.QLabel("MyGraph")
        # title.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        # pb_close = QtWidgets.QPushButton('X')
        # pb_close.setObjectName("pb_close")
        # pb_close.setMaximumSize(22, 22)
        # pb_close.setMinimumSize(22, 22)
        # pb_close.clicked.connect(lambda: self.close())
        # pb_hide = QtWidgets.QPushButton('_')
        # pb_hide.setObjectName("pb_hide")
        # pb_hide.setMaximumSize(22, 22)
        # pb_hide.setMinimumSize(22, 22)
        # pb_hide.clicked.connect(lambda: self.showMinimized())
        #
        # layout_title = QtWidgets.QHBoxLayout()
        # layout_title.addWidget(title, alignment=QtCore.Qt.AlignRight)
        # layout_title.addWidget(pb_hide)
        # layout_title.addWidget(pb_close)
        # layout_title.setAlignment(QtCore.Qt.AlignRight)
        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        #
        # self.setStyleSheet("""
        # #pb_close {
        #     background-color: #bd93f9;
        #     color: #f8f8f2;
        #     border-style: none;
        #     border-radius: 11px;
        # }
        # #pb_hide {
        #     background-color: #6272a4;
        #     color: #f8f8f2;
        #     border-style: none;
        #     border-radius: 11px;
        # }
        # #pb_close:hover, #pb_hide:hover {
        #     background-color: #ff5555;
        # }
        # #pb_close:pressed, #pb_hide:pressed {
        #     background-color: #44475a;
        # }
        # #cw {
        #     background-color: #44475a;
        # }
        # #toolbar {
        #     border-style: 1px solid #000
        # }
        # QLabel {
        #     color: white
        # }
        # QSpinBox {
        #     border:none;
        #     background-color: #6272a4;
        #     border-width: 3;
        #     font: bold 14px;
        #     color: white
        # }
        # """)

        layout = QtWidgets.QVBoxLayout()
        layout.addLayout(layout_title)  # Раскомментировать, если устанавливаем стили
        layout.addWidget(toolbar)
        layout.addLayout(paramLayout)
        layout.addWidget(self.canvas)

        cw = QtWidgets.QFrame()
        cw.setObjectName('cw')
        cw.setLayout(layout)

        self.setCentralWidget(cw)

    def start_timer(self):
        self.timer = QtCore.QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()

    def update_plot(self):
        num = self.spinBoxMax.value()
        if num == 0:
            num = random.randint(0, 100)
        self.ydata = self.ydata[1:] + [random.randint(0, num)]
        self.canvas.axes.cla()  # Clear the canvas.
        self.canvas.axes.plot(self.xdata, self.ydata, 'r')

        self.canvas.draw()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    w = MainWindow()
    w.show()

    app.exec_()
