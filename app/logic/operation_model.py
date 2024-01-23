import logging
logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w+")
from common.db.database import dataBase
from pydantic import BaseModel
from pydantic import BaseModel, validator
from typing import Optional, List

class Operation(BaseModel):
    operation_id: int
    operation_date: str
    amount: int
    category_id: int
    account_id: int
    description: str
    user_id: int
    currency_id: int
    is_incoming: bool

    @classmethod
    def from_db(cls, operation_id: int, operation_date: str, amount: int, category_id: int,
                account_id: int, description: str, user_id: int, currency_id: int, is_incoming: bool):
        return cls(
            operation_id=operation_id,
            operation_date=operation_date,
            amount=amount,
            category_id=category_id,
            account_id=account_id,
            description=description,
            user_id=user_id,
            currency_id=currency_id,
            is_incoming=is_incoming
        )

    @validator('operation_date', pre=True, always=True)
    def validate_operation_date(cls, v):
        # Add any validation logic for operation_date if needed
        return v

    @classmethod
    def edit_operation(cls, operation_id: int, name_column: str, data):
        is_updated = dataBase.edit_operation(operation_id, name_column=name_column, data=data)
        if is_updated:
            logging.info(f"{name_column} updated successfully to {data}")
            return True
        else:
            logging.error(f"Failed to update {name_column} to {data}")
            return False

    @classmethod
    def get_all_operations(cls, user_id: int, account_id: int) -> List['Operation']:
        operations = dataBase.get_all_operations(user_id, account_id=account_id)
        if not operations:
            logging.error("Error while loading in operation class")
            return []
        return [cls.from_db(*op) for op in operations]

    @classmethod
    def add_operation(cls, user_id: int, account_id: int, category_id: int,
                      currency_id: int, is_incoming: bool, amount: int,
                      operation_date: str, description: str) -> bool:
        is_added = dataBase.add_new_operation(user_id, account_id, category_id,
                                              currency_id, is_incoming, amount,
                                              operation_date, description)
        return is_added

    def delete_operation(self):
        is_deleted = dataBase.delete_operation(self.operation_id)
        if is_deleted:
            logging.info(f"Operation with ID {self.operation_id} deleted successfully")
            return True
        else:
            logging.error(f"Failed to delete operation with ID {self.operation_id}")
            return False

    