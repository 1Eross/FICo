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
            dbname="FiCO",
            user="postgres",
            password="admin",
            host="localhost",
            port="5433"
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
            dbname="FiCO",
            user="postgres",
            password="admin",
            host="localhost",
            port="5433"
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
