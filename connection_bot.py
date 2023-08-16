from PySide6 import QtWidgets,QtSql



class Bot_bd():


    def __init__(self):
        super(Bot_bd, self).__init__()

    def create_connection_bot(self,name):
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName(f"database/bots/{name}_dir/{name}_bot_db.db")
        

        #Если не открывется выводить ошибку
        if not db.open():
            QtWidgets.QMessageBox.critical(None,"Не удалось открыть базу данных",
                                           "Нажми Cancel чтобы выйти",QtWidgets.QMessageBox.Cancel)
            return False
        # Подключение к бд и создание таблицы если её нету
        quary = QtSql.QSqlQuery()
        quary.exec("CREATE TABLE IF NOT EXISTS Bots_deals_info(ID integer primary key AUTOINCREMENT, Время VARCHAR(20), "
                   "Тип_сделки VARCHAR(20), Цена VARCHAR(100), Объём VARCHAR(20), Комиссия VARCHAR(100), pnl VARCHAR(20))")            
        return True 
    
    def remove_connection(self,db):
        db.removeDatabase()