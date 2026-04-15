#WAP to check whether a given length of the string is odd or not. if odd, to append the new string ("Hii") from the starting of the given string, or else to avoid the starting character and ending character of the given string and to display the remaining characters.

string = input("Enter a string: ")
if len(string) % 2 != 0:
    print("Haii" + string)
else:
    print("Remaining characters:",string[1:-1])