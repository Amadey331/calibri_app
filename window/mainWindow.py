# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'v1.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import psutil
import subprocess
from functools import partial
import threading
import os,sys
from cryptography.fernet import Fernet
from binance.client import Client
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, QThread, Signal)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QVBoxLayout, QWidget,QTableView, QGroupBox, QTextBrowser,QMessageBox)
from connection import Data

# Класс для обновления баланса в новом потоке 
class CheckBalanceThread(QThread):
    balance_updated = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)

    def run(self):
        balance = self.chech_balance()
        self.balance_updated.emit(balance)

    def chech_balance(self):
        api, secret = self.get_api_binance()
        api, secret  = api.decode('utf-8'), secret.decode('utf-8')
        # return line_api
        client = Client(api,secret)
        acc_balance = client.futures_account_balance()
        for check_balance in acc_balance:
            if check_balance["asset"] == "USDT":
                usdt_balance = check_balance["balance"]
                return(str(float('{:.3f}'.format(float(usdt_balance)))))   
# Получение информации о api из зашифрованного файла
    def get_api_binance(self):
        with open("database/ApiData.txt", "r") as file:
            first_lale = file.readline()
            list_split = first_lale.split(" ")[0].split("'")
            secret_key = self.get_secretKey()
            fernet = Fernet(secret_key)
            return fernet.decrypt(bytes(list_split[1].encode('utf-8'))), fernet.decrypt(bytes(list_split[3].encode('utf-8')))
            
    
#     получение секретного ключа из файла для дешифпрвки
    def get_secretKey(self):
        with open("database/key.txt", "r") as file:
            first_lale = file.readline()
            
            return first_lale       

