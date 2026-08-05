from database import users

def transfer(sender_account:int,receiver_account:int,transfer_amount:int)-> str:
    if sender_account == receiver_account:
        return "Cannot transfer to the same account"

    if receiver_account not in users:
        return "Receiver account does not exist"

    if users[sender_account]['balance'] >= transfer_amount:
        users[sender_account]['balance'] -= transfer_amount
        users[receiver_account]['balance'] += transfer_amount

        return f"{transfer_amount} transferred successfully to account {receiver_account} and\
                 current balance is :{users[sender_account]['balance']}"

    return "Insufficient Amount"