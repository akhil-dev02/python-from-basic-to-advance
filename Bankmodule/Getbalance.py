from data import users

def get_balance(account: int):

    curr_balance = users[account]["balance"]

    return f"Current Balance is : {curr_balance}"