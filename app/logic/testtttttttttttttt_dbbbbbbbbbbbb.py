import sys
sys.path.append("C:/Users/user/Documents/GitHub/FICo")
from common.db.database import dataBase
x = dataBase.delete_user(1)
print(x)