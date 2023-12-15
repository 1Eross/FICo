import psycopg2

class dataBase:
    @staticmethod
    def findUser(login: str, password: str) -> list[tuple]: #поиск пользователя в таблице
        conn = psycopg2.connect(database="FICo", user="postgres",
        password="#M135246i#", host="localhost", port=5432)
        cur = conn.cursor()
        
        cur.execute(f"SELECT * FROM user_account WHERE user_login = '{login}' AND user_password = '{password}'")
        result = cur.fetchall()
        return result
    @staticmethod
    def addUser (login: str, password: str) -> None:
        conn = psycopg2.connect(database="FICo", user="postgres",
        password="#M135246i#", host="localhost", port=5432)
        cur = conn.cursor()
        
        cur.execute(f"INSERT INTO user_account (user_login, user_password) VALUES ('{login}', '{password}')")
        conn.commit()
        
dataBase.addUser("tymba", "umba")