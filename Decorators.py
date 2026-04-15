# Decorators :
# #Adding functionality without changing the main function is called Decorators.
# OR
# A decorators is a function which takes another function as an argument, add some extra functionality and
# return another function without altering The source code of the original function.

# def outer(func):  # Step 1: outer function takes a function as argument
#     def inner(*args, **kwargs):  # Step 2: inner function handles all arguments
#         print("Before calling the main function")
#         result = func(*args, **kwargs)  # Step 4: call the original function
#         print("After calling the main function")
#         return result  # Return the result of original function
#     return inner  # Step 3: return the inner function
# @outer
# def main_func(name):
#     print(f"Hello, {name}!")
# main_func("XYZ")

# 1 WADF TO CHECK IF THE 1ST ARGUMENT IS LESSER THAN 2ND ARGUMENT IF THEN SWAP THEM AND PERFORM DIVISION BUT THE
# CONDITION IS YOU SHOULD NOT MODIFY THE ORIGINAL FUNC
# def outer(func):  # func = div
#     def inner(a, b):
#         if a < b:
#             a, b = b, a  # swap if a < b
#         return func(a, b)  # call original function with swapped (if needed) values
#     return inner
#
# @outer
# def div(a, b):
#     print(a / b)
#
# # Test
# div(2, 4)  # a < b, so swap → div(4, 2) → output: 2.0
# div(10, 2) # a > b, no swap → div(10, 2) → output: 5.0

#2. WADF TO ADD 2 NUMBERS AND DISPLAY THE MESSAGE BEFORE AND AFTER PERFORMING THE ADDITION
#
# def addition(func):         # func == add
#     def inner(*args):       # Wrapper to handle any number of arguments
#         print("I'm performing addition")
#         func(*args)         # Call the original function
#         print("Addition is done")
#     return inner            # Return the wrapper function
#
# @addition
# def add(*args):             # Function to perform actual addition
#     c = sum(args)
#     print(c)
#
# # Function Call
# add(1, 2, 3, 4, 5, 3, 4, 6, 8)

#3. CREATE A DECORATOR TO RETURN ONLY POSITIVE OUT FROM ANY SUBTRACTION
# def outer(func):
#     def inner(*args,**kwargs):
#         res = func(*args,**kwargs)
#         return (abs(res))
#     return inner
# @outer
# def sub(a,b):
#      return a-b
# print(sub(-20,2))


# Class

# def outer(func):
#     def inner(*args,**kwargs):
#         print("demo method first")
#         func(*args,**kwargs)
#     return inner
# @outer
# def spam():
#     print("its spam method")
# spam()
#
# @outer
# def spam2():
#     print("spam2 method")
# spam2()
#
# @outer
# def demo1():
#     print("demo1 method")
# demo1()
#
# @outer
# def demo2():
#     print("demo 2 methods")
# demo2()


# ******************************************************************
# def outer(func):
#     def inner(*args,**kwargs):
#         print("demo method first")
#         func(*args,**kwargs)
#     return inner
#
# def outer1(func):
#     def inner1(*args,**kwargs):
#         print("demo method first**************")
#         func(*args,**kwargs)
#     return inner1
#
# @outer
# @outer1
# def demo(name,age):
#     print(f'my name is {name} and my age is {age}')
#
# demo("abc",23)
#
# @outer
# @outer1
# def greet():
#     print("Good day")
# greet()

#***********************************************
# def outer(func):
#     def inner(*args,**kwargs):
#         print(func.__name__)
#         func(*args,**kwargs)
#     return inner
#
# @outer
# def Greet():
#     print("good morning")
# Greet()

#
# *********************************************
# Total_count=0
# def outer(func):
#     def inner(*args,**kwargs):
#         global Total_count
#         # print(func.__name__)
#         Total_count=Total_count+1
#         func(*args,**kwargs)
#     return inner
#
# @outer
# def Greet():
#     pass
# Greet()
# Greet()
# Greet()
# Greet()
# print(Total_count)
#
#
# *************************************************
# import time
# def outer(func):
#     def inner(*args,**kwargs):
#         time.sleep(5)
#         print(func.__name__)
#         time.sleep(3)
#         func(*args,**kwargs)
#     return inner
#
# @outer
# def Greet():
#     time.sleep(2)
#     print("good morning")
# Greet()
#
#
# ****************************************************
# import time
# def outer(func):
#     def inner(*args,**kwargs):
#         start=time.time()
#         func(*args,**kwargs)
#         end=time.time()
#         print(f"total time taken to execute the program is {start-end}")
#     return inner
# @outer
# def Greet():
#     time.sleep(2)
#     print("good morning")
# Greet()

#****************************************
# def outer_most(Parameter):
#     def outer(func):
#         def inner(*args,**kwargs):
#             statement
#             func(*args,**kwargs)
#         return inner
#     return outer
# @outer_most(statement)
#
# def mainfunction(parameters):
#     statement
# mainfunction(arguments)


#**************************************************
# def outer_most(x):
#     def outer(func):
#         def inner(*args,**kwargs):
#             print(x)  #time .sleep(x)
#             func(*args,**kwargs)
#         return inner
#     return outer
# @outer_most("First function")
# def Joy():
#     print("its Joy day")
#
# @outer_most("second function")
# def fun():
#     print("its fun day")
#
# @outer_most("Third function")
# def Class_():
#     print("its Python class")
#
# Joy()
# fun()
# Class_()



