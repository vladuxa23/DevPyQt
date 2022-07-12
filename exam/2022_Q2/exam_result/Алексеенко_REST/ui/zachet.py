# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'zachet.ui'
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
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTabWidget,
    QTableView, QTextEdit, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(606, 535)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButtonLogin = QPushButton(Form)
        self.pushButtonLogin.setObjectName(u"pushButtonLogin")
        self.pushButtonLogin.setMinimumSize(QSize(120, 24))

        self.horizontalLayout_7.addWidget(self.pushButtonLogin)

        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(90, 24))
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_7)

        self.label_user = QLabel(Form)
        self.label_user.setObjectName(u"label_user")

        self.horizontalLayout_7.addWidget(self.label_user)

        self.pushButtonLogOut = QPushButton(Form)
        self.pushButtonLogOut.setObjectName(u"pushButtonLogOut")
        self.pushButtonLogOut.setMinimumSize(QSize(120, 24))

        self.horizontalLayout_7.addWidget(self.pushButtonLogOut)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableView = QTableView(self.tab)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout.addWidget(self.tableView)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.pushButtonGet = QPushButton(self.tab)
        self.pushButtonGet.setObjectName(u"pushButtonGet")
        self.pushButtonGet.setMinimumSize(QSize(160, 24))

        self.horizontalLayout_8.addWidget(self.pushButtonGet)

        self.pushButtonDetails = QPushButton(self.tab)
        self.pushButtonDetails.setObjectName(u"pushButtonDetails")
        self.pushButtonDetails.setMinimumSize(QSize(140, 24))

        self.horizontalLayout_8.addWidget(self.pushButtonDetails)

        self.pushButtonPut = QPushButton(self.tab)
        self.pushButtonPut.setObjectName(u"pushButtonPut")
        self.pushButtonPut.setMinimumSize(QSize(80, 24))

        self.horizontalLayout_8.addWidget(self.pushButtonPut)

        self.pushButtonDelete = QPushButton(self.tab)
        self.pushButtonDelete.setObjectName(u"pushButtonDelete")
        self.pushButtonDelete.setMinimumSize(QSize(90, 24))

        self.horizontalLayout_8.addWidget(self.pushButtonDelete)


        self.verticalLayout.addLayout(self.horizontalLayout_8)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_2 = QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.tab_2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(100, 22))
        self.label.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.tab_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(120, 22))

        self.horizontalLayout.addWidget(self.lineEdit)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.tab_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(100, 22))
        self.label_2.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.textEdit = QTextEdit(self.tab_2)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_2.addWidget(self.textEdit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.tab_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(100, 22))
        self.label_3.setMaximumSize(QSize(80, 16777215))
        self.label_3.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.label_3.setLayoutDirection(Qt.LeftToRight)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.checkBox = QCheckBox(self.tab_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setMinimumSize(QSize(120, 22))

        self.horizontalLayout_3.addWidget(self.checkBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.tab_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(100, 22))
        self.label_4.setMaximumSize(QSize(80, 16777215))
        self.label_4.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.label_4.setLayoutDirection(Qt.LeftToRight)
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.checkBox_2 = QCheckBox(self.tab_2)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setMinimumSize(QSize(120, 22))

        self.horizontalLayout_4.addWidget(self.checkBox_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.tab_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(100, 22))
        self.label_5.setMaximumSize(QSize(80, 16777215))
        self.label_5.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.label_5.setLayoutDirection(Qt.LeftToRight)
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_5)

        self.comboBox = QComboBox(self.tab_2)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(120, 22))

        self.horizontalLayout_5.addWidget(self.comboBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(self.tab_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(100, 22))
        self.label_6.setMaximumSize(QSize(80, 16777215))
        self.label_6.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.label_6.setLayoutDirection(Qt.LeftToRight)
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_6)

        self.dateTimeEdit = QDateTimeEdit(self.tab_2)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setMinimumSize(QSize(120, 22))
        self.dateTimeEdit.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.dateTimeEdit.setCurrentSection(QDateTimeEdit.YearSection)
        self.dateTimeEdit.setCalendarPopup(True)
        self.dateTimeEdit.setTimeSpec(Qt.UTC)

        self.horizontalLayout_6.addWidget(self.dateTimeEdit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.create_todo = QPushButton(self.tab_2)
        self.create_todo.setObjectName(u"create_todo")

        self.verticalLayout_2.addWidget(self.create_todo)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tabWidget.addTab(self.tab_4, "")

        self.verticalLayout_3.addWidget(self.tabWidget)


        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButtonLogin.setText(QCoreApplication.translate("Form", u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u043e\u0432\u0430\u0442\u044c\u0441\u044f", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c: ", None))
        self.label_user.setText("")
        self.pushButtonLogOut.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0439\u0442\u0438 \u0438\u0437 \u0430\u043a\u043a\u0430\u0443\u043d\u0442\u0430", None))
        self.pushButtonGet.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u043b\u0443\u0447\u0438\u0442\u044c \u0441\u043f\u0438\u0441\u043e\u043a \u0432\u0441\u0435\u0445 \u0434\u0435\u043b", None))
        self.pushButtonDetails.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u043f\u043e\u0434\u0440\u043e\u0431\u043d\u043e\u0441\u0442\u0438", None))
        self.pushButtonPut.setText(QCoreApplication.translate("Form", u"\u0412\u043d\u0435\u0441\u0442\u0438 \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f \u0432 \u0434\u0435\u043b\u043e", None))
        self.pushButtonDelete.setText(QCoreApplication.translate("Form", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0434\u0435\u043b\u043e", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0432\u0441\u0435\u0445 \u0434\u0435\u043b", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0422\u0435\u043a\u0441\u0442 \u0437\u0430\u0434\u0430\u043d\u0438\u044f", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u041f\u0443\u0431\u043b\u0438\u0447\u043d\u0430\u044f", None))
        self.checkBox.setText("")
        self.label_4.setText(QCoreApplication.translate("Form", u"\u0412\u0430\u0436\u043d\u0430\u044f", None))
        self.checkBox_2.setText("")
        self.label_5.setText(QCoreApplication.translate("Form", u"\u0421\u0442\u0430\u0442\u0443\u0441", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u0421\u0440\u043e\u043a \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f", None))
        self.create_todo.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0434\u0435\u043b\u043e", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("Form", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
    # retranslateUi

