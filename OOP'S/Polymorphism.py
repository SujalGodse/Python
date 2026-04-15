# Polymorphism :
# An object showing diff behaviour at diff stages of lifecycle
# Its best example of method overloading and method overridng and duck type.
# Run time polymorphism : method overriding
# Compile time polymorphism : method overloading

# Method  Overloading : Developing multiple method with same name but diff argument
# 1. method overloading 2. constructor overloading 3.operator overloading
#Method Overriding :
# 1. Method overriding 2.constructor overriding

# Method Overloading : -----> in python we cant achieve method overloading because python is dynamically typed lang
# But we can achieve it partially by using default parameter
# class Math:
#     def Add(self,a):
#         print(a)
#     def Add(self, a,b):
#         print(a,b)
#     def Add(self, a=0,b=0,c=0):
#         print(a,b,c)
# m=Math()
# m.Add()
# m.Add(100)
# m.Add(100,200)
# m.Add(100,200,300)

#Constructor Overloading :
# class Math:
#     def __init__(self,a):
#         print(a)
#     def __init__(self, a,b):
#         print(a,b)
#     def __init__(self, a=0,b=0,c=0):
#         print(a,b,c)
# m=Math()
# m.__init__()

# Multiple methods of Overloading
# class Data:
#     def spam(self,*args):
#         if len(args)==2:
#             return args[0]+args[1]
#         elif len(args)==3:
#             return args[0]+args[1]+args[2]
#         elif len(args)==4:
#             return args[0]+args[1]+args[2]+args[3]
#         else:
#             raise ValueError
# d=Data()
# d.spam()
# d.spam(1,2)
# d.spam(1,2,3)
# d.spam(1,2,3,4)

# class operation:
#     def math(self,a=None,b=None,c=None):
#         if a is not None and b is not None and c is not None:
#             return a+b+c
#         elif a is not None and b is not None:
#             return a+b
#         if a is not None:
#             return a
#         else:
#             return 0
# x=operation()
# print(x.math(10,20,30))
# print(x.math(10,20))
# print(x.math(10))
# print(x.math())


# Operator Overloading : to achieve operator overloading we have to use magic method such as --->
# 1. __add__  2. __sub__  3. __mul__ 4.__str__ etc.
# class Total:
#     def __init__(self,marks):
#         self.mark=marks
# t=Total(100)
# t1=Total(200)
# print(t+t1)   # Error

# class Total:
#     def __init__(self,marks):
#         self.mark=marks
#     def __add__(self, other):     # using magic method error is removed
#         return self.mark+other.mark
# t=Total(100)
# t1=Total(200)
# print(t+t1)

# Using multiple parameter format ----> it will show object address as output to avoid this we use __str__ magic method to get output
# class Operation:
#     def __init__(self,a,b,c):
#         self.a=a
#         self.b=b
#         self.c=c
#
#     def __add__(self, other):
#         return Operation(self.a+other.a,self.b+other.b,self.c+other.c)
#
#     def __mul__(self, other):
#         return (self.a * other.a, self.b * other.b, self.c * other.c)
#
#     def __sub__(self, other):
#         return (self.a - other.a, self.b - other.b, self.c - other.c)
#
#     def __eq__(self, other):
#         return (self.a,self.b,self.c)==(other.a,other.b,other.c)
#
#     def __gt__(self, other):
#         return (self.a, self.b, self.c) > (other.a, other.b, other.c)
#
#     def __lt__(self, other):
#         return (self.a, self.b, self.c) < (other.a, other.b, other.c)
#
#     def __str__(self):
#         return f'{self.a} and {self.b} and {self.c}'
# o=Operation(2,2,3)
# o1=Operation(2,2,3)
# print(o+o1)
# print(o*o1)
# print(o-o1)
# print(o==o1)
# print(o>o1)
# print(o<o1)


# class Total:
#     def __init__(self,marks):
#         self.mark=marks
# t=Total(100)
# t1=Total(200)
# print(t+t1)  #TypeError: unsupported operand type(s) for +: 'Total' and 'Total'
# print(t-t1)  #TypeError: unsupported operand type(s) for -: 'Total' and 'Total'
# print(t*t1) #TypeError: unsupported operand type(s) for *: 'Total' and 'Total'

# Method Overriding
# class Fun:
#     def sound(self):
#         print("Sound1")
# class joy(Fun):
#     def sound(self):
#         print("Sound2")
# j=joy()
# j.sound()

# to avoide overriding we use super class
# class Fun:
#     def sound(self):
#         print("Sound1")
# class joy(Fun):
#     super().sound()
#     def sound(self):
#         print("Sound2")
# j=joy()
# j.sound()
#
# # Constructor overriding
# class Information:
#     def __init__(self):
#         print("Constructor 1")
# class Data(Information):
#     def __init__(self):
#         print("Constructor 2")
# d=Data()


# Duck Type : we can achieve overriding without using inheritance. we have to create one duck method.
# class car:
#     def start(self):
#         print("Car started")
# class laptop:
#     def start(self):
#         print("Laptop started")
# class engine:
#     def start(self):
#         print("Engine started")
# def Start_for_Operation(d):
#     d.start()                                #creating duck object
# Start_for_Operation(car())
# Start_for_Operation(laptop())
# Start_for_Operation(engine())

# class PDF_File:
#     def read(self):
#         print("reading PfDfile")
#
# class Text_File:
#     def read(self):
#         print("i am reading Text file")
#
# class CSV_File:
#     def read(self):
#         print("i am reading CSV file")
#
# def Reading_Data(r):
#     r.read()    #object.method_name()
#
# p=PDF_File()
# t=Text_File()
# c=CSV_File()
#
# Reading_Data(p)
# Reading_Data(t)
# Reading_Data(c)
#
# print()
#
# Reading_Data(PDF_File())
# Reading_Data(CSV_File())
# Reading_Data(Text_File())



