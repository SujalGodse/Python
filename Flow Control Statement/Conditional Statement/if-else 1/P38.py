#WAP to check whether a given value is present inside the collection or not. If present, print the value or else print value is not found.

collection = [1, 2, 3, 4, 5, "hello"]
value = eval(input("Enter value to search: "))
if value in collection:
    print("Value is found:",value)
else:
    print("Value is not found")