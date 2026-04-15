#WAP to the given number integer, if n is greater than 21,print the absolute difference between n and 21 otherwise print twice the absolute difference.

n = eval(input("Enter a number: "))
if n > 21:
    print("Absolute Difference: ",(abs(n - 21)))
else:
    print("Twice the Absolute Difference: ",(2 * abs(n - 21)))