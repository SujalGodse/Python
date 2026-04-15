#WAP to check whether a given character is uppercase or other character. if uppercase, convert to lowercase .or else display the ascii number.

char = input("Enter a character: ")
if char.isupper():
    print("Lowercase:",char.lower())
else:
    print("ASCII:",ord(char))