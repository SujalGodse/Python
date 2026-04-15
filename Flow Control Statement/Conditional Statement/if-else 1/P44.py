#WAP to check whether a given number is palindrome or not. If palindrome, display the given value as a palindrome or else not a palindrome.

num = input("Enter a string: ")
if num == num[::-1]:
    print(num,"is a Palindrome")
else:
    print("Not a Palindrome")