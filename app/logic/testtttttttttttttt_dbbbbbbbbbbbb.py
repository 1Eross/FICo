import sys
sys.path.append("C://Users//gripo//PycharmProjects//FiCo//")
from common.db.database import dataBase
from app.auth.user import User
x = dataBase.find_user("biba", "abasdfsdfs")
print(x)