from PySide2 import QtCore, QtWidgets
from PySide2.QtGui import QIcon


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 500)  # размер окна приложения

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.pbtn_img = QtWidgets.QButtonGroup(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)

        """
        Кнопки на игровой сетке
        """
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(2, -1, -1, -1)

        self.position1 = QtWidgets.QPushButton(self.centralwidget)
        self.position1.setMinimumSize(QtCore.QSize(70, 70))
        self.pbtn_img.addButton(self.position1)
        self.gridLayout_2.addWidget(self.position1, 0, 0, 1, 1)



        self.position2 = QtWidgets.QPushButton(self.centralwidget)
        self.position2.setMinimumSize(QtCore.QSize(70, 70))
        self.pbtn_img.addButton(self.position2)
        self.gridLayout_2.addWidget(self.position2, 0, 1, 1, 1)

        self.position3 = QtWidgets.QPushButton(self.centralwidget)
        self.position3.setMinimumSize(QtCore.QSize(70, 70))
        self.pbtn_img.addButton(self.position3)
        self.gridLayout_2.addWidget(self.position3, 0, 2, 1, 1)

        self.position4 = QtWidgets.QPushButton(self.centralwidget)
        self.position4.setMinimumSize(QtCore.QSize(70, 70))
        self.pbtn_img.addButton(self.position4)
        self.gridLayout_2.addWidget(self.position4, 0, 3, 1, 1)

        self.position5 = QtWidgets.QPushButton(self.centralwidget)
        self.position5.setMinimumSize(QtCore.QSize(70, 70))
        self.pbtn_img.addButton(self.position5)
        self.gridLayout_2.addWidget(self.position5, 1, 0, 1, 1)

        self.position6 = QtWidgets.QPushButton(self.centralwidget)
        self.position6.setMinimumSize(QtCore.QSize(70, 70))
        self.pbtn_img.addButton(self.position6)
        self.gridLayout_2.addWidget(self.position6, 1, 1, 1, 1)

        self.position7 = QtWidgets.QPushButton(self.centralwidget)
        self.position7.setMinimumSize(QtCore.QSize(70, 70))
        self.pbtn_img.addButton(self.position7)
        self.gridLayout_2.addWidget(self.position7, 1, 2, 1, 1)

        self.position8 = QtWidgets.QPushButton(self.centralwidget)
        self.position8.setMinimumSize(QtCore.QSize(70, 70))
        self.pbtn_img.addButton(self.position8)
        self.gridLayout_2.addWidget(self.position8, 1, 3, 1, 1)

        self.position9 = QtWidgets.QPushButton(self.centralwidget)
        self.position9.setMinimumSize(QtCore.QSize(70, 70))
        self.pbtn_img.addButton(self.position9)
        self.gridLayout_2.addWidget(self.position9, 2, 0, 1, 1)

        self.position10 = QtWidgets.QPushButton(self.centralwidget)
        self.position10.setMinimumSize(QtCore.QSize(70, 70))
        self.pbtn_img.addButton(self.position10)
        self.gridLayout_2.addWidget(self.position10, 2, 1, 1, 1)

        self.position11 = QtWidgets.QPushButton(self.centralwidget)
        self.position11.setMinimumSize(QtCore.QSize(70, 70))
        self.pbtn_img.addButton(self.position11)
        self.gridLayout_2.addWidget(self.position11, 2, 2, 1, 1)

        self.position12 = QtWidgets.QPushButton(self.centralwidget)
        self.position12.setMinimumSize(QtCore.QSize(70, 70))
        self.pbtn_img.addButton(self.position12)
        self.gridLayout_2.addWidget(self.position12, 2, 3, 1, 1)

        self.position13 = QtWidgets.QPushButton(self.centralwidget)
        self.position13.setMinimumSize(QtCore.QSize(70, 70))
        self.pbtn_img.addButton(self.position13)
        self.gridLayout_2.addWidget(self.position13, 3, 0, 1, 1)

        self.position14 = QtWidgets.QPushButton(self.centralwidget)
        self.position14.setMinimumSize(QtCore.QSize(70, 70))
        self.pbtn_img.addButton(self.position14)
        self.gridLayout_2.addWidget(self.position14, 3, 1, 1, 1)

        self.position15 = QtWidgets.QPushButton(self.centralwidget)
        self.position15.setMinimumSize(QtCore.QSize(70, 70))
        self.pbtn_img.addButton(self.position15)
        self.gridLayout_2.addWidget(self.position15, 3, 2, 1, 1)

        self.position16 = QtWidgets.QPushButton(self.centralwidget)
        self.position16.setMinimumSize(QtCore.QSize(70, 70))
        self.pbtn_img.addButton(self.position16)
        self.gridLayout_2.addWidget(self.position16, 3, 3, 1, 1)

        """
        Кнопки управления
        """
        self.gridLayout_3 = QtWidgets.QGridLayout()

        self.left = QtWidgets.QPushButton("ВЛЕВО", self.centralwidget)
        self.left.setMinimumSize(QtCore.QSize(70, 50))
        self.gridLayout_3.addWidget(self.left, 1, 0, 1, 1)

        self.up = QtWidgets.QPushButton("ВВЕРХ", self.centralwidget)
        self.up.setMinimumSize(QtCore.QSize(70, 50))
        self.gridLayout_3.addWidget(self.up, 0, 1, 1, 1)

        self.down = QtWidgets.QPushButton("ВНИЗ", self.centralwidget)
        self.down.setMinimumSize(QtCore.QSize(70, 50))
        self.gridLayout_3.addWidget(self.down, 2, 1, 1, 1)

        self.right = QtWidgets.QPushButton("ВПРАВО", self.centralwidget)
        self.right.setMinimumSize(QtCore.QSize(70, 50))
        self.gridLayout_3.addWidget(self.right, 1, 2, 1, 1)

        """
        Расположение кнопок управления
        """
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.addLayout(self.gridLayout_3, 1, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 0, 0, 1, 2)

        """
        Кнопка правил игры
        """
        self.ruls = QtWidgets.QPushButton(QIcon('book-4.jpg'), "ПРАВИЛА", self.centralwidget)
        self.ruls.setMinimumSize(QtCore.QSize(250, 50))
        self.gridLayout_4.addWidget(self.ruls)

        """
        Кнопка рестарта
        """
        self.restart = QtWidgets.QPushButton("ЗАНОВО", self.centralwidget)
        self.restart.setMinimumSize(QtCore.QSize(250, 50))
        self.gridLayout_4.addWidget(self.restart)

        """
        Кнопка выхода
        """
        self.exit = QtWidgets.QPushButton(QIcon('exit.png'), "ЗАКРЫТЬ", self.centralwidget)
        self.exit.setMinimumSize(QtCore.QSize(250, 50))
        self.gridLayout_4.addWidget(self.exit)

