#wap to return uppercase if the char is lower,else return same char (by taking user input)

char = input("Enter the character : ")
if char.islower():
    print(char.upper())
else:
    print(char)