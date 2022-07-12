# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'help_design.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Help(object):
    def setupUi(self, Help):
        if not Help.objectName():
            Help.setObjectName(u"Help")
        Help.resize(453, 673)
        Help.setMinimumSize(QSize(453, 673))
        Help.setMaximumSize(QSize(453, 673))
        self.textEdit = QTextEdit(Help)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(0, 0, 451, 671))

        self.retranslateUi(Help)

        QMetaObject.connectSlotsByName(Help)
    # setupUi

    def retranslateUi(self, Help):
        Help.setWindowTitle(QCoreApplication.translate("Help", u"Help", None))
        self.textEdit.setHtml(QCoreApplication.translate("Help", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'-apple-system','BlinkMacSystemFont','Segoe UI','Arial','sans-serif'; font-size:16pt; color:#222222; background-color:#ffffff;\">\u0418\u0433\u0440\u043e\u0432\u043e\u0435 \u043f\u043e\u043b\u0435 \u0434\u043b\u044f 2048 \u043f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u043b\u044f\u0435\u0442 \u0441\u043e\u0431\u043e\u0439 \u043a\u0432\u0430\u0434\u0440\u0430\u0442 4\u00d74.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font"
                        "-family:'-apple-system','BlinkMacSystemFont','Segoe UI','Arial','sans-serif'; font-size:16pt; color:#222222; background-color:#ffffff;\">\u00ab\u041a\u043e\u0441\u0442\u044f\u0448\u043a\u0438\u00bb \u043c\u043e\u0436\u043d\u043e \u043f\u0435\u0440\u0435\u043c\u0435\u0449\u0430\u0442\u044c \u0432 \u043e\u0434\u043d\u0443 \u0438\u0437 \u0447\u0435\u0442\u044b\u0440\u0451\u0445 \u0441\u0442\u043e\u0440\u043e\u043d (\u0435\u0441\u043b\u0438 \u044d\u0442\u043e\u043c\u0443 \u043d\u0435 \u043c\u0435\u0448\u0430\u0435\u0442 \u0440\u0430\u0441\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435), \u043f\u0440\u0438 \u044d\u0442\u043e\u043c, \u043a\u043e\u0433\u0434\u0430 \u0434\u0432\u0435 \u043f\u043b\u0438\u0442\u043a\u0438 \u043e\u0434\u0438\u043d\u0430\u043a\u043e\u0432\u043e\u0433\u043e \u043d\u043e\u043c\u0438\u043d\u0430\u043b\u0430 \u0441\u0442\u0430\u043b\u043a\u0438\u0432\u0430\u044e\u0442\u0441\u044f \u0434\u0440\u0443\u0433 \u0441 \u0434\u0440\u0443\u0433\u043e\u043c, \u0442\u043e \u0441\u0442\u0430\u043d"
                        "\u043e\u0432\u044f\u0442\u0441\u044f \u043e\u0434\u043d\u0438\u043c \u0442\u0430\u0439\u043b\u043e\u043c, \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043a\u043e\u0442\u043e\u0440\u043e\u0433\u043e \u0443\u0434\u0432\u0430\u0438\u0432\u0430\u0435\u0442\u0441\u044f. \u0417\u0430 \u043e\u0434\u0438\u043d \u0445\u043e\u0434 \u043f\u043b\u0438\u0442\u043a\u0430 \u043c\u043e\u0436\u0435\u0442 \u0441\u043a\u043b\u0430\u0434\u044b\u0432\u0430\u0442\u044c\u0441\u044f \u0432 \u0440\u0430\u0437\u043d\u044b\u0445 \u043c\u0435\u0441\u0442\u0430\u0445 \u0438\u0433\u0440\u043e\u0432\u043e\u0433\u043e \u043f\u043e\u043b\u044f, \u043d\u043e \u043b\u0438\u0448\u044c \u043e\u0434\u0438\u043d \u0440\u0430\u0437 \u0443\u0432\u0435\u043b\u0438\u0447\u0438\u0432\u0430\u0442\u044c \u0441\u0432\u043e\u0439 \u043d\u043e\u043c\u0438\u043d\u0430\u043b. \u0414\u0440\u0443\u0433\u0438\u043c\u0438 \u0441\u043b\u043e\u0432\u0430\u043c\u0438, \u0435\u0441\u043b\u0438 \u043f\u043e\u0434\u0440\u044f\u0434 \u0440\u0430\u0441\u043f\u043e\u043b"
                        "\u043e\u0436\u0435\u043d\u044b \u00ab2\u00bb, \u00ab2\u00bb \u0438 \u00ab4\u00bb, \u0442\u043e \u0437\u0430 \u0445\u043e\u0434 \u043c\u043e\u0436\u043d\u043e \u043e\u0431\u044a\u0435\u0434\u0438\u043d\u0438\u0442\u044c \u0442\u043e\u043b\u044c\u043a\u043e \u00ab2\u00bb \u0438 \u00ab2\u00bb \u0432 \u00ab4\u00bb, \u0430 \u043f\u043e\u043b\u0443\u0447\u0438\u0432\u0448\u0443\u044e\u0441\u044f \u00ab4\u00bb \u0441 \u0431\u043b\u043e\u043a\u043e\u043c \u0442\u0430\u043a\u043e\u0433\u043e \u0436\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f \u2013 \u043b\u0438\u0448\u044c \u0432\u043e \u0432\u0440\u0435\u043c\u044f \u0441\u043b\u0435\u0434\u0443\u044e\u0449\u0435\u0433\u043e \u0445\u043e\u0434\u0430.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'-apple-system','BlinkMacSystemFont','Segoe UI','Arial','sans-serif'; font-size:16pt; color:#222222; background-color:#ffffff;\">\u0423\u0441\u043b\u043e"
                        "\u0432\u0438\u044f \u043f\u043e\u0431\u0435\u0434\u044b: \u043f\u043e\u043b\u0443\u0447\u0435\u043d\u0438\u0435 \u043f\u043b\u0438\u0442\u043a\u0438 \u0441\u043e \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435\u043c 2048</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'-apple-system','BlinkMacSystemFont','Segoe UI','Arial','sans-serif'; font-size:16pt; color:#222222; background-color:#ffffff;\">\u0423\u0441\u043b\u043e\u0432\u0438\u044f \u043f\u043e\u0440\u0430\u0436\u0435\u043d\u0438\u044f: \u043e\u0442\u0441\u0443\u0442\u0441\u0432\u0438\u0435 \u043f\u0443\u0441\u0442\u044b\u0445 \u043a\u043b\u0435\u0442\u043e\u043a \u043d\u0430 \u043f\u043e\u043b\u0435.</span></p></body></html>", None))
    # retranslateUi

