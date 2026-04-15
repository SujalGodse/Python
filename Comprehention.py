# list comprehensions  example
# ***********************
# 1.wap to check even numbers in a list and return a list containing only even
# numbers
# l=[2,32,1,52,31,24,56,75]
# a=[i for i in l if i%2==0]
# print(a)

# 2.wap to check elements inside the collection are even or odd,if it is even
# make it square of that numbers,if it is odd make it as cube of that numbers
# l=[2,3,5,1,7,2,3]
# l1=[i**2 if i%2==0  else i**3 for i in l]
# print(l1)


# 3.wap to return a list containing 10 multiples of 2
# l=[i*2 for i in range(11)]
# print(l)

# 4.wap to return a list containing 10 multiples of given value(take user input)
# n=eval(input("Enter a value: "))
# l=[i*n for i in range(1,10+1)]
# print(l)

# 5.wap to take two lists as input and add that elements and return a single
# lists
# l1=eval(input())
# l2=eval(input())
# l3=[i+j for i,j in zip(l1,l2)]
# print(l3)


# 6.wap to create a list containing tuples having two elements that is index and
# value of list
# l=["hey","hello","good","evening","python"]
# l1=[(i,j) for i,j in enumerate(l)]
# print(l1)


# 7.wap to check length of strings present in tuple,if length is even append as
# it is ,else reverse it and append
# l=("hey","hello","good","evenings","python")
# l1=[i if len(i)%2==0 else i[::-1] for i in l]
# print(l1)


# set comprehension example
# 1.wap to remove repeated values and return in set
# l=[2,3,4,2,5,6,2,3]
# s={i for i in l}
# print(s)


# 2.wap to take two lists and return a set by adding elements present same index
# l1=[2,3,4,5,6,7,8,9]
# l2=[5,6,7,8,9,1,2,3]
# s={i+j for i,j in zip(l1,l2)}
# print(s)


# Dict comprehensions
# 1.wap to create a dictionary keys by taking from list,values are square of that
# key
# l=[2,3,4,1,6,2,7,8,4]
# d={i:i**2 for i in l}
# print(d)


# 2.wap to create a dictionary of values and index pair
# l=["google","apple","python","orange"]
# d={i:j for i,j in enumerate(l)}
# print(d)

# 3.wap create a dictionary having first char of word and word pair if word
# having even length
# l=["google","apple","python","orange"]
# d={i[0]:i for i in l if len(i)%2==0}
# print(d)

# 4.wap to check length of words and create a dict having word and word pair if
# it is even odd as it is else reverse and add
# l=["google","apple","python","orange"]
# d={i:i if len(i)%2==0 else i[::-1] for i in l}
# print(d)

# 5.wap to check elements is palindrome key and value should be same else value
# is reverse of key
# l=["banana","malayalam","madam","sir","mom","dad"]
# d={i:i if i==i[::-1] else i[::-1] for i  in l}
# print(d)