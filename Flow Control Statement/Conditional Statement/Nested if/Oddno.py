#wap to check the given no. is odd and divisible by 7

num=eval(input("Enter a number : "))
if num%2!=0:
    print(f"The given number {num} is  odd")
    if num%7==0:
        print(f"The number {num} is divisible by 5")
    else:
        print(f"The number {num} is not divisible by 5")
else:
    print(f"The given number {num} is  even")