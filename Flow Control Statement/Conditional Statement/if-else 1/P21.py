#WAP to check whether the given character is in lowercase or uppercase. If it is in lowercase, convert it into uppercase, or else it is in uppercase and convert it into lowercase. Display the value.

char = input("Enter a character: ")
if char.islower():
    print("Uppercase:",char.upper())
else:
    print("Lowercase:",char.lower())