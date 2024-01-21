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
    def add_new_user (login: str, password: str) -> None:
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
            conn.close()
            cur.close()
            #log output
        
    @staticmethod
    def add_new_operation (user_id: int, account_id: int,
                           category_id: int, currency_id: int,
                           is_incoming: bool, amount: int,
                           operation_date: str,  ) -> None: ##Может возвращает id созданной операции ?
        
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
                        (account_id, user_id, category_id, currency_id, incoming, amount, operation_date) 
                        VALUES ({account_id}, {user_id}, {category_id}, {currency_id}, {is_incoming}, {amount}, {timestamp_value})")
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
    def get_all_operations (user_id: int, account_id: int) -> list[tuple]:
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
    def add_new_bank_account () -> None:
        pass
    @staticmethod 
    def add_new_category () -> None:
        pass
    @staticmethod
    def find_category () -> None:
        pass
    
    
    #функция добавления новой валюты?
    #функции удаления пользователя, операции, счёта, валюты и т.д?
    #функция редактирования данных у пользователя (непонятно как её сделать, как понять что человек на фронте поменял)
    #функции редактирования других данных, нужны ли? 
    #