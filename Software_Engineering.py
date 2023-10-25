def encode():
    userinput = input("Enter Password: ")
    if len(userinput) == 8:
        newstring = ''
        for char in userinput:
            char1 = int(char) + 3
            newstring += str(char1)
    return newstring

