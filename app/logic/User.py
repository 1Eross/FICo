import sys
sys.path.append("C:/Users/user/Documents/GitHub/FICo")
from common.db.db1 import *

#Юнит тесты написать к каждой функции 
class userAccount:
    def __init__(self, name, phoneNumber, emailAddress, login, password, token, bankAccountID) -> None:
        self.name = name
        self.phoneNumber = phoneNumber
        self.emailAddress = emailAddress
        self.login = login 
        self.password = password
        self.token = token
        self.bankAccountID = bankAccountID #мы договаривались что это будет список, может надо либо полность убрать либо оставить как пустой список 
        
    @staticmethod
    def Authorization (user_login: str, user_password: str) -> bool:
        result = dataBase.findUser(user_login, user_password)
        if len(result) == 0:
            return False
        else:
            return True
        
    @staticmethod
    def Registration (userLogin: str, userPassword: str) -> bool:
        result = dataBase.findUser(userLogin, userPassword)
        if len(result) == 0:
            dataBase.addUser(userLogin, userPassword)
            return True
        else:
            return False
    @staticmethod
    def EditPersonalData (tmp: str, data: str) -> bool:
        pass
    
userAccount.Registration("syka", "bliat")