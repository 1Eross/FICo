import psycopg2

class Operation:
    def __init__(self, operationID, date, amount, categoryID, bankAccountID, description, userID):
        self._operationID = operationID
        self._date = date
        self._amount = amount
        self._categoryID = categoryID
        self._bankAccountID = bankAccountID
        self._description = description
        self._userID = userID

    @property
    def operationID(self):
        return self._operationID

    @property
    def date(self):
        return self._date

    @property
    def amount(self):
        return self._amount

    @property
    def categoryID(self):
        return self._categoryID

    @property
    def bankAccountID(self):
        return self._bankAccountID

    @property
    def description(self):
        return self._description

    @property
    def userID(self):
        return self._userID

    def setOperationInfo(self, date, amount, categoryID, bankAccountID, description, userID):
        self._date = date
        self._amount = amount
        self._categoryID = categoryID
        self._bankAccountID = bankAccountID
        self._description = description
        self._userID = userID

        connection = psycopg2.connect(
            dbname="FiCO",
            user="postgres",
            password="admin",
            host="localhost",
            port="5433"
        )
        cursor = connection.cursor()

        try:
            query = "UPDATE operations SET date = %s, amount = %s, categoryID = %s, bankAccountID = %s, description = %s, userID = %s WHERE operationID = %s;"
            cursor.execute(query, (self._date, self._amount, self._categoryID, self._bankAccountID, self._description, self._userID, self._operationID))
            connection.commit()
        except psycopg2.Error as e:
            # Обработка ошибок
            pass
        finally:
            cursor.close()
            connection.close()

    def delete(self):
        connection = psycopg2.connect(
            dbname="YourDBName",
            user="YourDBUser",
            password="YourDBPassword",
            host="YourDBHost",
            port="YourDBPort"
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

    def copy(self):
        connection = psycopg2.connect(
            dbname="FiCO",
            user="postgres",
            password="admin",
            host="localhost",
            port="5433"
        )
        cursor = connection.cursor()

        try:
            query = "INSERT INTO operations (date, amount, categoryID, bankAccountID, description, userID) VALUES (%s, %s, %s, %s, %s, %s) RETURNING operationID;"
            cursor.execute(query, (self._date, self._amount, self._categoryID, self._bankAccountID, self._description, self._userID))
            new_operation_id = cursor.fetchone()[0]
            connection.commit()
            return new_operation_id
        except psycopg2.Error as e:
            # Обработка ошибок
            pass
        finally:
            cursor.close()
            connection.close()

    def edit(self, date=None, amount=None, categoryID=None, bankAccountID=None, description=None, userID=None):
        # Позволяет редактировать отдельные атрибуты операции
        if date is not None:
            self._date = date
        if amount is not None:
            self._amount = amount
        if categoryID is not None:
            self._categoryID = categoryID
        if bankAccountID is not None:
            self._bankAccountID = bankAccountID
        if description is not None:
            self._description = description
        if userID is not None:
            self._userID = userID

        connection = psycopg2.connect(
            dbname="FiCO",
            user="postgres",
            password="admin",
            host="localhost",
            port="5433"
        )
        cursor = connection.cursor()

        try:
            query = "UPDATE operations SET date = %s, amount = %s, categoryID = %s, bankAccountID = %s, description = %s, userID = %s WHERE operationID = %s;"
            cursor.execute(query, (self._date, self._amount, self._categoryID, self._bankAccountID, self._description, self._userID, self._operationID))
            connection.commit()
        except psycopg2.Error as e:
            # Обработка ошибок
            pass
        finally:
            cursor.close()
            connection.close()

# Пример использования:
# operation = Operation(operationID=1, date="2024-01-20", amount=100.0, categoryID=2, bankAccountID=3, description="Expense", userID=4)
# operation.setOperationInfo(date="2024-01-21", amount=150.0, categoryID=3, bankAccountID=4, description="Updated Expense", userID=5)
# operation.edit(amount=200.0, description="Edited Expense")
# operation.delete()
# new_operation_id = operation.copy()
