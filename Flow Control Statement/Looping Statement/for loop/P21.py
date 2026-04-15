#23.wap to create a dictionary of characters and its indices pair s="hello python"
#o/p:-->{"h":[0,9],"e":1..........}

s="hello python"
d={}
for i in range(0,len(s)):
    if s[i] not in d:
        d[s[i]]=[i]
    else:
        d[s[i]] += [i]
print(d)