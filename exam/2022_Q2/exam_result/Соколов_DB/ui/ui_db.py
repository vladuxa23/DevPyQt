# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'db.ui'
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
        MainWindow.resize(864, 659)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(840, 540))
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(120, 20))
        self.label.setMaximumSize(QSize(120, 20))
        self.label.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit_topic = QLineEdit(self.groupBox)
        self.lineEdit_topic.setObjectName(u"lineEdit_topic")

        self.horizontalLayout.addWidget(self.lineEdit_topic)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(120, 20))
        self.label_2.setMaximumSize(QSize(120, 20))

        self.horizontalLayout_2.addWidget(self.label_2)

        self.textEdit = QTextEdit(self.groupBox)
        self.textEdit.setObjectName(u"textEdit")

        self.horizontalLayout_2.addWidget(self.textEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(120, 20))
        self.label_3.setMaximumSize(QSize(120, 20))

        self.horizontalLayout_3.addWidget(self.label_3)

        self.comboBox_status = QComboBox(self.groupBox)
        self.comboBox_status.setObjectName(u"comboBox_status")

        self.horizontalLayout_3.addWidget(self.comboBox_status)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(120, 20))
        self.label_4.setMaximumSize(QSize(120, 20))

        self.horizontalLayout_4.addWidget(self.label_4)

        self.checkBox_importance = QCheckBox(self.groupBox)
        self.checkBox_importance.setObjectName(u"checkBox_importance")

        self.horizontalLayout_4.addWidget(self.checkBox_importance)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(120, 20))
        self.label_5.setMaximumSize(QSize(120, 20))

        self.horizontalLayout_5.addWidget(self.label_5)

        self.checkBox_publish = QCheckBox(self.groupBox)
        self.checkBox_publish.setObjectName(u"checkBox_publish")

        self.horizontalLayout_5.addWidget(self.checkBox_publish)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(120, 20))
        self.label_8.setMaximumSize(QSize(120, 20))

        self.horizontalLayout_8.addWidget(self.label_8)

        self.lineEdit_author = QLineEdit(self.groupBox)
        self.lineEdit_author.setObjectName(u"lineEdit_author")
        self.lineEdit_author.setEnabled(True)
        self.lineEdit_author.setReadOnly(True)

        self.horizontalLayout_8.addWidget(self.lineEdit_author)


        self.verticalLayout.addLayout(self.horizontalLayout_8)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.tableView = QTableView(self.groupBox)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout_2.addWidget(self.tableView)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.pushButtonADD = QPushButton(self.groupBox)
        self.pushButtonADD.setObjectName(u"pushButtonADD")
        self.pushButtonADD.setMinimumSize(QSize(200, 30))
        self.pushButtonADD.setMaximumSize(QSize(200, 30))
        self.pushButtonADD.setMouseTracking(True)
        self.pushButtonADD.setFlat(False)

        self.horizontalLayout_9.addWidget(self.pushButtonADD)

        self.pushButtonDEL = QPushButton(self.groupBox)
        self.pushButtonDEL.setObjectName(u"pushButtonDEL")
        self.pushButtonDEL.setMinimumSize(QSize(200, 30))
        self.pushButtonDEL.setMaximumSize(QSize(200, 30))
        self.pushButtonDEL.setMouseTracking(True)

        self.horizontalLayout_9.addWidget(self.pushButtonDEL)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 864, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043c\u0435\u0442\u043a\u0438 \u0434\u043b\u044f \u0432\u0435\u0434\u0435\u043d\u0438\u044f \u0441\u043f\u0438\u0441\u043a\u0430 \u0434\u0435\u043b", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0441\u0442 \u0437\u0430\u043c\u0435\u0442\u043a\u0438", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0443\u0441", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0430\u0436\u043d\u043e", None))
        self.checkBox_importance.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0443\u0431\u043b\u0438\u043a\u043e\u0432\u0430\u0442\u044c", None))
        self.checkBox_publish.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u0440", None))
        self.pushButtonADD.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.pushButtonDEL.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
    # retranslateUi

