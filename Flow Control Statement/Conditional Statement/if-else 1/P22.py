#WAP to check whether the given string of the first character is a special symbol or not. If a special symbol, to extract and display the middle character or else to reverse the string and display the half of the string.

s = input("Enter a string: ")
if not s[0].isalnum():
    print("Middle character:",s[len(s)//2])
else:
    print("Reversed half:",s[::-1][:len(s)//2])