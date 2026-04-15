#.wap to return lower case if the upper ,else return same char (by taking user input)

char = input("Enter the character : ")
if char.isupper():
    print(char.lower())
else:
    print(char)