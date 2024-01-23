
import sys
sys.path.append("C:\\Users\\gripo\\PycharmProjects\\FiCo")

import logging
from common.db.database import dataBase
logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w+")
from pydantic import BaseModel, validator
from typing import Optional

class BankAccount(BaseModel):
    account_id: int
    balance: float
    currency: str
    userID: int
    currency_id: int

    @classmethod
    def from_db(cls, account_id: int, userID: int, balance: float, account_name:str, currency_id: int):
        return cls(
            account_id=account_id,
            userID=userID,
            balance=balance,
            account_name=account_name,
            currency_id=currency_id,
        )

    @validator('balance')
    def validate_balance(cls, v):
        if v < 0:
            raise ValueError("Balance must be non-negative")
        return v

    @classmethod
    def edit_bank_data(cls, account_id: int, name_column: str, data):
        is_updated = dataBase.edit_bank_data(account_id, name_column=name_column, data=data)
        if is_updated:
            logging.info(f"{name_column} updated successfully to {data}")
            return True
        else:
            logging.error(f"Failed to update {name_column} to {data}")
            return False

    @classmethod
    def get_all_bank_accounts(cls, user_id: int):
        bank_accounts = dataBase.get_all_bank_account(user_id)
        if not bank_accounts:
            logging.error("Error while loading in operation class")
            return []
        print([op for op in bank_accounts])
        return [cls.from_db(*op) for op in bank_accounts]
        

    def delete_bank_account(self):
        is_deleted = dataBase.delete_bank_account(self.account_id)
        if is_deleted:
            logging.info(f"Data for account {self.account_id} deleted successfully")
            return True
        else:
            logging.error(f"Failed to delete data for account {self.account_id}")
            return False
