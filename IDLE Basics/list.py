Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
q=[["instagram",["snapchat","walmart","Tycompany"],"Happy days"]
   q
   
SyntaxError: '[' was never closed
q=[["instagram",["snapchat","walmart","Tycompany"],"Happy days"]]
   
q
   
[['instagram', ['snapchat', 'walmart', 'Tycompany'], 'Happy days']]
q[0][1][2][2:6:1]
   
'comp'
q[0]
   
['instagram', ['snapchat', 'walmart', 'Tycompany'], 'Happy days']
q[0][1]
   
['snapchat', 'walmart', 'Tycompany']
q[0][1][0]
   
'snapchat'
q[0][1][0][-2:-9:-2]
   
'acas'

a=[[[[[[["instagram",["snapchat","walmart","Tycompany"],"Happy days"]]]]]]]
   
a
   
[[[[[[['instagram', ['snapchat', 'walmart', 'Tycompany'], 'Happy days']]]]]]]
a[0][0][0][0][0][0][1]
   
['snapchat', 'walmart', 'Tycompany']
a[0][0][0][0][0][0][1][1]
   
'walmart'
a[-1][-1][-1][-1][-1][-1][-2][-2]
   
'walmart'
a[0][0][0][0][0][0]
   
['instagram', ['snapchat', 'walmart', 'Tycompany'], 'Happy days']
a[0][0][0][0][0][0][5:9:1]
   
[]
a[0][0][0][0][0][0][0][5:9:1]
   
'gram'
a[-1][-1][-1][-1][-1][-1]
   
['instagram', ['snapchat', 'walmart', 'Tycompany'], 'Happy days']
a[-1][-1][-1][-1][-1][-1][-3][-1:-5:-1]
   
'marg'
a[-1][-1][-1][-1][-1][-1][-3][5:9:1]
   
'gram'
a[0][0][0][0][0][0][2][6:10:1]
   
'days'
a[-1][-1][-1][-1][-1][-1][-1][6:10:1]
   
'days'
a[0][0][0][0][0][0][2][1:5:1]
   
'appy'
a[-1][-1][-1][-1][-1][-1][-1][1:5:1]
   
'appy'
a[-1][-1][-1][-1][-1][-1][-3][0:9:2]
   
'isarm'






#Adding element in the list
   
#append()------> var_name.append(element)    ----both data type
   
x=[]
   
x.append("hii")
   
x
   
['hii']
x.append(1)
   
x
   
['hii', 1]

#extend()------> var_name.extend(element)   ----only iterable/collection data type
   
x.extend(["Hello"])
   
x
   
['hii', 1, 'Hello']

#insert()------> var_name.insert(element)    ----both data type
   

>>> #insert()------>var_name.insert(position,value)    ----both data type
...    
>>> x.insert(2,4)
...    
>>> x
...    
['hii', 1, 4, 'Hello']
>>> 
>>> 3removing element from the list
...    
SyntaxError: invalid decimal literal
>>> #pop()
...    
>>> x.pop(2)
...    
4
>>> x
...    
['hii', 1, 'Hello']
>>> x.pop()
...    
'Hello'
>>> x
...    
['hii', 1]
