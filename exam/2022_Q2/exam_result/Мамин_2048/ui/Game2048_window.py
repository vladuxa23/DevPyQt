# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Game2048_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(450, 515)
        MainWindow.setAcceptDrops(True)
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        self.action3_3 = QAction(MainWindow)
        self.action3_3.setObjectName(u"action3_3")
        self.action4_4 = QAction(MainWindow)
        self.action4_4.setObjectName(u"action4_4")
        self.action5_5 = QAction(MainWindow)
        self.action5_5.setObjectName(u"action5_5")
        self.action_reset_record = QAction(MainWindow)
        self.action_reset_record.setObjectName(u"action_reset_record")
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 451, 44))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Sitka Text")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setCursor(QCursor(Qt.WaitCursor))
        self.label.setContextMenuPolicy(Qt.CustomContextMenu)
        self.label.setToolTipDuration(-1)
        self.label.setFrameShadow(QFrame.Plain)
        self.label.setMargin(6)

        self.horizontalLayout.addWidget(self.label)

        self.label_3 = QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setFamily(u"Sitka Text")
        font1.setPointSize(14)
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_3)

        self.label_2 = QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setMargin(5)

        self.horizontalLayout.addWidget(self.label_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 450, 21))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menu)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.action_reset_record)
        self.menu.addAction(self.action)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.action3_3)
        self.menu_2.addAction(self.action4_4)
        self.menu_2.addAction(self.action5_5)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Play Game 2048"))
        self.label.setText(_translate("MainWindow", "time"))
        self.label_3.setText(_translate("MainWindow", "Game 2048"))
        self.label_2.setText(_translate("MainWindow", "points"))
        self.menu.setTitle(_translate("MainWindow", "Параметры"))
        self.menu_2.setTitle(_translate("MainWindow", "Кол-во клеток"))
        self.action3_3.setText(_translate("MainWindow", "Поле 3 х 3"))
        self.action4_4.setText(_translate("MainWindow", "Поле 4 х 4"))
        self.action5_5.setText(_translate("MainWindow", "Поле 5 х 5"))
        self.action_reset_record.setText(_translate("MainWindow", "Обнулить рекорд"))
        self.action.setText(_translate("MainWindow", "Начать заново"))
