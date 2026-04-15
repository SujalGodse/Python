#WAP to find out the greatest of two numbers and display the greatest number. if the greatest number, display the greatest message with value.

a = eval(input("Enter first number: "))
b = eval(input("Enter second number: "))
if a > b:
    print("Greatest:",a)
elif b > a:
    print("Greatest:",b)
else:
    print("Both are equal")