# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'KadrPrikaz_2.ui'
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
        Form.resize(700, 706)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(700, 500))
        Form.setMaximumSize(QSize(1200, 800))
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        font = QFont()
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setIconSize(QSize(25, 25))
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab1 = QWidget()
        self.tab1.setObjectName(u"tab1")
        self.verticalLayout_3 = QVBoxLayout(self.tab1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox = QGroupBox(self.tab1)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFont(font)
        self.verticalLayout_5 = QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.tableView = QTableView(self.groupBox)
        self.tableView.setObjectName(u"tableView")

        self.horizontalLayout_5.addWidget(self.tableView)

        self.pushButton_3 = QPushButton(self.groupBox)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_5.addWidget(self.pushButton_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.pushButton_2 = QPushButton(self.groupBox)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_4.addWidget(self.pushButton_2)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.tab1)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFont(font)
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.radioButton = QRadioButton(self.groupBox_2)
        self.radioButton.setObjectName(u"radioButton")
        font1 = QFont()
        font1.setPointSize(10)
        self.radioButton.setFont(font1)

        self.verticalLayout_2.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.groupBox_2)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setFont(font1)

        self.verticalLayout_2.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.groupBox_2)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setFont(font1)

        self.verticalLayout_2.addWidget(self.radioButton_3)

        self.radioButton_4 = QRadioButton(self.groupBox_2)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setFont(font1)

        self.verticalLayout_2.addWidget(self.radioButton_4)


        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(80, 0))
        self.label_3.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.lineEdit_3 = QLineEdit(self.groupBox_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy1)
        self.lineEdit_3.setMaximumSize(QSize(1111111, 25))

        self.horizontalLayout_2.addWidget(self.lineEdit_3)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.lineEdit_2 = QLineEdit(self.groupBox_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy1.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy1)
        self.lineEdit_2.setMaximumSize(QSize(10000000, 25))

        self.horizontalLayout_3.addWidget(self.lineEdit_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.pushButton = QPushButton(self.groupBox_2)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)


        self.horizontalLayout_4.addLayout(self.verticalLayout)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.tabWidget.addTab(self.tab1, "")
        self.tab2 = QWidget()
        self.tab2.setObjectName(u"tab2")
        self.verticalLayout_6 = QVBoxLayout(self.tab2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.tableView_2 = QTableView(self.tab2)
        self.tableView_2.setObjectName(u"tableView_2")

        self.verticalLayout_6.addWidget(self.tableView_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pushButton_4 = QPushButton(self.tab2)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_6.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.tab2)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout_6.addWidget(self.pushButton_5)


        self.verticalLayout_6.addLayout(self.horizontalLayout_6)

        self.tabWidget.addTab(self.tab2, "")
        self.tab3 = QWidget()
        self.tab3.setObjectName(u"tab3")
        self.verticalLayout_7 = QVBoxLayout(self.tab3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.tableView_3 = QTableView(self.tab3)
        self.tableView_3.setObjectName(u"tableView_3")

        self.verticalLayout_7.addWidget(self.tableView_3)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButton_6 = QPushButton(self.tab3)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.horizontalLayout_7.addWidget(self.pushButton_6)


        self.verticalLayout_7.addLayout(self.horizontalLayout_7)

        self.tabWidget.addTab(self.tab3, "")
        self.tab4 = QWidget()
        self.tab4.setObjectName(u"tab4")
        self.verticalLayout_8 = QVBoxLayout(self.tab4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.tableView_4 = QTableView(self.tab4)
        self.tableView_4.setObjectName(u"tableView_4")

        self.verticalLayout_8.addWidget(self.tableView_4)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.pushButton_7 = QPushButton(self.tab4)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.horizontalLayout_9.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(self.tab4)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.horizontalLayout_9.addWidget(self.pushButton_8)


        self.verticalLayout_8.addLayout(self.horizontalLayout_9)

        self.tabWidget.addTab(self.tab4, "")

        self.horizontalLayout.addWidget(self.tabWidget)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u041f\u0440\u0438\u043a\u0430\u0437\u044b \u0432 \u0431\u0430\u0437\u0435", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u043f\u0440\u0438\u043a\u0430\u0437", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0432\u0441\u0435 \u043f\u0440\u0438\u043a\u0430\u0437\u044b", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"\u0412\u043d\u0435\u0441\u0435\u043d\u0438\u0435 \u043f\u0440\u0438\u043a\u0430\u0437\u043e\u0432", None))
        self.radioButton.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u0447\u0438\u0441\u043b\u0435\u043d\u0438\u0435 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430", None))
        self.radioButton_2.setText(QCoreApplication.translate("Form", u"\u0423\u0432\u043e\u043b\u044c\u043d\u0435\u043d\u0438\u0435 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430", None))
        self.radioButton_3.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0430 \u043d\u0430 \u0434\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c", None))
        self.radioButton_4.setText(QCoreApplication.translate("Form", u"\u0421\u043d\u044f\u0442\u0438\u0435 \u0441 \u0434\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u0438", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u2116 \u0432\u043d\u043e\u0441\u0438\u043c\u043e\u0433\u043e \u043f\u0440\u0438\u043a\u0430\u0437\u0430", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u043e\u043c\u0435\u0440 \u043f\u0440\u0438\u043a\u0430\u0437\u0430 \u0434\u043e 7 \u0441\u0438\u043c\u0432\u043e\u043b\u043e\u0432 \u0432\u043a\u043b\u044e\u0447\u0438\u0442\u0435\u043b\u044c\u043d\u043e", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f \u043f\u043e\u0434\u043f\u0438\u0441\u0430\u0432\u0448\u0435\u0433\u043e", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Form", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f \u0434\u043e 20 \u0441\u0438\u043c\u0432\u043e\u043b\u043e\u0432", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u0412\u043d\u0435\u0441\u0442\u0438 \u043f\u0440\u0438\u043a\u0430\u0437", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), QCoreApplication.translate("Form", u"\u041f\u0440\u0438\u043a\u0430\u0437\u044b", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), QCoreApplication.translate("Form", u"\u0421\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0438", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u0441\u0442\u0430\u0432\u0438\u0442\u044c \u043d\u0430 \u0434\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3), QCoreApplication.translate("Form", u"\u041f\u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0430 \u043d\u0430 \u0434\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0440\u0430\u0441\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0443", None))
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0440\u0430\u0441\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0443", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab4), QCoreApplication.translate("Form", u"\u0420\u0430\u0441\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0430 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u043e\u0432", None))
    # retranslateUi

