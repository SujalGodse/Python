#WAP to check whether a given character is lowercase or other character. if lowercase, display the lowercase with character or else display the other character with character.

char = input("Enter a character : ")
if char.islower():
    print("Lowercase :",char)
else:
    print("Other character :",char)