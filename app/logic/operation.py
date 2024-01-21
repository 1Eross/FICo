import psycopg2

class Operation:
    def __init__(self, operationID, operation_date, amount, category_id, account_id, description, user_id, currency_id, is_incoming):
        self._operationID = operationID
        self._operation_date = operation_date
        self._amount = amount
        self._category_id = category_id
        self._account_id = account_id
        self._description = description
        self._user_id = user_id
        self._currency_id = currency_id
        self._is_incoming = is_incoming

    @property
    def operationID(self):
        return self._operationID

    @property
    def operation_date(self):
        return self._operation_date

    @property
    def amount(self):
        return self._amount

    @property
    def category_id(self):
        return self._category_id

    @property
    def account_id(self):
        return self._account_id

    @property
    def description(self):
        return self._description

    @property
    def user_id(self):
        return self._user_id
    
    @property
    def currency_id(self):
        return self._currency_id
    
    @property
    def is_incoming(self):
        return self._is_incoming

    def setOperationInfo(self, operation_date, amount, category_id, account_id, description, user_id, currency_id, is_incoming):
        self._operation_operation_date = operation_date
        self._amount = amount
        self._category_id = category_id
        self._account_id = account_id
        self._description = description
        self._user_id = user_id
        self._currency_id = currency_id
        self._is_incoming = is_incoming

        connection = psycopg2.connect(
            dbname="FICo",
            user="postgres",
            password="admin",
            host="localhost",
            port=5432
        )
        cursor = connection.cursor()

        try:
            query = "UPoperation_date operations SET operation_date = %s, amount = %s, category_id = %s, account_id = %s, description = %s, user_id = %s WHERE operationID = %s;"
            cursor.execute(query, (self._operation_date, self._amount, self._category_id, self._account_id, self._description, self._user_id, self._operationID, self._currency_id))
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
            query = "DELETE FROM operations WHERE operationID = %s;"
            cursor.execute(query, (self._operationID,))
            connection.commit()
        except psycopg2.Error as e:
            # Обработка ошибок
            pass
        finally:
            cursor.close()
            connection.close()

    # def copy(self):
    #     connection = psycopg2.connect(
    #         dbname="FICo",
    #         user="postgres",
    #         password="admin",
    #         host="localhost",
    #         port=5432
    #     )
    #     cursor = connection.cursor()

    #     try:
    #         query = "INSERT INTO operations (operation_date, amount, category_id, account_id, description, user_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING operationID;"
    #         cursor.execute(query, (self._operation_date, self._amount, self._category_id, self._account_id, self._description, self._user_id))
    #         new_operation_id = cursor.fetchone()[0]
    #         connection.commit()
    #         return new_operation_id
    #     except psycopg2.Error as e:
    #         # Обработка ошибок
    #         pass
    #     finally:
    #         cursor.close()
    #         connection.close()

    def edit(self, operation_date=None, amount=None, category_id=None, account_id=None, description=None, user_id=None):
        # Позволяет редактировать отдельные атрибуты операции
        if operation_date is not None:
            self._operation_date = operation_date
        if amount is not None:
            self._amount = amount
        if category_id is not None:
            self._category_id = category_id
        if account_id is not None:
            self._account_id = account_id
        if description is not None:
            self._description = description
        if user_id is not None:
            self._user_id = user_id

        connection = psycopg2.connect(
            dbname="FICo",
            user="postgres",
            password="admin",
            host="localhost",
            port=5432
        )
        cursor = connection.cursor()

        try:
            query = "UPoperation_date operations SET operation_date = %s, amount = %s, category_id = %s, account_id = %s, description = %s, user_id = %s WHERE operationID = %s;"
            cursor.execute(query, (self._operation_date, self._amount, self._category_id, self._account_id, self._description, self._user_id, self._operationID))
            connection.commit()
        except psycopg2.Error as e:
            # Обработка ошибок
            pass
        finally:
            cursor.close()
            connection.close()

# Пример использования:
# operation = Operation(operationID=1, operation_date="2024-01-20", amount=100.0, category_id=2, account_id=3, description="Expense", user_id=4)
# operation.setOperationInfo(operation_date="2024-01-21", amount=150.0, category_id=3, account_id=4, description="Upoperation_dated Expense", user_id=5)
# operation.edit(amount=200.0, description="Edited Expense")
# operation.delete()
# new_operation_id = operation.copy()
