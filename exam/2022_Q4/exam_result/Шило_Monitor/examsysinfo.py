# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'examsysinfo.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QProgressBar, QScrollArea,
    QSizePolicy, QSpacerItem, QTabWidget, QTableWidget,
    QTableWidgetItem, QTextEdit, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(620, 660)
        Form.setMinimumSize(QSize(620, 660))
        Form.setMaximumSize(QSize(620, 660))
        self.horizontalLayout_7 = QHBoxLayout(Form)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(600, 620))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 240, 570, 180))
        self.groupBox.setMinimumSize(QSize(570, 150))
        font = QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.layoutWidget = QWidget(self.groupBox)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(438, 30, 122, 140))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.progressBar_mem = QProgressBar(self.layoutWidget)
        self.progressBar_mem.setObjectName(u"progressBar_mem")
        self.progressBar_mem.setMinimumSize(QSize(120, 50))
        self.progressBar_mem.setValue(24)
        self.progressBar_mem.setOrientation(Qt.Vertical)

        self.verticalLayout.addWidget(self.progressBar_mem)

        self.label_9 = QLabel(self.layoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(120, 0))
        font1 = QFont()
        font1.setPointSize(9)
        self.label_9.setFont(font1)

        self.verticalLayout.addWidget(self.label_9)

        self.layoutWidget1 = QWidget(self.groupBox)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 30, 410, 132))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_7 = QLabel(self.layoutWidget1)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(200, 0))
        self.label_7.setMaximumSize(QSize(200, 50))
        self.label_7.setFont(font1)

        self.horizontalLayout_6.addWidget(self.label_7)

        self.textEdit_mem_1 = QTextEdit(self.layoutWidget1)
        self.textEdit_mem_1.setObjectName(u"textEdit_mem_1")
        self.textEdit_mem_1.setMinimumSize(QSize(200, 26))
        self.textEdit_mem_1.setMaximumSize(QSize(200, 25))
        self.textEdit_mem_1.setFont(font1)

        self.horizontalLayout_6.addWidget(self.textEdit_mem_1)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_8 = QLabel(self.layoutWidget1)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(200, 0))
        self.label_8.setMaximumSize(QSize(200, 50))
        self.label_8.setFont(font1)

        self.horizontalLayout_5.addWidget(self.label_8)

        self.textEdit_mem_2 = QTextEdit(self.layoutWidget1)
        self.textEdit_mem_2.setObjectName(u"textEdit_mem_2")
        self.textEdit_mem_2.setMinimumSize(QSize(200, 26))
        self.textEdit_mem_2.setMaximumSize(QSize(200, 26))
        self.textEdit_mem_2.setFont(font1)

        self.horizontalLayout_5.addWidget(self.textEdit_mem_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_11 = QLabel(self.layoutWidget1)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(200, 0))
        self.label_11.setMaximumSize(QSize(200, 50))
        self.label_11.setFont(font1)

        self.horizontalLayout_4.addWidget(self.label_11)

        self.textEdit_mem_3 = QTextEdit(self.layoutWidget1)
        self.textEdit_mem_3.setObjectName(u"textEdit_mem_3")
        self.textEdit_mem_3.setMinimumSize(QSize(200, 26))
        self.textEdit_mem_3.setMaximumSize(QSize(200, 26))
        self.textEdit_mem_3.setFont(font1)

        self.horizontalLayout_4.addWidget(self.textEdit_mem_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_13 = QLabel(self.layoutWidget1)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(200, 0))
        self.label_13.setMaximumSize(QSize(200, 50))
        self.label_13.setFont(font1)

        self.horizontalLayout_14.addWidget(self.label_13)

        self.textEdit_mem_4 = QTextEdit(self.layoutWidget1)
        self.textEdit_mem_4.setObjectName(u"textEdit_mem_4")
        self.textEdit_mem_4.setMinimumSize(QSize(200, 26))
        self.textEdit_mem_4.setMaximumSize(QSize(200, 26))
        self.textEdit_mem_4.setFont(font1)

        self.horizontalLayout_14.addWidget(self.textEdit_mem_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_14)

        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 50, 570, 180))
        self.groupBox_2.setMinimumSize(QSize(570, 150))
        self.groupBox_2.setFont(font)
        self.layoutWidget2 = QWidget(self.groupBox_2)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(440, 20, 122, 140))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.progressBar_proc = QProgressBar(self.layoutWidget2)
        self.progressBar_proc.setObjectName(u"progressBar_proc")
        self.progressBar_proc.setMinimumSize(QSize(120, 50))
        self.progressBar_proc.setValue(24)
        self.progressBar_proc.setOrientation(Qt.Vertical)

        self.verticalLayout_2.addWidget(self.progressBar_proc)

        self.label_5 = QLabel(self.layoutWidget2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(120, 0))
        self.label_5.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_5)

        self.layoutWidget3 = QWidget(self.groupBox_2)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(10, 31, 410, 122))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.layoutWidget3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(200, 0))
        self.label_3.setMaximumSize(QSize(200, 50))
        self.label_3.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.textEdit_proc_name = QTextEdit(self.layoutWidget3)
        self.textEdit_proc_name.setObjectName(u"textEdit_proc_name")
        self.textEdit_proc_name.setMinimumSize(QSize(200, 50))
        self.textEdit_proc_name.setMaximumSize(QSize(200, 50))
        self.textEdit_proc_name.setFont(font1)

        self.horizontalLayout_2.addWidget(self.textEdit_proc_name)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_4 = QLabel(self.layoutWidget3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(200, 0))
        self.label_4.setMaximumSize(QSize(200, 50))
        self.label_4.setFont(font1)

        self.horizontalLayout_13.addWidget(self.label_4)

        self.textEdit_proc_core = QTextEdit(self.layoutWidget3)
        self.textEdit_proc_core.setObjectName(u"textEdit_proc_core")
        self.textEdit_proc_core.setMinimumSize(QSize(200, 26))
        self.textEdit_proc_core.setMaximumSize(QSize(200, 26))
        self.textEdit_proc_core.setFont(font1)

        self.horizontalLayout_13.addWidget(self.textEdit_proc_core)


        self.verticalLayout_4.addLayout(self.horizontalLayout_13)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_12 = QLabel(self.layoutWidget3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(200, 0))
        self.label_12.setMaximumSize(QSize(200, 50))
        self.label_12.setFont(font1)

        self.horizontalLayout.addWidget(self.label_12)

        self.textEdit_proc_core_2 = QTextEdit(self.layoutWidget3)
        self.textEdit_proc_core_2.setObjectName(u"textEdit_proc_core_2")
        self.textEdit_proc_core_2.setMinimumSize(QSize(200, 26))
        self.textEdit_proc_core_2.setMaximumSize(QSize(200, 26))
        self.textEdit_proc_core_2.setFont(font1)

        self.horizontalLayout.addWidget(self.textEdit_proc_core_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.groupBox_3 = QGroupBox(self.tab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 420, 570, 152))
        self.groupBox_3.setMinimumSize(QSize(570, 150))
        self.groupBox_3.setFont(font)
        self.horizontalLayout_9 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.groupBox_4 = QGroupBox(self.groupBox_3)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMinimumSize(QSize(150, 110))
        self.groupBox_4.setFont(font1)
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.textEdit_HDD = QTextEdit(self.groupBox_4)
        self.textEdit_HDD.setObjectName(u"textEdit_HDD")

        self.verticalLayout_5.addWidget(self.textEdit_HDD)


        self.horizontalLayout_8.addWidget(self.groupBox_4)

        self.groupBox_6 = QGroupBox(self.groupBox_3)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setMinimumSize(QSize(150, 110))
        self.groupBox_6.setFont(font1)
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.textEdit_HDD2 = QTextEdit(self.groupBox_6)
        self.textEdit_HDD2.setObjectName(u"textEdit_HDD2")

        self.verticalLayout_7.addWidget(self.textEdit_HDD2)


        self.horizontalLayout_8.addWidget(self.groupBox_6)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_8)

        self.layoutWidget4 = QWidget(self.tab)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(14, 12, 563, 28))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget4)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(170, 0))

        self.horizontalLayout_3.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(310, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.comboBox = QComboBox(self.layoutWidget4)
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_3.addWidget(self.comboBox)

        self.tabWidget.addTab(self.tab, "")
        self.Process = QWidget()
        self.Process.setObjectName(u"Process")
        self.verticalLayout_8 = QVBoxLayout(self.Process)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_2 = QLabel(self.Process)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(170, 0))

        self.verticalLayout_8.addWidget(self.label_2)

        self.scrollArea = QScrollArea(self.Process)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 576, 561))
        self.horizontalLayout_10 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.table_proc = QTableWidget(self.scrollAreaWidgetContents)
        self.table_proc.setObjectName(u"table_proc")
        self.table_proc.setFont(font1)

        self.horizontalLayout_10.addWidget(self.table_proc)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_8.addWidget(self.scrollArea)

        self.tabWidget.addTab(self.Process, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_6 = QVBoxLayout(self.tab_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_6 = QLabel(self.tab_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(170, 0))

        self.verticalLayout_6.addWidget(self.label_6)

        self.scrollArea_2 = QScrollArea(self.tab_3)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 576, 561))
        self.horizontalLayout_11 = QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.table_service = QTableWidget(self.scrollAreaWidgetContents_2)
        self.table_service.setObjectName(u"table_service")
        self.table_service.setFont(font1)

        self.horizontalLayout_11.addWidget(self.table_service)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_6.addWidget(self.scrollArea_2)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayout_12 = QHBoxLayout(self.tab_2)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_10 = QLabel(self.tab_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(170, 0))

        self.verticalLayout_10.addWidget(self.label_10)

        self.scrollArea_3 = QScrollArea(self.tab_2)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 574, 559))
        self.horizontalLayout_15 = QHBoxLayout(self.scrollAreaWidgetContents_3)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.table_sched = QTableWidget(self.scrollAreaWidgetContents_3)
        self.table_sched.setObjectName(u"table_sched")
        self.table_sched.setFont(font1)

        self.horizontalLayout_15.addWidget(self.table_sched)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_10.addWidget(self.scrollArea_3)


        self.horizontalLayout_12.addLayout(self.verticalLayout_10)

        self.tabWidget.addTab(self.tab_2, "")

        self.horizontalLayout_7.addWidget(self.tabWidget)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
