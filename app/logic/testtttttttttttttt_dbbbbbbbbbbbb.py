import sys
sys.path.append("C://Users//gripo//PycharmProjects//FiCo//")
from common.db.database import dataBase
x = dataBase.delete_user(1)
print(x)