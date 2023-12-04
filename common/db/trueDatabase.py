import psycopg2
try:
    # пытаемся подключиться к базе данных
    connection = psycopg2.connect(dbname='TestDB', user='postgres', password='#M135246i#', host='localhost') #не трогайте пж мой пароль и название моей дб, если будете менять на свою то мои данные сюда закоментите. 
    cursor = connection.cursor()
    cursor.execute("SELECT version();")
    print(f"Server version: {cursor.fetchone()}") 
    cursor.execute("select * from data_user;") #название бд в 4 и 8 строчке поменять 
    result = cursor.fetchall()
    print(result)
    
    
    
    cursor.close()
    
except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection == True:
        cursor.close()
        print("[INFO] PostgreSQL connection closed")