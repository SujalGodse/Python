#wap to check the given number is smaller than 10 ,if it is smaller find the exponent of it else print the number as it is

num = eval(input("Enter a number: "))
if num < 10:
    print("Exponent :", num ** 2)
else:
    print("Number :", num)