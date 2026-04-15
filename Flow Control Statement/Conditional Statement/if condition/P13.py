#wap to check the given value is string (take user input)

value = eval(input("Enter a value: "))
if isinstance(value, str):
    print("The given value is a string.")