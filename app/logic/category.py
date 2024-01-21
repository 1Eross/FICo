import psycopg2

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
            # Обработка ошибок
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
            # Обработка ошибок
            pass
        finally:
            cursor.close()
            connection.close()

# Пример использования:
# category = Category(categoryID=1, icon="icon.png", name="Example Category")
# category.setCategoryInfo(icon="new_icon.png", name="Updated Category")
# category.delete()
