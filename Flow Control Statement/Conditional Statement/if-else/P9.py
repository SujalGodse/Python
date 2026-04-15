#wap to check number should be divisible by 3 and 7 (take user input)

num = eval(input("Enter the number : "))
if num%3==0 and num%7==0:
    print("The number is divisible by 3 and 7")
else:
    print("The number is not divisible by 3 and 7")