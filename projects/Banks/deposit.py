from database import users

def deposit(account:int,deposit_amount:int)-> str:
    users[account]['balance'] += deposit_amount
    return f"{deposit_amount} deposite successful and\
                             current balance is :{users[account]['balance']}"