import psycopg2

def findUser(login: str, password: str):
    conn = psycopg2.connect(database="FICo", user="postgres",
    password="#M135246i#", host="localhost", port=5432)
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM user_account WHERE user_login = '{login}' AND user_password = '{password}'")
    result = cur.fetchall()
    print(result)

findUser("biba", "syka")