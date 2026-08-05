from database import users
from emailsend import SingleEmailSend

def withdraw(account: int, withdraw_amount: int) -> str:
    curr_balance = users[account]["balance"]

    if curr_balance >= withdraw_amount:
        users[account]["balance"] -= withdraw_amount

        email_status = SingleEmailSend(
            to_email=users[account]["email"],
            subject="Withdrawal Alert",
            body=f"{withdraw_amount} withdrawn successfully.\nCurrent Balance: {users[account]['balance']}"
        )

        print(email_status)   # <-- Important

        return f"{withdraw_amount} withdrawn successful and current balance is : {users[account]['balance']}"

    return "Insufficient Amount"