#1.wap to print the number form 1 -20 segregate even and odd number into list

even_list = []
odd_list = []
for i in range(1, 21):
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
print("Even Numbers:", even_list)
print("Odd Numbers:", odd_list)