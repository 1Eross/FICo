import logging
from common.db.database import dataBase

logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w")

class BankAccount:
    def __init__(self, account_id, balance, currency, userID: int):
        self._account_id = account_id
        self._balance = balance
        self._currency = currency
        self._userID = userID

    @property
    def account_id(self):
        return self._account_id

    @property
    def balance(self):
        return self._balance

    @property
    def currency(self):
        return self._currency

    @property
    def userID(self):
        return self._userID
    
    @account_id.setter
    def account_id(self, new_account_id):
        is_updated = dataBase.edit_bank_data(self.id, name_column='account_id', data=new_account_id)
        if is_updated:
            # Логирование успешного обновления
            logging.info(f"Account ID updated successfully to {new_account_id}")
            self._account_id = new_account_id
            return True
        else:
            # Логирование неудачного обновления
            logging.error(f"Failed to update Account ID to {new_account_id}")
            return False
    
    @balance.setter
    def balance(self, new_balance):
        is_updated = dataBase.edit_bank_data(self.id, name_column='balance', data=new_balance)
        if is_updated:
            # Логирование успешного обновления
            logging.info(f"Balance updated successfully to {new_balance}")
            self._balance = new_balance
            return True
        else:
            # Логирование неудачного обновления
            logging.error(f"Failed to update Balance to {new_balance}")
            return False
    
    @currency.setter
    def currency(self, new_currency):
            is_updated = dataBase.edit_bank_data(self.id, name_column='currency', data=new_currency)
            if is_updated:
                # Логирование успешного обновления
                logging.info(f"Currency updated successfully to {new_currency}")
                self._currency = new_currency
                return True
            else:
                # Логирование неудачного обновления
                logging.error(f"Failed to update Currency to {new_currency}")
                return False
    
    @userID.setter
    def userID(self, new_userID):
        is_updated = dataBase.edit_bank_data(self.id, name_column='user_id', data=new_userID)
        if is_updated:
            # Логирование успешного обновления
            logging.info(f"User ID updated successfully to {new_userID}")
            self._userID = new_userID
            return True
        else:
            # Логирование неудачного обновления
            logging.error(f"Failed to update User ID to {new_userID}")
            return False

  