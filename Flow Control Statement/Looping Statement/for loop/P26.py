#3. WAP to remove duplicates from the list without using inbuilt function

d=[1,2,3,4,5,6,7,1,2,3,4]
l=[]
for i in d:
    if i not  in l:
        l.append(i)
print(l)