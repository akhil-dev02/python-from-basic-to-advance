from Login import login
from Register import register
from Deposite import deposit
from Getbalance import get_balance
from Withdraw import withdraw
from Transfer import transfer
from Ministatement import mini_statement
from logout import logout

while True:

    print("\n===== BANK MENU =====")
    print("1.Register")
    print("2.Login")
    print("3.Deposit")
    print("4.Withdraw")
    print("5.Get Balance")
    print("6.Transfer")
    print("7.Mini Statement")
    print("8.Logout")
    print("9.Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        username = input("Enter Name: ")
        gmail = input("Enter Gmail: ")
        balance = int(input("Enter Balance: "))
        password = input("Enter Password: ")

        print(register(username, gmail, balance, password))

    elif choice == 2:
        login()

    elif choice == 3:
        account = int(input("Enter Account Number: "))
        amount = int(input("Enter Amount: "))

        print(deposit(account, amount))

    elif choice == 4:
        account = int(input("Enter Account Number: "))
        amount = int(input("Enter Amount: "))

        print(withdraw(account, amount))

    elif choice == 5:
        account = int(input("Enter Account Number: "))

        print(get_balance(account))

    elif choice == 6:
        sender = int(input("Enter Sender Account: "))
        receiver = int(input("Enter Receiver Account: "))
        amount = int(input("Enter Amount: "))

        print(transfer(sender, receiver, amount))

    elif choice == 7:
        account = int(input("Enter Account Number: "))

        print(mini_statement(account))

    elif choice == 8:
        logout()

    elif choice == 9:
        print("Thank You...")
        break

    else:
        print("Invalid Choice")