# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'v3.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_AddapiWindow(object):
    def setupUi(self, AddapiWindow):
        if not AddapiWindow.objectName():
            AddapiWindow.setObjectName(u"AddapiWindow")
        AddapiWindow.setWindowIcon(QIcon("img\icon4.png"))
        AddapiWindow.resize(500, 240)
        AddapiWindow.setMinimumSize(QSize(500, 240))
        AddapiWindow.setMaximumSize(QSize(500, 240))
        AddapiWindow.setStyleSheet(u"background-color:#161616;\n"
"font-family:Eirik Raudel;\n"
"")
        self.verticalLayout_2 = QVBoxLayout(AddapiWindow)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.line_binanceAPI_edit = QLineEdit(AddapiWindow)
        self.line_binanceAPI_edit.setObjectName(u"line_binanceAPI_edit")
        self.line_binanceAPI_edit.setMinimumSize(QSize(0, 35))
        self.line_binanceAPI_edit.setStyleSheet(u"color:#FFFFFF;\n"
"font-weight:bold;\n"
"font-size:17px;\n"
"border:1px solid rgba(255,255,255,100);")

        self.verticalLayout.addWidget(self.line_binanceAPI_edit)

        self.line_binanceSecretkey_edit = QLineEdit(AddapiWindow)
        self.line_binanceSecretkey_edit.setObjectName(u"line_binanceSecretkey_edit")
        self.line_binanceSecretkey_edit.setMinimumSize(QSize(0, 35))
        self.line_binanceSecretkey_edit.setMaximumSize(QSize(16777215, 35))
        self.line_binanceSecretkey_edit.setStyleSheet(u"color:#FFFFFF;\n"
"font-weight:bold;\n"
"font-size:17px;\n"
"border:1px solid rgba(255,255,255,100);")

        self.verticalLayout.addWidget(self.line_binanceSecretkey_edit)

        self.line_bybitAPI_edit = QLineEdit(AddapiWindow)
        self.line_bybitAPI_edit.setObjectName(u"line_bybitAPI_edit")
        self.line_bybitAPI_edit.setMinimumSize(QSize(0, 35))
        self.line_bybitAPI_edit.setStyleSheet(u"color:#FFFFFF;\n"
"font-weight:bold;\n"
"font-size:17px;\n"
"border:1px solid rgba(255,255,255,100);")

        self.verticalLayout.addWidget(self.line_bybitAPI_edit)

        self.line_bybitSecretkey_edit = QLineEdit(AddapiWindow)
        self.line_bybitSecretkey_edit.setObjectName(u"line_bybitSecretkey_edit")
        self.line_bybitSecretkey_edit.setMinimumSize(QSize(0, 35))
        self.line_bybitSecretkey_edit.setMaximumSize(QSize(16777215, 35))
        self.line_bybitSecretkey_edit.setStyleSheet(u"color:#FFFFFF;\n"
"font-weight:bold;\n"
"font-size:17px;\n"
"border:1px solid rgba(255,255,255,100);")

        self.verticalLayout.addWidget(self.line_bybitSecretkey_edit)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.bt_add_api = QPushButton(AddapiWindow)
        self.bt_add_api.setObjectName(u"bt_add_api")
        self.bt_add_api.setMinimumSize(QSize(150, 35))
        self.bt_add_api.setMaximumSize(QSize(150, 16777215))
        self.bt_add_api.setLayoutDirection(Qt.LeftToRight)
        self.bt_add_api.setAutoFillBackground(False)
        self.bt_add_api.setStyleSheet(u"QPushButton{\n"
"color:#FFFFFF;\n"
"font-weight:bold;\n"
"background-color:#202020;\n"
"border:2px solid rgba(103,103,101,100);\n"
"border-radius:10px;\n"
"margin-left:7px;\n"
"font-size:20px;\n"
"font-stretch:expanded ;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background-color:#313131;\n"
"border:2px solid rgba(103,103,101,40);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:#3D3B3B;\n"
"border:2px solid rgba(103,103,101,70);\n"
"}")

        self.verticalLayout_2.addWidget(self.bt_add_api, 0, Qt.AlignHCenter)


        self.retranslateUi(AddapiWindow)

        QMetaObject.connectSlotsByName(AddapiWindow)
    # setupUi

    def retranslateUi(self, AddapiWindow):
        AddapiWindow.setWindowTitle(QCoreApplication.translate("AddapiWindow", u"Calibri:addAPI", None))
        self.line_binanceAPI_edit.setPlaceholderText(QCoreApplication.translate("AddapiWindow", u"Binance API", u"Binance"))
        self.line_binanceSecretkey_edit.setPlaceholderText(QCoreApplication.translate("AddapiWindow", u"Binance Secret Key", None))
        self.line_bybitAPI_edit.setPlaceholderText(QCoreApplication.translate("AddapiWindow", u"Bybit API", None))
        self.line_bybitSecretkey_edit.setPlaceholderText(QCoreApplication.translate("AddapiWindow", u"Bybit Secret Key", None))
        self.bt_add_api.setText(QCoreApplication.translate("AddapiWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
    # retranslateUi

