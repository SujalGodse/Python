#WAP to get below o/p: s = 'Hi how are you'
#exp o/p : 'iH woh era uoy'

s = 'Hi how are you'
s1=""
for i in s.split():
    s1=s1+i[::-1]+" "
print(s1)