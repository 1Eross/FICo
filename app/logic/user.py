import hashlib

import logging
logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w+")

from common.db.database import dataBase
from common.errors.errors import UserExistsError
from common.errors.errors import UserNotFoundError
from common.errors.errors import UserDeletionError

from typing import Optional

#ОБРАБОТКА ОСУЩЕСТВЛЯЕТСЯ ПРИ ПОМОЩИ САМОПИСНЫХ КЛАССОВ ОШИБОК, И ПРОВЕРЯЕТСЯ ЧЕРЕЗ TRY EXCEPT В КОДЕ API
class User:
    def __init__(self, id: int, login: str, password: str , email: str | None,\
                phoneNumber: str | None, FNameLName: str | None, token: str | None, status: str | None):
        self._id = id
        self._login = login
        self._password = User.hash_password(password)
        self._email = email
        self._phoneNumber = phoneNumber
        self._FNameLName = FNameLName
        self._token = token
        self._status = status
        
    #Cоздать конструктор по id ?
    
    @property
    def id(self):
        return self._id

    @id.setter ##Может ли быть Id setter ?
    def id(self, value):
        self._id = value

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, new_login: str) -> bool:
        is_updated = dataBase.edit_personal_data(self.id, name_column='user_login', data=new_login)
        if is_updated:
            logging.info(f"User id:{self.id} login updated succesfully on {new_login}")
            self._login = new_login
            return True
        else:
            logging.error(f"User id:{self.id} login update error")
            return False
        

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, new_password: str):
        hashed_password = User.hash_password(new_password)
        is_updated = dataBase.edit_personal_data(self.id, name_column='user_password', data=hashed_password)
        if is_updated:
            self._password = hashed_password
            logging.info(f"User id:{self.id} password updated succesfully on {new_password}")
            return True
        else:
            logging.error(f"User id:{self.id} password update error")
            return False
            
            
        

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, new_email: str) -> bool:
        is_updated = dataBase.edit_personal_data(self.id, name_column='email', data=new_email)
        if is_updated:
            logging.info(f"User id:{self.id} email updated succesfully on {new_email}")
            self._email = new_email
            return True
        else:
            logging.error(f"User id:{self.id} email update error")
            return False
        

    @property
    def phoneNumber(self):
        return self._phoneNumber

    @phoneNumber.setter
    def phoneNumber(self, new_phone_number: str) -> bool:
        is_updated = dataBase.edit_personal_data(self.id, name_column='phone', data=new_phone_number)
        if is_updated:
            logging.info(f"User id:{self.id} phone updated succesfully on {new_phone_number}")
            self._phoneNumber = new_phone_number
            return True
        else:
            logging.error(f"User id:{self.id} phone update error")
            return False

    @property
    def FNameLName(self):
        return self._FNameLName

    @FNameLName.setter
    def FNameLName(self, new_name):
        is_updated = dataBase.edit_personal_data(self.id, name_column='user_name', data=new_name)
        if is_updated:
            logging.info(f"User id:{self.id} name updated succesfully on {new_name}")
            self._FNameLName = new_name
            return True
        else:
            logging.error(f"User id:{self.id} phone update error")
            return False

    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, new_token: str):
        is_updated = dataBase.edit_personal_data(self.id, name_column='user_token', data=new_token)
        if is_updated:
            logging.info(f"User id:{self.id} token updated succesfully on {new_token}")
            self._token = new_token
            return True
        else:
            logging.error(f"User id:{self.id} token update error")
            return False

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, new_status: str):
        is_updated = dataBase.edit_personal_data(self.id, name_column='user_token', data=new_status)
        if is_updated:
            logging.info(f"User id:{self.id} status updated succesfully on {new_status}")
            self._status = new_status
            return True
        else:
            logging.error(f"User id:{self.id} token update error")
            return False
    
                
    
    @staticmethod    
    def hash_password(password: str) -> int:
        hashedPassword = hashlib.new("sha256")
        hashedPassword.update(password.encode())
        return hashedPassword
    
    @staticmethod
    def find_user(login: str, password: str) -> Optional['User']:
        user_data = dataBase.find_user(login, password)
        if user_data:
            logging.info(f"User with id {user_data[0]} found seccesfully {user_data}")
            return User(id=user_data[0][0], login=user_data[0][1],
                        password=user_data[0][2], email=user_data[0][3],
                        phoneNumber=user_data[0][4], FNameLName=user_data[0][5],
                        token=user_data[0][6], status=user_data[0][6])
        else:
            logging.error(f"User with params (login={login}, password={password}) not exists")
            raise UserNotFoundError(f"User with params (login={login}, password={password}) not exists")
        
    
    @staticmethod
    def createUser(login: str, password: str,
                   email: str | None, phoneNumber: str | None,
                   FNameLName: str | None, token: str | None,
                   status: str | None) -> bool:
        user = dataBase.find_user_in_database_by_login(login)
        if user:
            logging.error(f"Create user attempt failed: User with (login={login}) allready exists")
            raise UserExistsError(f"Create user attempt failed: User with (login={login}) allready exists")
        else:
            logging.info(f"User successfully created with params ({login, password, email, phoneNumber, FNameLName, token, status})")
            dataBase.add_new_user(login, password, email, phoneNumber, FNameLName, token, status)
            
    ##Выйти из сессии при удалении пользователя
    @staticmethod
    def deleteUser(user_id: int) -> bool:
        is_deleted = dataBase.delete_user(user_id)
        if is_deleted:
            logging.info(f"User (id={user_id}) deleted successfully")
            return True
        else:
            logging.error(f"Delete user attempt failed with params (id={user_id})")
            raise UserDeletionError(f"Delete user attempt failed with params (id={user_id})")
        