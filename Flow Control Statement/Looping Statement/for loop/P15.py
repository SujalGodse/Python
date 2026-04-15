#15.wap to create a dictionary index and word pair s="tomorrow is weekend and non-veg special"
from os.path import split

s = "tomorrow is weekend and non-veg special"
d={}
count=0
for i in s.split():
    d.update({count:i})
    count+=1
print(d)

#OR

print()
d1={}
x=s.split()
for i in range(len(x)):
    d1[i]=x[i]
print(d1)

#OR


print()
d2={}
for i,j in enumerate(s.split()):
    d2[i]=j
print(d2)