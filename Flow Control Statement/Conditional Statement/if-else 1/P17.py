#WAP to check whether a given character is in the alphabet or not. if alphabet, display the alphabet with character or else display the not alphabet with character.

char = input("Enter a character: ")
if char.isalpha():
    print("Alphabet:",char)
else:
    print("Not an alphabet:",char)