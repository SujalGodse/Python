#wap to check whether a given value is divisible by 5 and 7,if the value is divisible then display the square of the values (take user input)

value = eval(input("Enter the value : "))
if value%5==0 and value%7==0:
    print("Square : ",value**2)