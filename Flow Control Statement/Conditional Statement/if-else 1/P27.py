#WAP to check whether a given string is less than 3 characters, to print the entire string otherwise to print after third positions to the remaining string.

string = input("Enter a string: ")
if len(string) < 3:
    print("Entire string: ",string)
else:
    print("String after third position :",string[3:])