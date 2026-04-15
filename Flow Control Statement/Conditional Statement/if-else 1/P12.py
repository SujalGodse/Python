#WAP to check whether the given input is divisible by 3 and 5. If yes print the actual number or else print string of that number.

num = eval(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print("Divisible by 3 and 5:",num)
else:
    print("String of the number:",str(num))