Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Relational Operators
>>> 
>>> #lesser than operator(<)
>>> a=4
>>> b
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    b
NameError: name 'b' is not defined
>>> b=10
>>> a<b
True
>>> 
>>> x="two"
>>> y="nine"
>>> x<y
False
>>> 
>>> m=[1,3,5]
>>> n=[2,4,6]
>>> n<m
False
>>> m<n
True


#Greater than operator(>)
a=10
b=100
a>b
False
b>a
True

x="hii"
y="hello"
y>x
False
x>y
True

m=(22,45,67)
n(12,45,66)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    n(12,45,66)
TypeError: 'list' object is not callable
n=(12,45,66)
m>n
True


#lesser than equals(<=)
a=4
b=6
a<=b
True

x="seven"
y="seven"
x<=y
True

m={1,2,3,4,5}
n={6,7,8,9,1}
m<=n
False


#Greater than equals(>=)
a=12
b=5
a>=b
True

x="hii"
y="hello"
x>=y
True

y="Hii"
x>=y
True

[20, 26, 48] >= [20, 26, 49]
False


#Equals to operator(=)
12=13
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
a=12
b=13
a=b
a==b
True

#Equals to operator(==)
"four"=="five"
False

(1,2,3)==(1,2,3)
True


#not equals to (!=)
33!=34
True

'sea'!='see'
True

True!=False
True

{1,2,3}!={3,2,1}
False
