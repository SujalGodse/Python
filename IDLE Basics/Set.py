Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Set data type-----> accepts unique elements, unordered, wont accept duplicate, mutable
x={1,2,3}
type(x)
<class 'set'>
dir(set)
['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']


#add()
a={"hello",23,45,(1,2)}
a
{45, (1, 2), 'hello', 23}
a.add(45)
a
{45, (1, 2), 'hello', 23}

#update(iterable)
b={"hii",33,45,(1,2)}
b.update("hello")
b
{33, 'o', 'h', (1, 2), 'e', 'l', 45, 'hii'}
b.update([1,2,3]}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
b.update([1,2,3])
b
{33, 'o', 'h', (1, 2), 1, 'e', 2, 3, 'l', 45, 'hii'}

#clear
b={"hii",33,45,(1,2),88}
b.clear()
b
set()

#copy
c={22,45,"cat",(2,4)}
d=c
c
{(2, 4), 45, 'cat', 22}
id(c)
2227210514752
id(d)
2227210514752

#pop()
d
{(2, 4), 45, 'cat', 22}
d.pop()
(2, 4)
d
{45, 'cat', 22}
d.pop()
45

#remove(element)
e={22,34,56,76,15}
e.remove(22)
e
{34, 56, 76, 15}
e.remove(777)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    e.remove(777)
KeyError: 777

#discard(element)
e.discard(56)
e
{34, 76, 15}
e.discard(777)
e
{34, 76, 15}

#intersection ------> set1.intersection.set2
m={1,2,3,4}
n={5,6,2,3}
m.intersection(n)
{2, 3}
#intersection ------> set1.intersection(set2)
m
{1, 2, 3, 4}
n
{2, 3, 5, 6}

#intersection_update ------>set1.intersection_update(set2)
o={1,2,4,5}
p={3,4,5,6}
o.intersection_update(p)
o
{4, 5}
p
{3, 4, 5, 6}


#symmetric_difference ----> set1.symmetric_difference(set2)
p={1,2,3,4,5}
q={10,11,2,3,14}
p.symmetric_difference(q)
{1, 4, 5, 10, 11, 14}
p
{1, 2, 3, 4, 5}
q
{2, 3, 10, 11, 14}


#symmetric_difference_update ----> set1.symmetric_difference_update(set2)
p.symmetric_difference_update(q)
p
{1, 4, 5, 10, 11, 14}
q
{2, 3, 10, 11, 14}


#difference()
p.difference(q)
{1, 4, 5}
q.difference(p)
{2, 3}

#difference_update()
p.difference_update(q)
p
{1, 4, 5}
q
{2, 3, 10, 11, 14}


#union()
x={1,2,3,4,5}
y={6,7,8,9,10}
x.union(y)
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

#isdisjoint
l={1,5,7}
m={1,5,8,7,9}
l.isdisjoint(m)
False

n={2,3,4}
l.disjoint(n)
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    l.disjoint(n)
AttributeError: 'set' object has no attribute 'disjoint'. Did you mean: 'isdisjoint'?
l.isdisjoint(n)
True
>>> 
>>> 
>>> #issuperset
>>> a={1,2,3,4}
>>> b={11,22,33,44,1,2,3,4}
>>> a.issuperset(b)
False
>>> 
>>> b.issuperset(a)
True
>>> 
>>> 
>>> #issubset
>>> x={11,12,13}
>>> y={25,22,11,12,13,19}
>>> x.subset(y)
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    x.subset(y)
AttributeError: 'set' object has no attribute 'subset'. Did you mean: 'issubset'?
>>> x.issubset(y)
True
>>> 
>>> y.issubset(x)
False
