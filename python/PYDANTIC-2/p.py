from pydantic import BaseModel , PositiveFloat, EmailStr, Field
from datetime import date
from typing import Optional
from enum import Enum

class AccountStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    FROZEN = "frozen"

#pydantic model for BankAccount
class BankAccount(BaseModel):
    account_number: str =Field(min_length=10, max_length=100, description="account number")
    account_holder: str=Field(min_length=2, max_length=100, description="account holder")
    email: EmailStr=Field(description="email")
    balance: PositiveFloat=Field(description="balance")
    created_date: date=Field(description="date")
    account_status: AccountStatus=Field(deafult=AccountStatus.ACTIVE,description="account status")
    last_transcation: Optional[date]=Field(None, description="last transcation")


if __name__ == "__main__":

    try:
        valid_account_data= {
            "account_number": "12345678908",
            "account_holder":"s k patel",
            "email": "samim1000@gmail.com",
            "balance": 10.0,
            "created_date": date(2025, 7, 29),
            "account_status": AccountStatus.ACTIVE,
            "last_transcation": date(2024,7,29)
        }
    except ValueError as e:
        print(f" Error is {e}")
    account = BankAccount(**valid_account_data)
    print(account)

    # Example of a data conflict
    conflicting_account_data = {
        "account_number": "123456789",  # Too short (9 digits instead of 10)
        "account_holder": "Bob",  # Valid
        "email": "invalid-email",  # Invalid email format
        "account_status": "closed",  # Invalid status (not in AccountStatus enum)
        "balance": -100.0,  # Negative balance
        "created_date": date(2024, 3, 10),
        "last_transaction": None
    }

    try:
        conflicting_account = BankAccount(**conflicting_account_data)
    except ValueError as e:
        print("Validation Errors:", e)
