import logging
from common.db.database import dataBase
logging.basicConfig(level=logging.INFO, filename="common/log/py_log.log",filemode="w+")

class BankAccount:
    def __init__(self, account_id, balance, currency, user_id: int):
        self._account_id = account_id
        self._balance = balance
        self._currency = currency
        self._user_id = user_id

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
    def user_id(self):
        return self._user_id
    
    @account_id.setter
    def account_id(self, new_account_id):
        is_updated = dataBase.add_new_bank_account(self.id, name_column='account_id', data=new_account_id)
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
    
    @user_id.setter
    def user_id(self, new_user_id):
        is_updated = dataBase.edit_bank_data(self.id, name_column='user_id', data=new_user_id)
        if is_updated:
            # Логирование успешного обновления
            logging.info(f"User ID updated successfully to {new_user_id}")
            self._userID = new_user_id
            return True
        else:
            # Логирование неудачного обновления
            logging.error(f"Failed to update User ID to {new_user_id}")
            return False
    
    @staticmethod
    def create_bank_account(user_id = int, balance = int, currency_id = int, account_name = str) -> bool:
        is_created = dataBase.add_new_bank_account(user_id, balance, currency_id, account_name)
        if is_created:
            logging.error(f"Bank account succesfully created")
            dataBase.add_new_bank_account(user_id, balance, currency_id, account_name)
        else:
            logging.info(f"Bank account creating failed)")

    def delete(self):
        is_deleted = dataBase.delete_bank_account(self.id)
        if is_deleted:
            logging.info(f"Data for account {self.id} deleted successfully")
            return True
        else:
            logging.error(f"Failed to delete data for account {self.id}")
            return False
  