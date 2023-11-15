# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_weather.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_FormWeather(object):
    def setupUi(self, FormWeather):
        if not FormWeather.objectName():
            FormWeather.setObjectName(u"FormWeather")
        FormWeather.resize(718, 628)
        self.verticalLayout = QVBoxLayout(FormWeather)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayoutCoord = QHBoxLayout()
        self.horizontalLayoutCoord.setObjectName(u"horizontalLayoutCoord")
        self.labelLatitude = QLabel(FormWeather)
        self.labelLatitude.setObjectName(u"labelLatitude")

        self.horizontalLayoutCoord.addWidget(self.labelLatitude)

        self.lineEditLatitude = QLineEdit(FormWeather)
        self.lineEditLatitude.setObjectName(u"lineEditLatitude")
        self.lineEditLatitude.setMinimumSize(QSize(0, 30))

        self.horizontalLayoutCoord.addWidget(self.lineEditLatitude)

        self.labelLongitude = QLabel(FormWeather)
        self.labelLongitude.setObjectName(u"labelLongitude")

        self.horizontalLayoutCoord.addWidget(self.labelLongitude)

        self.lineEditLongitude = QLineEdit(FormWeather)
        self.lineEditLongitude.setObjectName(u"lineEditLongitude")
        self.lineEditLongitude.setMinimumSize(QSize(0, 30))

        self.horizontalLayoutCoord.addWidget(self.lineEditLongitude)


        self.verticalLayout.addLayout(self.horizontalLayoutCoord)

        self.groupBoxUpdate = QGroupBox(FormWeather)
        self.groupBoxUpdate.setObjectName(u"groupBoxUpdate")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxUpdate.sizePolicy().hasHeightForWidth())
        self.groupBoxUpdate.setSizePolicy(sizePolicy)
        self.groupBoxUpdate.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_2 = QHBoxLayout(self.groupBoxUpdate)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.radioButton3 = QRadioButton(self.groupBoxUpdate)
        self.radioButton3.setObjectName(u"radioButton3")

        self.horizontalLayout_2.addWidget(self.radioButton3)

        self.radioButton5 = QRadioButton(self.groupBoxUpdate)
        self.radioButton5.setObjectName(u"radioButton5")

        self.horizontalLayout_2.addWidget(self.radioButton5)

        self.radioButton10 = QRadioButton(self.groupBoxUpdate)
        self.radioButton10.setObjectName(u"radioButton10")
        self.radioButton10.setChecked(True)

        self.horizontalLayout_2.addWidget(self.radioButton10)


        self.verticalLayout.addWidget(self.groupBoxUpdate)

        self.textEditData = QTextEdit(FormWeather)
        self.textEditData.setObjectName(u"textEditData")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.textEditData.sizePolicy().hasHeightForWidth())
        self.textEditData.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.textEditData)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButtonGetData = QPushButton(FormWeather)
        self.pushButtonGetData.setObjectName(u"pushButtonGetData")

        self.horizontalLayout_3.addWidget(self.pushButtonGetData)

        self.pushButtonStopGetData = QPushButton(FormWeather)
        self.pushButtonStopGetData.setObjectName(u"pushButtonStopGetData")

        self.horizontalLayout_3.addWidget(self.pushButtonStopGetData)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(FormWeather)

        QMetaObject.connectSlotsByName(FormWeather)
    # setupUi

    def retranslateUi(self, FormWeather):
        FormWeather.setWindowTitle(QCoreApplication.translate("FormWeather", u"\u0414\u0430\u043d\u043d\u044b\u0435 \u043e \u043f\u043e\u0433\u043e\u0434\u0435", None))
        self.labelLatitude.setText(QCoreApplication.translate("FormWeather", u"\u0428\u0438\u0440\u043e\u0442\u0430:", None))
        self.labelLongitude.setText(QCoreApplication.translate("FormWeather", u"\u0414\u043e\u043b\u0433\u043e\u0442\u0430:", None))
        self.lineEditLongitude.setText("")
        self.groupBoxUpdate.setTitle(QCoreApplication.translate("FormWeather", u"\u0427\u0430\u0441\u0442\u043e\u0442\u0430 \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u044f \u043f\u043e\u0433\u043e\u0434\u044b", None))
        self.radioButton3.setText(QCoreApplication.translate("FormWeather", u"3\u0441\u0435\u043a", None))
        self.radioButton5.setText(QCoreApplication.translate("FormWeather", u"5\u0441\u0435\u043a", None))
        self.radioButton10.setText(QCoreApplication.translate("FormWeather", u"10\u0441\u0435\u043a", None))
        self.pushButtonGetData.setText(QCoreApplication.translate("FormWeather", u"\u041f\u043e\u043b\u0443\u0447\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.pushButtonStopGetData.setText(QCoreApplication.translate("FormWeather", u"\u041e\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c", None))
    # retranslateUi
