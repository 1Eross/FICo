import psycopg2
from datetime import datetime

class dataBase:
    #Подумать над передачей файлов (скорее всего json)
    @staticmethod
    def find_user(login: str, password: str) -> list[tuple]: #поиск пользователя в таблице
        try:
            conn = psycopg2.connect(
                database="FICo",
                user="postgres",
                password="admin",
                host="localhost",
                port=5432)
            cur = conn.cursor()
            cur.execute(f"SELECT * FROM user_account WHERE user_login = '{login}' AND user_password = '{password}'")
            result = cur.fetchall()
        
        except psycopg2.Error as e:
            pass #logoutput
        
        finally:    
            conn.close()
            cur.close()
            return result
    
    @staticmethod
    def add_new_user (login: str, password: str) -> None: #добавление нового пользователя
        try:
            conn = psycopg2.connect(
                database="FICo",
                user="postgres",
                password="admin",
                host="localhost",
                port=5432)
            cur = conn.cursor()

            cur.execute(f"INSERT INTO user_account (user_login, user_password) VALUES ('{login}', '{password}')")
            conn.commit()
            
        except psycopg2.Error as e:
            pass #logOutputError
        
        finally:            
            #return id
            conn.close()
            cur.close()
            #log output
        
    @staticmethod
    def add_new_operation (user_id: int, account_id: int, #добавление новой операции 
                           category_id: int, currency_id: int,
                           is_incoming: bool, amount: int,
                           operation_date: str,  description: str) -> None: ##Может возвращает id созданной операции ?
        
        timestamp_value = datetime.strptime(operation_date, "%Y-%m-%d %H:%M:%S")
        
        try:
            conn = psycopg2.connect(
            database = "FICo",
            user = "postgres",
            password = "admin",
            host = "localhost",
            port = 5432
            )
            
            cur = conn.cursor()
            cur.execute(f"INSERT INTO operation 
                        (account_id, user_id, category_id, currency_id, incoming, amount, operation_date, description) 
                        VALUES ({account_id}, {user_id}, {category_id}, {currency_id}, {is_incoming}, {amount}, '{timestamp_value}', '{description}')")
                        #Может быть ошибка в связи с передачей timestamp_value
            conn.commit()
        
        except psycopg2.Error as e:
            pass
            #log output
        
        finally:
            if conn:
                conn.close()
            if cur:
                cur.close()
            
    @staticmethod
    def get_all_operations (user_id: int, account_id: int) -> list[tuple]: #получение все операций пользователя
        try:  
            conn = psycopg2.connect(
                    database="FICo",
                    user="postgres",
                    password="admin",
                    host="localhost",
                    port=5432)
            cur = conn.cursor()
            cur.execute(f"SELECT * FROM operation WHERE user_id = {user_id} AND account_id = {account_id}")
            result = cur.fetchall()
            return result
        except psycopg2.Error as e:
            pass #logoutput
        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()
            
    @staticmethod
    def add_new_bank_account (user_id: int, balance: int, currency: str, account_name: str) -> None: #добавление нового кошелька у пользователя
        try:
            conn = psycopg2.connect(
            database = "FICo",
            user = "postgres",
            password = "admin",
            host = "localhost",
            port = 5432
            )
            
            cur = conn.cursor()
            cur.execute(f"INSERT INTO bank_account 
                        (user_id, balance, currency, account_name) 
                        VALUES ({user_id}, {balance}, '{currency}', '{account_name}')")
            conn.commit()
        
        except psycopg2.Error as e:
            pass
            #log output
        
        finally:
            if conn:
                conn.close()
            if cur:
                cur.close()
                #наверно ретурн тру или фолс
    
    @staticmethod 
    def edit_personal_data (user_id: int, name_column: str, data: str,) -> None:
        try:
            conn = psycopg2.connect(
            database = "FICo",
            user = "postgres",
            password = "admin",
            host = "localhost",
            port = 5432
            )
            
            cur = conn.cursor()
            cur.execute(f"UPRDATE user_account SET '{name_column}' = '{data}' WHERE useraccount_id = {user_id}")
            conn.commit()
        
        except psycopg2.Error as e:
            pass
            #log output
        
        finally:
            if conn:
                conn.close()
            if cur:
                cur.close()
                #наверно ретурн тру или фолс
    
    @staticmethod
    def get_all_personal_data (user_id: int) -> list[tuple]:
        try:  
            conn = psycopg2.connect(
                    database="FICo",
                    user="postgres",
                    password="admin",
                    host="localhost",
                    port=5432)
            cur = conn.cursor()
            cur.execute(f"SELECT * FROM user_account WHERE useraccount_id = {user_id}")
            result = cur.fetchall()
            return result
        except psycopg2.Error as e:
            pass #logoutput
        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()
    
    @staticmethod 
    def add_new_category (user_id: int, category_name: str, description: str) -> None:
        try:
            conn = psycopg2.connect(
            database = "FICo",
            user = "postgres",
            password = "admin",
            host = "localhost",
            port = 5432
            )
            
            cur = conn.cursor()
            cur.execute(f"INSERT INTO user_category
                        (user_id, category_name, description) 
                        VALUES ({user_id}, '{category_name}', '{description}')")
            conn.commit()
        
        except psycopg2.Error as e:
            pass
            #log output
        
        finally:
            if conn:
                conn.close()
            if cur:
                cur.close()
                #наверно ретурн тру или фолс
    
    @staticmethod
    def find_category () -> None:
        pass
    
    @staticmethod
    def delete_opereation (operation_id: int) -> None: #удаление оперделённой операции 
        #id операции есть на фронте, поэтому норм 
        try:
            conn = psycopg2.connect(
            database = "FICo",
            user = "postgres",
            password = "admin",
            host = "localhost",
            port = 5432
            )
            
            cur = conn.cursor()
            cur.execute(f"DELETE FROM operation WHERE operation_id = {operation_id}")
            conn.commit()
        
        except psycopg2.Error as e:
            pass
            #log output
        
        finally:
            if conn:
                conn.close()
            if cur:
                cur.close()
                #наверно ретурн тру или фолс
    
    @staticmethod
    def delete_bank_account (bank_account_id: int) -> None: #удаление кошелька пользователя
        try:
            conn = psycopg2.connect(
            database = "FICo",
            user = "postgres",
            password = "admin",
            host = "localhost",
            port = 5432
            )
            
            cur = conn.cursor()
            cur.execute(f"DELETE FROM operation WHERE account_id = {bank_account_id}") #удаление всех операций в этом кошельке
            conn.commit()
            cur.execute(f"DELETE FROM bank_account WHERE bank_account_id = {bank_account_id}") #удаление кошелька пользователя
            conn.commit()
        except psycopg2.Error as e:
            pass
            #log output
        
        finally:
            if conn:
                conn.close()
            if cur:
                cur.close()
                #наверно ретурн тру или фолс
    
    @staticmethod 
    def edit_operation (operation_id: int, name_column: str, data: str,) -> None:
        try:
            conn = psycopg2.connect(
            database = "FICo",
            user = "postgres",
            password = "admin",
            host = "localhost",
            port = 5432
            )
            
            cur = conn.cursor()
            if (name_column == "incoming" or name_column == "amount"):
                
            cur.execute(f"UPRDATE operation SET '{name_column}' = '{data}' WHERE operation_id = {operation_id}")
            conn.commit()
        
        except psycopg2.Error as e:
            pass
            #log output
        
        finally:
            if conn:
                conn.close()
            if cur:
                cur.close()
                #наверно ретурн тру или фолс
    #функция добавления новой валюты?
    #функции удаления пользователя, операции, счёта, валюты и т.д?
    #функция редактирования данных у пользователя (непонятно как её сделать, как понять что человек на фронте поменял)
    #функции редактирования других данных, нужны ли? 
    #