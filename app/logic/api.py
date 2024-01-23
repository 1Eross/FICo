import sys
sys.path.append("C:\\Users\\gripo\\PycharmProjects\\FiCo")

from app.auth.api import get_current_user
from app.logic.user_model import User


from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from datetime import datetime  # Import datetime for parsing operation_date
from app.logic.operation_model import Operation  # Assuming Operation class is defined in operation module
from fastapi import Depends, HTTPException
from app.logic.bank_account_model import BankAccount
from app.auth.api import get_current_user, TokenData

app = FastAPI()

@app.get("/bank_accounts", response_model=list[BankAccount])
async def get_all_bank_accounts(current_user: TokenData = Depends(get_current_user)):
    bank_accounts = BankAccount.get_all_bank_accounts(current_user.username)
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
    
    
