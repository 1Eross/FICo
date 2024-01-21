import psycopg2
import logging

logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w")

class Category:
    def __init__(self, categoryID, icon, name):
        self._categoryID = categoryID
        self._icon = icon
        self._name = name

    @property
    def categoryID(self):
        return self._categoryID

    @property
    def icon(self):
        return self._icon

    @property
    def name(self):
        return self._name

    def setCategoryInfo(self, icon, name):
        self._icon = icon
        self._name = name

        connection = psycopg2.connect(
            dbname="FICo",
            user="postgres",
            password="admin",
            host="localhost",
            port=5432
        )
        cursor = connection.cursor()

        try:
            query = "UPDATE categories SET icon = %s, name = %s WHERE categoryID = %s;"
            cursor.execute(query, (self._icon, self._name, self._categoryID))
            connection.commit()
        except psycopg2.Error as e:
            logging.error(f"Error setting category: {e}")
            pass
        finally:
            cursor.close()
            connection.close()

    def delete(self):
        connection = psycopg2.connect(
            dbname="FICo",
            user="postgres",
            password="admin",
            host="localhost",
            port=5432
        )
        cursor = connection.cursor()

        try:
            query = "DELETE FROM categories WHERE categoryID = %s;"
            cursor.execute(query, (self._categoryID,))
            connection.commit()
        except psycopg2.Error as e:
            logging.error(f"Error deleting category: {e}")
            pass
        finally:
            cursor.close()
            connection.close()

