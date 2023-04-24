# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'notes_design.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDateTimeEdit, QHBoxLayout, QHeaderView,
    QLabel, QPlainTextEdit, QPushButton, QSizePolicy,
    QTreeWidget, QTreeWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(656, 536)
        self.treeWidget = QTreeWidget(Form)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setGeometry(QRect(10, 320, 631, 192))
        self.saveButton = QPushButton(Form)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setGeometry(QRect(370, 280, 75, 24))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 81, 16))
        self.noteHead = QPlainTextEdit(Form)
        self.noteHead.setObjectName(u"noteHead")
        self.noteHead.setGeometry(QRect(100, 20, 341, 31))
        self.note_Text = QPlainTextEdit(Form)
        self.note_Text.setObjectName(u"note_Text")
        self.note_Text.setGeometry(QRect(100, 80, 541, 191))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 80, 81, 16))
        self.delete_Button = QPushButton(Form)
        self.delete_Button.setObjectName(u"delete_Button")
        self.delete_Button.setGeometry(QRect(460, 280, 75, 24))
        self.newNoteButton = QPushButton(Form)
        self.newNoteButton.setObjectName(u"newNoteButton")
        self.newNoteButton.setGeometry(QRect(550, 280, 88, 24))
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(450, 20, 160, 24))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.dateTimeEdit = QDateTimeEdit(self.widget)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setCalendarPopup(True)

        self.horizontalLayout.addWidget(self.dateTimeEdit)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("Form", u"\u0414\u0430\u0442\u0430 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("Form", u"\u041d\u043e\u0432\u044b\u0439 \u0441\u0442\u043e\u043b\u0431\u0435\u0446", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("Form", u"\u0417\u0430\u043c\u0435\u0442\u043a\u0430", None));
        self.saveButton.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0422\u0435\u043a\u0441\u0442 \u0437\u0430\u043c\u0435\u0442\u043a\u0438", None))
        self.delete_Button.setText(QCoreApplication.translate("Form", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.newNoteButton.setText(QCoreApplication.translate("Form", u"\u041d\u043e\u0432\u0430\u044f \u0437\u0430\u043c\u0435\u0442\u043a\u0430", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u0414\u0435\u0434\u043b\u0430\u0439\u043d", None))
    # retranslateUi

