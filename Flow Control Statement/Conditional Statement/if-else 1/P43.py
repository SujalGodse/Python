#WAP to check whether the given string is palindrome or not if it is a palindrome string palindrome along with the string if it is not a palindrome print not palindrome

string = input("Enter a string: ")
if string == string[::-1]:
    print(string,"is a Palindrome")
else:
    print("Not a Palindrome")