#if QT_CONFIG(tooltip)
        self.groupBox.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:11pt; color:#aa5500;\">\u041e\u043f\u0435\u0440\u0430\u0442\u0438\u0432\u043d\u0430\u044f \u043f\u0430\u043c\u044f\u0442\u044c </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u041e\u043f\u0435\u0440\u0430\u0442\u0438\u0432\u043d\u0430\u044f \u043f\u0430\u043c\u044f\u0442\u044c ", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430 \u043f\u0430\u043c\u044f\u0442\u0438</p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u041e\u0431\u044a\u0451\u043c \u043e\u043f\u0435\u0440\u0430\u0442\u0438\u0432\u043d\u043e\u0439 \u043f\u0430\u043c\u044f\u0442\u0438", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u0421\u0432\u043e\u0431\u043e\u0434\u043d\u0430\u044f \u043f\u0430\u043c\u044f\u0442\u044c", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"\u0418\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u043e \u043f\u0430\u043c\u044f\u0442\u0438", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430 \u043f\u0430\u043c\u044f\u0442\u0438", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"\u041f\u0440\u043e\u0446\u0435\u0441\u0441\u043e\u0440", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430 \u043f\u0440\u043e\u0446\u0435\u0441\u0441\u043e\u0440\u0430</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u043f\u0440\u043e\u0446\u0435\u0441\u0441\u043e\u0440\u0430", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u044f\u0434\u0435\u0440", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430 \u043f\u0440\u043e\u0446\u0435\u0441\u0441\u043e\u0440\u0430", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"\u0416\u0435\u0441\u0442\u043a\u0438\u0435 \u0434\u0438\u0441\u043a\u0438", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Form", u"\u0416\u0435\u0441\u0442\u043a\u0438\u0439 \u0434\u0438\u0441\u043a 1", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("Form", u"\u0416\u0435\u0441\u0442\u043a\u0438\u0439 \u0434\u0438\u0441\u043a 2", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:14pt; color:#aa0000;\">\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u041e \u041f\u041a</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"PC INFO", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:14pt; color:#aa0000;\">\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u0437\u0430\u043f\u0443\u0449\u0435\u043d\u044b\u0445 \u043f\u0440\u043e\u0446\u0435\u0441\u0441\u0430\u0445</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Process), QCoreApplication.translate("Form", u"Process", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:14pt; color:#aa0000;\">\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u0437\u0430\u043f\u0443\u0449\u0435\u043d\u044b\u0445 \u0441\u043b\u0443\u0436\u0431\u0430\u0445</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Form", u"Services", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:14pt; color:#aa0000;\">\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u043f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0449\u0438\u043a\u0435 \u0437\u0430\u0434\u0430\u0447</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"Scheduler", None))
    # retranslateUi

