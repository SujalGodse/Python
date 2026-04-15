#WAP to check if the given string of first and second character should be sequence or not. if the sequence prints the first, second and last two characters, or else the first half string is reversed and the remaining half string should be normal and display it.

string = input("Enter a string: ")
if len(string) >= 2 and ord(string[1]) - ord(string[0]) == 1:
    print(string[:2] + string[-2:])
else:
    half = len(string) // 2
    print(string[:half][::-1] + string[half:])