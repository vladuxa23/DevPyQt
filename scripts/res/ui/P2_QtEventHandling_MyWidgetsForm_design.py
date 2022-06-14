# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'P2_QtEventHandling_MyWidgetsForm_design.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(700, 450)
        Form.setMinimumSize(QSize(700, 450))
        self.horizontalLayout_2 = QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pushButtonLT = QPushButton(Form)
        self.pushButtonLT.setObjectName(u"pushButtonLT")
        self.pushButtonLT.setMinimumSize(QSize(0, 50))

        self.horizontalLayout_6.addWidget(self.pushButtonLT)

        self.pushButtonRT = QPushButton(Form)
        self.pushButtonRT.setObjectName(u"pushButtonRT")
        self.pushButtonRT.setMinimumSize(QSize(0, 50))

        self.horizontalLayout_6.addWidget(self.pushButtonRT)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.pushButtonCenter = QPushButton(Form)
        self.pushButtonCenter.setObjectName(u"pushButtonCenter")
        self.pushButtonCenter.setMinimumSize(QSize(0, 50))

        self.verticalLayout_3.addWidget(self.pushButtonCenter)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButtonLB = QPushButton(Form)
        self.pushButtonLB.setObjectName(u"pushButtonLB")
        self.pushButtonLB.setMinimumSize(QSize(0, 50))

        self.horizontalLayout_5.addWidget(self.pushButtonLB)

        self.pushButtonRB = QPushButton(Form)
        self.pushButtonRB.setObjectName(u"pushButtonRB")
        self.pushButtonRB.setMinimumSize(QSize(0, 50))

        self.horizontalLayout_5.addWidget(self.pushButtonRB)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.pushButtonGetData = QPushButton(Form)
        self.pushButtonGetData.setObjectName(u"pushButtonGetData")

        self.verticalLayout_3.addWidget(self.pushButtonGetData)


        self.verticalLayout_2.addLayout(self.verticalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.dial = QDial(Form)
        self.dial.setObjectName(u"dial")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dial.sizePolicy().hasHeightForWidth())
        self.dial.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.dial)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.comboBox = QComboBox(Form)
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout.addWidget(self.comboBox)

        self.lcdNumber = QLCDNumber(Form)
        self.lcdNumber.setObjectName(u"lcdNumber")

        self.verticalLayout.addWidget(self.lcdNumber)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalSlider = QSlider(Form)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.verticalLayout_2.addWidget(self.horizontalSlider)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.plainTextEdit = QPlainTextEdit(Form)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_2.addWidget(self.plainTextEdit)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButtonLT.setText(QCoreApplication.translate("Form", u"\u041b\u0435\u0432\u043e/\u0412\u0435\u0440\u0445", None))
        self.pushButtonRT.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u0430\u0432\u043e/\u0412\u0435\u0440\u0445", None))
        self.pushButtonCenter.setText(QCoreApplication.translate("Form", u"\u0426\u0435\u043d\u0442\u0440", None))
        self.pushButtonLB.setText(QCoreApplication.translate("Form", u"\u041b\u0435\u0432\u043e/\u041d\u0438\u0437", None))
        self.pushButtonRB.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u0430\u0432\u043e/\u041d\u0438\u0437", None))
        self.pushButtonGetData.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u043b\u0443\u0447\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435 \u043e\u043a\u043d\u0430", None))
    # retranslateUi

