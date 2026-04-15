#list data type, if option 1 pop(), option 2 sort(), option 3 clear()

data=eval(input("Enter a list : "))
if isinstance(data,list):
    option=eval(input("Enter the option(1,2,3) : "))
    if option==1:
        print(data.pop())
    elif option==2:
        print(data.sort())
    elif option==3:
        print(data.clear())
    else:
        print("Invalid option")
else:
    print("Invalid data type")


#wap to give 10% off only who is purchasing in credit card and minimum 3 product should be purchased and each product price should be more than 500.
#wap to book ticket in Bookmyshow