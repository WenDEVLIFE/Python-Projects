print(" Pin number: 678903")
print(" Account Number: 893021")
print(" Account Password: @PYTH0N1SL1F3")
pin = int(input("Enter your pin number:"))

if pin == 678903:
    print("==============================")
    print("|Welcome To Python ATM Machine|")
    print("|Select an Option to continue |")
    print("==============================")
    print("[1] Deposit")
    print("[2] payout")
    print("[3] Exit")

    selection = int(input("Select An Option"))
    if selection == 1:

        print("==============================")
        print("=======Deposit Section========")
        print("==============================")
        account = int(input("Enter the Account number:\n"))
        password = input("Enter Your Password:\n")

        if account == 893021 and password == '@PYTH0N1SL1F3':
            bal1 = int(input("Enter The Balance"))
            bal = int(input("Enter The Remaining Balance"))
            addition: int = bal1 + bal
            print("The Total Balance is:", + addition)

        else:
            print("Unknown Account Please Try Again Later!!")

    elif selection == 2:
        print("==============================")
        print("=======Deposit Section========")
        print("==============================")
        account = int(input("Enter the Account number:\n"))
        password = input("Enter Your Password:\n")
        if account == 893021 and password == '@PYTH0N1SL1F3':
            bal1 = int(input("Enter The Balance"))
            bal = int(input("Enter The Remaining Balance"))
            difference: int = bal1 - bal
            print("The Total Balance is:", + difference)
        else:
            print("Unknown Account Please Try Again Later!!")
    else:
        print("Are you sure you want to exit")

else:
    print("No Pin Number Found, Please Try Again Later")

user_input = ''

while True:
    user_input = input('Do you want to continue? yes/no: ')

    if user_input.lower() == 'yes' or 'Yes' == user_input.upper():
        print(" Pin number: 678903")
        print(" Account Number: 893021")
        print(" Account Password: @PYTH0N1SL1F3")
        pin = int(input("Enter your pin number:"))

        if pin == 678903:
            print("==============================")
            print("|Welcome To Python ATM Machine|")
            print("|Select an Option to continue |")
            print("==============================")
            print("[1] Deposit")
            print("[2] payout")
            print("[3] Exit")

            selection = int(input("Select An Option"))
            if selection == 1:

                print("==============================")
                print("=======Deposit Section========")
                print("==============================")
                account = int(input("Enter the Account number:\n"))
                password = input("Enter Your Password:\n")

                if account == 893021 and password == '@PYTH0N1SL1F3':
                    bal1 = int(input("Enter The Balance"))
                    bal = int(input("Enter The Remaining Balance"))
                    addition: int = bal1 + bal
                    print("The Total Balance is:", + addition)

                else:
                    print("Unknown Account Please Try Again Later!!")

            elif selection == 2:
                print("==============================")
                print("=======Deposit Section========")
                print("==============================")
                account = int(input("Enter the Account number:\n"))
                password = input("Enter Your Password:\n")
                if account == 893021 and password == '@PYTH0N1SL1F3':
                    bal1 = int(input("Enter The Balance"))
                    bal = int(input("Enter The Remaining Balance"))
                    difference: int = bal1 - bal
                    print("The Total Balance is:", + difference)
                else:
                    print("Unknown Account Please Try Again Later!!")
            else:
                print("Are you sure you want to exit")

        else:
            print("No Pin Number Found, Please Try Again Later")
        continue
    elif user_input.lower() == 'no' or 'No' == user_input.upper():
        print('Program is going to terminate')
        break
    else:
        print('Type yes/no')
