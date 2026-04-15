#WAP to check whether a given collection is set or not. if set, append the new value, or else eliminate the duplicate values in collection. final results should be set type.

collection = eval(input("Enter a collection: "))
if isinstance(collection, set):
    collection.add(eval(input("Enter a new value: ")))
else:
    collection = set(collection)
print(collection)