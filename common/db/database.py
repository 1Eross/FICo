import psycopg2
import logging
from datetime import datetime
from config.config import DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT, DB_USER

self_db_password = "admin"

class dataBase:
    #Подумать над передачей файлов (скорее всего json)
    #Чтобы код работал, надо поменять пароль во всех функциях 
    
    @staticmethod #работает
    def find_user (login: str, password: str) -> list[tuple]: #поиск пользователя в таблице
        conn = None
        cur = None
        try:
            conn = psycopg2.connect(
                database=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD,
                host=DB_HOST,
                port=DB_PORT)
            cur = conn.cursor()
            cur.execute(f"SELECT * FROM user_account WHERE user_login = '{login}' AND user_password = '{password}'")
            result = cur.fetchall()
            return result
        except psycopg2.Error as e:
            logging.error(f"user search error: {e}")
            print(f"error: {e}")
            return None
        finally:    
            if conn:
                conn.close()
            if cur:
                cur.close()
    
    @staticmethod #работает
    def find_user_in_database_by_login (login: str) -> bool: #если есть в базе - true, если нет - false
        conn = None
        cur = None
        try:
            conn = psycopg2.connect(
                database=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD,
                host=DB_HOST,
                port=DB_PORT)
            cur = conn.cursor()
            cur.execute(f"SELECT * FROM user_account WHERE user_login = '{login}'")
            result = cur.fetchall()
            if (result == []):
                return False
            else:
                return True
        except psycopg2.Error as e:
            logging.error(f"user search error: {e}")
            return None
        finally:    
            if conn:
                conn.close()
            if cur:
                cur.close()
    
    @staticmethod #
    def find_category () -> None:
        pass
    
    @staticmethod #работает
    def add_new_user (login: str, password: str, email: str | None, phoneNumber: str | None,
                   FNameLName: str | None, token: str | None,
                   status: str | None) -> bool: #добавление нового пользователя
        conn = None
        cur = None
        try:
            conn = psycopg2.connect(
                database=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD,
                host=DB_HOST,
                port=DB_PORT)
            cur = conn.cursor()

            cur.execute(f"""INSERT INTO user_account (user_login, user_password, email, phone, user_name, user_token, user_status)
                        VALUES ('{login}', '{password}', '{email}', '{phoneNumber}', '{FNameLName}', '{token}', '{status}')""")
            conn.commit()
            return True
            
        except psycopg2.Error as e:
            logging.error(f"error adding user: {e}")
            return False
        
        finally:            
            if conn:
                conn.close()
            if cur:
                cur.close()
        
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
            database = "postgres",
            user = "postgres",
            password = self_db_password,
            host = "localhost",
            port = 5433
            )
            
            cur = conn.cursor()
            cur.execute(f"""INSERT INTO operation
                        (account_id, user_id, category_id, currency_id, incoming, amount, operation_date, description) 
                        VALUES ({account_id}, {user_id}, {category_id}, {currency_id}, {is_incoming}, {amount}, '{timestamp_value}', '{description}')""")
                        #Может быть ошибка в связи с передачей timestamp_value
            conn.commit()
            return True
        
        except psycopg2.Error as e:
            logging.error(f"Error adding operation: {e}")
            return False
        
        finally:
            if conn:
                conn.close()
            if cur:
                cur.close()
    
    @staticmethod #работает
    def add_new_bank_account (user_id: int, balance: int, currency_id: int, account_name: str) -> bool: #добавление нового кошелька у пользователя
        conn = None
        cur = None
        try:
            conn = psycopg2.connect(
            database = "postgres",
            user = "postgres",
            password = self_db_password,
            host = "localhost",
            port = 5433
            )
            
            cur = conn.cursor()
            cur.execute(f"""INSERT INTO bank_account 
                        (user_id, balance, currency_id, account_name) 
                        VALUES ({user_id}, {balance}, {currency_id}, '{account_name}')""")
            conn.commit()
            return True
        
        except psycopg2.Error as e:
            logging.error(f"Error setting bank account: {e}")
            return False
        
        finally:
            if conn:
                conn.close()
            if cur:
                cur.close()
    
    @staticmethod #работает
    def add_new_category (category_name: str, description: str) -> bool:
        conn = None
        cur = None
        try:
            conn = psycopg2.connect(
            database = "postgres",
            user = "postgres",
            password = self_db_password,
            host = "localhost",
            port = 5433
            )
            
            cur = conn.cursor()
            cur.execute(f"""INSERT INTO general_category
                        (category_name, description) 
                        VALUES ('{category_name}', '{description}')""")
            conn.commit()
            return True
        
        except psycopg2.Error as e:
            logging.error(f"Error adding  new category: {e}")
            return False
        
        finally:
            if conn:
                conn.close()
            if cur:
                cur.close()
    
    @staticmethod #работает 
    def get_all_operations (user_id: int, account_id: int) -> list[tuple]: #получение все операций пользователя
        conn = None
        cur = None
        try:  
            conn = psycopg2.connect(
                    database=DB_NAME,
                    user=DB_USER,
                    password=DB_PASSWORD,
                    host=DB_HOST,
                    port=DB_PORT)
            cur = conn.cursor()
            cur.execute(f"SELECT * FROM operation WHERE user_id = {user_id} AND account_id = {account_id}")
            result = cur.fetchall()
        except psycopg2.Error as e:
            logging.error(f"error receiving all operations: {e}")
            return None
        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()
            return result
    
    @staticmethod #работает
    def get_all_personal_data (user_id: int) -> list[tuple]:
        conn = None
        cur = None
        try:  
            conn = psycopg2.connect(
                    database=DB_NAME,
                    user=DB_USER,
                    password=DB_PASSWORD,
                    host=DB_HOST,
                    port=DB_PORT)
            cur = conn.cursor()
            cur.execute(f"SELECT * FROM user_account WHERE useraccount_id = {user_id}")
            result = cur.fetchall()
        except psycopg2.Error as e:
            logging.error(f"error getting all user data: {e}")
            return None
        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()
            return result
    
    @staticmethod #работает
    def get_all_bank_account (user_id: int) -> list[tuple]: #получение всех кошельков пользователя
        conn = None
        cur = None
        try:  
            conn = psycopg2.connect(
                    database=DB_NAME,
                    user=DB_USER,
                    password=DB_PASSWORD,
                    host=DB_HOST,
                    port=DB_PORT)
            cur = conn.cursor()
            cur.execute(f"SELECT * FROM bank_account WHERE user_id = {user_id}")
            result = cur.fetchall()
            return result
        except psycopg2.Error as e:
            logging.error(f"error getting all bank accounts: {e}")
            return None
        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()
    
    @staticmethod #как должна работать эта функция?  
    def get_all_bank_account_and_operations (user_id: int) -> list[tuple]: #получение все операций пользователя
        conn = None
        cur = None
        try:  
            conn = psycopg2.connect(
                    database=DB_NAME,
                    user=DB_USER,
                    password=DB_PASSWORD,
                    host=DB_HOST,
                    port=DB_PORT)
            cur = conn.cursor()
            cur.execute(f"SELECT * FROM bank_account WHERE user_id = {user_id}") #получаем список кошельков пользователя
            result_bank_account = cur.fetchall()
            for bank in result_bank_account:
                result = dataBase.get_all_operations(user_id, bank[0]) #для каждого id кошелька ищем операции на этом кошельке
            return result
        except psycopg2.Error as e:
            logging.error(f"error receiving all operations: {e}")
            return None
        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()
    
    @staticmethod #работает
    def edit_personal_data (user_id: int, name_column: str, data: str,) -> bool:
        conn = None
        cur = None
        try:
            conn = psycopg2.connect(
            database = "postgres",
            user = "postgres",
            password = self_db_password,
            host = "localhost",
            port = 5433
            )
            
            cur = conn.cursor()
            cur.execute(f"UPDATE user_account SET {name_column} = '{data}' WHERE useraccount_id = {user_id}")
            conn.commit()
            return True
        
        except psycopg2.Error as e:
            logging.error(f"error editing user data: {e}")
            return False
        
        finally:
            if conn:
                conn.close()
            if cur:
                cur.close()
            
    @staticmethod #работает
    def edit_operation (operation_id: int, name_column: str, data: str,) -> bool: #редактирование операции
        conn = None
        cur = None
        try:
            conn = psycopg2.connect(
            database = "postgres",
            user = "postgres",
            password = self_db_password,
            host = "localhost",
            port = 5433
            )
            
            cur = conn.cursor()
            if (name_column == "incoming" or name_column == "amount"): #когда bool в дб нам надо кавычки ставить? 
                cur.execute(f"UPDATE operation SET {name_column} = {data} WHERE operation_id = {operation_id}")
            else:
                cur.execute(f"UPDATE operation SET {name_column} = '{data}' WHERE operation_id = {operation_id}")
            conn.commit()
            return True
        
        except psycopg2.Error as e:
            logging.error(f"Error editing operation: {e}")
            return False
        
        finally:
            if conn:
                conn.close()
            if cur:
                cur.close()
    
    @staticmethod #работает
    def edit_bank_data (bank_account_id: int, name_column: str, data: str,) -> bool: #редактирование операции
        conn = None
        cur = None
        try:
            conn = psycopg2.connect(
            database = "postgres",
            user = "postgres",
            password = self_db_password,
            host = "localhost",
            port = 5433
            )
            
            cur = conn.cursor()
            if (name_column == "balance"):
                cur.execute(f"UPDATE bank_account SET {name_column} = {data} WHERE bank_account_id = {bank_account_id}")
            else:
                cur.execute(f"UPDATE bank_account SET {name_column} = '{data}' WHERE bank_account_id = {bank_account_id}")
            conn.commit()
            return True
        
        except psycopg2.Error as e:
            logging.error(f"error editing bank account: {e}")
            return False
        
        finally:
            if conn:
                conn.close()
            if cur:
                cur.close()
    
    @staticmethod #работает
    def edit_category (category_id: int, name_column: str, data: str,) -> bool: #редактирование операции
        conn = None
        cur = None
        try:
            conn = psycopg2.connect(
            database = "postgres",
            user = "postgres",
            password = self_db_password,
            host = "localhost",
            port = 5433
            )
            
            cur = conn.cursor()
            cur.execute(f"UPDATE general_category SET {name_column} = '{data}' WHERE category_id = {category_id}")
            conn.commit()
            return True
        
        except psycopg2.Error as e:
            logging.error(f"category editing error: {e}")
            return False
        
        finally:
            if conn:
                conn.close()
            if cur:
                cur.close()
    
    @staticmethod #работает
    def delete_operation (operation_id: int) -> bool: #удаление оперделённой операции 
        #id операции есть на фронте, поэтому норм 
        conn = None
        cur = None
        try:
            conn = psycopg2.connect(
            database = "postgres",
            user = "postgres",
            password = self_db_password,
            host = "localhost",
            port = 5433
            )
            
            cur = conn.cursor()
            cur.execute(f"DELETE FROM operation WHERE operation_id = {operation_id}")
            conn.commit()
            return True
        
        except psycopg2.Error as e:
            logging.error(f"Error deleting operation: {e}")
            return False
        
        finally:
            if conn:
                conn.close()
            if cur:
                cur.close()
        
    @staticmethod #работает
    def delete_category (category_id: int) -> bool: #удаление оперделённой операции 
        #id категории есть на фронте, поэтому норм 
        conn = None
        cur = None
        try:
            conn = psycopg2.connect(
            database = "postgres",
            user = "postgres",
            password = self_db_password,
            host = "localhost",
            port = 5433
            )
            
            cur = conn.cursor()
            cur.execute(f"DELETE FROM general_category WHERE category_id = {category_id}")
            conn.commit()
            return True
        
        except psycopg2.Error as e:
            logging.error(f"Error deleting category: {e}")
            return False
        
        finally:
            if conn:
                conn.close()
            if cur:
                cur.close()
    
    @staticmethod #работает
    def delete_bank_account (bank_account_id: int) -> bool: #удаление кошелька пользователя
        conn = None
        cur = None
        try:
            conn = psycopg2.connect(
            database = "postgres",
            user = "postgres",
            password = self_db_password,
            host = "localhost",
            port = 5433
            )
            
            cur = conn.cursor()
            cur.execute(f"DELETE FROM operation WHERE account_id = {bank_account_id}") #удаление всех операций в этом кошельке
            conn.commit()
            cur.execute(f"DELETE FROM bank_account WHERE bank_account_id = {bank_account_id}") #удаление кошелька пользователя
            conn.commit()
            return True
        except psycopg2.Error as e:
            logging.error(f"error deleting bank account: {e}")
            return False
        
        finally:
            if conn:
                conn.close()
            if cur:
                cur.close()
    
    @staticmethod #работает
    def delete_user (useraccount_id: int) -> bool: #удаление кошелька пользователя
        conn = None
        cur = None
        try:
            conn = psycopg2.connect(
            database = "postgres",
            user = "postgres",
            password = self_db_password,
            host = "localhost",
            port = 5433
            )
            
            cur = conn.cursor()
            cur.execute(f"DELETE FROM user_account WHERE useraccount_id = {useraccount_id}") #удаление пользователя
            conn.commit()
            cur.execute(f"DELETE FROM bank_account WHERE user_id = {useraccount_id}") #удаление всех кошельков пользователя
            conn.commit()
            cur.execute(f"DELETE FROM operation WHERE user_id = {useraccount_id}") #удаление всех операций пользователя
            conn.commit()
            return True
        except psycopg2.Error as e:
            logging.error(f"user deletion error: {e}")
            return False
        
        finally:
            if conn:
                conn.close()
            if cur:
                cur.close()
    
    
    #функция добавления новой валюты?
    #функции удаления пользователя, операции, счёта, валюты и т.д?
    #функция редактирования данных у пользователя (непонятно как её сделать, как понять что человек на фронте поменял)
    #функции редактирования других данных, нужны ли? 
    #