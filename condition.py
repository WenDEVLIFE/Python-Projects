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