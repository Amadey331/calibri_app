# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'v2.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_AddbotWindow(object):
    def setupUi(self, AddbotWindow):
        if not AddbotWindow.objectName():
            AddbotWindow.setObjectName(u"AddbotWindow")
        AddbotWindow.setWindowIcon(QIcon("img\icon4.png"))
        
        AddbotWindow.resize(840, 550)
        AddbotWindow.setMinimumSize(QSize(0, 550))
        AddbotWindow.setStyleSheet(u"background-color:#161616;\n"
"font-family:Eirik Raudel;\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(AddbotWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.main_frame = QFrame(AddbotWindow)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setStyleSheet(u"background-color:#1E1E1E;\n"
"")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.main_frame)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.upper_box = QGroupBox(self.main_frame)
        self.upper_box.setObjectName(u"upper_box")
        self.upper_box.setStyleSheet(u"background-color:rgba(30,30,30,100);\n"
"border:2px solid rgba(255,255,255,20);\n"
"border-radius:7px;")
        self.verticalLayout_2 = QVBoxLayout(self.upper_box)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.add_bot_text = QLabel(self.upper_box)
        self.add_bot_text.setObjectName(u"add_bot_text")
        self.add_bot_text.setMinimumSize(QSize(0, 40))
        self.add_bot_text.setMaximumSize(QSize(16777215, 40))
        self.add_bot_text.setLayoutDirection(Qt.LeftToRight)
        self.add_bot_text.setStyleSheet(u"color:rgba(255,255,255,1);\n"
"font-weight:bold;\n"
"font-size:25px;\n"
"background-color:rgba(255,255,255,20);\n"
"border:none;\n"
"border-radius:7px;")
        self.add_bot_text.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.add_bot_text)

        self.name_tool_line = QHBoxLayout()
        self.name_tool_line.setSpacing(0)
        self.name_tool_line.setObjectName(u"name_tool_line")
        self.name_tool_text = QLabel(self.upper_box)
        self.name_tool_text.setObjectName(u"name_tool_text")
        self.name_tool_text.setMaximumSize(QSize(250, 23))
        self.name_tool_text.setStyleSheet(u"color:#CAC9C8;\n"
"font-weight:bold;\n"
"font-size:20px;\n"
"border:none;")

        self.name_tool_line.addWidget(self.name_tool_text, 0, Qt.AlignVCenter)

        self.name_tool_enter = QLineEdit(self.upper_box)
        self.name_tool_enter.setObjectName(u"name_tool_enter")
        self.name_tool_enter.setMaximumSize(QSize(150, 23))
        self.name_tool_enter.setStyleSheet(u"color:#FFFFFF;\n"
"font-weight:bold;\n"
"font-size:17px;\n"
"border:1px solid rgba(255,255,255,100);")

        self.name_tool_line.addWidget(self.name_tool_enter, 0, Qt.AlignLeft)


        self.verticalLayout_2.addLayout(self.name_tool_line)

        self.Info_stratege_line = QHBoxLayout()
        self.Info_stratege_line.setObjectName(u"Info_stratege_line")
        self.info_stratege_text = QLabel(self.upper_box)
        self.info_stratege_text.setObjectName(u"info_stratege_text")
        self.info_stratege_text.setMinimumSize(QSize(222, 0))
        self.info_stratege_text.setMaximumSize(QSize(222, 16777215))
        self.info_stratege_text.setStyleSheet(u"color:#CAC9C8;\n"
"font-weight:bold;\n"
"font-size:20px;\n"
"border:none;")

        self.Info_stratege_line.addWidget(self.info_stratege_text)

        self.info_stratege_enter = QLineEdit(self.upper_box)
        self.info_stratege_enter.setObjectName(u"info_stratege_enter")
        self.info_stratege_enter.setMinimumSize(QSize(550, 0))
        self.info_stratege_enter.setMaximumSize(QSize(16777215, 23))
        self.info_stratege_enter.setStyleSheet(u"color:#FFFFFF;\n"
"font-weight:bold;\n"
"font-size:17px;\n"
"border:1px solid rgba(255,255,255,100);")

        self.Info_stratege_line.addWidget(self.info_stratege_enter)


        self.verticalLayout_2.addLayout(self.Info_stratege_line)

        self.balance_line = QHBoxLayout()
        self.balance_line.setSpacing(0)
        self.balance_line.setObjectName(u"balance_line")
        self.balance_text = QLabel(self.upper_box)
        self.balance_text.setObjectName(u"balance_text")
        self.balance_text.setMinimumSize(QSize(0, 0))
        self.balance_text.setMaximumSize(QSize(85, 16777215))
        self.balance_text.setStyleSheet(u"color:#CAC9C8;\n"
"font-weight:bold;\n"
"font-size:20px;\n"
"border:none;")
        self.balance_text.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.balance_line.addWidget(self.balance_text)

        self.balance_enter = QLineEdit(self.upper_box)
        self.balance_enter.setObjectName(u"balance_enter")
        self.balance_enter.setMaximumSize(QSize(100, 16777215))
        self.balance_enter.setStyleSheet(u"color:#FFFFFF;\n"
"font-weight:bold;\n"
"font-size:17px;\n"
"border:1px solid rgba(255,255,255,100);")

        self.balance_line.addWidget(self.balance_enter, 0, Qt.AlignLeft)


        self.verticalLayout_2.addLayout(self.balance_line)

        self.file_input_line = QHBoxLayout()
        self.file_input_line.setObjectName(u"file_input_line")
        self.file_input_text = QLabel(self.upper_box)
        self.file_input_text.setObjectName(u"file_input_text")
        self.file_input_text.setMaximumSize(QSize(230, 16777215))
        self.file_input_text.setStyleSheet(u"color:#CAC9C8;\n"
"font-weight:bold;\n"
"font-size:20px;\n"
"border:none;")

        self.file_input_line.addWidget(self.file_input_text)

        self.file_input_res = QLineEdit(self.upper_box)
        self.file_input_res.setObjectName(u"lineEdit")
        self.file_input_res.setMaximumSize(QSize(150, 23))
        self.file_input_res.setStyleSheet(u"color:#FFFFFF;\n"
"font-weight:bold;\n"
"font-size:17px;\n"
"border:1px solid rgba(255,255,255,100);\n"
"\n"
"margin-right:5px;")

        self.file_input_line.addWidget(self.file_input_res)

        self.bt_file_input_enter = QPushButton(self.upper_box)
        self.bt_file_input_enter.setObjectName(u"bt_file_input_enter")
        self.bt_file_input_enter.setMinimumSize(QSize(150, 0))
        self.bt_file_input_enter.setMaximumSize(QSize(180, 30))
        self.bt_file_input_enter.setStyleSheet(u"QPushButton{\n"
"color:#CAC9C8;\n"
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

        self.file_input_line.addWidget(self.bt_file_input_enter, 0, Qt.AlignLeft)


        self.verticalLayout_2.addLayout(self.file_input_line)

        self.select_item = QComboBox(self.upper_box)
        self.select_item.addItem("")
        self.select_item.addItem("")
        self.select_item.setObjectName(u"select_item")
        self.select_item.setMinimumSize(QSize(0, 35))
        self.select_item.setMaximumSize(QSize(150, 20))
        self.select_item.setAcceptDrops(False)
        self.select_item.setStyleSheet(u"color:#CAC9C8;\n"
"font-weight:bold;\n"
"border:1px solid rgba(255,255,255,100);")

        self.verticalLayout_2.addWidget(self.select_item)

        self.select_burse = QComboBox(self.upper_box)
        self.select_burse.addItem("")
        self.select_burse.addItem("")
        self.select_burse.setObjectName(u"select_burse")
        self.select_burse.setMinimumSize(QSize(0, 35))
        self.select_burse.setMaximumSize(QSize(150, 20))
        self.select_burse.setStyleSheet(u"color:#CAC9C8;\n"
"font-weight:bold;\n"
"border:1px solid rgba(255,255,255,100);")

        self.verticalLayout_2.addWidget(self.select_burse)


        self.verticalLayout_8.addWidget(self.upper_box)


        self.verticalLayout.addWidget(self.main_frame)

        self.bt_add_bot = QPushButton(AddbotWindow)
        self.bt_add_bot.setObjectName(u"bt_add_bot_secondWd")
        self.bt_add_bot.setMinimumSize(QSize(200, 0))
        self.bt_add_bot.setMaximumSize(QSize(300, 35))
        self.bt_add_bot.setStyleSheet(u"QPushButton{\n"
"color:#CAC9C8;\n"
"font-weight:bold;\n"
"background-color:#202020;\n"
"border:2px solid rgba(103,103,101,100);\n"
"border-radius:10px;\n"
"margin-left:7px;\n"
"font-size:25px;\n"
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
"}\n"
"")

        self.verticalLayout.addWidget(self.bt_add_bot, 0, Qt.AlignHCenter)


        self.retranslateUi(AddbotWindow)

        QMetaObject.connectSlotsByName(AddbotWindow)
    # setupUi

    def retranslateUi(self, AddbotWindow):
        AddbotWindow.setWindowTitle(QCoreApplication.translate("AddbotWindow", u"Calibri:addBot", None))
        self.add_bot_text.setText(QCoreApplication.translate("AddbotWindow", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0431\u043e\u0442\u0430", None))
        self.name_tool_text.setText(QCoreApplication.translate("AddbotWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0438\u043d\u0441\u0442\u0440\u0443\u043c\u0435\u043d\u0442\u0430:", None))
        self.info_stratege_text.setText(QCoreApplication.translate("AddbotWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0441\u0442\u0440\u0430\u0442\u0435\u0433\u0438\u0438:", None))
        self.balance_text.setText(QCoreApplication.translate("AddbotWindow", u"\u0411\u0430\u043b\u0430\u043d\u0441:", None))
        self.file_input_text.setText(QCoreApplication.translate("AddbotWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0444\u0430\u0439\u043b \u0431\u043e\u0442\u0430:", None))
        self.bt_file_input_enter.setText(QCoreApplication.translate("AddbotWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0444\u0430\u0439\u043b", None))
        self.select_item.setItemText(0, QCoreApplication.translate("AddbotWindow", u"Futures-USDT", None))
        self.select_item.setItemText(1, QCoreApplication.translate("AddbotWindow", u"SPOT", None))

        self.select_burse.setItemText(0, QCoreApplication.translate("AddbotWindow", u"Binance", None))
        self.select_burse.setItemText(1, QCoreApplication.translate("AddbotWindow", u"Bybit", None))

        self.bt_add_bot.setText(QCoreApplication.translate("AddbotWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
    # retranslateUi

