#wap to create a dictionary word and reverse word pair s="tomorrow is weekend and non-veg special"
#o/p:-->{'tomorrow': 'worromot', 'is': 'si', 'weekend': 'dnekeew', 'and': 'dna', 'non-veg': 'gev-non', 'special': 'laiceps'}

s="tomorrow is weekend and non-veg special"
d={}
for i in s.split():
    d[i]=i[::-1]
print(d)