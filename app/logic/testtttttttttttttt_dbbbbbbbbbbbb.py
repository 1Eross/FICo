import sys
sys.path.append("C:/Users/user/Documents/GitHub/FICo")
from common.db.database import dataBase
x = dataBase.add_new_bank_account(1, 100, 1, "zp")
print(x)