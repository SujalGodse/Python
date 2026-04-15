#wap to check the length of dictionary and length of dictionary is even or Not if even print as it is or else add a item and make it even

D={"a":"apple","b":"ball","c":"cat"}
print("The length of the dictionary is",len(D))
if len(D)%2==0:
    print(D)
else:
    D.update({"d":"dog"})
    print("Updated dictionary :",D)