import re

# match()
# s="lets play with python"
# x=re.match("lets",s)
# print(x)
# print(x.start())
# print(x.end())
# print(x.group())
# y=re.match("with",s)
# print(y)

# s="lets play with python"
# y=re.fullmatch("lets play with python",s)
# print(y)
# z=re.fullmatch("play with python",s)
# print(z)

s = "lets play with python"
# m = re.search("l", s)
# print(m)
# print(m.start())
# print(m.end())
# print(m.group())

# s = "lets play with PYTHON"
# n = re.findall('[A-Z]', s)
# print(n)
# n1 = re.findall("[a-z]", s)
# print(n1)
# n2 = re.findall("\s", s)
# print(len(n), len(n1), len(n2))

# r="python programming language"
# x=re.sub("a","*",r)
# print(x)

# r="python programming language"
# y=re.subn("a","*",r,2)
# print(y)

# r="python programming language"
# x=re.split("a",r,2)
# print(x)

# y="abaaabaa"
# t=re.finditer("ab",y)
# # print(list(t)) #address
# for i in t:
#     print(i)

# ^---> start
# x="everything"
# y=re.findall('^every',x)
# print(y)
#
# $ ---> end
# y1=re.findall('ing$',x)
# print(y1)

# [A-Z] ---> range
# x="1234-4567-7891 and 3456-7819-3451"
# y=re.findall('[0-9]{4}-[0-9]{4}-[0-9]{4}',x)
# print(y)
# a="DPUPG5321P"
# b=re.findall('[A-Z]{5}[0-9]{4}[A-Z]{1}',a)
# print(b)


##1.matches any number between 0-9
# a="The cost of the book is Rs.100"



#2.matches only lower case letter and upper case letter
#b="hello HOW ARE YOU"



#3.write a program to count the number of white space in a given string
#c="HELLO world welcome to python Hi how are you. Hi how are you"



#4.sum all the numbers in the below string
# word="PYTHON12nREG567exp2"
# x=re.findall(r"\d",word)
# print(x)


#5.matches everything apart from numbers between 0-9
#a="The cost of the book is Rs.100"

#9.wap to extract only pincode
# s="Bangalore pincode is 560001 and area code is BSK234567 and state code is KAR123"
# s1=re.findall('[0-9]{6}',s)
# print(s1)

#10.wap to print the AADHAR CARD numbers
# s="my aadhar number is 1234-4567-8910"
# s1=re.findall('[0-9]{4}-[0-9]{4}-[0-9]{4}',s)
# print(s1)

#11.wap to print the pan card number
# a="my pan number is ABCDE1234X and other number is PQRST5678W and id is 123abcd45"
# s1=re.findall('[A-Z]{5}[0-9]{4}[A-Z]{1}',a)
# print(s1)

# 12.How to fetch the protocols
# a="https://www.google.com"
# b=re.findall('[a-z]+',a)
# print(b)
# b1=re.findall('.+',a)
# print(b1)

# 13.creating acronyms of the file format
# file_format=["Graphic Interchange Format",
#               "Advanced Audio Coding",
#             "HyperText Markup Language",
#              "Content Management System",
#             "Windows Media,Audio",
#             "Comma Separated Values"]
# for i in file_format:
#     data=re.findall('[A-Z]',i)
#     print("".join(data),end=",")
# o/p-->GIF,AAC,HTML,CMS,WMA,CSV


# 14.wap to match email ids
# emails=["test.user@company.gov","test_user@company.edu","123test-T.user@company.in","testing@company","pspider@company.in"]
# for i in emails:
#     data=re.findall('.+[.]+.+',i)
#     print(data)

#15.matching phone numbers
# phonenumbers=["123-345-0987","456-9832-098","800-987-4756","080-1029384727","123-345-12","900-938-0987"]
# for i in phonenumbers:
#     match=re.findall('[0-9]{3}-[0-9]{3}-[0-9]{4}',i)
#     print(match)

#16.replace whitespace with newline characters
# s="helloworld welcome to python"
# t=re.sub("\s","\n",s)
# print(t)

#17.replace all digits with **
# s="hello 123 mic testing 123 123"
# t=re.sub(r"\d","*",s)
# print(t)

#18.Extracting Dates
# date = "The event is scheduled for 22-05-2025 or 22/05/2025."
# m=re.findall(r'\d{2}[-/]\d{2}[-/]\d{4}',date)
# print(m)
