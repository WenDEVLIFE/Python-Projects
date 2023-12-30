# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# String
name = input("Enter your name:")
address = input("Enter your address:")
age = input("Age:")
birthday = input("Enter your birthday:")
# Print the variables
print("My Name is " + name)
print("My address is " + address)
print("My age  is " + age)
print("My Name is " + birthday)
# While loop conditions
user = ''
while True:
    user = input('Do you want to continue? yes/no: ')

    if user.lower() == 'yes':
        name = input("Enter your name:")
        address = input("Enter your address:")
        age = input("Age:")
        birthday = input("Enter your birthday:")

        print("My Name is " + name)
        print("My address is " + address)
        print("My age  is " + age)
        print("My Name is " + birthday)
        continue
    elif user.lower() == 'no':
        print('User typed no')
        break
    else:
        print('Type yes/no')
user_input = ''

while True:
    user_input = input('Do you want to continue? yes/no: ')

    if user_input.lower() == 'yes':
        print('User typed yes')
        continue
    elif user_input.lower() == 'no':
        print('User typed no')
        break
    else:
        print('Type yes/no')