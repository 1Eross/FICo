<<<<<<< Updated upstream
=======
import sys
sys.path.append("C:/Users/user/Documents/GitHub/FICo")
>>>>>>> Stashed changes
from common.db.database import dataBase
from app.logic.user import User
x = dataBase.find_user("biba", "abasdfsdfs")
print(x)