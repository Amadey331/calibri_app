# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'exemple_bot.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QTableView, QTextBrowser,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1236, 720)
        MainWindow.setMinimumSize(QSize(800, 720))
        MainWindow.setCursor(QCursor(Qt.ArrowCursor))
        MainWindow.setStyleSheet(u"background-color:#1E1E1E;\n"
"font-family:Eirik Raudel;\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea_bot = QScrollArea(self.centralwidget)
        self.scrollArea_bot.setObjectName(u"scrollArea_bot")
        self.scrollArea_bot.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1216, 644))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.bot_widget = QWidget(self.scrollAreaWidgetContents)
        self.bot_widget.setObjectName(u"bot_widget")
        self.bot_widget.setMinimumSize(QSize(0, 350))
        self.bot_widget.setMaximumSize(QSize(16777215, 350))
        self.bot_widget.setStyleSheet(u"background-color:rgba(255,255,255,20);\n"
"border:1px solid rgba(255,255,255,100);\n"
"border-radius:7px;")
        self.horizontalLayout_3 = QHBoxLayout(self.bot_widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(1, 1, 0, 1)
        self.horizontalLayout_main = QHBoxLayout()
        self.horizontalLayout_main.setObjectName(u"horizontalLayout_main")
        self.verticalLayout_for_text = QVBoxLayout()
        self.verticalLayout_for_text.setSpacing(5)
        self.verticalLayout_for_text.setObjectName(u"verticalLayout_for_text")
        self.verticalLayout_for_text.setContentsMargins(5, 10, -1, -1)
        self.horizontalLayout_for_upperInfo = QHBoxLayout()
        self.horizontalLayout_for_upperInfo.setObjectName(u"horizontalLayout_for_upperInfo")
        self.horizontalFrame_instName = QFrame(self.bot_widget)
        self.horizontalFrame_instName.setObjectName(u"horizontalFrame_instName")
        self.horizontalFrame_instName.setStyleSheet(u"border:None;\n"
"background-color:None;")
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalFrame_instName)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.inst_name = QLabel(self.horizontalFrame_instName)
        self.inst_name.setObjectName(u"inst_name")
        self.inst_name.setMinimumSize(QSize(0, 25))
        self.inst_name.setMaximumSize(QSize(16777215, 25))
        self.inst_name.setStyleSheet(u"color:rgba(255,255,255,1);\n"
"font-weight:bold;\n"
"font-size:20px;\n"
"background-color:None;\n"
"\n"
"border:none;\n"
"border-radius:7px;")

        self.horizontalLayout_4.addWidget(self.inst_name)

        self.label = QLabel(self.horizontalFrame_instName)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color:rgba(255,255,255,1);\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"background-color:None;\n"
"margin-left:4px;\n"
"border:none;\n"
"border-radius:7px;")

        self.horizontalLayout_4.addWidget(self.label)

        self.label_2 = QLabel(self.horizontalFrame_instName)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color:rgba(255,255,255,1);\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"background-color:None;\n"
