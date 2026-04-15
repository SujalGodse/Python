#1.wap to replace all the character with "-" if the characters occurs more than once in a strings="hellohai"
#/p---->-e--o-ai
from dataclasses import replace

strings="hellohai"
for i in strings:
    if strings.count(i)>1:
        strings=strings.replace(i,"-")
print(strings)