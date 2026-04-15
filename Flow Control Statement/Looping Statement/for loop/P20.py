#22.wap to create a dictionary with letter and its words starting with that letter pair s="hi hello good morning welcome to python session"
#o/p:-->{'h': ['hi', 'hello'], 'g': ['good'], 'm': ['morning'], 'w': ['welcome'], 't': ['to'], 'p': ['python'], 's': ['session']}

s="hi hello good morning welcome to python session"
d={}
for i in s.split():
    if i[0] not in d:
        d[i[0]]=[i]
    else:
        d[i[0]]+=[i]
print(d)