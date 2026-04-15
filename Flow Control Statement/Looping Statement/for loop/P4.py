#4.wap to extract only individual data types form the list l=["hello",1,23.4,5+6j,"guys",[2,3,4],True,False]

l=["hello",1,23.4,5+6j,"guys",[2,3,4],True,False]
integers=[]
floats=[]
booleans=[]
complexs=[]
for i in l:
    if isinstance(i,int):
        integers.append(i)
    if isinstance(i,float):
        floats.append(i)
    if isinstance(i,bool):
        booleans.append(i)
    if isinstance(i,complex):
        complexs.append(i)
print("Integer : ",integers)
print("Float : ",floats)
print("Complex : ",complexs)
print("Boolean : ",booleans)

print("\n")

for i  in l:
    if type(i) in((int,float,complex,bool)):
        print(i)