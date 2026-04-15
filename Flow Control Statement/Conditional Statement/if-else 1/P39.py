#WAP to check whether a given key is present in the dict or not. if key is present: display the value or else add key and new value inside the dict.

dictionary = {"a": 1, "b": 2, "c": 3}
key = input("Enter a key: ")
if key in dictionary:
    print("Key found, value:",dictionary[key])
else:
    dictionary[key] = input("Enter a new value: ")
    print(dictionary)