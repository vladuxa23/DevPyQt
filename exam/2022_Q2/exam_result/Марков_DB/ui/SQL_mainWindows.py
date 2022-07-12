# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SQL_mainWindows.ui'
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
        MainWindow.resize(945, 617)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(690, 483))
        icon = QIcon()
        icon.addFile(u":/res/icons/database.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.exit_action = QAction(MainWindow)
        self.exit_action.setObjectName(u"exit_action")
        self.about_action = QAction(MainWindow)
        self.about_action.setObjectName(u"about_action")
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.horizontalLayout_4 = QHBoxLayout(self.centralWidget)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox_sql_drivers = QGroupBox(self.centralWidget)
        self.groupBox_sql_drivers.setObjectName(u"groupBox_sql_drivers")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_sql_drivers.sizePolicy().hasHeightForWidth())
        self.groupBox_sql_drivers.setSizePolicy(sizePolicy1)
        self.groupBox_sql_drivers.setMinimumSize(QSize(250, 45))
        self.label_qodbc_icon = QLabel(self.groupBox_sql_drivers)
        self.label_qodbc_icon.setObjectName(u"label_qodbc_icon")
        self.label_qodbc_icon.setGeometry(QRect(20, 23, 13, 13))
        self.label_8 = QLabel(self.groupBox_sql_drivers)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(40, 22, 65, 13))

        self.verticalLayout_2.addWidget(self.groupBox_sql_drivers)

        self.groupBox_sql_connect = QGroupBox(self.centralWidget)
        self.groupBox_sql_connect.setObjectName(u"groupBox_sql_connect")
        sizePolicy1.setHeightForWidth(self.groupBox_sql_connect.sizePolicy().hasHeightForWidth())
        self.groupBox_sql_connect.setSizePolicy(sizePolicy1)
        self.groupBox_sql_connect.setMinimumSize(QSize(250, 390))
        font = QFont()
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_sql_connect.setFont(font)
        self.groupBox_sql_connect.setFlat(False)
        self.groupBox_sql_connect.setCheckable(False)
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_sql_connect)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox_engine = QGroupBox(self.groupBox_sql_connect)
        self.groupBox_engine.setObjectName(u"groupBox_engine")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_engine)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.radio_mssql = QRadioButton(self.groupBox_engine)
        self.radio_mssql.setObjectName(u"radio_mssql")
        self.radio_mssql.setChecked(True)

        self.horizontalLayout_8.addWidget(self.radio_mssql)


        self.verticalLayout_5.addLayout(self.horizontalLayout_8)


        self.verticalLayout_4.addWidget(self.groupBox_engine)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_9 = QLabel(self.groupBox_sql_connect)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(67, 16777215))

        self.horizontalLayout_3.addWidget(self.label_9)

        self.lineEdit_driver = QLineEdit(self.groupBox_sql_connect)
        self.lineEdit_driver.setObjectName(u"lineEdit_driver")
        self.lineEdit_driver.setMaximumSize(QSize(150, 16777215))
        self.lineEdit_driver.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.lineEdit_driver)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(self.groupBox_sql_connect)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(67, 16777215))

        self.horizontalLayout_5.addWidget(self.label_3)

        self.lineEdit_server_address = QLineEdit(self.groupBox_sql_connect)
        self.lineEdit_server_address.setObjectName(u"lineEdit_server_address")
        self.lineEdit_server_address.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_5.addWidget(self.lineEdit_server_address)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(self.groupBox_sql_connect)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(67, 16777215))

        self.horizontalLayout_6.addWidget(self.label_6)

        self.spinBox_server_port = QSpinBox(self.groupBox_sql_connect)
        self.spinBox_server_port.setObjectName(u"spinBox_server_port")
        self.spinBox_server_port.setMinimumSize(QSize(0, 0))
        self.spinBox_server_port.setMaximumSize(QSize(150, 16777215))
        self.spinBox_server_port.setBaseSize(QSize(0, 0))
        self.spinBox_server_port.setMaximum(65535)
        self.spinBox_server_port.setValue(0)

        self.horizontalLayout_6.addWidget(self.spinBox_server_port)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_4 = QLabel(self.groupBox_sql_connect)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(67, 16777215))

        self.horizontalLayout_7.addWidget(self.label_4)

        self.lineEdit_database_name = QLineEdit(self.groupBox_sql_connect)
        self.lineEdit_database_name.setObjectName(u"lineEdit_database_name")
        self.lineEdit_database_name.setMinimumSize(QSize(0, 0))
        self.lineEdit_database_name.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_7.addWidget(self.lineEdit_database_name)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.groupBox_authentication = QGroupBox(self.groupBox_sql_connect)
        self.groupBox_authentication.setObjectName(u"groupBox_authentication")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_authentication)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.radio_windows_authentication = QRadioButton(self.groupBox_authentication)
        self.radio_windows_authentication.setObjectName(u"radio_windows_authentication")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.radio_windows_authentication.sizePolicy().hasHeightForWidth())
        self.radio_windows_authentication.setSizePolicy(sizePolicy2)
        self.radio_windows_authentication.setChecked(True)

        self.verticalLayout.addWidget(self.radio_windows_authentication)

        self.radio_sql_authentication = QRadioButton(self.groupBox_authentication)
        self.radio_sql_authentication.setObjectName(u"radio_sql_authentication")
        sizePolicy2.setHeightForWidth(self.radio_sql_authentication.sizePolicy().hasHeightForWidth())
        self.radio_sql_authentication.setSizePolicy(sizePolicy2)
        self.radio_sql_authentication.setChecked(False)

        self.verticalLayout.addWidget(self.radio_sql_authentication)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.groupBox_authentication)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(67, 16777215))

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit_login = QLineEdit(self.groupBox_authentication)
        self.lineEdit_login.setObjectName(u"lineEdit_login")
        self.lineEdit_login.setEnabled(False)
        self.lineEdit_login.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout.addWidget(self.lineEdit_login)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.groupBox_authentication)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(67, 16777215))

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit_password = QLineEdit(self.groupBox_authentication)
        self.lineEdit_password.setObjectName(u"lineEdit_password")
        self.lineEdit_password.setEnabled(False)
        self.lineEdit_password.setMaximumSize(QSize(150, 16777215))
        self.lineEdit_password.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_2.addWidget(self.lineEdit_password)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.verticalLayout_4.addWidget(self.groupBox_authentication)

        self.button_connect = QPushButton(self.groupBox_sql_connect)
        self.button_connect.setObjectName(u"button_connect")
        self.button_connect.setAutoDefault(True)

        self.verticalLayout_4.addWidget(self.button_connect)


        self.verticalLayout_2.addWidget(self.groupBox_sql_connect)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.groupBox_database_browser = QGroupBox(self.centralWidget)
        self.groupBox_database_browser.setObjectName(u"groupBox_database_browser")
        self.groupBox_database_browser.setEnabled(False)
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.groupBox_database_browser.sizePolicy().hasHeightForWidth())
        self.groupBox_database_browser.setSizePolicy(sizePolicy3)
        self.groupBox_database_browser.setMinimumSize(QSize(300, 300))
        self.gridLayout_2 = QGridLayout(self.groupBox_database_browser)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 3, 1, 1)

        self.comboBox_table_name = QComboBox(self.groupBox_database_browser)
        self.comboBox_table_name.setObjectName(u"comboBox_table_name")
        sizePolicy1.setHeightForWidth(self.comboBox_table_name.sizePolicy().hasHeightForWidth())
        self.comboBox_table_name.setSizePolicy(sizePolicy1)
        self.comboBox_table_name.setMinimumSize(QSize(130, 0))
        self.comboBox_table_name.setSizeIncrement(QSize(130, 0))

        self.gridLayout_2.addWidget(self.comboBox_table_name, 0, 1, 1, 1)

        self.button_show_table = QPushButton(self.groupBox_database_browser)
        self.button_show_table.setObjectName(u"button_show_table")
        self.button_show_table.setAutoDefault(True)

        self.gridLayout_2.addWidget(self.button_show_table, 0, 2, 1, 1)

        self.label_5 = QLabel(self.groupBox_database_browser)
        self.label_5.setObjectName(u"label_5")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy4)

        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)

        self.tableView_database_table = QTableView(self.groupBox_database_browser)
        self.tableView_database_table.setObjectName(u"tableView_database_table")
        sizePolicy4.setHeightForWidth(self.tableView_database_table.sizePolicy().hasHeightForWidth())
        self.tableView_database_table.setSizePolicy(sizePolicy4)
        self.tableView_database_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableView_database_table.setTabKeyNavigation(False)
        self.tableView_database_table.setDragDropOverwriteMode(False)
        self.tableView_database_table.setSortingEnabled(True)
        self.tableView_database_table.horizontalHeader().setProperty("showSortIndicator", False)

        self.gridLayout_2.addWidget(self.tableView_database_table, 1, 0, 1, 4)


        self.horizontalLayout_4.addWidget(self.groupBox_database_browser)

        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 945, 21))
        self.menu = QMenu(self.menuBar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menuBar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menuBar)
        QWidget.setTabOrder(self.radio_mssql, self.lineEdit_driver)
        QWidget.setTabOrder(self.lineEdit_driver, self.lineEdit_server_address)
        QWidget.setTabOrder(self.lineEdit_server_address, self.spinBox_server_port)
        QWidget.setTabOrder(self.spinBox_server_port, self.radio_sql_authentication)
        QWidget.setTabOrder(self.radio_sql_authentication, self.lineEdit_login)
        QWidget.setTabOrder(self.lineEdit_login, self.lineEdit_password)
        QWidget.setTabOrder(self.lineEdit_password, self.radio_windows_authentication)
        QWidget.setTabOrder(self.radio_windows_authentication, self.lineEdit_database_name)
        QWidget.setTabOrder(self.lineEdit_database_name, self.button_connect)
        QWidget.setTabOrder(self.button_connect, self.comboBox_table_name)
        QWidget.setTabOrder(self.comboBox_table_name, self.button_show_table)
        QWidget.setTabOrder(self.button_show_table, self.tableView_database_table)

        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.exit_action)
        self.menu_2.addAction(self.about_action)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0412\u043d\u0435\u0448\u043d\u0438\u0439 SQL \u043e\u0431\u043e\u0437\u0440\u0435\u0432\u0430\u0442\u0435\u043b\u044c", None))
        self.exit_action.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.about_action.setText(QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.groupBox_sql_drivers.setTitle(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u043b\u0435\u043d\u043d\u044b\u0439 SQL \u0434\u0440\u0430\u0439\u0432\u0435\u0440", None))
        self.label_qodbc_icon.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"PYODBC", None))
        self.groupBox_sql_connect.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0435 \u043a \u0441\u0435\u0440\u0432\u0435\u0440\u0443", None))
        self.groupBox_engine.setTitle(QCoreApplication.translate("MainWindow", u"\u0414\u0432\u0438\u0436\u043e\u043a", None))
        self.radio_mssql.setText(QCoreApplication.translate("MainWindow", u"MSSQL", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0440\u0430\u0439\u0432\u0435\u0440:", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_driver.setToolTip(QCoreApplication.translate("MainWindow", u"For ODBC/MSSQL: \"SQL Server\" (Windows), \"ODBC Driver 13 for SQL Server\" (unix), etc.", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_driver.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f \u0441\u0435\u0440\u0432\u0435\u0440\u0430:", None))
        self.lineEdit_server_address.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440 \u043f\u043e\u0440\u0442\u0430:", None))
#if QT_CONFIG(tooltip)
        self.spinBox_server_port.setToolTip(QCoreApplication.translate("MainWindow", u"Default: MySQL 3306; MSSQL 1433", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f \u0411\u0414:", None))
        self.lineEdit_database_name.setText("")
        self.groupBox_authentication.setTitle(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f \u0430\u0443\u0442\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u0438", None))
        self.radio_windows_authentication.setText(QCoreApplication.translate("MainWindow", u"Windows authentication", None))
        self.radio_sql_authentication.setText(QCoreApplication.translate("MainWindow", u"SQL Server authentication", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u0438\u043d:", None))
        self.lineEdit_login.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c:", None))
        self.lineEdit_password.setText("")
        self.button_connect.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0438\u0442\u044c\u0441\u044f", None))
        self.groupBox_database_browser.setTitle(QCoreApplication.translate("MainWindow", u"\u0411\u0414 \u043e\u0431\u043e\u0437\u0440\u0435\u0432\u0430\u0442\u0435\u043b\u044c", None))
        self.button_show_table.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0430\u0431\u043b\u0438\u0446\u0430", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"?", None))
    # retranslateUi

