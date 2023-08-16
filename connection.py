from PySide6 import QtWidgets,QtSql
from datetime import datetime
class Data:

    def __init__(self):
        super(Data, self).__init__()
        self.db = None
        self.create_connection()

# Создание бд
    def create_connection(self):
        self.db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("database/bots_db.db")
        

        #Если не открывется выводить ошибку
        if not self.db.open():
            QtWidgets.QMessageBox.critical(None,"Не удалось открыть базу данных",
                                           "Нажми Cancel чтобы выйти",QtWidgets.QMessageBox.Cancel)
            return False
        # Создания основной таблицы со всеми добавленными ботами
    def create_main_table_bd(self):    
        # Подключение к бд и создание таблицы если её нету
        quary = QtSql.QSqlQuery()
        quary.exec("CREATE TABLE IF NOT EXISTS BOTS_info(ID integer primary key AUTOINCREMENT, Date VARCHAR(20), "
                   "Name_inst VARCHAR(20), Info_strategies VARCHAR(100), Balance_bot VARCHAR(20), File_directory VARCHAR(100), Type_burse VARCHAR(20), Name_burse VARCHAR(20))")            
        return True 
    
# Создание отдельной таблицы со сделками бота
    def create_bot_table_deals(self,name):
        quary = QtSql.QSqlQuery()
        quary.exec(f"CREATE TABLE IF NOT EXISTS Bots_{name}_deals_info(Время VARCHAR(20), "
                   "Тип_сделки VARCHAR(20), Цена VARCHAR(100), Объём VARCHAR(20), Комиссия VARCHAR(100), pnl VARCHAR(20))")            
        return True 
    
# Создание отдельной таблицы для подсчёта информации о сделках 

    def create_bot_table_deals_Info(self,name):
        quary = QtSql.QSqlQuery()
        quary.exec(f"CREATE TABLE IF NOT EXISTS Bots_{name}_All_deals_info(Время VARCHAR(20), "
                   "Тип_сделки VARCHAR(20), Цена VARCHAR(100), Объём VARCHAR(20), Комиссия VARCHAR(100), pnl VARCHAR(20))")
        return True 

# Добавление уникальной сделки в базу данных которая подсчитывает информацию по всем сделкам

    def add_deals_forInfo(self,date, type_d, price, qty, commision, pnl, name_inst, deal_data):
        
        if not self.check_deal_exists(name_inst, deal_data):
            sql_query = f"INSERT INTO Bots_{name_inst}_All_deals_info (Время, Тип_сделки, Цена, Объём, Комиссия, pnl) VALUES(?, ?, ?, ?, ?, ?)"
            self.execute_query_with_params(sql_query, [date, type_d, price, qty, str(round(float(commision),3)) + "$", str(round(float(pnl),3)) + "$"])

# Проверка существует ли слелка в таблицы для подсчёта всей информации о стратегии
    def check_deal_exists(self, name, deal_time):
        sql_query = f"SELECT COUNT(*) FROM Bots_{name}_All_deals_info WHERE Время = ?"
        query = self.execute_query_with_params(sql_query,[deal_time])
        if query.exec_() and query.next():
            return query.value(0) > 0
        return False

# Получение суммы всех сделок
    def get_all_pnl(self,name_inst):
        sql_query = f"SELECT SUM(CAST(pnl AS REAL)) FROM Bots_{name_inst}_All_deals_info"
        result_query = self.execute_query_with_params(sql_query)
        total_pnl_sum = float(0)
        if result_query.isActive() and result_query.next():
            total_pnl_sum = result_query.value(0)
        return total_pnl_sum

# Получение суммы всех сделок за день
    def get_day_pnl(self, name_inst):
        current_date = datetime.today().strftime('%Y-%m-%d')

        sql_query = f"SELECT SUM(CAST(pnl AS REAL)) FROM Bots_{name_inst}_All_deals_info WHERE CAST(pnl AS REAL) > 0 AND DATE(Время) = '{current_date}'"
        query_positive_sum = self.execute_query_with_params(sql_query)

        sql_query = f"SELECT SUM(CAST(pnl AS REAL)) FROM Bots_{name_inst}_All_deals_info WHERE CAST(pnl AS REAL) < 0 AND DATE(Время) = '{current_date}'"
        query_negative_sum = self.execute_query_with_params(sql_query)

        positive_sum = 0.0
        if query_positive_sum.isActive() and query_positive_sum.next():
            positive_sum = query_positive_sum.value(0) or 0.0

        negative_sum = 0.0
        if query_negative_sum.isActive() and query_negative_sum.next():
            negative_sum = query_negative_sum.value(0) or 0.0

        return round(positive_sum - -negative_sum,4)

