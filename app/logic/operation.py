import logging
logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w")
from common.db.database import dataBase
class Operation:
    def __init__(self, operation_id, operation_date, amount, category_id, account_id, description, user_id, currency_id, is_incoming):
        self._operation_id = operation_id
        self._operation_date = operation_date
        self._amount = amount
        self._category_id = category_id
        self._account_id = account_id
        self._description = description
        self._user_id = user_id
        self._currency_id = currency_id
        self._is_incoming = is_incoming

    @property
    def operation_id(self):
        return self._operation_id
    
    def operation_id(self, new_operation_id):
        is_updated = dataBase.edit_operation(self.id, name_column='operation_id', data=new_operation_id)
        if is_updated:
            # Логирование успешного обновления
            logging.info(f"operation_id updated successfully to {new_operation_id}")
            self._operation_id = new_operation_id
            return True
        else:
            # Логирование неудачного обновления
            logging.error(f"Failed to update operation_id to {new_operation_id}")
            return False

    @property
    def operation_date(self):
        return self._operation_date

    def operation_date(self, new_operation_date):
        is_updated = dataBase.edit_operation(self.id, name_column='operation_date', data=new_operation_date)
        if is_updated:
            # Логирование успешного обновления
            logging.info(f"Operation date updated successfully to {new_operation_date}")
            self._operation_date = new_operation_date
            return True
        else:
            # Логирование неудачного обновления
            logging.error(f"Failed to update operation date to {new_operation_date}")
            return False

    @property
    def amount(self):
        return self._amount

    def amount(self, new_amount):
        is_updated = dataBase.edit_operation(self.id, name_column='amount', data=new_amount)
        if is_updated:
            # Логирование успешного обновления
            logging.info(f"Amount updated successfully to {new_amount}")
            self._amount = new_amount
            return True
        else:
            # Логирование неудачного обновления
            logging.error(f"Failed to update amount to {new_amount}")
            return False

    @property
    def category_id(self):
        return self._category_id

    def category_id(self, new_category_id):
        is_updated = dataBase.edit_operation(self.id, name_column='category_id', data=new_category_id)
        if is_updated:
            # Логирование успешного обновления
            logging.info(f"Category ID updated successfully to {new_category_id}")
            self._category_id = new_category_id
            return True
        else:
            # Логирование неудачного обновления
            logging.error(f"Failed to update category ID to {new_category_id}")
            return False

    @property
    def account_id(self):
        return self._account_id
    
    def account_id(self, new_account_id):
        is_updated = dataBase.edit_operation(self.id, name_column='account_id', data=new_account_id)
        if is_updated:
            # Логирование успешного обновления
            logging.info(f"Account ID updated successfully to {new_account_id}")
            self._account_id = new_account_id
            return True
        else:
            # Логирование неудачного обновления
            logging.error(f"Failed to update account ID to {new_account_id}")
            return False

    @property
    def description(self):
        return self._description

    def description(self, new_description):
        is_updated = dataBase.edit_operation(self.id, name_column='description', data=new_description)
        if is_updated:
            # Логирование успешного обновления
            logging.info(f"Description updated successfully to {new_description}")
            self._description = new_description
            return True
        else:
            # Логирование неудачного обновления
            logging.error(f"Failed to update description to {new_description}")
            return False

    @property
    def user_id(self):
        return self._user_id
    
    def user_id(self, new_user_id):
        is_updated = dataBase.edit_operation(self.id, name_column='user_id', data=new_user_id)
        if is_updated:
            # Логирование успешного обновления
            logging.info(f"User ID updated successfully to {new_user_id}")
            self._user_id = new_user_id
            return True
        else:
            # Логирование неудачного обновления
            logging.error(f"Failed to update user ID to {new_user_id}")
            return False


    @property
    def currency_id(self):
        return self._currency_id
    
    def currency_id(self, new_currency_id):
        is_updated = dataBase.edit_operation(self.id, name_column='currency_id', data=new_currency_id)
        if is_updated:
            # Логирование успешного обновления
            logging.info(f"Currency ID updated successfully to {new_currency_id}")
            self._currency_id = new_currency_id
            return True
        else:
            # Логирование неудачного обновления
            logging.error(f"Failed to update currency ID to {new_currency_id}")
            return False

    @property
    def is_incoming(self):
        return self._is_incoming
    
    def is_incoming(self, new_is_incoming):
        is_updated = dataBase.edit_operation(self.id, name_column='is_incoming', data=new_is_incoming)
        if is_updated:
            # Логирование успешного обновления
            logging.info(f"Is incoming updated successfully to {new_is_incoming}")
            self._is_incoming = new_is_incoming
            return True
        else:
            # Логирование неудачного обновления
            logging.error(f"Failed to update is incoming to {new_is_incoming}")
            return False