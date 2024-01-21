import sys
sys.path.append('C:/Users/gripo/PycharmProjects/FiCo')
from common.db.database import *

if __name__ == "__main__":
    # Создаем объекты QueryBuilder и PostgresConnector
    query_builder = QueryBuilder('userAccount')
    postgres_connector = PostgresConnector(
        dbname="postgres",
        user="postgres",
        password="admin",
        host="127.0.0.1",
        port="5432"
    )

    try:
        # Подключаемся к базе данных PostgreSQL
        postgres_connector.connect()

        # Пример CRUD операций
        # SELECT
        select_query = query_builder.select() # ["accountID", "userLogin"]
        result = postgres_connector.execute_query(select_query)
        print("SELECT Result:", result)

        # # INSERT
        # insert_values = {"column1": "value1", "column2": "value2"}
        # insert_query = query_builder.insert(insert_values)
        # result = postgres_connector.execute_query(insert_query, list(insert_values.values()))
        # print("INSERT Result:", result)

        # # UPDATE
        # update_values = {"column1": "new_value1"}
        # update_query = query_builder.update(update_values, "column2 = 'value2'")
        # result = postgres_connector.execute_query(update_query, list(update_values.values()))
        # print("UPDATE Result:", result)

        # # DELETE
        # delete_query = query_builder.delete("column1 = 'new_value1'")
        # result = postgres_connector.execute_query(delete_query)
        # print("DELETE Result:", result)

    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        # Закрываем подключение к базе данных PostgreSQL
        postgres_connector.close_connection()