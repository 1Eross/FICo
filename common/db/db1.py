import psycopg2

class QueryBuilder:
    def __init__(self, table_name):
        self.table_name = table_name

    def select(self, columns=None):
        if columns:
            columns = ', '.join(columns)
        else:
            columns = '*'
        return f"SELECT {columns} FROM {self.table_name}"

    def insert(self, values):
        columns = ', '.join(values.keys())
        placeholders = ', '.join(['%s'] * len(values))
        return f"INSERT INTO {self.table_name} ({columns}) VALUES ({placeholders}) RETURNING *"

    def update(self, values, condition):
        set_clause = ', '.join([f"{key} = %s" for key in values.keys()])
        return f"UPDATE {self.table_name} SET {set_clause} WHERE {condition} RETURNING *"

    def delete(self, condition):
        return f"DELETE FROM {self.table_name} WHERE {condition} RETURNING *"

class PostgresConnector:
    def __init__(self, dbname, user, password, host, port, log=None):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.log = log
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            self.cursor = self.connection.cursor()
            if self.log:
                self.log.info("Successfully connected to the PostgreSQL database.")
        except Exception as e:
            if self.log:
                self.log.error(f"Connection error: {str(e)}")
            raise

    def execute_query(self, query, parameters=None):
        try:
            if parameters:
                self.cursor.execute(query, parameters)
            else:
                self.cursor.execute(query)
            result = self.cursor.fetchall()
            if self.log:
                self.log.info(f"Query executed successfully: {query}")
            return result
        except Exception as e:
            if self.log:
                self.log.error(f"Query execution error: {str(e)}")
            raise
        finally:
            self.close_connection()

    def close_connection(self):
        if self.connection:
            self.connection.commit()
            self.connection.close()
            if self.log:
                self.log.info("Connection closed.")

# Пример использования:
if __name__ == "__main__":
    # Создаем объекты QueryBuilder и PostgresConnector
    query_builder = QueryBuilder("example_table")
    postgres_connector = PostgresConnector(
        dbname="your_db_name",
        user="your_user",
        password="your_password",
        host="your_host",
        port="your_port"
    )

    try:
        # Подключаемся к базе данных PostgreSQL
        postgres_connector.connect()

        # Пример CRUD операций
        # SELECT
        select_query = query_builder.select(["column1", "column2"])
        result = postgres_connector.execute_query(select_query)
        print("SELECT Result:", result)

        # INSERT
        insert_values = {"column1": "value1", "column2": "value2"}
        insert_query = query_builder.insert(insert_values)
        result = postgres_connector.execute_query(insert_query, list(insert_values.values()))
        print("INSERT Result:", result)

        # UPDATE
        update_values = {"column1": "new_value1"}
        update_query = query_builder.update(update_values, "column2 = 'value2'")
        result = postgres_connector.execute_query(update_query, list(update_values.values()))
        print("UPDATE Result:", result)

        # DELETE
        delete_query = query_builder.delete("column1 = 'new_value1'")
        result = postgres_connector.execute_query(delete_query)
        print("DELETE Result:", result)

    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        # Закрываем подключение к базе данных PostgreSQL
        postgres_connector.close_connection()
