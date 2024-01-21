import hashlib
import sys
from typing import Optional
sys.path.append("/common/db/")
from common.db import database

class User:
    def __init__(self, id: int, login: str, password: str , email: str | None,\
                phoneNumber: str | None, FNameLName: str | None, token: str | None, status: str | None):
        self._id = id
        self._login = login
        self._password = User.hashPassword(password)
        self._email = email
        self._phoneNumber = phoneNumber
        self._FNameLName = FNameLName
        self._token = token
        self._status = status
    
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, value):
        database.dataBase.edit_personal_data(self.id, )
        self._login = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = User.hashPassword(value)

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def phoneNumber(self):
        return self._phoneNumber

    @phoneNumber.setter
    def phoneNumber(self, value):
        self._phoneNumber = value

    @property
    def FNameLName(self):
        return self._FNameLName

    @FNameLName.setter
    def FNameLName(self, value):
        self._FNameLName = value

    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, value):
        self._token = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    
                
    
    @staticmethod    
    def hashPassword(password: str) -> int:
        hashedPassword = hashlib.new("sha256")
        hashedPassword.update(password.encode())
        return hashedPassword
    
    @staticmethod
    def findUser(login: str, password: str) -> Optional['User']:
        user_data = database.dataBase.find_user(login, password)
        if user_data:
            #logoutput
            return User(id=user_data[0], login=user_data[1],
                        password=user_data[2], email=user_data[3],
                        phoneNumber=user_data[4], FNameLName=user_data[5],
                        token=user_data[6], status=user_data[6])
        else:
            #logoutput
            return None
        
    @staticmethod
    def updateUser():
        pass
        
    
    @staticmethod
    def createUser():
        pass
    
    @staticmethod
    def deleteUser():
        pass
    
        