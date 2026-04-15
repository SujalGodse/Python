#11.wap to create a dictionary with element and its count pair l=["yellow","red","black","pink","orange","green","red","pink","yello w"]

l = ["yellow", "red", "black", "pink", "orange", "green", "red", "pink", "yellow"]
count_dict = {}
for item in l:
    if item in count_dict:
        count_dict[item] += 1
    else:
        count_dict[item] = 1
print(count_dict)

print("\n*****************************\n")
d={}
for i in l:
    d[i]=l.count(i)
print(d)