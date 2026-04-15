#WAP to check whether the last of the given string is a special character or not, if the special character prints reverse the string except the last character or else to check if the length of the string is odd or not, if odd to extract the middle character to the end of the string.

string = input("Enter a string: ")
if not string[-1].isalnum():
    print("Reversed without last character:",string[-2::-1])
elif len(string) % 2 != 0:
    middle = len(string) // 2
    print(string[:middle] + string[middle+1:] + string[middle])
else:
    print(string)