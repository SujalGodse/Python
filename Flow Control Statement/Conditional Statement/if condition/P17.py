#wap to check whether the given number is even or not,if even store the value inside the list (take user input)

num = eval(input("Enter the number : "))
l = []
if num%2==0:
    l.append(num)
    print(l)