import sys
sys.path.append("C:/Users/user/Documents/GitHub/FICo")
from common.db.database import dataBase
x = dataBase.get_all_bank_account(1)
print(x)