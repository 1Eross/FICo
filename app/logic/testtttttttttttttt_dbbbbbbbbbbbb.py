import sys
sys.path.append("C:/Users/user/Documents/GitHub/FICo")
from common.db.database import dataBase
x = dataBase.find_user_in_database_by_login("zxc")
print(x)