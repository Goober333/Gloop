def encode(userinput):
    if len(userinput) == 8:
        newstring = ''
        for char in userinput:
            char1 = int(char) + 3
            newstring += str(char1)
    return newstring

def decode(password):
    new_list = []
    pass_list = list(password)
    for i in pass_list:
        new_list.append(int(i))
    for i in range(len(new_list)):
        if new_list[i] > 2:
            new_list[i] -= 3
        elif new_list[i] < 3:
            new_list[i] += 7
    new_string = ''.join(map(str, new_list))
    return new_string


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
