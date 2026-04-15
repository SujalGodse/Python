#WAP to check whether the given number lies between 1 to 19, if it is true square that number or else false cube that number and display the number.

num = eval(input("Enter a number: "))
if 1 <= num <= 19:
    print("Square:",num ** 2)
else:
    print("Cube:",num ** 3)