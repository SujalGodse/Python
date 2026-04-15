#wap to check the given number is odd, if it is odd divide it by 2 and print reminder and quotient else print it is even (take user input)

num = eval(input("Enter a number : "))
if num%2!=0:
    print("Quotient and Remainder :",divmod(num,2))
else:
    print("It is even.")