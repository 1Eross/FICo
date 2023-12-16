import psycopg2

class dataBase:
    @staticmethod
    def findUser(self, login: str, password: str) -> list[tuple]: #поиск пользователя в таблице
        conn = psycopg2.connect(database="FICo", user="postgres",
        password="#M135246i#", host="localhost", port=5432)
        cur = conn.cursor()
        
        cur.execute(f"SELECT * FROM user_account WHERE user_login = '{login}' AND user_password = '{password}'")
        result = cur.fetchall()
        return result
    @staticmethod
    def addNewUser (self, login: str, password: str) -> None:
        conn = psycopg2.connect(database="FICo", user="postgres",
        password="#M135246i#", host="localhost", port=5432)
        cur = conn.cursor()
        
        cur.execute(f"INSERT INTO user_account (user_login, user_password) VALUES ('{login}', '{password}')")
        conn.commit()
    @staticmethod
    def addNewOperation () -> None:
        pass
    @staticmethod
    def findOperations () -> None:
        pass
    @staticmethod
    def addNewBankAccount () -> None:
        pass
    @staticmethod 
    def addNewCategory () -> None:
        pass
    @staticmethod
    def findCategory () -> None:
        pass
    
    
    #функция добавления новой валюты?
    #функции удаления пользователя, операции, счёта, валюты и т.д?
    #функция редактирования данных у пользователя (непонятно как её сделать, как понять что человек на фронте поменял)
    #функции редактирования других данных, нужны ли? 
    #