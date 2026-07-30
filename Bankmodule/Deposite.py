from data import users

def deposit(account, amount):

    users[account]["balance"] += amount

    return f"{amount} Deposited Successfully\nCurrent Balance : {users[account]['balance']}"