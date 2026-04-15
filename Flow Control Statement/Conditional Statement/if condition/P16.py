#wap to check whether given input is divisible by 2 and 6 if condition is True ,convert the given number to complex number.(take user input)

x = eval(input("Enter the number : "))
if x%2==0 and x%6==0:
    print(complex(x))