import sys
sys.path.append("C:/Users/user/Documents/GitHub/FICo")
from common.db.database import Database


testDB = Database()
testDB.connect()

#Юнит тесты написать к каждой функции 
class UserAccount:
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
       if Database.read_records(testDB.read_records(Database.getUser(user_login, user_password))):
           return True
       else:
           return False
    @staticmethod
    def Registration (userName: str, userPhoneNumber: str, userEmailAddress: str, userLogin: str, userPassword: str) -> bool:
        #мэйби всё вынести в отедельные функции в отдельный класс и импортировать и тогда проще будет 
        if userName != None:
            return False
        if userPhoneNumber.count != 11:
            return False
        if userEmailAddress.__contains__("@mail.ru") != True:
            return False
        if userLogin.count < 8 or userLogin.count > 20: #сделать проверку на минимум одно число, минимум один символ, отсутствие запрещённых символов, проверить в бд есть ли такие логины
            return False
        if userPassword.count < 8 or userPassword.count > 20: #сделать проверку на минимум одно число, минимум один символ, отсутствие запрещённых символов
            return False
        
        return True
    @staticmethod
    def EditPersonalData (tmp: str, data: str) -> bool:
        if tmp == "name":
            pass
            #проверка на коректность data
        elif tmp == "password":
            pass
            #проверка на коректность data
        elif tmp == "login":
            pass
        elif tmp == "phoneNumber":
            pass
        elif tmp == "emailAddress":
            pass
    