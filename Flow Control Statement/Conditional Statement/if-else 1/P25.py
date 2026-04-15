#WAP to check whether a given string of first character is alphabet or not if the alphabet prints, reverse the string or else print the middle character.

string = input("Enter a string: ")
if string[0].isalpha():
    print("Reversed string:",string[::-1])
else:
    print("Middle character:",string[len(string)//2])