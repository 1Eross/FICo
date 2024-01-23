import sys
sys.path.append("C:\\Users\\gripo\\PycharmProjects\\FiCo")

import hashlib

import logging
logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w+")

from common.db.database import dataBase
from typing import Optional

from typing import Optional
from pydantic import BaseModel, validator


class User(BaseModel):
    id: int
    login: str
    password: str
    email: Optional[str] = None
    phoneNumber: Optional[str] = None
    FNameLName: Optional[str] = None
    token: Optional[str] = None
    status: Optional[str] = None

    @staticmethod    
    def hash_password(password: str) -> str:
        hashedPassword = hashlib.new("sha256")
        hashedPassword.update(password.encode())
        return hashedPassword.hexdigest()

    @classmethod
    def find_user(cls, login: str, password: str) -> Optional['User']:
        user_data = dataBase.find_user(login, password)
        if user_data:
            logging.info(f"User with id {user_data[0]} found successfully {user_data}")
            return User(
                id=user_data[0][0],
                login=user_data[0][1],
                password=user_data[0][2],
                email=user_data[0][3],
                phoneNumber=user_data[0][4],
                FNameLName=user_data[0][5],
                token=user_data[0][6],
                status=user_data[0][7]  # Исправлен индекс
            )
        else:
            logging.error(f"User with params (login={login}, password={password}) not exists")
            return None
        
    @classmethod
    def get_id_by_login(cls, login: str) -> int:
        user_data = dataBase.get_id_by_login(login)
        if user_data:
            logging.info(f"User with id {user_data} found successfully {user_data}")
            return user_data
        else:
            logging.error(f"User with params (login={login}) not exists")
            return None

    @classmethod
    def create_user(cls, login: str, password: str,
                    email: Optional[str] = None, phoneNumber: Optional[str] = None,
                    FNameLName: Optional[str] = None, token: Optional[str] = None,
                    status: Optional[str] = None) -> bool:
        user = dataBase.find_user_in_database_by_login(login)
        if user:
            logging.error(f"Create user attempt failed: User with (login={login}) already exists")
            return False
        else:
            logging.info(f"User successfully created with params ({login, password, email, phoneNumber, FNameLName, token, status})")
            dataBase.add_new_user(login, password, email, phoneNumber, FNameLName, token, status)
            return True

    @classmethod
    def delete_user(cls, user_id: int) -> bool:
        is_deleted = dataBase.delete_user(user_id)
        if is_deleted:
            logging.info(f"User (id={user_id}) deleted successfully")
            return True
        else:
            logging.error(f"Delete user attempt failed with params (id={user_id})")
            return False
