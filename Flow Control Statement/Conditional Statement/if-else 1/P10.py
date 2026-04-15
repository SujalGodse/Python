#WAP to check whether the given number is even or odd. If it is even then make it as an odd number, if it is an odd number then make it as even number.

num = eval(input("Enter a number: "))
if num % 2 == 0:
    print("Converted to Odd:",num + 1)
else:
    print("Converted to Even:",num - 1)