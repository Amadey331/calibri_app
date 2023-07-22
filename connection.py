from PySide6 import QtWidgets,QtSql

class Data:

    def __init__(self):
        super(Data, self).__init__()
        self.create_connection()

# Создание бд
    def create_connection(self):
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("database/bots_db.db")


        #Если не открывется выводить ошибку
        if not db.open():
            QtWidgets.QMessageBox.critical(None,"Не удалось открыть базу данных",
                                           "Нажми Cancel чтобы выйти",QtWidgets.QMessageBox.Cancel)
            return False
        # Подключение к бд и создание таблицы если её нету
        quary = QtSql.QSqlQuery()
        quary.exec("CREATE TABLE IF NOT EXISTS BOTS_info(ID integer primary key AUTOINCREMENT, Date VARCHAR(20), "
                   "Name_inst VARCHAR(20), Info_strategies VARCHAR(100), Balance_bot VARCHAR(20), File_directory VARCHAR(100), Type_burse VARCHAR(20), Name_burse VARCHAR(20))")            
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

    # Запрос для добавлнения бота
    def add_new_bot_toDB(self,date, name_inst, info_strategies, balance_bot, file_derectory, type_burse, name_burse):
        sql_query = "INSERT INTO BOTS_INFO (Date, Name_inst, Info_strategies, Balance_bot, File_directory, Type_burse, Name_burse) VALUES(?, ?, ?, ?, ?, ?, ?)"
        self.execute_query_with_params(sql_query, [date, name_inst, info_strategies, balance_bot, file_derectory, type_burse, name_burse])

    # Запрос для удаление бота
    def delete_bot(self,id):
        sql_query = "DELETE FROM BOTS_INFO WHERE ID=?"
        self.execute_query_with_params(sql_query, [id])

    # Запрос для выведения сумарного баланса ботов
    def get_total_balance_bots(self):
        sql_query = f"SELECT SUM (Balance_bot) FROM BOTS_INFO"

        query = self.execute_query_with_params()
        if query.next():
            return str(query.value(0))
        return "0"