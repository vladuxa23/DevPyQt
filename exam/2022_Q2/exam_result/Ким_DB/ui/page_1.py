# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_1.ui'
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
        MainWindow.resize(1117, 618)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.groupBoxCases = QGroupBox(self.centralwidget)
        self.groupBoxCases.setObjectName(u"groupBoxCases")
        self.groupBoxCases.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.horizontalLayout = QHBoxLayout(self.groupBoxCases)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButtonCases = QPushButton(self.groupBoxCases)
        self.pushButtonCases.setObjectName(u"pushButtonCases")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonCases.sizePolicy().hasHeightForWidth())
        self.pushButtonCases.setSizePolicy(sizePolicy)
        self.pushButtonCases.setMaximumSize(QSize(350, 350))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonCases.setFont(font)
        self.pushButtonCases.setStyleSheet(u"background-color: rgb(212, 212, 255);\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout.addWidget(self.pushButtonCases)


        self.horizontalLayout_3.addWidget(self.groupBoxCases)

        self.groupBoxEmp = QGroupBox(self.centralwidget)
        self.groupBoxEmp.setObjectName(u"groupBoxEmp")
        self.groupBoxEmp.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBoxEmp)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButtonEmp = QPushButton(self.groupBoxEmp)
        self.pushButtonEmp.setObjectName(u"pushButtonEmp")
        sizePolicy.setHeightForWidth(self.pushButtonEmp.sizePolicy().hasHeightForWidth())
        self.pushButtonEmp.setSizePolicy(sizePolicy)
        self.pushButtonEmp.setMaximumSize(QSize(350, 350))
        self.pushButtonEmp.setFont(font)
        self.pushButtonEmp.setStyleSheet(u"background-color: rgb(212, 212, 255);\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout_2.addWidget(self.pushButtonEmp)


        self.horizontalLayout_3.addWidget(self.groupBoxEmp)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1117, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBoxCases.setTitle("")
        self.pushButtonCases.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0415\u041b\u0410", None))
        self.groupBoxEmp.setTitle("")
        self.pushButtonEmp.setText(QCoreApplication.translate("MainWindow", u"\u0421\u041e\u0422\u0420\u0423\u0414\u041d\u0418\u041a\u0418", None))
    # retranslateUi

