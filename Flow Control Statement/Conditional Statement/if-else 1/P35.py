#WAP to check whether a given value is a list and first and last values should be integer if condition is satisfied first value is True division by 3 and perform the bitwise not for last value and those result values are stored in same positions in given list or else, to perform length of the collection power by 2 and display value.

value = eval(input("Enter a list: "))  # Using eval to accept list input
if isinstance(value, list) and isinstance(value[0], int) and isinstance(value[-1], int):
    value[0] = value[0] // 3
    value[-1] = ~value[-1]
    print(value)
else:
    print(len(value) ** 2)