#5.wap to extract only individual data types from the list and sum all the individual data types l=["hello",1,23.4,5+6j,"guys",[2,3,4],True,False]

l=["hello",1,23.4,5+6j,"guys",[2,3,4],True,False]
integers=0
floats=0
booleans=0
complexs=0
for i in l:
    if isinstance(i,int):
        integers+=i
    if isinstance(i,float):
        floats+=i
    if isinstance(i,bool):
        booleans+=i
    if isinstance(i,complex):
        complexs+=i
print("Integer : ",integers)
print("Float : ",floats)
print("Complex : ",complexs)
print("Boolean : ",booleans)

print("\n\n\n")
print("***********************************")
print("\n\n\n")
sum=0
for i in l:
    if isinstance(i,(int,float,complex,bool)):
        sum+=i
        print(i)
print("Sum = ",sum)
