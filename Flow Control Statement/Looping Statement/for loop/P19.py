#19.wap to  create a list of characters and its Ascii value pair s="sunday"
#o/p:-->[('s', 115), ('u', 117), ('n', 110), ('d', 100), ('a', 97), ('y', 121)

s="sunday"
l=[]
for i in s:
    l.append((i,ord(i)))
print(l)