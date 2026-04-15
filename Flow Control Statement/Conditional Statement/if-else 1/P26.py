#WAP to check whether the given input character is uppercase or lowercase. If the input character is upper case convert into lower case and vice versa.

char = input("Enter a character: ")
if char.isupper():
    print("Converted to lowercase:",char.lower())
else:
    print("Converted to uppercase:",char.upper())