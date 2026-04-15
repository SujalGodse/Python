# #wap to print lowercase a........z
# i=ord("a")
# while i<=ord("z"):
#     print(chr(i),end=" ")
#     i+=1
# print()
#
# #wap to print uppercase A........Z
# i=ord("A")
# while i<=ord("Z"):
#     print(chr(i),end=" ")
#     i+=1
# print()
#
# #wap  for AaBbCc......Zz
# i=ord("A")
# j=ord("a")
# while i<=ord("Z") and i<=ord("z"):
#     print(chr(i),chr(j),end=" ")
#     i+=1
#     j+=1
# print()
#
# #wap to print only collection data types
# x=[1.2,6+7j,[1,2,3],"python class",{1,2,3},100,{56:90}]
# i=0
# while i<len(x):
#     if isinstance(x[i],(list,tuple,str,set,dict)):
#         print(x[i],end=" ")
#     i+=1
# print()
#
# #wap to print sum of number
# e=[1,2,3,4,5,6]
# sum=0
# i=0
# while i<len(e):
#     sum+=e[i]
#     i+=1
# print(sum)
# print()
#
# #wap to print even length character
# z=["Tycompany","DXC","apple","samsung","ey"]
# i=0
# while i<len(z):
#     if len(z[i])%2==0:
#         print(z[i])
#     i+=1
# print()
#
# #wap to print 1 to 20 number even and odd number
# l1=[]
# l2=[]
# i=1
# while i<=20:
#     if i%2==0:
#         l1+=[i]
#     else:
#         l2+=[i]
#     i+=1
# print("Even :",l1)
# print("Odd :",l2)
# print()
from os import remove

#wap to print the name which is starting with vowel in the given list
# names=["agra","bangalore","mumbai","pune","indore","isha","eshwar","surat"]
# i=0
# while i<len(names):
#     if names[i][0] in "aeiou":
#         print(names[i],end=" ")
#     i+=1
# print()
#
# #wap to extract only vowels and digits from the given string
# s="hellopython123"
# i=0
# while i<len(s):
#     if s[i].isdigit() or s[i] in "aeiou":
#         print(s[i],end=" ")
#     i+=1
# print()
#
# #wap to iterate inside the list check if it is having nested list if yes merge it
# list1=["hello",10,20.55,True,False,"hai","bye",[False,"goodnight","enjoy the holiday"]]
# list2=[]
# i=0
# while i<len(list1):
#     if isinstance(list1[i],list):
#         list2.extend(list1[i])
#     else:
#         list2.append(list1[i])
#     i+=1
# print(list2)
# print()
#
#
# #wap if a names ends with vowels then reverse a names else print its length
# names=["Kumar","Latika","Umesh a","Priyanka"]
# i=0
# while i<len(names):
#     if names[i][-1] in "aeiou":
#         print(names[i][::-1])
#     else:
#         print(len(names[i]))
#     i+=1
# print()
#
# #wap to print all individual data types from list
# data=[34,"hai",3+4j,(1,2),{3,4},False,3.4]
# i=0
# while i<len(data):
#     if isinstance(data[i],(int,float,complex,bool)):
#         print(data[i],end=" ")
#     i+=1
# print()
#
# #wap to print each character from a string
# s="python masters"
# i=0
# while i<len(s):
#     print(s[i],end=" ")
#     i+=1
# print()


# wap to iterate inside the list check if it is having nested list if yes merge it
list1=["hello",10,20.55,True,False,"hai","bye",[False,"goodnight","enjoy the holiday"]]
list2=[]
i=0
while i<len(list1):
    if isinstance(list1[i],list):
        a=list1.pop(i)
        list2.extend(a)
    else:
        list2.append(list1[i])
    i+=1
print(list2)