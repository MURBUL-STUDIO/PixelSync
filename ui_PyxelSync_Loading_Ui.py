# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PyxelSync_Loading_UiGLLabC.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(529, 373)
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.dropShadowFrame = QFrame(self.centralwidget)
        self.dropShadowFrame.setObjectName(u"dropShadowFrame")
        self.dropShadowFrame.setStyleSheet(u"QFrame{	\n"
"	background-color: rgb(55, 85, 39);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}")
        self.dropShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QFrame.Raised)
        self.label_title = QLabel(self.dropShadowFrame)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(-77, 40, 661, 81))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(40)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(u"color: rgb(181, 200, 184);")
        self.label_title.setAlignment(Qt.AlignCenter)
        self.myprogressBar = QProgressBar(self.dropShadowFrame)
        self.myprogressBar.setObjectName(u"myprogressBar")
        self.myprogressBar.setGeometry(QRect(-430, 220, 981, 31))
        font1 = QFont()
        font1.setBold(False)
        font1.setWeight(50)
        self.myprogressBar.setFont(font1)
        self.myprogressBar.setCursor(QCursor(Qt.BusyCursor))
        self.myprogressBar.setStyleSheet(u"QProgressBar{\n"
"	\n"
"	background-color: rgb(108, 175, 113);\n"
"	border-style: none;\n"
"	border-radius: 10px;\n"
"	color: rgb(94, 139, 69);\n"
"}\n"
"QProgressBar::chunk{\n"
"	background-color: rgb(52, 105, 158);\n"
"	border-radius: 17px;\n"
"}")
        self.myprogressBar.setValue(24)
        self.myprogressBar.setTextVisible(False)

        self.verticalLayout.addWidget(self.dropShadowFrame)

        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"MainWindow", None))
        self.label_title.setText(QCoreApplication.translate("SplashScreen", u"<html><head/><body><p>PyxelSync</p></body></html>", None))
    # retranslateUi

