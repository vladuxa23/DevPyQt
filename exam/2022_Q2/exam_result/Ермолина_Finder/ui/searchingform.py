# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'searchingform.ui'
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
from PySide2.QtWidgets import (QApplication, QCheckBox, QComboBox, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QSplitter, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(508, 513)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.splitter_2 = QSplitter(Form)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.lineEdit = QLineEdit(self.splitter_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.splitter_2.addWidget(self.lineEdit)
        self.pushButton = QPushButton(self.splitter_2)
        self.pushButton.setObjectName(u"pushButton")
        self.splitter_2.addWidget(self.pushButton)

        self.verticalLayout.addWidget(self.splitter_2)

        self.splitter_3 = QSplitter(Form)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Horizontal)
        self.lineEdit_2 = QLineEdit(self.splitter_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.splitter_3.addWidget(self.lineEdit_2)
        self.comboBox = QComboBox(self.splitter_3)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.splitter_3.addWidget(self.comboBox)

        self.verticalLayout.addWidget(self.splitter_3)

        self.checkBox = QCheckBox(Form)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout.addWidget(self.checkBox)

        self.splitter = QSplitter(Form)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.label = QLabel(self.splitter)
        self.label.setObjectName(u"label")
        self.splitter.addWidget(self.label)
        self.lineEdit_3 = QLineEdit(self.splitter)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.splitter.addWidget(self.lineEdit_3)
        self.label_2 = QLabel(self.splitter)
        self.label_2.setObjectName(u"label_2")
        self.splitter.addWidget(self.label_2)

        self.verticalLayout.addWidget(self.splitter)

        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout.addWidget(self.pushButton_2)

        self.listWidget = QListWidget(Form)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout.addWidget(self.listWidget)

        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout.addWidget(self.pushButton_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043f\u0443\u0442\u044c \u043a \u043f\u0430\u043f\u043a\u0435", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u041e\u0431\u0437\u043e\u0440", None))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0437\u0430\u043f\u0440\u043e\u0441 (\u0434\u043b\u044f \u0441\u0442\u0440\u043e\u043a\u0438: .\u0440\u0430\u0441\u0448\u0438\u0440\u0435\u043d\u0438\u0435)", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"\u0421\u0442\u0440\u043e\u043a\u043e\u0432\u044b\u0439 \u043f\u043e\u0438\u0441\u043a", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"\u041f\u043e\u0438\u0441\u043a \u043f\u043e \u0431\u0430\u0439\u0442\u0430\u043c", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Form", u"\u041f\u043e\u0438\u0441\u043a \u043f\u043e \u0431\u0438\u043d\u0430\u0440\u043d\u044b\u043c \u0441\u0438\u0433\u043d\u0430\u0442\u0443\u0440\u0430\u043c", None))

        self.checkBox.setText(QCoreApplication.translate("Form", u"\u0423\u0447\u0438\u0442\u044b\u0432\u0430\u0442\u044c \u0440\u0430\u0437\u043c\u0435\u0440 \u0444\u0430\u0439\u043b\u043e\u0432", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0418\u0441\u043a\u0430\u0442\u044c \u0432 \u0444\u0430\u0439\u043b\u0430\u0445 \u0440\u0430\u0437\u043c\u0435\u0440\u043e\u043c \u043c\u0435\u043d\u044c\u0448\u0435", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0431\u0430\u0439\u0442", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0447\u0430\u0442\u044c \u043f\u043e\u0438\u0441\u043a", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Form", u"\u041f\u0443\u0442\u044c \u043a \u0444\u0430\u0439\u043b\u0443 1", None));
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("Form", u"\u041f\u0443\u0442\u044c \u043a \u0444\u0430\u0439\u043b\u0443 2", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0440\u0430\u0441\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435", None))
    # retranslateUi


