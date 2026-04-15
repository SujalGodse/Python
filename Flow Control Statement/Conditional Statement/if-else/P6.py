#wap to check if the given number is even or not,if it is not even add+1 and make it even (take user input)

num = eval(input("Enter the number : "))
if num%2==0:
    print("The given number is even.")
else:
    num+=1
    print("The even number is ",num)