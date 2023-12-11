
import hashlib

class User:
    def __init__(self, id: int, login: str, password: str , email: str | None,\
                phoneNumber: str | None, FNameLName: str | None, token: str | None, status: str | None):
        self.id = id
        self.login = login
        self.password = User.hashPassword(password)
        self.email = email
        self.phoneNumber = phoneNumber
        self.FNameLName = FNameLName
        self.token = token
        self.status = status
    
    def setNewLogin(self, NewLogin: str):
        self.login = NewLogin
                
    
    @staticmethod    
    def hashPassword(password: str) -> int:
        hashedPassword = hashlib.new("sha256")
        hashedPassword.update(password.encode())
        return hashedPassword
    
    @staticmethod
    def findUser():
        pass
    
    @staticmethod
    def updateUser():
        pass
    
    @staticmethod
    def createUser():
        pass
    
    @staticmethod
    def deleteUser():
        pass
    
        