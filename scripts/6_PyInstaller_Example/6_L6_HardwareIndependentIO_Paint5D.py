from PySide2 import QtCore, QtWidgets, QtGui

# TODO: 1.   Придумать как обработать ситуацию с чёрным цветом
#       2.   Кнопка сохранить изображение
#       3*.  Сделать кисть "Распылитель"


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.initBrush()

        self.sliderSize.valueChanged.connect(self.setBrushSize)
        self.pbColor.clicked.connect(self.setColor)

    def initUI(self):
        self.setWindowTitle("Paint 5D")
        self.setGeometry(QtCore.QRect(200, 200, 800, 500))
        self.setMinimumSize(300, 200)

        centralWidget = QtWidgets.QWidget()
        self.setCentralWidget(centralWidget)

        self.pbColor = QtWidgets.QPushButton("Цвет", self)
        self.pbColor.setMaximumWidth(150)
        self.pbColorBackground = QtGui.QPalette()

        self.sliderSize = QtWidgets.QSlider(self)
        self.sliderSize.setMinimum(2)
        self.sliderSize.setMaximum(32)
        self.sliderSize.setOrientation(QtCore.Qt.Horizontal)

        self.brushSizeLine = QtWidgets.QLineEdit("2")
        self.brushSizeLine.setAlignment(QtCore.Qt.AlignHCenter)
        self.brushSizeLine.setMaximumWidth(30)
        self.brushSizeLine.setEnabled(False)

        brushSizeLabel = QtWidgets.QLabel("Текущий размер кисти:")
        brushSizeLabel.setMaximumWidth(120)

        self.image = QtGui.QImage(QtCore.QSize(800, 500), QtGui.QImage.Format_ARGB32_Premultiplied)
        self.image.fill(QtCore.Qt.gray)
        self.label = QtWidgets.QLabel()
        self.label.setPixmap(QtGui.QPixmap.fromImage(self.image))

        layoutH = QtWidgets.QHBoxLayout()
        layoutH.addWidget(self.pbColor)
        layoutH.addWidget(self.sliderSize)
        layoutH.addWidget(brushSizeLabel)
        layoutH.addWidget(self.brushSizeLine)
        layoutH.setSpacing(10)

        layoutV = QtWidgets.QVBoxLayout()
        layoutV.addWidget(self.label)
        layoutV.addItem(layoutH)

        centralWidget.setLayout(layoutV)

    def initBrush(self):
        self.brushSize = 2
        self.brushColor = QtCore.Qt.black
        self.lastPoint = QtCore.QPoint()

    def setBrushSize(self):
        size = self.sliderSize.value()
        self.brushSize = size
        self.brushSizeLine.setText(str(size))

    def setColor(self):
        color = QtWidgets.QColorDialog.getColor(parent=self, title="Выбор цвета")
        self.brushColor = color
        self.pbColor.setStyleSheet(f"background-color: {color.name()}")

    def paintEvent(self, event):
        painter = QtGui.QPainter(self.label.pixmap())
        painter.drawImage(event.rect(), self.image, self.rect())

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.lastPoint = event.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() and QtCore.Qt.LeftButton:
            painter = QtGui.QPainter(self.image)
            painter.setPen(QtGui.QPen(self.brushColor, self.brushSize, QtCore.Qt.SolidLine, QtCore.Qt.RoundCap,
                                      QtCore.Qt.RoundJoin))
            painter.drawLine(self.lastPoint, event.pos())
            self.lastPoint = event.pos()
            self.update()


if __name__ == "__main__":
    app = QtWidgets.QApplication()
    window = Window()
    window.show()
    app.exec_()
