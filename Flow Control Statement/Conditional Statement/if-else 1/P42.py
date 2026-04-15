#WAP to check whether a given value is even and in between 47 to 58 and not in 0 or odd. if condition is True, to perform display the ascii character or else to perform floor division with 5 and display it.

value = eval(input("Enter a number: "))
if value % 2 == 0 and 47 <= value <= 58:
    print(chr(value))
else:
    print(value // 5)