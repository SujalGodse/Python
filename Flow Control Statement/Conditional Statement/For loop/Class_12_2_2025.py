# input d=[20,29,11,55]
# output get=[95,86,104,60]
#
# d=[20,29,11,55]
# out=[]
# for i in d:
#     sum=0
#     for j in d:
#         if i!=j:
#             sum+=j
#     out=out+[sum]
# print(out)
# print()

#input l=[45,"Program",45,2+4j,"break"]
#output out={'Program': 'oa', 'break': 'ea'}

# l=[45,"Program",45,2+4j,"break"]
# d={}
# for i in l:
#     s=""
#     if isinstance(i,str):
#         for j in i:
#             if j in "aeiouAEIOU":
#                 s=s+j
#         d[i]=s
# print(d)
# print()


# for i in range(3):
#     for j in range(2):
#         print("*",end=" ")
#     print()
#
# for i in range(2):
#     for j in range(4):
#         print("*",end=" ")
#     print()

# for i in range(3):
#     for j in range(3):
#         print("*",end=" ")
#     print()

# for i in range(3):
#     for j in range(4):
#         if i == 0 or i == 2 or j == 0 or j == 3:
#             print("*", end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# for i in range(4):
#     for j in range(4):
#         if i == 0 or i == 3 or j == 0 or j == 3:
#             print("*", end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# n=eval(input("Enter a number : "))
# for i in range(n):
#     for j in range(n):
#         if i==j:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# n=eval(input("Enter a number : "))
# for i in range(n):
#     for j in range(n):
#         if i+j==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# n=eval(input("Enter a number : "))
# for i in range(n):
#     for j in range(n):
#         if i==j or i+j==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# n=eval(input("Enter a number : "))
# for i in range(n):
#     for j in range(n):
#         if i==j or i+j==n-1 or i==n//2 or j==n//2:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# n=eval(input("Enter a number : "))
# for i in range(n):
#     for j in range(n):
#         if i==j or i+j==n-1 or i==n//2 or j==n//2 or i == 0 or i == n-1 or j == 0 or j == n-1:
#             print("*",end="  ")
#         else:
#             print(" ",end="  ")
#     print()

# for i in range(3):
#     for j in range(3):
#         print("*",end="  ")
#     print()

# n=eval(input("Enter a number : "))
# for i in range(n):
#      for j in range(n):
#          if j<=i:
#             print("*",end="  ")
#      print()

# n=eval(input("Enter a number : "))
# for i in range(n):
#      for j in range(n):
#          if j>=i:
#             print("*",end=" ")
#          else:
#             print(" ",end=" ")
#      print()

# n=eval(input("Enter a number : "))
# for i in range(n):
#      for j in range(n):
#          if j>=i:
#             print("*",end=" ")
#      print()

# n=eval(input("Enter a number : "))
# for i in range(n):
#      for j in range(n):
#          if i+j>=n-1:
#             print("*",end=" ")
#          else:
#             print(" ",end=" ")
#      print()

# n=eval(input("Enter a number : "))
# for i in range(n):
#      for j in range(n):
#          if j+i>=n-1:
#             print("*",end=" ")
#          else:
#             print("#",end=" ")
#      print()

# n=eval(input("Enter a number : "))
# for i in range(n):
#      for j in range(n):
#          if j<=i:
#             print(chr(65+j),end="  ")
#      print()

# n=eval(input("Enter a number : "))
# for i in range(n):
#      for j in range(n):
#          if j<=i:
#             print(j+1,end="  ")
#      print()
#
# n=eval(input("Enter a number : "))
# for i in range(n):
#      for j in range(n):
#          if j<=i:
#             print(chr(97+j),end="  ")
#      print()

# n=eval(input("Enter a number : "))
# for i in range(n):
#      for j in range(i+1):
#          if j<=i:
#             print(i+j+1,end="  ")
#      print()

# n=eval(input("Enter a number : "))
# for i in range(n):
#      for j in range(n*2-1):
#          if i+j>=n-1 and j-i<=n-1:
#              print("*",end="  ")
#          else:
#              print(" ",end="  ")
#      print()

# n=eval(input("Enter a number : "))
# for i in range(n):
#      for j in range(n*2-1):
#          if i+j<=n*2-2 and j>=i:
#              print("*",end="  ")
#          else:
#              print(" ",end="  ")
#      print()