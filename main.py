import sys

import asyncio

from typing import Optional

from cryptography.fernet import Fernet

from shutil import copy2



from PySide6 import QtWidgets
import PySide6.QtCore

import PySide6.QtGui
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtSql import QSqlTableModel

from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QVBoxLayout, QWidget,QTableView, QGroupBox, QTextBrowser)

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, QThread, Signal, Slot )

import os , psutil

from threading import Thread
import multiprocessing as mp
import time

from binance.client import Client
from time import sleep
from window.mainWindow import Ui_MainWindow
from window.add_botWindow import Ui_AddbotWindow
from window.add_APIWindow import Ui_AddapiWindow
from connection import Data
from connectionAPI import DataAPI


from datetime import datetime


basedir = os.path.dirname(__file__)

try:
    from ctypes import windll  # Only exists on Windows.
    myappid = 'mycompany.myproduct.subproduct.version'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass


# Step 1: Create a worker class




# class Worker(QObject):
#     def do_work(self,funk,date, name_inst, info_strategies, balance_bot, file_derictory, type_burse, name_burse):
        
#         funk(date, name_inst, info_strategies, balance_bot, file_derictory, type_burse, name_burse)



class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent=parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Создаём экземпляр класса для работы с бд
        
        self.conn = Data()
        self.connApi = DataAPI()
        
        # self.ui.set(self.conn)



        # self.ui.bt_add_bot.clicked.connect(self.open_add_botWindow())
        # Открытие окна
        self.ui.bt_add_bot.clicked.connect(lambda btn = self.ui.bt_add_bot: self.open_add_botWindow(btn))
        self.ui.bt_add_API.clicked.connect(lambda btn = self.ui.bt_add_API: self.open_add_APIWindow(btn))
        self.ui.setupBots_fromBd(self.conn)
    #     self.ui.bt_start2.clicked.connect(self.test2)
    #     self.ui.bt_start223.clicked.connect(self.test223)
    # def test2(self):
    #     print("2")
    # def test223(self):
    #     print("Копка223")



        # Функция для сохранения бота в нужный каталог бд 
    def copy_file(self , src , name):
            copy2(src,f"database/bots/{name}_bot.py")
            
            return f"database/bots/{name}_bot.py"


        # Открытие окна для ввода пути файла
    def open_file(self):
            res = QtWidgets.QFileDialog.getOpenFileName(self,"Open file","/", "PY file(*.py)" )
            # Очень важная функция для отображения активного окна после открытия окна выбор файла
            self.new_window.activateWindow()
            self.ui_window.file_input_res.setText(res[0])
            
            
        # Открытие окна добавления API
    def open_add_APIWindow(self,btn):
            self.new_window = QtWidgets.QDialog()
            self.ui_window = Ui_AddapiWindow()
            self.ui_window.setupUi(self.new_window)
            self.new_window.show()
            
            self.ui_window.bt_add_api.clicked.connect(self.add_API)
        
    def get_secretKey(self):
        with open("database/key.txt", "r") as file:
            first_lale = file.readline()
            
            return first_lale              
    def add_API(self):
            cipher = Fernet(self.get_secretKey())
            binanceAPI = bytes(str(self.ui_window.line_binanceAPI_edit.text()), encoding = ('utf-8'))
            binanceSecretKey = bytes(str(self.ui_window.line_binanceSecretkey_edit.text()), encoding = ('utf-8'))
            bybitAPI = bytes(str(self.ui_window.line_bybitAPI_edit.text().encode('utf-8')), encoding = ('utf-8') )
            bybitSecretKey = bytes(str(self.ui_window.line_binanceSecretkey_edit.text()), encoding= ('utf-8'))
            
            api_data = f"Binance-{cipher.encrypt(binanceAPI)}({cipher.encrypt(binanceSecretKey)}) Bybit-{cipher.encrypt(bybitAPI)}({cipher.encrypt(bybitSecretKey)})"
            self.connApi.add_api_data(api_data)

            
            self.new_window.close()


        # Открытие окна довабления бота
    def open_add_botWindow(self,btn):
            
            self.new_window = QtWidgets.QDialog()
            self.ui_window = Ui_AddbotWindow()
            self.ui_window.setupUi(self.new_window)
            
            self.new_window.show()
            # Какую кнопку нажимает пользователь
            sender = self.sender()
            
            self.ui_window.bt_file_input_enter.clicked.connect(self.open_file)
            self.ui_window.bt_add_bot.clicked.connect(self.add_newBot)


    def add_newBot(self):
            # Записть в базу данных
            date = str(datetime.now())[:16]
            name_inst = self.ui_window.name_tool_enter.text()
            info_strategies = self.ui_window.info_stratege_enter.text()
            balance_bot = self.ui_window.balance_enter.text()
            file_derictory = self.copy_file(self.ui_window.file_input_res.text(), self.ui_window.name_tool_enter.text())
            type_burse = self.ui_window.select_item.currentText()
            name_burse = self.ui_window.select_burse.currentText()

            self.conn.add_new_bot_toDB(date, name_inst, info_strategies, balance_bot, file_derictory, type_burse, name_burse)
        
            # self.worker.do_work(self.create_widget_bot,date, name_inst, info_strategies, balance_bot, file_derictory, type_burse, name_burse)
            self.ui.create_widget_bot(date, name_inst, info_strategies, balance_bot, file_derictory, type_burse, name_burse)
            bt_start = getattr(self.ui,  f"bt_start{name_inst}" )
            bt_update = getattr(self.ui,  f"bt_update{name_inst}" ) 
            bt_delete = getattr(self.ui,  f"bt_delete{name_inst}" ) 
            self.ui.create_connection_bt(name_inst, bt_start, bt_delete, bt_update ,self.conn)
            
            
            
            self.new_window.close()
            

    # # Создание конектов кнопок
    #     def create_connection_bt(self,bt_start):
    #         # bt_start = self.findChild(QPushButton, f"bt_start{name_inst}")
            
            

    #         # bt_start.clicked.connect(self.start_bot(name_inst,bt_start))
    #         # someone = Comunicate()
    #         # bt_start.clicked.connect(lambda name = name_inst, bt = bt_start: self.start_bot(name, bt))
    #         print()
    #         print("Запущен", bt_start.__dict__)
    #         print()
    #         bt_start.clicked.connect(lambda bt = bt_start: self.start_bot(bt))
            
        





        

            
            # print(os.getcwd())
            # print(f'database/bots/{self.inst_name.text()}_bot.py')
            # subprocess.call(f'database/bots/{self.inst_name}_bot.py')
            # os.startfile(f'/database/bots/{self.inst_name.text()}_bot.py')Screen Color Picker v2.0.exe'"Каталог1"\"Каталог2"\"Нужный файл"'
            
            # os.startfile(f"{os.getcwd()}\\database\\bots\\text.txt")
            # if bt_start.text() == "Запустить":    
            #     os.startfile(f"database\\bots\\{name}_bot.py")
            #     bt_start.setText("Остановить")
            # else:
            #     bt_start.setText("Запустить")





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
#     Вместо функции создовать класс
#     совершать конкт к новой созданой кнопке по обджект name



    

    def mouseDoubleClickEvent(self,ev):
        
        self.ui.refresh_info_lowerPanel()
        
        return super().mouseDoubleClickEvent(ev)

if __name__ =="__main__":
    app = QApplication(sys.argv)
    
    
    app.setStyle("Fusion")
    
    window = MainWindow()

    window.show()

    app.exec()
    
