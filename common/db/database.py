import psycopg2
from psycopg2 import Error

class Database:
    
    def __init__(self, dbname, user, password, host, port) -> None:
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.connection = None
        
    
    def connect(self) -> bool:
        try:
            self.connection = psycopg2.connect(dbname=self.dbname,
                                      user=self.user,
                                      password=self.password,
                                      host=self.host,
                                      port=self.port)
            return True
        except (Error) as error:
            #log has been needed
            return False
        
    def disconnect(self):
        if self.connection:
            self.connection.close()
            self.connection = None

    def execute_query(self, query, params=None):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            return cursor
        except (Error) as error:
            #log has been needed
            return None
        
    def rollback(self):
        if self.connection:
            self.connection.rollback()

    def commit(self):
        if self.connection:
            self.connection.commit()

    ##CRUD operations

    def create_record(self, query, params):
        cursor = self.execute_query(query, params)
        if cursor:
            self.commit()
            cursor.close()

    def read_records(self, query, params=None):
        cursor = self.execute_query(query, params)
        if cursor:
            records = cursor.fetchall()
            return records

    def update_record(self, query, params):
        cursor = self.execute_query(query, params)
        if cursor:
            self.commit()
            cursor.close()

    def delete_record(self, query, params):
        cursor  = self.execute_query()
        if cursor:
            self.commit()
            cursor.close()


    def getUser(user_login: str, user_password: str) -> str:
        sqlQuerry = f"SELECT * FROM \"FICoReg\".user_data\
                        WHERE user_login = '{user_login}' and user_password = '{user_password}'\
                        ORDER BY id ASC"
        return sqlQuerry