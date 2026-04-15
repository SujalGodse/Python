#wap to check whether a character is in uppercase or not,if uppercase,convert to lowercase and store the value inside the dictionary (character as key and ascii as value) take user input

char = input("Enter the character : ")
a = {}
if char.isupper():
    a.update({char:ord(char.lower())})
    print("Dictionary : ",a)