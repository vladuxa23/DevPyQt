# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'put.ui'
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
from PySide2.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_FormPut(object):
    def setupUi(self, FormPut):
        if not FormPut.objectName():
            FormPut.setObjectName(u"FormPut")
        FormPut.resize(466, 380)
        self.gridLayout = QGridLayout(FormPut)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_author = QLabel(FormPut)
        self.label_author.setObjectName(u"label_author")
        self.label_author.setMinimumSize(QSize(110, 22))
        self.label_author.setMaximumSize(QSize(110, 22))

        self.horizontalLayout.addWidget(self.label_author)

        self.lineEdit_author = QLineEdit(FormPut)
        self.lineEdit_author.setObjectName(u"lineEdit_author")
        self.lineEdit_author.setEnabled(False)

        self.horizontalLayout.addWidget(self.lineEdit_author)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_title = QLabel(FormPut)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setMinimumSize(QSize(110, 22))
        self.label_title.setMaximumSize(QSize(110, 22))

        self.horizontalLayout_2.addWidget(self.label_title)

        self.lineEdit_title = QLineEdit(FormPut)
        self.lineEdit_title.setObjectName(u"lineEdit_title")
        self.lineEdit_title.setEnabled(True)

        self.horizontalLayout_2.addWidget(self.lineEdit_title)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_message = QLabel(FormPut)
        self.label_message.setObjectName(u"label_message")
        self.label_message.setMinimumSize(QSize(110, 22))
        self.label_message.setMaximumSize(QSize(110, 22))

        self.horizontalLayout_3.addWidget(self.label_message)

        self.textEdit_message = QTextEdit(FormPut)
        self.textEdit_message.setObjectName(u"textEdit_message")
        self.textEdit_message.setEnabled(True)
        self.textEdit_message.setMinimumSize(QSize(0, 100))

        self.horizontalLayout_3.addWidget(self.textEdit_message)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_public = QLabel(FormPut)
        self.label_public.setObjectName(u"label_public")
        self.label_public.setMinimumSize(QSize(110, 22))
        self.label_public.setMaximumSize(QSize(110, 22))

        self.horizontalLayout_4.addWidget(self.label_public)

        self.checkBox_public = QCheckBox(FormPut)
        self.checkBox_public.setObjectName(u"checkBox_public")
        self.checkBox_public.setEnabled(True)

        self.horizontalLayout_4.addWidget(self.checkBox_public)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 3, -1, -1)
        self.label_importance = QLabel(FormPut)
        self.label_importance.setObjectName(u"label_importance")
        self.label_importance.setMinimumSize(QSize(110, 22))
        self.label_importance.setMaximumSize(QSize(110, 22))

        self.horizontalLayout_5.addWidget(self.label_importance)

        self.checkBox_importance = QCheckBox(FormPut)
        self.checkBox_importance.setObjectName(u"checkBox_importance")
        self.checkBox_importance.setEnabled(True)

        self.horizontalLayout_5.addWidget(self.checkBox_importance)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_status = QLabel(FormPut)
        self.label_status.setObjectName(u"label_status")
        self.label_status.setMinimumSize(QSize(110, 22))
        self.label_status.setMaximumSize(QSize(110, 22))

        self.horizontalLayout_6.addWidget(self.label_status)

        self.comboBox_status = QComboBox(FormPut)
        self.comboBox_status.setObjectName(u"comboBox_status")

        self.horizontalLayout_6.addWidget(self.comboBox_status)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_deadline = QLabel(FormPut)
        self.label_deadline.setObjectName(u"label_deadline")
        self.label_deadline.setMinimumSize(QSize(110, 22))
        self.label_deadline.setMaximumSize(QSize(110, 22))

        self.horizontalLayout_7.addWidget(self.label_deadline)

        self.dateTimeEdit = QDateTimeEdit(FormPut)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")

        self.horizontalLayout_7.addWidget(self.dateTimeEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_createdate = QLabel(FormPut)
        self.label_createdate.setObjectName(u"label_createdate")
        self.label_createdate.setMinimumSize(QSize(110, 22))
        self.label_createdate.setMaximumSize(QSize(110, 22))

        self.horizontalLayout_8.addWidget(self.label_createdate)

        self.lineEdit_createdate = QLineEdit(FormPut)
        self.lineEdit_createdate.setObjectName(u"lineEdit_createdate")
        self.lineEdit_createdate.setEnabled(False)

        self.horizontalLayout_8.addWidget(self.lineEdit_createdate)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_updatedate = QLabel(FormPut)
        self.label_updatedate.setObjectName(u"label_updatedate")
        self.label_updatedate.setMinimumSize(QSize(110, 22))
        self.label_updatedate.setMaximumSize(QSize(110, 22))

        self.horizontalLayout_9.addWidget(self.label_updatedate)

        self.lineEdit_updatedate = QLineEdit(FormPut)
        self.lineEdit_updatedate.setObjectName(u"lineEdit_updatedate")
        self.lineEdit_updatedate.setEnabled(False)

        self.horizontalLayout_9.addWidget(self.lineEdit_updatedate)


        self.verticalLayout.addLayout(self.horizontalLayout_9)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.pushButtonPut = QPushButton(FormPut)
        self.pushButtonPut.setObjectName(u"pushButtonPut")

        self.gridLayout.addWidget(self.pushButtonPut, 1, 0, 1, 1)


        self.retranslateUi(FormPut)

        QMetaObject.connectSlotsByName(FormPut)
    # setupUi

    def retranslateUi(self, FormPut):
        FormPut.setWindowTitle(QCoreApplication.translate("FormPut", u"Form", None))
        self.label_author.setText(QCoreApplication.translate("FormPut", u"\u0410\u0432\u0442\u043e\u0440:", None))
        self.label_title.setText(QCoreApplication.translate("FormPut", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0434\u0435\u043b\u0430:", None))
        self.label_message.setText(QCoreApplication.translate("FormPut", u"\u041f\u043e\u0434\u0440\u043e\u0431\u043d\u043e\u0441\u0442\u0438 \u0434\u0435\u043b\u0430:", None))
        self.label_public.setText(QCoreApplication.translate("FormPut", u"\u041f\u0443\u0431\u043b\u0438\u0447\u043d\u0430\u044f::", None))
        self.checkBox_public.setText("")
        self.label_importance.setText(QCoreApplication.translate("FormPut", u"\u0412\u0430\u0436\u043d\u0430\u044f:", None))
        self.checkBox_importance.setText("")
        self.label_status.setText(QCoreApplication.translate("FormPut", u"\u0421\u0442\u0430\u0442\u0443\u0441:", None))
        self.label_deadline.setText(QCoreApplication.translate("FormPut", u"\u0421\u0440\u043e\u043a \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f:", None))
        self.label_createdate.setText(QCoreApplication.translate("FormPut", u"\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f:", None))
        self.label_updatedate.setText(QCoreApplication.translate("FormPut", u"\u0414\u0430\u0442\u0430 \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f:", None))
        self.pushButtonPut.setText(QCoreApplication.translate("FormPut", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c \u0434\u0435\u043b\u043e", None))
    # retranslateUi

