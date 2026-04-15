#WAP to check whether the given number is divisible by 3 or not if yes, print the number or else print the cube of the numbers.

num = eval(input("Enter a number: "))
if num % 3 == 0:
    print("Divisible by 3:",num)
else:
    print("Cube of the number:",num**3)