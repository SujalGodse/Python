#wap to print 1 2 3 5 6 8 9
for i in range(1,10):
    if i==4 or i==7:
        continue
    else:
        print(i,end=" ")
print()


#using while loop print 1 2 4 6 7 8
i=0
while i<9:
    i+=1
    if i==3 or i==5:
        continue
    else:
        print(i,end=" ")
print()