import psycopg2
import logging
from datetime import datetime

self_db_password = "#M135246i#"

class dataBase:
    #Подумать над передачей файлов (скорее всего json)
    #Чтобы код работал, надо поменять пароль во всех функциях 
    
    @staticmethod #работает
    def find_user (login: str, password: str) -> list[tuple]: #поиск пользователя в таблице
        conn = None
        cur = None
        try:
            conn = psycopg2.connect(
                database="FICo",
                user="postgres",
                password=self_db_password,
                host="localhost",
                port=5432)
            cur = conn.cursor()
            cur.execute(f"SELECT * FROM user_account WHERE user_login = '{login}' AND user_password = '{password}'")
            result = cur.fetchall()
        
        except psycopg2.Error as e:
            pass #logoutput
            return None
        finally:    
            if conn:
                conn.close()
            if cur:
                cur.close()
            return result
    
    @staticmethod #работает
    def add_new_user (login: str, password: str, email: str | None, phoneNumber: str | None,
                   FNameLName: str | None, token: str | None,
                   status: str | None) -> bool: #добавление нового пользователя
        conn = None
        cur = None
        try:
            conn = psycopg2.connect(
                database="FICo",
                user="postgres",
                password=self_db_password,
                host="localhost",
                port=5432)
            cur = conn.cursor()

            cur.execute(f"""INSERT INTO user_account (user_login, user_password, email, phone, user_name, user_token, user_status)
                        VALUES ('{login}', '{password}', '{email}', '{phoneNumber}', '{FNameLName}', '{token}', '{status}')""")
            conn.commit()
            
        except psycopg2.Error as e:
            #logOutputError
            print(e)
            return False
        
        finally:            
            if conn:
                conn.close()
            if cur:
                cur.close()
            return True
            #log output
        
    @staticmethod #работает
    def add_new_operation (user_id: int, account_id: int, #добавление новой операции 
                           category_id: int, currency_id: int,
                           is_incoming: bool, amount: int,
                           operation_date: str,  description: str) -> bool: ##Может возвращает id созданной операции ?
        
        timestamp_value = datetime.strptime(operation_date, "%Y-%m-%d %H:%M:%S")
        conn = None
        cur = None
        try:
            conn = psycopg2.connect(
            database = "FICo",
            user = "postgres",
            password = self_db_password,
            host = "localhost",
            port = 5432
            )
            
            cur = conn.cursor()
            cur.execute(f"""INSERT INTO operation
                        (account_id, user_id, category_id, currency_id, incoming, amount, operation_date, description) 
                        VALUES ({account_id}, {user_id}, {category_id}, {currency_id}, {is_incoming}, {amount}, '{timestamp_value}', '{description}')""")
                        #Может быть ошибка в связи с передачей timestamp_value
            conn.commit()
        
        except psycopg2.Error as e:
            pass
            logging.error(f"Error adding operation: {e}")
            return False
        
        finally:
            if conn:
                conn.close()
            if cur:
                cur.close()
            return True
            
    @staticmethod #работает 
    def get_all_operations (user_id: int, account_id: int) -> list[tuple]: #получение все операций пользователя
        conn = None
        cur = None
        try:  
            conn = psycopg2.connect(
                    database="FICo",
                    user="postgres",
                    password=self_db_password,
                    host="localhost",
                    port=5432)
            cur = conn.cursor()
            cur.execute(f"SELECT * FROM operation WHERE user_id = {user_id} AND account_id = {account_id}")
            result = cur.fetchall()
        except psycopg2.Error as e:
            pass #logoutput
            return None
        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()
            return result
    @staticmethod #работает
    def add_new_bank_account (user_id: int, balance: int, currency_id: int, account_name: str) -> bool: #добавление нового кошелька у пользователя
        conn = None
        cur = None
        try:
            conn = psycopg2.connect(
            database = "FICo",
            user = "postgres",
            password = self_db_password,
            host = "localhost",
            port = 5432
            )
            
            cur = conn.cursor()
            cur.execute(f"""INSERT INTO bank_account 
                        (user_id, balance, currency_id, account_name) 
                        VALUES ({user_id}, {balance}, {currency_id}, '{account_name}')""")
            conn.commit()
        
        except psycopg2.Error as e:
            logging.error(f"Error setting bank account: {e}")
            #log output
            return False
        
        finally:
            if conn:
                conn.close()
            if cur:
                cur.close()
            return True
                #наверно ретурн тру или фолс
    
    @staticmethod #работает
    def edit_personal_data (user_id: int, name_column: str, data: str,) -> bool:
        conn = None
        cur = None
        try:
            conn = psycopg2.connect(
            database = "FICo",
            user = "postgres",
            password = self_db_password,
            host = "localhost",
            port = 5432
            )
            
            cur = conn.cursor()
            cur.execute(f"UPDATE user_account SET {name_column} = '{data}' WHERE useraccount_id = {user_id}")
            conn.commit()
            return True
        
        except psycopg2.Error as e:
            #log output
            return False
        
        finally:
            if conn:
                conn.close()
            if cur:
                cur.close()
                #наверно ретурн тру или фолс
            
    
    @staticmethod #работает
    def get_all_personal_data (user_id: int) -> list[tuple]:
        conn = None
        cur = None
        try:  
            conn = psycopg2.connect(
                    database="FICo",
                    user="postgres",
                    password=self_db_password,
                    host="localhost",
                    port=5432)
            cur = conn.cursor()
            cur.execute(f"SELECT * FROM user_account WHERE useraccount_id = {user_id}")
            result = cur.fetchall()
        except psycopg2.Error as e:
            pass #logoutput
            return None
        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()
            return result
    
    @staticmethod #работает
    def add_new_category (category_name: str, description: str) -> bool:
        conn = None
        cur = None
        try:
            conn = psycopg2.connect(
            database = "FICo",
            user = "postgres",
            password = self_db_password,
            host = "localhost",
            port = 5432
            )
            
            cur = conn.cursor()
            cur.execute(f"""INSERT INTO general_category
                        (category_name, description) 
                        VALUES ('{category_name}', '{description}')""")
            conn.commit()
        
        except psycopg2.Error as e:
            logging.error(f"Error adding  new category: {e}")
            pass
            return False
            #log output
        
        finally:
            if conn:
                conn.close()
            if cur:
                cur.close()
            return True
                #наверно ретурн тру или фолс
    
    @staticmethod #
    def find_category () -> None:
        pass
    
    @staticmethod #
    def delete_opereation (operation_id: int) -> bool: #удаление оперделённой операции 
        #id операции есть на фронте, поэтому норм 
        conn = None
        cur = None
        try:
            conn = psycopg2.connect(
            database = "FICo",
            user = "postgres",
            password = self_db_password,
            host = "localhost",
            port = 5432
            )
            
            cur = conn.cursor()
            cur.execute(f"DELETE FROM operation WHERE operation_id = {operation_id}")
            conn.commit()
        
        except psycopg2.Error as e:
            logging.error(f"Error deleting operation: {e}")
            pass
            return False
            #log output
        
        finally:
            if conn:
                conn.close()
            if cur:
                cur.close()
            return True
                #наверно ретурн тру или фолс
        
    @staticmethod #
    def delete_category (category_id: int) -> bool: #удаление оперделённой операции 
        #id категории есть на фронте, поэтому норм 
        conn = None
        cur = None
        try:
            conn = psycopg2.connect(
            database = "FICo",
            user = "postgres",
            password = self_db_password,
            host = "localhost",
            port = 5432
            )
            
            cur = conn.cursor()
            cur.execute(f"DELETE FROM general_category WHERE category_id = {category_id}")
            conn.commit()
        
        except psycopg2.Error as e:
            logging.error(f"Error deleting category: {e}")
            pass
            return False
            #log output
        
        finally:
            if conn:
                conn.close()
            if cur:
                cur.close()
            return True
                #наверно ретурн тру или фолс
    
    @staticmethod #работает
    def delete_bank_account (bank_account_id: int) -> bool: #удаление кошелька пользователя
        conn = None
        cur = None
        try:
            conn = psycopg2.connect(
            database = "FICo",
            user = "postgres",
            password = self_db_password,
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
            return False
        
        finally:
            if conn:
                conn.close()
            if cur:
                cur.close()
            return True
                #наверно ретурн тру или фолс
    
    @staticmethod #работает
    def edit_operation (operation_id: int, name_column: str, data: str,) -> bool: #редактирование операции
        conn = None
        cur = None
        try:
            conn = psycopg2.connect(
            database = "FICo",
            user = "postgres",
            password = self_db_password,
            host = "localhost",
            port = 5432
            )
            
            cur = conn.cursor()
            if (name_column == "incoming" or name_column == "amount"): #когда bool в дб нам надо кавычки ставить? 
                cur.execute(f"UPDATE operation SET {name_column} = {data} WHERE operation_id = {operation_id}")
            else:
                cur.execute(f"UPDATE operation SET {name_column} = '{data}' WHERE operation_id = {operation_id}")

            conn.commit()
        
        except psycopg2.Error as e:
            logging.error(f"Error editing operation: {e}")
            pass
            #log output
            return False
        
        finally:
            if conn:
                conn.close()
            if cur:
                cur.close()
            return True
        
    #функция добавления новой валюты?
    #функции удаления пользователя, операции, счёта, валюты и т.д?
    #функция редактирования данных у пользователя (непонятно как её сделать, как понять что человек на фронте поменял)
    #функции редактирования других данных, нужны ли? 
    #