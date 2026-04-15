#13.wap to reverse a string without using inbuilt function x="you did it guys"

x = "you did it guys"
res=""
for i in x:
    res=i+res
print(res)

print()

for i in x[::-1]:
    print(i,end="")

print("\n")

for i in reversed(x):
    print(i,end="")