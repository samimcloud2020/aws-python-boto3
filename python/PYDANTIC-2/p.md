account_number='12345678908' 

account_holder='s k patel' 

email='samim1000@gmail.com' 

balance=10.0 

created_date=datetime.date(2025, 7, 29) 

account_status=<AccountStatus.ACTIVE: 'active'> 

last_transcation=datetime.date(2024, 7, 29)

Validation Errors: 4 validation errors for BankAccount
### account_number
  String should have at least 10 characters [type=string_too_short, input_value='123456789', input_type=str]
    For further information visit https://errors.pydantic.dev/2.11/v/string_too_short
### email
  value is not a valid email address: An email address must have an @-sign. [type=value_error, input_value='invalid-email', input_type=str]
### balance
  Input should be greater than 0 [type=greater_than, input_value=-100.0, input_type=float]
    For further information visit https://errors.pydantic.dev/2.11/v/greater_than
### account_status
  Input should be 'active', 'inactive' or 'frozen' [type=enum, input_value='closed', input_type=str]
    For further information visit https://errors.pydantic.dev/2.11/v/enum
