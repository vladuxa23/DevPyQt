# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide2.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_FormLogin(object):
    def setupUi(self, FormLogin):
        if not FormLogin.objectName():
            FormLogin.setObjectName(u"FormLogin")
        FormLogin.resize(300, 140)
        FormLogin.setMinimumSize(QSize(300, 140))
        FormLogin.setMaximumSize(QSize(300, 140))
        self.gridLayout = QGridLayout(FormLogin)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(FormLogin)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(60, 22))

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(FormLogin)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(150, 22))

        self.horizontalLayout.addWidget(self.lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(FormLogin)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(60, 22))

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit_2 = QLineEdit(FormLogin)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(150, 22))
        self.lineEdit_2.setEchoMode(QLineEdit.EchoMode.Password)

        self.horizontalLayout_2.addWidget(self.lineEdit_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.pushButtonLogin = QPushButton(FormLogin)
        self.pushButtonLogin.setObjectName(u"pushButtonLogin")

        self.verticalLayout_2.addWidget(self.pushButtonLogin)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)


        self.retranslateUi(FormLogin)

        QMetaObject.connectSlotsByName(FormLogin)
    # setupUi

    def retranslateUi(self, FormLogin):
        FormLogin.setWindowTitle(QCoreApplication.translate("FormLogin", u"Form", None))
        self.label.setText(QCoreApplication.translate("FormLogin", u"\u041b\u043e\u0433\u0438\u043d:", None))
        self.label_2.setText(QCoreApplication.translate("FormLogin", u"\u041f\u0430\u0440\u043e\u043b\u044c:", None))
        self.pushButtonLogin.setText(QCoreApplication.translate("FormLogin", u"\u0412\u043e\u0439\u0442\u0438", None))
    # retranslateUi

