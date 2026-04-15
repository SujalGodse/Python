#wap to check a data is individual or collection data type or not (take user input)

data = eval(input("Enter the data : "))
if isinstance(data,(str,tuple,dict,set,list)):
    print("Data is Collection Data type")
else:
    print("Individual data type")