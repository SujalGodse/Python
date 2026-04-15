#wap to check if the given number is even ,if it is even reduce it to its Half else make exponent (take user input)
x = eval(input("Enter the number : "))
if x%2==0:
    print("Half is ",x//2)
else:
    print("Exponent is ",x**2)