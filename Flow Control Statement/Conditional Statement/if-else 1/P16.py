#WAP to check whether a given value is less than 125 and in between47 to 125 or not. if condition is True, to perform store the given value as key and value as a character into the dict or else to append the value in list and display it.

num = eval(input("Enter a number: "))
result = {}
l = []
if 47 <= num < 125:
    result = {num: chr(num)}
    print("Dictionary:",result)
else:
    l.append(num)
    print("Added to list:",l)