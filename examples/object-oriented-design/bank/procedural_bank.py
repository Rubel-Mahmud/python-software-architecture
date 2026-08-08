# Global storage for bank accounts
ACCOUNTS = {}

# Procedures to operate the bank 
## Account creation
def create_account(account_id, owner):
    if not owner or not account_id:
        return "Provide account owner or account ID"

    if not account_id in ACCOUNTS:
        ACCOUNTS[account_id] = {
            "account_id": account_id,
            "owner": owner,
            "balance": 0,
        }
    
    return ACCOUNTS[account_id]

## Deposit Money
def deposit(account_id, amount):
    if not account_id or not amount:
        return "Provide account_id or amount"

    if not account_id in ACCOUNTS:
        return "Account not found."

    if amount <= 0:
        return "Amount should be greater than 0"

    ACCOUNTS[account_id]['balance'] += amount
    
    return ACCOUNTS[account_id]['balance']

## Withdraw Money
def withdraw(account_id, amount):
    if not account_id or not amount:
        return "Provide account_id or amount"

    if not account_id in ACCOUNTS:
            return "Account not found."
    
    if amount <= 0:
        return "Amount should be greater than 0"

    current_balance = ACCOUNTS[account_id]['balance']

    if current_balance < amount:
        return "Insufficient balance"

    ACCOUNTS[account_id]['balance'] -= amount

    return ACCOUNTS[account_id]['balance']


## Show balance
def get_balance(account_id):
    if not account_id:
        return "Provide account ID"

    if not account_id in ACCOUNTS:
        return "Account not found!"

    return ACCOUNTS[account_id]['balance']



# create_account("ACC01", "Rubel")
# print("Account Info: ")
# balance = get_balance('ACC01')
# print(f"Owner: {ACCOUNTS['ACC01']['owner']}, Balance: {balance}")
# print()

# deposit('ACC01', 100)
# print("Balance after deposit 100: ")
# balance = get_balance('ACC01')
# print(f"Owner: {ACCOUNTS['ACC01']['owner']}, Balance: {balance}")
# print()

# withdraw("ACC01", 50)
# print("Balance after withdraw 50: ")
# balance = get_balance('ACC01')
# print(f"Owner: {ACCOUNTS['ACC01']['owner']}, Balance: {balance}")
# print()

# print("Trying to withdraw insufficient(500) amount...")
# print(withdraw("ACC01", 500))
# print()

# print("Deposit negative amount(-500):")
# print(deposit('ACC01', -500))
# print()

# print("Trying withdraw from invalid account ('AC03')...")
# print(withdraw('AC03', 1000))
# print()

# print("Bypassing the deposit process and modifying account balance directly...")
# ACCOUNTS['ACC01']['balance'] += 999
# balance = get_balance('ACC01')
# print(f"Owner: {ACCOUNTS['ACC01']['owner']}, Balance: {balance}")
# print()