# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'authorization_form.ui'
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
        Form.resize(500, 600)
        Form.setMinimumSize(QSize(500, 600))
        Form.setMaximumSize(QSize(500, 600))
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        font = QFont()
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_Surname = QLabel(self.groupBox)
        self.label_Surname.setObjectName(u"label_Surname")
        self.label_Surname.setMinimumSize(QSize(90, 0))
        font1 = QFont()
        font1.setPointSize(8)
        self.label_Surname.setFont(font1)

        self.horizontalLayout.addWidget(self.label_Surname)

        self.lineEdit_Surname = QLineEdit(self.groupBox)
        self.lineEdit_Surname.setObjectName(u"lineEdit_Surname")

        self.horizontalLayout.addWidget(self.lineEdit_Surname)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_Name = QLabel(self.groupBox)
        self.label_Name.setObjectName(u"label_Name")
        self.label_Name.setMinimumSize(QSize(90, 0))
        self.label_Name.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_Name)

        self.lineEdit_Name = QLineEdit(self.groupBox)
        self.lineEdit_Name.setObjectName(u"lineEdit_Name")

        self.horizontalLayout_2.addWidget(self.lineEdit_Name)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_member_number = QLabel(self.groupBox)
        self.label_member_number.setObjectName(u"label_member_number")
        self.label_member_number.setMinimumSize(QSize(90, 0))
        self.label_member_number.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_member_number)

        self.lineEdit_member_number = QLineEdit(self.groupBox)
        self.lineEdit_member_number.setObjectName(u"lineEdit_member_number")

        self.horizontalLayout_3.addWidget(self.lineEdit_member_number)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.pushButton_Enter = QPushButton(Form)
        self.pushButton_Enter.setObjectName(u"pushButton_Enter")

        self.verticalLayout_2.addWidget(self.pushButton_Enter)

        self.verticalSpacer = QSpacerItem(20, 375, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.label_Surname.setText(QCoreApplication.translate("Form", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.label_Name.setText(QCoreApplication.translate("Form", u"\u0418\u043c\u044f", None))
        self.label_member_number.setText(QCoreApplication.translate("Form", u"\u041d\u043e\u043c\u0435\u0440 \u0431\u0438\u043b\u0435\u0442\u0430", None))
        self.pushButton_Enter.setText(QCoreApplication.translate("Form", u"\u0412\u043e\u0439\u0442\u0438", None))
    # retranslateUi