"margin-left:4px;\n"
"border:none;\n"
"border-radius:7px;")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.frame = QFrame(self.horizontalFrame_instName)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(1, 0))
        self.frame.setMaximumSize(QSize(1, 16777215))
        self.frame.setStyleSheet(u"background-color:#4F4F4F;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.frame)

        self.balance_bot_now = QLabel(self.horizontalFrame_instName)
        self.balance_bot_now.setObjectName(u"balance_bot_now")
        self.balance_bot_now.setMaximumSize(QSize(120, 99999))
        self.balance_bot_now.setStyleSheet(u"color:rgba(255,255,255,1);\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"background-color:None;\n"
"margin-left:4px;\n"
"border:none;\n"
"border-radius:7px;")

        self.horizontalLayout_4.addWidget(self.balance_bot_now)


        self.horizontalLayout_for_upperInfo.addWidget(self.horizontalFrame_instName, 0, Qt.AlignLeft)

        self.horizontlFrame_date = QFrame(self.bot_widget)
        self.horizontlFrame_date.setObjectName(u"horizontlFrame_date")
        self.horizontlFrame_date.setStyleSheet(u"border:None;\n"
"background-color:None;")
        self.horizontalLayout_2 = QHBoxLayout(self.horizontlFrame_date)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.balance_bot_be = QLabel(self.horizontlFrame_date)
        self.balance_bot_be.setObjectName(u"balance_bot_be")
        self.balance_bot_be.setMaximumSize(QSize(100, 16777215))
        self.balance_bot_be.setStyleSheet(u"color:rgba(255,255,255,1);\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"background-color:None;\n"
"margin-left:4px;\n"
"border:none;\n"
"border-radius:7px;")

        self.horizontalLayout_2.addWidget(self.balance_bot_be)

        self.date_info = QLabel(self.horizontlFrame_date)
        self.date_info.setObjectName(u"date_info")
        self.date_info.setMaximumSize(QSize(250, 16777215))
        self.date_info.setStyleSheet(u"color:rgba(255,255,255,1);\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"background-color:None;\n"
"margin-left:4px;\n"
"border:none;\n"
"border-radius:7px;")

        self.horizontalLayout_2.addWidget(self.date_info)


        self.horizontalLayout_for_upperInfo.addWidget(self.horizontlFrame_date, 0, Qt.AlignRight)


        self.verticalLayout_for_text.addLayout(self.horizontalLayout_for_upperInfo)

        self.horizontalLayout_mainInfo = QHBoxLayout()
        self.horizontalLayout_mainInfo.setObjectName(u"horizontalLayout_mainInfo")
        self.verticalLayout_left = QVBoxLayout()
        self.verticalLayout_left.setObjectName(u"verticalLayout_left")
        self.table_deals = QTableView(self.bot_widget)
        self.table_deals.setObjectName(u"table_deals")
        self.table_deals.setStyleSheet(u"border:None;")

        self.verticalLayout_left.addWidget(self.table_deals)

        self.Info_strat_line = QTextBrowser(self.bot_widget)
        self.Info_strat_line.setObjectName(u"Info_strat_line")
        self.Info_strat_line.setMaximumSize(QSize(16777215, 40))
        self.Info_strat_line.setStyleSheet(u"font-size:15px;\n"
"border:None;")

        self.verticalLayout_left.addWidget(self.Info_strat_line)


        self.horizontalLayout_mainInfo.addLayout(self.verticalLayout_left)

        self.verticalGroupBox_right = QGroupBox(self.bot_widget)
        self.verticalGroupBox_right.setObjectName(u"verticalGroupBox_right")
        self.verticalGroupBox_right.setMaximumSize(QSize(600, 16777215))
        self.verticalGroupBox_right.setStyleSheet(u"border:None;")
        self.verticalLayout_5 = QVBoxLayout(self.verticalGroupBox_right)
        self.verticalLayout_5.setSpacing(3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.tableView_stratInfo = QTableView(self.verticalGroupBox_right)
        self.tableView_stratInfo.setObjectName(u"tableView_stratInfo")
        self.tableView_stratInfo.setStyleSheet(u"border:none;")

        self.verticalLayout_5.addWidget(self.tableView_stratInfo)

        self.horizontalFrame_bt = QFrame(self.verticalGroupBox_right)
        self.horizontalFrame_bt.setObjectName(u"horizontalFrame_bt")
        self.horizontalFrame_bt.setStyleSheet(u"background-color:#404040;\n"
"border:None;")
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalFrame_bt)
        self.horizontalLayout_6.setSpacing(1)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 3, -1, 0)
        self.bt_start = QPushButton(self.horizontalFrame_bt)
        self.bt_start.setObjectName(u"bt_start")
        self.bt_start.setMinimumSize(QSize(165, 35))
        self.bt_start.setMaximumSize(QSize(125, 35))
        self.bt_start.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_6.addWidget(self.bt_start, 0, Qt.AlignHCenter)

        self.bt_update = QPushButton(self.horizontalFrame_bt)
        self.bt_update.setObjectName(u"bt_update")
        self.bt_update.setMinimumSize(QSize(165, 35))
        self.bt_update.setMaximumSize(QSize(150, 35))
        self.bt_update.setLayoutDirection(Qt.LeftToRight)
        self.bt_update.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_6.addWidget(self.bt_update, 0, Qt.AlignHCenter)

        self.bt_delete = QPushButton(self.horizontalFrame_bt)
        self.bt_delete.setObjectName(u"bt_delete")
        self.bt_delete.setMinimumSize(QSize(165, 35))
        self.bt_delete.setMaximumSize(QSize(125, 35))
        self.bt_delete.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_6.addWidget(self.bt_delete, 0, Qt.AlignHCenter)


        self.verticalLayout_5.addWidget(self.horizontalFrame_bt)


        self.horizontalLayout_mainInfo.addWidget(self.verticalGroupBox_right)


        self.verticalLayout_for_text.addLayout(self.horizontalLayout_mainInfo)


        self.horizontalLayout_main.addLayout(self.verticalLayout_for_text)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_main)


        self.verticalLayout_2.addWidget(self.bot_widget)

        self.scrollArea_bot.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea_bot)

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
        self.inst_name.setText(QCoreApplication.translate("MainWindow", u"DOGEUSDT", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"SPOT", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"binance", None))
        self.balance_bot_now.setText(QCoreApplication.translate("MainWindow", u"100 $", None))
        self.balance_bot_be.setText(QCoreApplication.translate("MainWindow", u"120$", None))
        self.date_info.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u044f:14.02.2022", None))
#if QT_CONFIG(whatsthis)
        self.Info_strat_line.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.Info_strat_line.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Eirik Raudel'; font-size:15px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:15px; color:#ffffff;\">sss</span></p></body></html>", None))
        self.bt_start.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c", None))
        self.bt_update.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.bt_delete.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.bt_add_bot.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0431\u043e\u0442\u0430", None))
        self.bt_add_API.setText(QCoreApplication.translate("MainWindow", u"\u0423\u043a\u0430\u0437\u0430\u0442\u044c AIP \u043a\u043b\u044e\u0447", None))
        self.balance_acc.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043b\u0430\u043d\u0441: 200 $", None))
        self.system_info.setText(QCoreApplication.translate("MainWindow", u"CPU 20% RAM 20%", None))
    # retranslateUi

