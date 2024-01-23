import sys
sys.path.append("C:/Users/gripo/PycharmProjects/FiCo/")

from pydantic import BaseModel
from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from datetime import datetime  # Import datetime for parsing operation_date
from app.logic.operation_model import Operation  # Assuming Operation class is defined in operation module
from app.logic.bank_account_model import BankAccount

from app.logic.user_model import User

import logging
logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="w+")

app = FastAPI()

SECRET_KEY = "your_secret_key"  # Замените на свой секретный ключ
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

class SessionToken(BaseModel):
    access_token: str
    token_type: str = "bearer"

class TokenData(BaseModel):
    username: str | None = None
        

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
        return token_data
    except JWTError:
        raise credentials_exception

@app.post("/token", response_model=SessionToken)
async def login_for_access_token(request: Request):
    form_data = await request.json()
    print(form_data)
    user = User.find_user(login=form_data['login'], password=form_data['password'])
    if user:
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": form_data['login']}, expires_delta=access_token_expires
        )
        return {"access_token": access_token, "token_type": "bearer"}
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
@app.post("/reg", response_model=SessionToken)
async def registrate(request: Request):
    form_data = await request.json()
    print(form_data)
    user = User.create_user(login=form_data['login'], password=form_data['password'],
                            email=form_data['email'], phoneNumber=form_data['phone'],
                            FNameLName=form_data['FNameLName'])
    if user:
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": form_data['login']}, expires_delta=access_token_expires
        )
        return {"access_token": access_token, "token_type": "bearer"}
    else:
        raise HTTPException(status_code=409, detail="User allready exists")
        

@app.get("/users/me", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

@app.get("/bank_accounts", response_model=list[BankAccount])
async def get_all_bank_accounts(current_user: TokenData = Depends(get_current_user)):
    id = User.get_id_by_login(current_user.username)
    bank_accounts = BankAccount.get_all_bank_accounts(id)
    print(current_user.username)
    return bank_accounts

# Sample route to edit the balance of a bank account
@app.post("/bank_account/{account_id}/edit_balance")
async def edit_balance(account_id: int, new_balance: float, current_user: TokenData = Depends(get_current_user)):
    # Perform additional authorization checks if needed
    # For example, check if the user has permission to edit this bank account
    # Create an instance of the BankAccount
    bank_account = BankAccount.from_db(account_id, balance=0, currency="USD", userID=current_user.username)
    # Edit the balance using the BankAccount method
    success = bank_account.edit_bank_data(account_id, 'balance', new_balance)
    if success:
        return {"message": "Balance updated successfully"}
    else:
        raise HTTPException(status_code=500, detail="Failed to update balance")

# Sample route to add a new category to a bank account
@app.post("/bank_account/{account_id}/add_category")
async def add_category(account_id: int, new_category: str, current_user: TokenData = Depends(get_current_user)):
    # Perform additional authorization checks if needed
    # For example, check if the user has permission to add a category to this bank account
    # Create an instance of the BankAccount
    bank_account = BankAccount.from_db(account_id, balance=0, currency="USD", userID=current_user.username)
    # Add a new category using the BankAccount method
    success = bank_account.add_new_category(new_category)
    if success:
        return {"message": f"Category '{new_category}' added successfully"}
    else:
        raise HTTPException(status_code=500, detail=f"Failed to add category '{new_category}'")

# Sample route to add a new operation to a bank account
@app.post("/bank_account/{account_id}/add_operation")
async def add_operation(account_id: int, new_operation: dict, current_user: TokenData = Depends(get_current_user)):
    # Perform additional authorization checks if needed
    # For example, check if the user has permission to add an operation to this bank account

    # Create an instance of the BankAccount
    bank_account = BankAccount.from_db(account_id, balance=0, currency="USD", userID=current_user.username)

    # Add a new operation using the BankAccount method
    success = bank_account.add_new_operation(new_operation)

    if success:
        return {"message": "Operation added successfully"}
    else:
        raise HTTPException(status_code=500, detail="Failed to add operation")
    
    # Sample route to edit the balance of a bank account
@app.post("/bank_account/{account_id}/edit_balance")
async def edit_balance(account_id: int, new_balance: float, current_user: TokenData = Depends(get_current_user)):
    # Perform additional authorization checks if needed
    # For example, check if the user has permission to edit this bank account

    # Create an instance of the BankAccount
    bank_account = BankAccount.from_db(account_id, balance=0, currency="USD", userID=current_user.username)

    # Edit the balance using the BankAccount method
    success = bank_account.edit_bank_data(account_id, 'balance', new_balance)

    if success:
        return {"message": "Balance updated successfully"}
    else:
        raise HTTPException(status_code=500, detail="Failed to update balance")

# Sample route to add a new category to a bank account
@app.post("/bank_account/{account_id}/add_category")
async def add_category(account_id: int, new_category: str, current_user: TokenData = Depends(get_current_user)):
    # Perform additional authorization checks if needed
    # For example, check if the user has permission to add a category to this bank account

    # Create an instance of the BankAccount
    bank_account = BankAccount.from_db(account_id, balance=0, currency="USD", userID=current_user.username)

    # Add a new category using the BankAccount method
    success = bank_account.add_new_category(new_category)

    if success:
        return {"message": f"Category '{new_category}' added successfully"}
    else:
        raise HTTPException(status_code=500, detail=f"Failed to add category '{new_category}'")

# Sample route to add a new operation to a bank account
@app.post("/bank_account/{account_id}/add_operation")
async def add_operation(account_id: int, new_operation: dict, current_user: TokenData = Depends(get_current_user)):
    # Perform additional authorization checks if needed
    # For example, check if the user has permission to add an operation to this bank account

    # Create an instance of the BankAccount
    bank_account = BankAccount.from_db(account_id, balance=0, currency="USD", userID=current_user.username)

    # Add a new operation using the BankAccount method
    success = bank_account.add_new_operation(new_operation)

    if success:
        return {"message": "Operation added successfully"}
    else:
        raise HTTPException(status_code=500, detail="Failed to add operation")
