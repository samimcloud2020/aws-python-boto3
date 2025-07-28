from pydantic import BaseModel, PositiveFloat, PositiveInt, constr
from typing import Optional

# Pydantic model for account data validation
class AccountData(BaseModel):
    account_holder: constr(min_length=1, max_length=100, pattern=r'^[A-Za-z\s]+$')  # Ensures string with letters and spaces
    account_number: PositiveInt  # Ensures positive integer
    balance: float = 0.0
    interest_rate: Optional[PositiveFloat] = None
    overdraft_limit: Optional[PositiveFloat] = None

# Base class for bank accounts
class BankAccount:
    def __init__(self, account_data: AccountData):
        self._account_holder = account_data.account_holder
        self._account_number = account_data.account_number
        self._balance = account_data.balance

    def deposit(self, amount: float) -> str:
        if amount <= 0:
            return "Invalid deposit amount"
        try:
            validated_amount = PositiveFloat(amount)
            self._balance += validated_amount
            return f"Deposited ${validated_amount:.2f}. New balance: ${self._balance:.2f}"
        except ValueError:
            return "Invalid deposit amount"

    def withdraw(self, amount: float) -> str:
        if amount <= 0:
            return "Invalid withdrawal amount"
        if amount <= self._balance:
            self._balance -= amount
            return f"Withdrew ${amount:.2f}. New balance: ${self._balance:.2f}"
        return "Insufficient funds"

    def get_balance(self) -> str:
        return f"Account balance: ${self._balance:.2f}"

    def get_account_info(self) -> str:
        return f"Account Holder: {self._account_holder}, Account Number: {self._account_number}"


# Derived class for Savings Account
class SavingsAccount(BankAccount):
    def __init__(self, account_data: AccountData):
        super().__init__(account_data)
        self._interest_rate = account_data.interest_rate or 0.02

    # Polymorphic method overriding withdraw
    def withdraw(self, amount: float) -> str:
        withdrawal_fee = 5
        if amount <= 0:
            return "Invalid withdrawal amount"
        try:
            validated_amount = PositiveFloat(amount)
            total_amount = validated_amount + withdrawal_fee
            if total_amount <= self._balance:
                self._balance -= total_amount
                return f"Withdrew ${validated_amount:.2f} (+${withdrawal_fee:.2f} fee). New balance: ${self._balance:.2f}"
            return "Insufficient funds"
        except ValueError:
            return "Invalid withdrawal amount"

    def apply_interest(self) -> str:
        interest = self._balance * self._interest_rate
        self._balance += interest
        return f"Applied interest ${interest:.2f}. New balance: ${self._balance:.2f}"


# Derived class for Checking Account
class CheckingAccount(BankAccount):
    def __init__(self, account_data: AccountData):
        super().__init__(account_data)
        self._overdraft_limit = account_data.overdraft_limit or 100

    # Polymorphic method overriding withdraw
    def withdraw(self, amount: float) -> str:
        if amount <= 0:
            return "Invalid withdrawal amount"
        try:
            validated_amount = PositiveFloat(amount)
            if validated_amount <= (self._balance + self._overdraft_limit):
                self._balance -= validated_amount
                return f"Withdrew ${validated_amount:.2f}. New balance: ${self._balance:.2f}"
            return "Overdraft limit exceeded"
        except ValueError:
            return "Invalid withdrawal amount"


# Example usage
def main():
    try:
        # Create validated account data using Pydantic
        savings_data = AccountData(
            account_holder="John Doe",
            account_number=123456,
            balance=1000,
            interest_rate=0.02
        )
        checking_data = AccountData(
            account_holder="Jane Smith",
            account_number=456789,
            balance=500,
            overdraft_limit=100
        )

        # Create instances of different account types
        savings = SavingsAccount(savings_data)
        checking = CheckingAccount(checking_data)

        # Demonstrate polymorphism through common interface
        accounts = [savings, checking]

        for account in accounts:
            print(account.get_account_info())
            print(account.deposit(200))
            print(account.withdraw(100))
            print(account.get_balance())
            if isinstance(account, SavingsAccount):
                print(account.apply_interest())
            print()

    except ValueError as e:
        print(f"Validation error: {e}")

if __name__ == "__main__":
    main()
