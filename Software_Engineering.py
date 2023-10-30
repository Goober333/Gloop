def encode(userinput):
    if len(userinput) == 8:
        newstring = ''
        for char in userinput:
            char1 = int(char) + 3
            newstring += str(char1)
    return newstring




while True:
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
    option = int(input('Please enter an option:'))

    if option == 1:
        password = input('Please enter your password to encode:')
        encode(password)
        print('Your password has been encoded and stored!')
    if option == 2:
        print(f'The encoded password is {encode(password)}, and the original password is {decode(encode(password))}')
    if option == 3:
        break
