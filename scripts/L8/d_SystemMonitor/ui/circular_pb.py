# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'circular_pb.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_CircularPB(object):
    def setupUi(self, CircularPB):
        if not CircularPB.objectName():
            CircularPB.setObjectName(u"CircularPB")
        CircularPB.resize(185, 185)
        CircularPB.setMinimumSize(QSize(185, 185))
        CircularPB.setMaximumSize(QSize(180, 180))
        self.centralwidget = QWidget(CircularPB)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.circularProgressBarBase = QFrame(self.centralwidget)
        self.circularProgressBarBase.setObjectName(u"circularProgressBarBase")
        self.circularProgressBarBase.setFrameShape(QFrame.NoFrame)
        self.circularProgressBarBase.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.circularProgressBarBase)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.circularBg = QFrame(self.circularProgressBarBase)
        self.circularBg.setObjectName(u"circularBg")
        self.circularBg.setStyleSheet(u"")
        self.circularBg.setFrameShape(QFrame.NoFrame)
        self.circularBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.circularBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.circularProgress = QFrame(self.circularBg)
        self.circularProgress.setObjectName(u"circularProgress")
        self.circularProgress.setStyleSheet(u"QFrame{\n"
"	border-radius: 77px;\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.circularProgress.setFrameShape(QFrame.NoFrame)
        self.circularProgress.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.circularProgress)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.container = QFrame(self.circularProgress)
        self.container.setObjectName(u"container")
        self.container.setStyleSheet(u"QFrame{\n"
"	border-radius: 70px;\n"
"	background-color: rgb(77, 77, 127);\n"
"}")
        self.container.setFrameShape(QFrame.NoFrame)
        self.container.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.container)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.labelTitle = QLabel(self.container)
        self.labelTitle.setObjectName(u"labelTitle")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(12)
        self.labelTitle.setFont(font)
        self.labelTitle.setStyleSheet(u"background-color: none;\n"
"color: #FFFFFF")
        self.labelTitle.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelTitle, 0, 0, 1, 1)

        self.labelPercentage = QLabel(self.container)
        self.labelPercentage.setObjectName(u"labelPercentage")
        font1 = QFont()
        font1.setFamily(u"Roboto Thin")
        font1.setPointSize(48)
        self.labelPercentage.setFont(font1)
        self.labelPercentage.setStyleSheet(u"background-color: none;\n"
"color: #FFFFFF")
        self.labelPercentage.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelPercentage, 1, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.verticalLayout_2.addWidget(self.container)


        self.verticalLayout_3.addWidget(self.circularProgress)


        self.verticalLayout_4.addWidget(self.circularBg)


        self.verticalLayout_5.addWidget(self.circularProgressBarBase)

        CircularPB.setCentralWidget(self.centralwidget)

        self.retranslateUi(CircularPB)

        QMetaObject.connectSlotsByName(CircularPB)
    # setupUi

    def retranslateUi(self, CircularPB):
        CircularPB.setWindowTitle(QCoreApplication.translate("CircularPB", u"MainWindow", None))
        self.labelTitle.setText(QCoreApplication.translate("CircularPB", u"<html><head/><body><p><span style=\" font-weight:600; color:#9b9bff;\">CPU</span> #</p></body></html>", None))
        self.labelPercentage.setText(QCoreApplication.translate("CircularPB", u"<html><head/><body><p><span style=\" font-size:36pt;\">0</span><span style=\" font-size:36pt; vertical-align:super;\">%</span></p></body></html>", None))
    # retranslateUi

