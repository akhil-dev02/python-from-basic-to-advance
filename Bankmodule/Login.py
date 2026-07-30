from data import users

def login():
    account = int(input("Enter Account Number: "))
    password = input("Enter Password: ")

    if account in users:
        if users[account]["password"] == password:
            print("Login Successful")
            return True

    print("Invalid Account or Password")
    return False