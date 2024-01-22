from fastapi import FastAPI
from enum import Enum
from app.logic.user import User

app = FastAPI()

class ModelName(str, Enum):
    apple = "apple"
    watermellon = "watermellon"
    grape = "grape"


#path params
#

# @app.get("/foo0/{my_key}")
# async def read_item(my_key):
#     return {'message': my_key}

#type notation
@app.get("/auth/")
async def read_item(my_key: int):
    return {'message': my_key, 'decriprion': "sended from id"}

# #predefined params with ENUM class
# @app.get("/foo2/{model_name}")
# async def read_item(model_name: ModelName):
#     if model_name.value == "apple":
#         return{"Position": model_name, "Cost": "15$"}
#     elif model_name is ModelName.watermellon:
#         return{"Position": model_name, "Cost": "20$"}
#     else:
#         return{"Position": model_name, "Cost": "30$"}
    
# #file path
# @app.get("/foo3/{filepath: path}")
# async def read_item(filepath: str):
#     return {"filepath": filepath}

# #Querry tools
# #

fake_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

#get with args ## http://127.0.0.1:8002/authorization?user_login=something&user_password=something
@app.get("/authorization")
async def read_item(user_login: str, user_password: str):
    gettedUser = User.find_user(login=user_login, password=user_password)
    if gettedUser:
        User.phoneNumber("1233567")
        return {"User_id": gettedUser.id}
    else:
        return {"Message": "User not found"}
    
@app.get("/registration")
async def read_item(user_login: str, user_password: str):
    gettedUser = User.find_user(login=user_login, password=user_password)
    if gettedUser:
        return {"User_id": gettedUser.id}
    else:
        return {"Message": "User not found"}

# #get with additional params
# @app.get("/foo5/{item_id}")
# async def read_item(item_id: str, q: str | None = None):
#     if q:
#         return {"item_id": item_id, "q": q}
#     return {"item_id": item_id.capitalize()}

# ##Best practice for RESTful API design is that path params
# # are used to identify a specific resource or resources,
# # while query parameters are used to sort/filter those resources.

# #few path and querry params in a row
# @app.get("/users/{user_id}/items/{item_id}")
# async def read_user_item(
#     user_id: int, item_id: str, q: str | None = None, short: bool = False):
#     item = {"item_id": item_id, "owner_id": user_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {"description": "This is an amazing item that has a long description"}
#         )
#     return item