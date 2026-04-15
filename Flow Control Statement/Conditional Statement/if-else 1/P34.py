#WAP whether a given string, if string length is more than 2, then it displays a new string with the first and last characters switched, otherwise the display the 3 copies of given string.

string = input("Enter a string: ")
if len(string) > 2:
    print(string[-1] + string[1:-1] + string[0])
else:
    print(string * 3)