# Получение количество прибыльных сделок и количество сделок в убыток
    def get_positive_negative_pnl_sum(self, name_inst):
        sql_query = f"SELECT COUNT(*) FROM Bots_{name_inst}_All_deals_info WHERE CAST(pnl AS REAL) > 0"
        query_positive = self.execute_query_with_params(sql_query)

        sql_query = f"SELECT COUNT(*) FROM Bots_{name_inst}_All_deals_info WHERE CAST(pnl AS REAL) < 0"
        query_negative = self.execute_query_with_params(sql_query)

        positive_count = 0
        if query_positive.isActive() and query_positive.next():
            positive_count = query_positive.value(0)

        negative_count = 0
        if query_negative.isActive() and query_negative.next():
            negative_count = query_negative.value(0)

        return positive_count, -negative_count
 
#  Получение количество прибыльных сделок и количество сделок в убыток только в этот день 
    def get_positive_negative_pnl_sum_today(self, name_inst):
        current_date = datetime.today().strftime('%Y-%m-%d')

        sql_query = f"SELECT COUNT(*) FROM Bots_{name_inst}_All_deals_info WHERE CAST(pnl AS REAL) > 0 AND DATE(Время) = '{current_date}'"
        query_positive = self.execute_query_with_params(sql_query)

        sql_query = f"SELECT COUNT(*) FROM Bots_{name_inst}_All_deals_info WHERE CAST(pnl AS REAL) < 0 AND DATE(Время) = '{current_date}'"
        query_negative = self.execute_query_with_params(sql_query)

        positive_count = 0
        if query_positive.isActive() and query_positive.next():
            positive_count = query_positive.value(0) or 0

        negative_count = 0
        if query_negative.isActive() and query_negative.next():
            negative_count = query_negative.value(0) or 0

        return positive_count, -negative_count

# очитска таблицы с ботом
    def clear_bot_bd(self,name):
        query = QtSql.QSqlQuery()
        query.exec(f"DELETE FROM Bots_{name}_deals_info")        
        return True 

# Исполнение запроса для бд(Добавление или удаление)
    def execute_query_with_params(self, sql_query, query_values = None):
        query = QtSql.QSqlQuery()
        query.prepare(sql_query)

            # Если есть значения то добавить в основной запрос
        if query_values is not None:
            for query_value in query_values:
                query.addBindValue(query_value)

        
        query.exec()
        return query
    
    # def execute_read_query(self, sql_query):
    #     query = QtSql.QSqlQuery()
    #     result = None
    #     try:
    #         query.prepare(sql_query)
    #         result = query
    #         return result
    #     except Error as e:
    #         print(f"The error '{e}' occurred")


    def get_all_data(self):
        sql_query = "SELECT * FROM BOTS_INFO"
        query = self.execute_query_with_params(sql_query)
        
        list_bots = []
        while query.next():
            res = []
            for valId in range (1,8):
                res.append(query.value(valId))
            list_bots.append(res)
        return(list_bots)
    
    
    # Получение даты по монете
    def get_token_data(self, name_inst):
        sql_query = "SELECT * FROM BOTS_INFO WHERE Name_inst = ?"
        query = self.execute_query_with_params(sql_query,[name_inst])
        
        if query.next():
            date_value = query.value(1)  

        else:
            print(f"Name_inst '{name_inst}' не найда дата")
        return date_value
    # Получение баланса по монете 
    def get_token_balance(self, name_inst):
        sql_query = "SELECT * FROM BOTS_INFO WHERE Name_inst = ?"
        query = self.execute_query_with_params(sql_query,[name_inst])
        
        if query.next():
            date_value = query.value(4)  

        else:
            print(f"Name_inst '{name_inst}' не найден баланс")
        return date_value


    
    # Запрос для добавлнения бота
    def add_new_bot_toDB(self,date, name_inst, info_strategies, balance_bot, file_derectory, type_burse, name_burse):
        sql_query = "INSERT INTO BOTS_INFO (Date, Name_inst, Info_strategies, Balance_bot, File_directory, Type_burse, Name_burse) VALUES(?, ?, ?, ?, ?, ?, ?)"
        self.execute_query_with_params(sql_query, [date, name_inst, info_strategies, balance_bot, file_derectory, type_burse, name_burse])
    
    #Добавление сделок в базу данных бота    
    def add_bot_deals(self,date, type_d, price, qty, commision, pnl, name_inst):
        sql_query = f"INSERT INTO Bots_{name_inst}_deals_info (Время, Тип_сделки, Цена, Объём, Комиссия, pnl) VALUES(?, ?, ?, ?, ?, ?)"
        
        self.execute_query_with_params(sql_query, [date, type_d, price, qty, str(round(float(commision),3)) + "$", str(round(float(pnl),3)) + "$"])
    
    


    # Запрос для удаление бота
    def delete_bot(self,name_inst):
        sql_query = "DELETE FROM BOTS_INFO WHERE Name_inst=?"
        self.execute_query_with_params(sql_query, [name_inst])

    # Запрос для выведения сумарного баланса ботов
    def get_total_balance_bots(self):
        sql_query = f"SELECT SUM (Balance_bot) FROM BOTS_INFO"

        query = self.execute_query_with_params()
        if query.next():
            return str(query.value(0))
        return "0"