#WAP to check whether the given value is present inside the given collection or not.if value is present, display the value is available or else the value is not present.

collection = [1, 2, 3, 4, 5, "hello"]
value = eval(input("Enter value to search: "))
if value in collection:
    print("Value is present")
else:
    print("Value is not present")