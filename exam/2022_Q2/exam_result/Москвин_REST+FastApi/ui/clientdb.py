# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'clientdb.ui'
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
        Form.resize(555, 560)
        self.verticalLayout_6 = QVBoxLayout(Form)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout = QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.listWidget = QListWidget(self.tab)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout.addWidget(self.listWidget)

        self.pd_open_file = QPushButton(self.tab)
        self.pd_open_file.setObjectName(u"pd_open_file")

        self.verticalLayout.addWidget(self.pd_open_file)

        self.pd_send_file = QPushButton(self.tab)
        self.pd_send_file.setObjectName(u"pd_send_file")

        self.verticalLayout.addWidget(self.pd_send_file)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_4 = QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.getinfoline = QLineEdit(self.tab_2)
        self.getinfoline.setObjectName(u"getinfoline")

        self.horizontalLayout.addWidget(self.getinfoline)

        self.pb_get_info = QPushButton(self.tab_2)
        self.pb_get_info.setObjectName(u"pb_get_info")

        self.horizontalLayout.addWidget(self.pb_get_info)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.scrollArea = QScrollArea(self.tab_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 98, 89))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tableView = QTableView(self.scrollAreaWidgetContents)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout_3.addWidget(self.tableView)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_4.addWidget(self.scrollArea)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pb_download_all = QPushButton(self.tab_2)
        self.pb_download_all.setObjectName(u"pb_download_all")

        self.horizontalLayout_2.addWidget(self.pb_download_all)

        self.pb_delete = QPushButton(self.tab_2)
        self.pb_delete.setObjectName(u"pb_delete")

        self.horizontalLayout_2.addWidget(self.pb_delete)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_5 = QVBoxLayout(self.tab_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.pb_about = QPushButton(self.tab_3)
        self.pb_about.setObjectName(u"pb_about")

        self.verticalLayout_5.addWidget(self.pb_about)

        self.pb_connect_adress = QPushButton(self.tab_3)
        self.pb_connect_adress.setObjectName(u"pb_connect_adress")

        self.verticalLayout_5.addWidget(self.pb_connect_adress)

        self.tabWidget.addTab(self.tab_3, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.labelUrl = QLabel(Form)
        self.labelUrl.setObjectName(u"labelUrl")
        self.labelUrl.setMargin(0)
        self.labelUrl.setIndent(-1)

        self.horizontalLayout_3.addWidget(self.labelUrl)

        self.horizontalSpacer = QSpacerItem(128, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.statusLabel = QLabel(Form)
        self.statusLabel.setObjectName(u"statusLabel")
        self.statusLabel.setMargin(0)
        self.statusLabel.setIndent(-1)

        self.horizontalLayout_3.addWidget(self.statusLabel)

        self.pb_reconnect = QPushButton(Form)
        self.pb_reconnect.setObjectName(u"pb_reconnect")
        self.pb_reconnect.setMinimumSize(QSize(23, 23))
        self.pb_reconnect.setMaximumSize(QSize(23, 23))

        self.horizontalLayout_3.addWidget(self.pb_reconnect)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.verticalLayout_6.addLayout(self.verticalLayout_2)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"MinIo - DB - Client", None))
        self.pd_open_file.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0444\u0430\u0439\u043b\u044b", None))
        self.pd_send_file.setText(QCoreApplication.translate("Form", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c \u0444\u0430\u0439\u043b\u044b", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c \u0444\u0430\u0439\u043b\u044b", None))
        self.pb_get_info.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u043b\u0443\u0447\u0438\u0442\u044c", None))
        self.pb_download_all.setText(QCoreApplication.translate("Form", u"\u0421\u043a\u0430\u0447\u0430\u0442\u044c \u0432\u0441\u0435", None))
        self.pb_delete.setText(QCoreApplication.translate("Form", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e\u0431 \u043e\u0442\u043f\u0440\u0430\u0432\u043a\u0435", None))
        self.pb_about.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c \u043f\u043e\u0434\u0441\u043a\u0430\u0437\u043a\u0443", None))
        self.pb_connect_adress.setText(QCoreApplication.translate("Form", u"\u0410\u0434\u0440\u0435\u0441 \u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u044f", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Form", u"About", None))
        self.labelUrl.setText(QCoreApplication.translate("Form", u"URL", None))
        self.statusLabel.setText(QCoreApplication.translate("Form", u"Status", None))
        self.pb_reconnect.setText(QCoreApplication.translate("Form", u"\u21ba", None))
    # retranslateUi

