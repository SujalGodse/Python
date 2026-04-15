#17.wap to create a dictionary characters and its corresponding upper case characters s="sunday"
#o/p:-->{'s': 'S', 'u': 'U', 'n': 'N', 'd': 'D', 'a': 'A', 'y': 'Y'}

s="sunday"
d={}
for i in s:
    d.update({i:i.upper()})
print(d)

#OR

print()
d1={}
for i in s:
    d1[i]=i.upper()
print(d)