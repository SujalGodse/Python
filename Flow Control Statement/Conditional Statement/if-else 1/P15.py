#WAP to check whether a given value is even and in range of 47 to 58 and not in 0 or odd. if condition is True, to perform display the ascii character. or else to perform floor division with 5 and display it.

num = eval(input("Enter a number: "))
if num % 2 == 0 and 47 <= num <= 58 and (num != 0 or num%2!=0):
    print("ASCII character:",chr(num))
else:
    print("Floor division by 5:",num // 5)