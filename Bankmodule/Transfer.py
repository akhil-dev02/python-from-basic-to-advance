from data import users

def transfer(sender_account, receiver_account, amount):

    if receiver_account not in users:
        return "Receiver Account Not Found"

    if users[sender_account]["balance"] >= amount:

        users[sender_account]["balance"] -= amount
        users[receiver_account]["balance"] += amount

        return f"{amount} Transfer Successful\nCurrent Balance : {users[sender_account]['balance']}"

    return "Insufficient Amount"