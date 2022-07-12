# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DataAnalysis.ui'
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
        Form.resize(808, 504)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.toolBox = QToolBox(Form)
        self.toolBox.setObjectName(u"toolBox")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.toolBox.setFont(font)
        self.pageStart = QWidget()
        self.pageStart.setObjectName(u"pageStart")
        self.pageStart.setGeometry(QRect(0, 0, 790, 426))
        self.widget_3 = QWidget(self.pageStart)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(0, 0, 467, 336))
        self.verticalLayout_3 = QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEditChooseFile = QLineEdit(self.widget_3)
        self.lineEditChooseFile.setObjectName(u"lineEditChooseFile")
        self.lineEditChooseFile.setMinimumSize(QSize(272, 22))
        font1 = QFont()
        font1.setPointSize(8)
        font1.setBold(False)
        font1.setWeight(50)
        self.lineEditChooseFile.setFont(font1)
        self.lineEditChooseFile.setReadOnly(True)

        self.horizontalLayout.addWidget(self.lineEditChooseFile)

        self.pushButtonChooseFile = QPushButton(self.widget_3)
        self.pushButtonChooseFile.setObjectName(u"pushButtonChooseFile")
        self.pushButtonChooseFile.setMinimumSize(QSize(131, 24))

        self.horizontalLayout.addWidget(self.pushButtonChooseFile)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(151, 20))

        self.horizontalLayout_3.addWidget(self.label)

        self.comboBoxChooseColumn = QComboBox(self.widget_3)
        self.comboBoxChooseColumn.setObjectName(u"comboBoxChooseColumn")
        self.comboBoxChooseColumn.setMinimumSize(QSize(152, 0))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setWeight(50)
        self.comboBoxChooseColumn.setFont(font2)

        self.horizontalLayout_3.addWidget(self.comboBoxChooseColumn)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalSpacer_2 = QSpacerItem(128, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_2 = QSpacerItem(20, 28, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.label_2 = QLabel(self.widget_3)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.radioButtonHist = QRadioButton(self.widget_3)
        self.buttonGroup = QButtonGroup(Form)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.radioButtonHist)
        self.radioButtonHist.setObjectName(u"radioButtonHist")
        self.radioButtonHist.setFont(font2)
        self.radioButtonHist.setChecked(True)

        self.verticalLayout_2.addWidget(self.radioButtonHist)

        self.radioButtonBoxplot = QRadioButton(self.widget_3)
        self.buttonGroup.addButton(self.radioButtonBoxplot)
        self.radioButtonBoxplot.setObjectName(u"radioButtonBoxplot")
        self.radioButtonBoxplot.setFont(font2)

        self.verticalLayout_2.addWidget(self.radioButtonBoxplot)

        self.radioButtonPlot = QRadioButton(self.widget_3)
        self.buttonGroup.addButton(self.radioButtonPlot)
        self.radioButtonPlot.setObjectName(u"radioButtonPlot")
        self.radioButtonPlot.setFont(font2)

        self.verticalLayout_2.addWidget(self.radioButtonPlot)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButtonBuildGraph = QPushButton(self.widget_3)
        self.pushButtonBuildGraph.setObjectName(u"pushButtonBuildGraph")
        self.pushButtonBuildGraph.setMinimumSize(QSize(161, 24))

        self.horizontalLayout_5.addWidget(self.pushButtonBuildGraph)

        self.horizontalSpacer_3 = QSpacerItem(278, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.toolBox.addItem(self.pageStart, u"\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430 \u0434\u0430\u043d\u043d\u044b\u0445 \u0434\u043b\u044f \u0430\u043d\u0430\u043b\u0438\u0437\u0430 \u0438 \u0432\u044b\u0431\u043e\u0440 \u0442\u0438\u043f\u0430 \u0433\u0440\u0430\u0444\u0438\u043a\u0430")
        self.pageResult = QWidget()
        self.pageResult.setObjectName(u"pageResult")
        self.pageResult.setGeometry(QRect(0, 0, 790, 426))
        self.verticalLayout_5 = QVBoxLayout(self.pageResult)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget = QWidget(self.pageResult)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(752, 160))
        self.widget.setMaximumSize(QSize(752, 160))
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.verticalLayout_11.addWidget(self.label_3)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(180, 0))

        self.horizontalLayout_9.addWidget(self.label_5)

        self.lineEditCountIsna = QLineEdit(self.widget)
        self.lineEditCountIsna.setObjectName(u"lineEditCountIsna")
        self.lineEditCountIsna.setReadOnly(True)

        self.horizontalLayout_9.addWidget(self.lineEditCountIsna)


        self.verticalLayout_11.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(180, 0))

        self.horizontalLayout_10.addWidget(self.label_6)

        self.lineEditPercentIsna = QLineEdit(self.widget)
        self.lineEditPercentIsna.setObjectName(u"lineEditPercentIsna")
        self.lineEditPercentIsna.setReadOnly(True)

        self.horizontalLayout_10.addWidget(self.lineEditPercentIsna)


        self.verticalLayout_11.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(180, 0))

        self.horizontalLayout_8.addWidget(self.label_10)

        self.lineEditMin = QLineEdit(self.widget)
        self.lineEditMin.setObjectName(u"lineEditMin")
        self.lineEditMin.setReadOnly(True)

        self.horizontalLayout_8.addWidget(self.lineEditMin)


        self.verticalLayout_11.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_11 = QLabel(self.widget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(180, 0))

        self.horizontalLayout_11.addWidget(self.label_11)

        self.lineEditMax = QLineEdit(self.widget)
        self.lineEditMax.setObjectName(u"lineEditMax")
        self.lineEditMax.setReadOnly(True)

        self.horizontalLayout_11.addWidget(self.lineEditMax)


        self.verticalLayout_11.addLayout(self.horizontalLayout_11)


        self.horizontalLayout_2.addLayout(self.verticalLayout_11)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalSpacer_5 = QSpacerItem(20, 18, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_5)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(180, 0))

        self.horizontalLayout_12.addWidget(self.label_4)

        self.lineEditAvg = QLineEdit(self.widget)
        self.lineEditAvg.setObjectName(u"lineEditAvg")
        self.lineEditAvg.setReadOnly(True)

        self.horizontalLayout_12.addWidget(self.lineEditAvg)


        self.verticalLayout_12.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(180, 0))

        self.horizontalLayout_13.addWidget(self.label_8)

        self.lineEditMedian = QLineEdit(self.widget)
        self.lineEditMedian.setObjectName(u"lineEditMedian")
        self.lineEditMedian.setReadOnly(True)

        self.horizontalLayout_13.addWidget(self.lineEditMedian)


        self.verticalLayout_12.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(180, 0))

        self.horizontalLayout_14.addWidget(self.label_9)

        self.lineEditInterquanlileRange = QLineEdit(self.widget)
        self.lineEditInterquanlileRange.setObjectName(u"lineEditInterquanlileRange")
        self.lineEditInterquanlileRange.setReadOnly(True)

        self.horizontalLayout_14.addWidget(self.lineEditInterquanlileRange)


        self.verticalLayout_12.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_12 = QLabel(self.widget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(180, 0))

        self.horizontalLayout_15.addWidget(self.label_12)

        self.lineEditQuantile = QLineEdit(self.widget)
        self.lineEditQuantile.setObjectName(u"lineEditQuantile")
        self.lineEditQuantile.setReadOnly(True)

        self.horizontalLayout_15.addWidget(self.lineEditQuantile)


        self.verticalLayout_12.addLayout(self.horizontalLayout_15)


        self.horizontalLayout_2.addLayout(self.verticalLayout_12)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)


        self.verticalLayout_5.addWidget(self.widget)

        self.toolBox.addItem(self.pageResult, u"\u0413\u0440\u0430\u0444\u0438\u043a \u0438 \u0440\u0430\u0441\u0447\u0435\u0442\u044b")

        self.verticalLayout.addWidget(self.toolBox)


        self.retranslateUi(Form)

        self.toolBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lineEditChooseFile.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0444\u0430\u0439\u043b \u0434\u043b\u044f \u0430\u043d\u0430\u043b\u0438\u0437\u0430", None))
        self.pushButtonChooseFile.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0444\u0430\u0439\u043b", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0441\u0442\u043e\u043b\u0431\u0435\u0446", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0432\u0438\u0434 \u0433\u0440\u0430\u0444\u0438\u043a\u0430", None))
        self.radioButtonHist.setText(QCoreApplication.translate("Form", u"\u0413\u0438\u0441\u0442\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430 Hist", None))
        self.radioButtonBoxplot.setText(QCoreApplication.translate("Form", u"\u042f\u0449\u0438\u043a \u0441 \u0443\u0441\u0430\u043c\u0438 Boxplot", None))
        self.radioButtonPlot.setText(QCoreApplication.translate("Form", u"\u0413\u0440\u0430\u0444\u0438\u043a Plot", None))
        self.pushButtonBuildGraph.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u0433\u0440\u0430\u0444\u0438\u043a", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.pageStart), QCoreApplication.translate("Form", u"\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430 \u0434\u0430\u043d\u043d\u044b\u0445 \u0434\u043b\u044f \u0430\u043d\u0430\u043b\u0438\u0437\u0430 \u0438 \u0432\u044b\u0431\u043e\u0440 \u0442\u0438\u043f\u0430 \u0433\u0440\u0430\u0444\u0438\u043a\u0430", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u0420\u0430\u0441\u0447\u0435\u0442\u044b:", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043f\u0440\u043e\u043f\u0443\u0441\u043a\u043e\u0432", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u043e\u043f\u0443\u0441\u043a\u0438 %", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"\u041c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"\u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u0421\u0440\u0435\u0434\u043d\u0435\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u041c\u0435\u0434\u0438\u0430\u043d\u0430", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"\u041c\u0435\u0436\u043a\u0432\u0430\u0440\u0442\u0438\u043b\u044c\u043d\u044b\u0439 \u0440\u0430\u0437\u043c\u0430\u0445", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"95% \u043a\u0432\u0430\u043d\u0442\u0438\u043b\u044c", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.pageResult), QCoreApplication.translate("Form", u"\u0413\u0440\u0430\u0444\u0438\u043a \u0438 \u0440\u0430\u0441\u0447\u0435\u0442\u044b", None))
    # retranslateUi

