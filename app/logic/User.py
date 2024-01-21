import sys
from common.db.database import dataBase

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
    def Authorization (user_login: str, user_password: str) -> str:
        result = dataBase.find_user(user_login, user_password)
        if len(result) == 0:
            return "User is not found"
        else:
            return "user found"
        
    @staticmethod
    def Registration (userLogin: str, userPassword: str) -> str:
        result = dataBase.findUser(userLogin, userPassword)
        if len(result) == 0:
            dataBase.addNewUser(userLogin, userPassword)
            return "user has been successfully registered"
        else:
            return "this user is already registered"
    @staticmethod
    def EditPersonalData (tmp: str, data: str) -> bool:
        pass
    
userAccount.Registration("syka", "bliat")