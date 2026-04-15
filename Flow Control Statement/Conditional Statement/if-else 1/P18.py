#WAP to check whether a given character is uppercase or other character. if uppercase, display the uppercase with character or else display the other character with character.

char = input("Enter a character : ")
if char.isupper():
    print("Uppercase :",char)
else:
    print("Other character :",char)