# Основной класс для загрузки UI
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
        self.verticalLayout_main = QVBoxLayout()
        self.verticalLayout_main.setObjectName(u"verticalLayout_main")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1021, 642))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_main.addWidget(self.scrollArea)

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


        self.verticalLayout_main.addWidget(self.lower_panel)


        self.verticalLayout.addLayout(self.verticalLayout_main)
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Critical)
        self.msg.setText("Error")
        self.msg.setInformativeText('More information')
        self.msg.setWindowTitle("Error")
        self.msg.setWindowIcon(QIcon("img\icon4.png"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
        
        
        
        
        # self.setupBots_fromBd(self.conn)


    # Обновление всей нижней информации
    def refresh_info_lowerPanel(self):
        self.system_info.setText(f"CPU {psutil.cpu_percent(0.1)} | RAM {psutil.virtual_memory()[2]}%")
        try:
        #     self.balance_acc.setText(f"  Баланс: {self.chech_balance()} $")
            self.check_balance_thread = CheckBalanceThread()
            self.check_balance_thread.balance_updated.connect(self.on_balance_updated)
            self.check_balance_thread.start()
        except:
            QMessageBox.critical(self.msg, 'Ошибка!', "Что бы обновить сначало коректно введите API!")

    def on_balance_updated(self, balance):
        self.balance_acc.setText(f"  Баланс: {balance} $")
        
    # Проверка баланса
#     def chech_balance(self):
#         api, secret = self.get_api_binance()
#         api, secret  = api.decode('utf-8'), secret.decode('utf-8')
#         # return line_api
#         client = Client(api,secret)
#         acc_balance = client.futures_account_balance()
#         for check_balance in acc_balance:
#             if check_balance["asset"] == "USDT":
#                 usdt_balance = check_balance["balance"]
#                 return(str(float('{:.3f}'.format(float(usdt_balance)))))   
# # Получение информации о api из зашифрованного файла
#     def get_api_binance(self):
#         with open("database/ApiData.txt", "r") as file:
#             first_lale = file.readline()
#             list_split = first_lale.split(" ")[0].split("'")
#             secret_key = self.get_secretKey()
#             fernet = Fernet(secret_key)
#             return fernet.decrypt(bytes(list_split[1].encode('utf-8'))), fernet.decrypt(bytes(list_split[3].encode('utf-8')))
            
    
# #     получение секретного ключа из файла для дешифпрвки
#     def get_secretKey(self):
#         with open("database/key.txt", "r") as file:
#             first_lale = file.readline()
            
#             return first_lale                    

        # Функция для конектов к кнопкам
    def create_connection_bt(self,name_inst,bt_start,bt_delete, bt_update,conn):
    # bt_start = self.findChild(QPushButton, f"bt_start{name_inst}")
    # bt_start.clicked.connect(self.start_bot(name_inst,bt_start))
    # someone = Comunicate()
    # bt_start.clicked.connect(lambda name = name_inst, bt = bt_start: self.start_bot(name, bt))
        
        bt_start.clicked.connect(partial(self.start_bot, name_inst, bt_start))
        bt_delete.clicked.connect(partial(self.delete_bot, name_inst, bt_start,conn))
        bt_update.clicked.connect(partial(self.update_bot, name_inst))
        # bt_start.clicked.connect(lambda  bt_start = bt_start, name_inst = name_inst: self.start_bot(bt_start, name_inst))       

# функция для обновления всей информации о боте
    def update_bot(self,name):
        print(name)

# Функция для удаления бота как виджет и из базы данных

    def delete_bot(self, name, bt_start, conn):
        
        if bt_start.text() == "Остановить":
            QMessageBox.critical(self.msg, 'Ошибка!', "Для удаления бота сначало остановите его!")
                
        else:
            bot_widget_name = getattr(self, f"bot_widget{name}" ) 
        #  self.verticalLayout_2.removeWidget(bot_widget_name)
        #  self.verticalLayout_2.deleteLater()
            
            bot_widget_name.deleteLater()
            conn.delete_bot(name)




#       Функция для старта файла
    def start_bot(self, name, bt_start):
        print("Запущен", name)
        # print(self.__dict__)
        print(os.getcwd())
        dict_file = os.path.join(os.getcwd(), 'database', 'bots', f"{name}_bot.py")
        setattr(self, f"dict_file{name}", dict_file)
        # subprocess.call(f'database/bots/{self.inst_name}_bot.py')
        
        
        # os.startfile(f"{os.getcwd()}\\database\\bots\\{name}_bot.py")
        if bt_start.text() == "Запустить": 
        #     subprocess.call([r'C:\WINDOWS\system32\cmd.exe', dict_file])
        #     python_exe = 'C:\Users\Amadey\AppData\Local\Programs\Python\Python311\python'
        #     shell_process = subprocess.Popen(('start', "", dict_file), shell=True)

        #     setattr(self, f"shell_process{name}", shell_process)
        #     pro = subprocess.Popen(['python.exe', dict_file], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, creationflags=subprocess.CREATE_NEW_CONSOLE, start_new_session=True)
        #     Для того что бы не видеть данные с других консолей в главной (ещё она не видна в диспетчере задач)))))
        #     pro = subprocess.Popen(["python", dict_file], shell=True, start_new_session=True)
        
        #     Для того что бы видеть все данные с консолей ботов в главной консоле
            pro = subprocess.Popen(["python", dict_file], )
        #     pro = subprocess.Popen(["python", dict_file], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, creationflags=subprocess.CREATE_NEW_CONSOLE, start_new_session=True)
            
            setattr(self, f"shell_process{name}", pro)

            bt_start.setText("Остановить")
        else:
            shell_process = getattr(self, f"shell_process{name}" )
            if shell_process:
        # Принудительно закрываем командную строку (терминал)
                children = psutil.Process(shell_process.pid).children(recursive=True)
                for child in children:
            # Принудительно завершаем каждый дочерний процесс Python
                        if child.name() == "python.exe":
                                child.terminate()
        # Принудительно завершаем сам процесс Python скрипта
            shell_process.terminate()                
            bt_start.setText("Запустить")
            
        #     psutil.pid_exists( pid )
        #     subprocess.call(f"taskkill /im {os.getcwd()}\\database\\bots\\{name}_bot.py")

            
        #     os.system("taskkill  /F /pid "+str(shell_process.pid))
            


#грузка ботов из бд в программу
    def setupBots_fromBd(self,connection):
    
        list_allBot = connection.get_all_data()
        
        
        for info_bot in list_allBot:
            date = info_bot[0]
            name_inst = info_bot[1]
            info_strategies = info_bot[2]
            balance_bot = info_bot[3]
            file_derictory = info_bot[4]
            type_burse = info_bot[5]
            name_burse = info_bot[6]
            
         # self.worker.do_work(self.create_widget_bot,date, name_inst, info_strategies, balance_bot, file_derictory, type_burse, name_burse)
            
            self.create_widget_bot(date, name_inst, info_strategies, balance_bot, file_derictory, type_burse, name_burse)
            bt_start_name = getattr(self,  f"bt_start{name_inst}" )
            bt_delete_name = getattr(self,  f"bt_delete{name_inst}" )
            bt_update_name = getattr(self,  f"bt_update{name_inst}" ) 
            self.create_connection_bt(name_inst,bt_start_name,bt_delete_name,bt_update_name,connection)
            
            
        #     bt_start_name.clicked.connect(lambda i=info_bot, bt_start = bt_start_name: self.test(i, bt_start))
            
           
# .................................................................................................................
# .................................................................................................................
# .................................................................................................................
# .................................................................................................................
# .................................................................................................................
# .................................................................................................................
# .................................................................................................................
# ...................................................................................................................................................................................................................................



    def create_widget_bot(self, date, name_inst, info_strategies, balance_bot, file_derictory, type_burse, name_burse):

         
        
        bot_widget = QWidget(self.scrollAreaWidgetContents)
        bot_widget.setObjectName(f"bot_widget")
        bot_widget.setMinimumSize(QSize(0, 350))
        bot_widget.setMaximumSize(QSize(16777215, 350))
        bot_widget.setStyleSheet(u"background-color:rgba(255,255,255,20);\n"
"border:1px solid rgba(255,255,255,100);\n"
"border-radius:7px;")
        setattr(self, f"bot_widget{name_inst}",bot_widget)
        bot_widget_name = getattr(self, f"bot_widget{name_inst}" ) 
        del bot_widget
        horizontalLayout_3 = QHBoxLayout(bot_widget_name)
        horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        horizontalLayout_3.setContentsMargins(1, 1, 0, 1)
        setattr(self, f"horizontalLayout_3{name_inst}",horizontalLayout_3)
        horizontalLayout_3_name = getattr(self, f"horizontalLayout_3{name_inst}" ) 
        

        horizontalLayout_main = QHBoxLayout()
        horizontalLayout_main.setObjectName(u"horizontalLayout_main")
        setattr(self, f"horizontalLayout_main{name_inst}",horizontalLayout_main)
        horizontalLayout_main_name = getattr(self, f"horizontalLayout_main{name_inst}" ) 
        

        verticalLayout_for_text = QVBoxLayout()
        verticalLayout_for_text.setSpacing(5)
        verticalLayout_for_text.setObjectName(u"verticalLayout_for_text")
        verticalLayout_for_text.setContentsMargins(5, 10, -1, -1)
        setattr(self, f"verticalLayout_for_text{name_inst}",verticalLayout_for_text)
        verticalLayout_for_text_name = getattr(self, f"verticalLayout_for_text{name_inst}" ) 
        del verticalLayout_for_text


        horizontalLayout_for_upperInfo = QHBoxLayout()
        horizontalLayout_for_upperInfo.setObjectName(u"horizontalLayout_for_upperInfo")
        setattr(self, f"horizontalLayout_for_upperInfo{name_inst}",horizontalLayout_for_upperInfo)
        horizontalLayout_for_upperInfo_name = getattr(self, f"horizontalLayout_for_upperInfo{name_inst}" ) 
        del horizontalLayout_for_upperInfo

        horizontalFrame_instName = QFrame(bot_widget_name)
        horizontalFrame_instName.setObjectName(u"horizontalFrame_instName")
        horizontalFrame_instName.setStyleSheet(u"border:None;\n"
"background-color:None;")
        setattr(self, f"horizontalFrame_instName{name_inst}",horizontalFrame_instName)
        horizontalFrame_instName_name = getattr(self, f"horizontalFrame_instName{name_inst}" ) 
        del horizontalFrame_instName

        horizontalLayout_4 = QHBoxLayout(horizontalFrame_instName_name)
        horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        setattr(self, f"horizontalLayout_4{name_inst}",horizontalLayout_4)
        horizontalLayout_4_name = getattr(self, f"horizontalLayout_4{name_inst}" )       
        del horizontalLayout_4

        inst_name = QLabel(horizontalFrame_instName_name)
        inst_name.setObjectName(u"inst_name")
        inst_name.setMinimumSize(QSize(0, 25))
        inst_name.setMaximumSize(QSize(16777215, 25))
        inst_name.setStyleSheet(u"color:rgba(255,255,255,1);\n"
"font-weight:bold;\n"
"font-size:20px;\n"
"background-color:None;\n"
"\n"
"border:none;\n"
"border-radius:7px;")
        setattr(self, f"inst_name{name_inst}",inst_name)
        inst_name_name = getattr(self, f"inst_name{name_inst}" )  
        del inst_name
        
        
        horizontalLayout_4_name.addWidget(inst_name_name)

        label_type_burse = QLabel(horizontalFrame_instName_name)
        label_type_burse.setObjectName(u"label")
        label_type_burse.setStyleSheet(u"color:rgba(255,255,255,1);\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"background-color:None;\n"
"margin-left:4px;\n"
"border:none;\n"
"border-radius:7px;")
        setattr(self, f"label_type_burse{name_inst}",label_type_burse)
        label_type_burse_name = getattr(self, f"label_type_burse{name_inst}" )  
        del label_type_burse

        horizontalLayout_4_name.addWidget(label_type_burse_name)

        label_name_burse = QLabel(horizontalFrame_instName_name)
        label_name_burse.setObjectName(u"label_2")
        label_name_burse.setStyleSheet(u"color:rgba(255,255,255,1);\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"background-color:None;\n"
"margin-left:4px;\n"
"border:none;\n"
"border-radius:7px;")
        setattr(self, f"label_name_burse{name_inst}",label_name_burse)
        label_name_burse_name = getattr(self, f"label_name_burse{name_inst}" ) 
        
        horizontalLayout_4_name.addWidget(label_name_burse_name)
        


        frame = QFrame(horizontalFrame_instName_name)
        frame.setObjectName(u"frame")
        frame.setMinimumSize(QSize(1, 0))
        frame.setMaximumSize(QSize(1, 16777215))
        frame.setStyleSheet(u"background-color:#4F4F4F;")
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setFrameShadow(QFrame.Raised)

        setattr(self, f"frame{name_inst}",frame)
        frame_name = getattr(self, f"frame{name_inst}" ) 

        horizontalLayout_4_name.addWidget(frame_name)

        balance_bot_now = QLabel(horizontalFrame_instName_name)
        balance_bot_now.setObjectName(u"balance_bot_now")
        balance_bot_now.setMaximumSize(QSize(120, 99999))
        balance_bot_now.setStyleSheet(u"color:rgba(255,255,255,1);\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"background-color:None;\n"
"margin-left:4px;\n"
"border:none;\n"
"border-radius:7px;")

        setattr(self, f"balance_bot_now{name_inst}",balance_bot_now)
        balance_bot_now_name = getattr(self, f"balance_bot_now{name_inst}" ) 

        horizontalLayout_4_name.addWidget(balance_bot_now_name)

        horizontalLayout_for_upperInfo_name.addWidget(horizontalFrame_instName_name, 0, Qt.AlignLeft)

        horizontlFrame_date = QFrame(bot_widget_name)
        horizontlFrame_date.setObjectName(u"horizontlFrame_date")
        horizontlFrame_date.setStyleSheet(u"border:None;\n"
"background-color:None;")
        setattr(self, f"horizontlFrame_date{name_inst}",horizontlFrame_date)
        horizontlFrame_date_name = getattr(self, f"horizontlFrame_date{name_inst}" )     

        horizontalLayout_2 = QHBoxLayout(horizontlFrame_date_name)
        horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        setattr(self, f"horizontalLayout_2{name_inst}",horizontalLayout_2)
        horizontalLayout_2_name = getattr(self, f"horizontalLayout_2{name_inst}" )   

        balance_bot_be = QLabel(horizontlFrame_date_name)
        balance_bot_be.setObjectName(u"balance_bot_be")
        balance_bot_be.setMaximumSize(QSize(100, 16777215))
        balance_bot_be.setStyleSheet(u"color:rgba(255,255,255,1);\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"background-color:None;\n"
"margin-left:4px;\n"
"border:none;\n"
"border-radius:7px;")
        setattr(self, f"balance_bot_be{name_inst}",balance_bot_be)
        balance_bot_be_name = getattr(self, f"balance_bot_be{name_inst}" )  

        horizontalLayout_2_name.addWidget(balance_bot_be_name)

        date_info = QLabel(horizontlFrame_date_name)
        date_info.setObjectName(u"date_info")
        date_info.setMaximumSize(QSize(250, 16777215))
        date_info.setStyleSheet(u"color:rgba(255,255,255,1);\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"background-color:None;\n"
"margin-left:4px;\n"
"border:none;\n"
"border-radius:7px;")
        setattr(self, f"date_info{name_inst}",date_info)
        date_info_name = getattr(self,  f"date_info{name_inst}" )  

        horizontalLayout_2_name.addWidget(date_info_name)


        horizontalLayout_for_upperInfo_name.addWidget(horizontlFrame_date_name, 0, Qt.AlignRight)


        verticalLayout_for_text_name.addLayout(horizontalLayout_for_upperInfo_name)

        horizontalLayout_mainInfo = QHBoxLayout()
        horizontalLayout_mainInfo.setObjectName(u"horizontalLayout_mainInfo")
        setattr(self, f"horizontalLayout_mainInfo{name_inst}",horizontalLayout_mainInfo)
        horizontalLayout_mainInfo_name = getattr(self,  f"horizontalLayout_mainInfo{name_inst}" )  


        verticalLayout_left = QVBoxLayout()
        verticalLayout_left.setObjectName(u"verticalLayout_left")
        setattr(self, f"verticalLayout_left{name_inst}",verticalLayout_left)
        verticalLayout_left_name = getattr(self,  f"verticalLayout_left{name_inst}" )   

        table_deals = QTableView(bot_widget_name)
        table_deals.setObjectName(u"table_deals")
        table_deals.setStyleSheet(u"border:None;")
        setattr(self, f"table_deals{name_inst}",table_deals)
        table_deals_name = getattr(self,  f"table_deals{name_inst}" )  

        verticalLayout_left_name.addWidget(table_deals_name)

        Info_strat_line = QTextBrowser(bot_widget_name)
        Info_strat_line.setObjectName(u"Info_strat_line")
        Info_strat_line.setMaximumSize(QSize(16777215, 40))
        Info_strat_line.setStyleSheet(u"font-size:15px;\n"
"border:None;")
        setattr(self, f"Info_strat_line{name_inst}",Info_strat_line)
        Info_strat_line_name = getattr(self,  f"Info_strat_line{name_inst}" )  

        verticalLayout_left_name.addWidget(Info_strat_line_name)


        horizontalLayout_mainInfo_name.addLayout(verticalLayout_left_name)

        verticalGroupBox_right = QGroupBox(bot_widget_name)
        verticalGroupBox_right.setObjectName(u"verticalGroupBox_right")
        verticalGroupBox_right.setMaximumSize(QSize(600, 16777215))
        verticalGroupBox_right.setStyleSheet(u"border:None;")
        setattr(self, f"verticalGroupBox_right{name_inst}",verticalGroupBox_right)
        verticalGroupBox_right_name = getattr(self,  f"verticalGroupBox_right{name_inst}" ) 

        verticalLayout_5 = QVBoxLayout(verticalGroupBox_right_name)
        verticalLayout_5.setSpacing(3)
        verticalLayout_5.setObjectName(u"verticalLayout_5")
        setattr(self, f"verticalLayout_5{name_inst}",verticalLayout_5)
        verticalLayout_5_name = getattr(self,  f"verticalLayout_5{name_inst}" ) 


        tableView_stratInfo = QTableView(verticalGroupBox_right_name)
        tableView_stratInfo.setObjectName(u"tableView_stratInfo")
        tableView_stratInfo.setStyleSheet(u"border:none;")
        setattr(self, f"tableView_stratInfo{name_inst}",tableView_stratInfo)
        tableView_stratInfo_name = getattr(self,  f"tableView_stratInfo{name_inst}" ) 


        verticalLayout_5_name.addWidget(tableView_stratInfo_name)

        horizontalFrame_bt = QFrame(verticalGroupBox_right_name)
        horizontalFrame_bt.setObjectName(u"horizontalFrame_bt")
        horizontalFrame_bt.setStyleSheet(u"background-color:#404040;\n"
"border:None;")
        setattr(self, f"horizontalFrame_bt{name_inst}",horizontalFrame_bt)
        horizontalFrame_bt_name = getattr(self,  f"horizontalFrame_bt{name_inst}" )         

        horizontalLayout_6 = QHBoxLayout(horizontalFrame_bt_name)
        horizontalLayout_6.setSpacing(1)
        horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        horizontalLayout_6.setContentsMargins(-1, 3, -1, 0)
        setattr(self, f"horizontalLayout_6{name_inst}",horizontalLayout_6)
        horizontalLayout_6_name = getattr(self,  f"horizontalLayout_6{name_inst}" ) 
        
#         bt_start = QPushButton(self.horizontalFrame_bt)
#         bt_start.setObjectName(f"bt_start")
#         bt_start.setMinimumSize(QSize(165, 35))
#         bt_start.setMaximumSize(QSize(125, 35))
#         bt_start.setStyleSheet(u"QPushButton{\n"
# "color:#FFFFFF;\n"
# "font-weight:bold;\n"
# "background-color:#202020;\n"
# "border:2px solid rgba(103,103,101,20);\n"
# "border-radius:10px;\n"
# "margin-left:7px;\n"
# "}\n"
# "\n"
# "\n"
# "QPushButton:hover{\n"
# "background-color:#313131;\n"
# "border:2px solid rgba(103,103,101,40);\n"
# "}\n"
# "\n"
# "QPushButton:pressed{\n"
# "background-color:#3D3B3B;\n"
# "border:2px solid rgba(103,103,101,70);\n"
# "}\n"
# "")
        bt_start = QPushButton(horizontalFrame_bt_name)
        bt_start.setObjectName(f"bt_start{name_inst}")
        bt_start.setMinimumSize(QSize(165, 35))
        bt_start.setMaximumSize(QSize(125, 35))
        bt_start.setStyleSheet(u"QPushButton{\n"
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
        
        setattr(self, f"bt_start{name_inst}",bt_start)
        bt_start_name = getattr(self,  f"bt_start{name_inst}" ) 
        
        horizontalLayout_6_name.addWidget(bt_start_name, 0, Qt.AlignHCenter)
        
        bt_update = QPushButton(horizontalFrame_bt_name)
        bt_update.setObjectName(f"bt_update{name_inst}")
        bt_update.setMinimumSize(QSize(165, 35))
        bt_update.setMaximumSize(QSize(150, 35))
        bt_update.setLayoutDirection(Qt.LeftToRight)
        bt_update.setStyleSheet(u"QPushButton{\n"
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
        
        setattr(self, f"bt_update{name_inst}",bt_update)
        bt_update_name = getattr(self,  f"bt_update{name_inst}" )

        horizontalLayout_6_name.addWidget(bt_update_name, 0, Qt.AlignHCenter)

        bt_delete = QPushButton(horizontalFrame_bt_name)
        bt_delete.setObjectName(f"bt_delete{name_inst}")
        bt_delete.setMinimumSize(QSize(165, 35))
        bt_delete.setMaximumSize(QSize(125, 35))
        bt_delete.setStyleSheet(u"QPushButton{\n"
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
        
        setattr(self, f"bt_delete{name_inst}",bt_delete)
        bt_delete_name = getattr(self,  f"bt_delete{name_inst}" )

        horizontalLayout_6_name.addWidget(bt_delete_name, 0, Qt.AlignHCenter)


        verticalLayout_5_name.addWidget(horizontalFrame_bt_name)


        horizontalLayout_mainInfo_name.addWidget(verticalGroupBox_right_name)


        verticalLayout_for_text_name.addLayout(horizontalLayout_mainInfo_name)
        
    
        

        horizontalLayout_main_name.addLayout(verticalLayout_for_text_name)


        horizontalLayout_3_name.addLayout(horizontalLayout_main_name)


        self.verticalLayout_2.addWidget(bot_widget_name)

        # self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        
        inst_name_name.setText(QCoreApplication.translate("MainWindow", f"{name_inst}", None))
        label_type_burse_name.setText(QCoreApplication.translate("MainWindow", f"{type_burse}", None))
        label_name_burse_name.setText(QCoreApplication.translate("MainWindow", f"{name_burse}", None))
        balance_bot_now_name.setText(QCoreApplication.translate("MainWindow", f"{balance_bot} $", None))
        balance_bot_be_name.setText(QCoreApplication.translate("MainWindow", f"{balance_bot} $", None))
        # self.date_info.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u044f:14.02.2022", None))
        date_info_name.setText(QCoreApplication.translate("MainWindow", f"{date}", None))
#if QT_CONFIG(whatsthis)
        Info_strat_line_name.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        Info_strat_line_name.setHtml(QCoreApplication.translate("MainWindow", f"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Eirik Raudel'; font-size:15px; font-weight:400; font-style:normal;\">\n"
f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:15px; font-weight:bold; color:#ffffff;\">{info_strategies}</span></p></body></html>", None))
        bt_start_name.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c", None))
        bt_update_name.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        bt_delete_name.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        

        

        # bt_start_name.clicked.connect(lambda name = name_inst, bt_start_name = bt_start_name: self.start_bot(bt_start_name, name))
        # self.create_connection_bt(name_inst,bt_start_name)
        
        

         # self.create_connection_bt(self)

            # self.bt_start.clicked.connect(lambda name = name_inst: self.start_bot(name_inst,self.bt_start))
            

    # /////////////////////////////////////////////////////////////////////////////////////
    # /////////////////////////////////////////////////////////////////////////////////////
    # /////////////////////////////////////////////////////////////////////////////////////
    # /////////////////////////////////////////////////////////////////////////////////////
    # /////////////////////////////////////////////////////////////////////////////////////

    # Функция для добавления бота в скрол ареа в качестве виджета

# /////////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////////    
# /////////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////////


    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Calibri ", None))
        self.bt_add_bot.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0431\u043e\u0442\u0430", None))
        self.bt_add_API.setText(QCoreApplication.translate("MainWindow", u"\u0423\u043a\u0430\u0437\u0430\u0442\u044c AIP \u043a\u043b\u044e\u0447", None))
        self.balance_acc.setText(QCoreApplication.translate("MainWindow", f"Баланс: None", None))
        self.system_info.setText(QCoreApplication.translate("MainWindow", f"CPU {psutil.cpu_percent(0.1)} | RAM {psutil.virtual_memory()[2]}%", None))
    # retranslateUi

