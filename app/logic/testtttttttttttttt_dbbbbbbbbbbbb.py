import sys
sys.path.append("C://Users//gripo//PycharmProjects//FiCo//")
from common.db.database import dataBase
x = dataBase.find_user("123123", "1231231")
print(x)