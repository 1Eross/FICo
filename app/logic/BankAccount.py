import psycopg2

class BankAccount:
    def __init__(self, bankAccountID, balance, currency, userID: int):
        self._bankAccountID = bankAccountID
        self._balance = balance
        self._currency = currency
        self._userID = userID

    @property
    def bankAccountID(self):
        return self._bankAccountID

    @property
    def balance(self):
        return self._balance

    @property
    def currency(self):
        return self._currency

    @property
    def userID(self):
        return self._userID

    def setBankAccountInfo(self, balance, currency, userID):
        self._balance = balance
        self._currency = currency
        self._userID = userID

        connection = psycopg2.connect(
            dbname="FICo",
            user="postgres",
            password="admin",
            host="localhost",
            port=5432
        )
        cursor = connection.cursor()

        try:
            query = "UPDATE bank_accounts SET balance = %s, currency = %s, userID = %s WHERE bankAccountID = %s;"
            cursor.execute(query, (self._balance, self._currency, self._userID, self._bankAccountID))
            connection.commit()
        except psycopg2.Error as e:
            # Обработка ошибок в лог
            pass
        finally:
            cursor.close()
            connection.close()

    def getBankAccountInfo(self):
        connection = psycopg2.connect(
            dbname="FICo",
            user="postgres",
            password="admin",
            host="localhost",
            port=5432
        )
        cursor = connection.cursor()

        try:
            query = "SELECT balance, currency, userID FROM bank_accounts WHERE bankAccountID = %s;"
            cursor.execute(query, (self._bankAccountID,))
            result = cursor.fetchone()

            if result:
                self._balance, self._currency, self._userID = result
            else:
                raise ValueError("Bank account not found")
        except psycopg2.Error as e:
            # Обработка ошибок
            pass
        finally:
            cursor.close()
            connection.close()

    def setBalance(self, balance):
        self.setBankAccountInfo(balance, self._currency, self._userID)

    def setCurrency(self, currency):
        self.setBankAccountInfo(self._balance, currency, self._userID)

    def setUserID(self, userID):
        self.setBankAccountInfo(self._balance, self._currency, userID)

    def add_new_category(self, category):
        connection = psycopg2.connect(
            dbname="FICo",
            user="postgres",
            password="admin",
            host="localhost",
            port=5432
        )
        cursor = connection.cursor()

        try:
            query = "INSERT INTO categories (categoryID, icon, name) VALUES (%s, %s, %s) RETURNING categoryID;"
            cursor.execute(query, (category.categoryID, category.icon, category.name))
            new_category_id = cursor.fetchone()[0]
            connection.commit()
            return new_category_id
        except psycopg2.Error as e:
            # Обработка ошибок
            pass
        finally:
            cursor.close()
            connection.close()

    def add_new_operation(self, operation):
        connection = psycopg2.connect(
            dbname="FICo",
            user="postgres",
            password="admin",
            host="localhost",
            port=5432
        )
        cursor = connection.cursor()

        try:
            query = "INSERT INTO operations (operationID, date, amount, categoryID, bankAccountID, description, userID) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING operationID;"
            cursor.execute(query, (operation.operationID, operation.date, operation.amount, operation.categoryID, operation.bankAccountID, operation.description, operation.userID))
            new_operation_id = cursor.fetchone()[0]
            connection.commit()
            return new_operation_id
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
            query = "DELETE FROM bank_accounts WHERE bankAccountID = %s;"
            cursor.execute(query, (self._bankAccountID,))
            connection.commit()
        except psycopg2.Error as e:
            # Обработка ошибок
            pass
        finally:
            cursor.close()
            connection.close()

# Пример использования:
# bank_account = BankAccount(bankAccountID=1, balance=1000.0, currency="USD", userID=1)
# category = Category(categoryID=1, icon="icon.png", name="Example Category")
# operation = Operation(operationID=1, date="2024-01-20", amount=100.0, categoryID=1, bankAccountID=1, description="Expense", userID=1)
# bank_account.add_new_category(category)
# bank_account.add_new_operation(operation)
# bank_account.delete()
