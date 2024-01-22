import sys
sys.path.append("C:\\Users\\gripo\\PycharmProjects\\FiCo")

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from operation import Operation
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
#get = получить с сервера, post = поместить на сервер, delete = удалить с сервера, put = изменение на сервере. 
app = FastAPI()

# class OperationRequest(Request):

class BankAccountRequest(BaseModel):
    user_id: int
class OperationRequest(BankAccountRequest):
    account_id: int
    
#добавление операции
@app.post("/add_operation")
async def add_operation(account_id: int, user_id: int, category_id: int, currency_id: int, incoming: bool, amount: int, operetion_date: str,description: str):
    #answer = 
    pass

@app.get("/account/get_all")
async def get_all_account(data: BankAccountRequest):
    pass

@app.get("/operation/get_all")
async def get_all_opertaions(data: OperationRequest):
    operations = Operation.get_all_operation(OperationRequest.user_id, OperationRequest.account_id)
    operations_json = jsonable_encoder(operations)
    return JSONResponse(content=operations_json)
        
#удаление операции
#добавление кошелька 
#удаление кошелька
#вернуть все операции пользователя для статистики


#predefined params with ENUM class
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

# fake_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

# #get with args
# @app.get("/foo4/")
# async def read_item(skip: int = 0, limit: int = 10):
#     return fake_db[skip : skip + limit]

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

