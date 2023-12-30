print("=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("|   Advance Python Calculator                |")
print("=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
num = int(input("Select a Number \n"))
if num == 1:
    num1 = int(input("Enter a First number \n"))
    num2 = int(input("Enter a Second number \n"))
    print("The result is ", + num1 + num2)
elif num == 2:
    num1 = int(input("Enter a First number \n"))
    num2 = int(input("Enter a Second number \n"))
    print("The result is ", + num1 - num2)
elif num == 3:
    num1 = int(input("Enter a First number \n"))
    num2 = int(input("Enter a Second number \n"))
    print("The result is ", + num1 * num2)
elif num == 4:
    num1 = int(input("Enter a First number \n"))
    num2 = int(input("Enter a Second number \n"))
    print("The result is ", + num1 / num2)
else:
    print("Error")

user_input = ''
while True:
    user_input = input('Do you want to continue? yes/no: ')

    if user_input.lower() == 'yes':
        print("=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("|   Advance Python Calculator                |")
        print("=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        num = int(input("Select a Number \n"))
        if num == 1:
            num1 = int(input("Enter a First number \n"))
            num2 = int(input("Enter a Second number \n"))
            print("The result is ", + num1 + num2)
        elif num == 2:
            num1 = int(input("Enter a First number \n"))
            num2 = int(input("Enter a Second number \n"))
            print("The result is ", + num1 - num2)
        elif num == 3:
            num1 = int(input("Enter a First number \n"))
            num2 = int(input("Enter a Second number \n"))
            print("The result is ", + num1 * num2)
        elif num == 4:
            num1 = int(input("Enter a First number \n"))
            num2 = int(input("Enter a Second number \n"))
            print("The result is ", + num1 / num2)
        else:
            print("Error")
        continue
    elif user_input.lower() == 'no':
        print('User typed no')
        break
    else:
        print('Type yes/no')


