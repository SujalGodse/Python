#wap to check the given number is greater than 5,if it is greater convert that number into negative number else print the same number

num = eval(input("Enter the number : "))
if num>5:
    print("Negative number after converting :",-abs(num))
else:
    print("Number is ",num)