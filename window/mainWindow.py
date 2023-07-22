# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'v1.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowIcon(QIcon("img\icon4.png"))
        MainWindow.resize(1043, 720)
        MainWindow.setMinimumSize(QSize(800, 720))
        MainWindow.setCursor(QCursor(Qt.ArrowCursor))
        MainWindow.setStyleSheet(u"background-color:#1E1E1E;\n"
"font-family:Eirik Raudel;\n"
"")     
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1023, 644))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.lower_panel = QFrame(self.centralwidget)
        self.lower_panel.setObjectName(u"lower_panel")
        self.lower_panel.setMinimumSize(QSize(0, 35))
        self.lower_panel.setStyleSheet(u"background-color:#161616;\n"
"")
        self.horizontalLayout = QHBoxLayout(self.lower_panel)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(2, -1, -1, -1)
        self.bt_add_bot = QPushButton(self.lower_panel)
        self.bt_add_bot.setObjectName(u"bt_add_bot")
        self.bt_add_bot.setMinimumSize(QSize(0, 32))
        self.bt_add_bot.setMaximumSize(QSize(125, 30))
        font = QFont()
        font.setFamilies([u"Eirik Raudel"])
        font.setBold(True)
        self.bt_add_bot.setFont(font)
        self.bt_add_bot.setStyleSheet(u"QPushButton{\n"
"color:#FFFFFF;\n"
"font-weight:bold;\n"
"background-color:#202020;\n"
"border:2px solid rgba(103,103,101,20);\n"
"border-radius:10px;\n"
"margin-left:7px;\n"
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
"}\n"
"")

        self.horizontalLayout.addWidget(self.bt_add_bot)

        self.bt_add_API = QPushButton(self.lower_panel)
        self.bt_add_API.setObjectName(u"bt_add_API")
        self.bt_add_API.setMinimumSize(QSize(0, 32))
        self.bt_add_API.setMaximumSize(QSize(150, 30))
        self.bt_add_API.setStyleSheet(u"QPushButton{\n"
"color:#FFFFFF;\n"
"font-weight:bold;\n"
"background-color:rgba(23, 33, 43,100);\n"
"border:2px solid rgba(103,103,101,20);\n"
"border-radius:10px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background-color:#222931;\n"
"\n"
"border:2px solid rgba(103,103,101,40);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:#222B36;\n"
"border:2px solid rgba(103,103,101,70);\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.bt_add_API)

        self.line_2 = QFrame(self.lower_panel)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_2)

        self.balance_acc = QLabel(self.lower_panel)
        self.balance_acc.setObjectName(u"balance_acc")
        self.balance_acc.setMinimumSize(QSize(150, 30))
        self.balance_acc.setLayoutDirection(Qt.LeftToRight)
        self.balance_acc.setAutoFillBackground(False)
        self.balance_acc.setStyleSheet(u"color:#FFFFFF;\n"
"font-weight:bold;")
        self.balance_acc.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.balance_acc, 0, Qt.AlignRight)

        self.line_for_balance_system = QFrame(self.lower_panel)
        self.line_for_balance_system.setObjectName(u"line_for_balance_system")
        self.line_for_balance_system.setFrameShape(QFrame.VLine)
        self.line_for_balance_system.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_for_balance_system)

        self.system_info = QLabel(self.lower_panel)
        self.system_info.setObjectName(u"system_info")
        self.system_info.setMinimumSize(QSize(100, 25))
        self.system_info.setMaximumSize(QSize(150, 25))
        self.system_info.setStyleSheet(u"color:#FFFFFF;\n"
"font-weight:bold;")

        self.horizontalLayout.addWidget(self.system_info, 0, Qt.AlignVCenter)


        self.verticalLayout.addWidget(self.lower_panel)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Calibri ", None))
        self.bt_add_bot.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0431\u043e\u0442\u0430", None))
        self.bt_add_API.setText(QCoreApplication.translate("MainWindow", u"\u0423\u043a\u0430\u0437\u0430\u0442\u044c AIP \u043a\u043b\u044e\u0447", None))
        self.balance_acc.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043b\u0430\u043d\u0441: 200 $", None))
        self.system_info.setText(QCoreApplication.translate("MainWindow", u"CPU 20% RAM 20%", None))
    # retranslateUi

