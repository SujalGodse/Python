#WAP to accept two integers and check whether those two values are equal or not. If equal, multiply to value or else to display the quotation value.

num1 = eval(input("Enter first number: "))
num2 = eval(input("Enter second number: "))
if num1 == num2:
    print("Product:", num1 * num2)
else:
    print("Quotient:", num1 // num2)