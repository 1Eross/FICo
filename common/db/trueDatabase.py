import psycopg2
try:
    # пытаемся подключиться к базе данных
    connection = psycopg2.connect(dbname='FICo', user='postgres', password='#M135246i#', host='localhost') #не трогайте пж мой пароль и название моей дб, если будете менять на свою то мои данные сюда закоментите. 
    cursor = connection.cursor()
    cursor.execute("SELECT version();")
    print(f"Server version: {cursor.fetchone()}") 
    
except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection == True:
        cursor.close()
        print("[INFO] PostgreSQL connection closed")