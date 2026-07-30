from data import users

def withdraw(account, amount):

    if users[account]["balance"] >= amount:

        users[account]["balance"] -= amount

        return f"{amount} Withdraw Successful\nCurrent Balance : {users[account]['balance']}"

    return "Insufficient Amount"