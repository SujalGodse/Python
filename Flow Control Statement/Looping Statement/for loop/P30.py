#2.wap to Sum of numbers

s = 'Sony12India567pvt21ltd'
sum=0
for i in s:
    if  i.isdigit():
        sum=sum+int(i)
print(sum)