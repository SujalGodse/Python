#How to create empty class

# class Python:
#     pass

# class Python:
#     ...

#Object creation ---> new_var=Class_name()
# class First:
#     pass
# obj=First()  #Object Creation
# print(obj)
# obj1=First
# print

#Accesing variables of class
# class Pooja:
#     num1=100
#     num2=200
#     num3=300
# o1=Pooja()
# #Accessing using class_name
# print(Pooja.num1)
# print(Pooja.num2)
# print(Pooja.num3)
# #Accessing using object
# print(o1.num1)
# print(o1.num2)
# print(o1.num3)

#Modification
# class MainClass:
#     num1=100
#     num2=200
# o1=MainClass()
# o2=MainClass()
# #Modification in main class --> it will affect objects
# MainClass.num1=500
# print(MainClass.num1)
# print(o1.num1)
# print(o2.num1)
# print()
# #Modification in o1 --> it will not affect main class and other object
# o1.num1=1000
# print(MainClass.num1)
# print(o1.num1)
# print(o2.num1)
# print()
# #Again modifying num1 using class_name --> it will not affect he num1 of o1 because connection is lost due to modification made using o1
# MainClass.num1=1500
# print(MainClass.num1)
# print(o1.num1)
# print(o2.num1)
# print()

#structure of class internally --> key value pair
# class Pooja:
#     h=2
#     w=100
# a=Pooja()
# print(Pooja.__dict__)

#doc string
# class Pooja:
#     '''This is Pooja's Class'''
#     h=3
# p=Pooja()
# print(Pooja.__doc__)

#help --> to get full structure of class
# class Anushka:
#     a=10
#     b=20
# obj1=Anushka()
# obj2=Anushka()
# help(Anushka)


#------- Class Methods ---------

#--------> instance class
# class Test1:
#     def Student(self):
#         print("Good Luck")
# t=Test1()
#by calling through the object
# t.Student()   #----> internally t.student(t)
#by calling through class_name
# Test1.Student(t)  #----> explicitly we have to bass object t.Student(t)

# class Spam:
#     def demo1(self):
#         print("demo")
#         print(self)    #<__main__.Spam object at 0x00000277A2507CB0>
# s=Spam()
# print(s)   #<__main__.Spam object at 0x00000277A2507CB0>
# s.demo1()

# class Spam1:
#     def demo1(z):
#         print("demo")
#         print(z)     #<__main__.Spam1 object at 0x000001839D867CB0>
# s=Spam1()
# print(s)    #<__main__.Spam1 object at 0x000001839D867CB0>
# s.demo1()

#without passing parameter
# class Amazon:
#     def Shop(self):
#         product="Watch"    #local variable
#         price=1000
#         address="Pune"
#         print(f"The product name is {product} and its price is {price} and delivery location is {address}")
# a=Amazon()
# a.Shop()
# Amazon.Shop(a)

#passing parameter
# class Myntra:
#     def Shopping(self,product,price,address):
#         print(f"The product name is {product} and its price is {price} and delivery location is {address}")
# a=Myntra()
# a.Shopping("Watch",1000,"Pune")
# Myntra.Shopping(a,"Shoes",2000,"Nashik")

# class Flipkart:
#     product="Mobile"
#     price=25000
#     def data(self):
#         print(f"My product is {Flipkart.product} of price {Flipkart.price}")
#
#     def details(self):
#         print(f"My product is {self.product} of price {self.price}")
# a=Flipkart()
# a.data()
# a.details()
# #modification through class name
# Flipkart.product="Watch"
# a.data()
# a.details()
# #modification through object
# a.product="Shoes"
# a.data()
# a.details()
# #again modifying trough class name
# Flipkart.product="Laptop"
# a.data()
# a.details()


#----------> class method


# class Myclass:
#     @classmethod
#     def Mymethod(cls):
#         print(cls)    #<class '__main__.Myclass'>
#         print("Its class method")
# x=Myclass()
# print(x)     #<__main__.Myclass object at 0x00000221FC2A7CB0>
# x.Mymethod()
# Myclass.Mymethod()
#
# class Myclass:
#     @classmethod
#     def Mymethod(self):
#         print(self)    #<class '__main__.Myclass'>
#         print("Its class method")
# x=Myclass()
# print(x)     #<__main__.Myclass object at 0x00000221FC2A7CB0>
# x.Mymethod()
# Myclass.Mymethod()

# class VTU:
#     exam="10-04-2025"
#
#     @classmethod
#     def ExamHall1(cls):
#         print(f"Exam will start soon {VTU.exam}")
#         print(f"Exam will start soon {cls.exam}")
#
#     @classmethod
#     def ExamHall2(cls):
#         print(f"Exam will start soon {VTU.exam}")
#         print(f"Exam will start soon {cls.exam}")
#
# v=VTU()
# # v.exam="15-04-2025"
# # VTU.exam="15-04-2025"
# VTU.ExamHall1()
# VTU.ExamHall2()

#alternative way of constructor
# class VTU:
#     exam="10-04-2025"
#
#     @classmethod
#     def ExamHall1(cls):
#         new=cls()
#         new.exam="25-04-2025"
#         print(f"Exam will start soon {new.exam}")
#
#     @classmethod
#     def ExamHall2(cls):
#         a = cls()
#         a.exam = "15-04-2025"
#         print(f"Exam will start soon {a.exam}")
#
# v=VTU()
# v.ExamHall1()
# v.ExamHall2()
# VTU.ExamHall1()
# VTU.ExamHall2()

#1.Create a class as bank and declare all the bank name, bank address, bank ifsc and bank phn no. as
# class Bank:
#     Bname="BOB"
#     Badd="Deolali Camp"
#     ifsc=12345
#     phn=8888888888
#
#     @classmethod
#     def banking(cls):
#         print(f"Name of Bank : ",cls.Bname)
#         print(f"Address of Bank : ", cls.Badd)
#         print(f"IFSC of Bank : ", cls.ifsc)
#         print(f"Phone Number of Bank : ", cls.phn)
# b=Bank()
# b.banking()
# Bank.banking()

#2.Write a Python program that defines a class called Vehicle. The Vehicle class should have the following attributes: model, and year, all of which are strings. It should also have a class attribute count, which keeps track of the number of Vehicle objects that have been created.

#3.Write a Python program that defines a class called Book. The Book class should have the following attributes: title, author, and year, all of which are strings. It should also have a class attribute books, which is a list of all Book objects that have been created.
# class Book:
#     Title="Life of Pie"
#     Author="XYZ"
#     Year="2000"

##Through instance method wp to accept List from user when the method is called, 1st index ele in list if it is "string" then reverse the string then replace in same postion and return else if it is a "integer" then ask for user to add a ele into a list and retunthe updates list else reverse the list and return
# class Abcd:
#     def fun(self,l):
#         if isinstance(l[0],str):
#             l[0]=l[0][::-1]
#             return l
#         elif isinstance(l[0],int):
#             l.append(eval(input("Add an element : ")))
#             return l
#         else:
#             l=l[::-1]
#             return l
# a=Abcd()
# print(a.fun(eval(input("Enter a List : "))))


#----------> Static Method


# class Student:
#     @staticmethod
#     def fun():
#         print("Its fun method")
# x=Student()
# x.fun()
# Student.fun()

# class Student:
#     @staticmethod
#     def grade(score):
#         if score>=90:
#             print("Grade A")
#         elif score>=80:
#             print("Grade B")
#         elif score>=70:
#             print("Grade C")
#         elif score>=60:
#             print("Grade D")
#         else:
#             print("Grade F")
# Student.grade(67)

# class Fun:
#     a=20
#     b=10
#     @staticmethod
#     def Add(a,b):
#         return a+b
#
#     @staticmethod
#     def Sub(a, b):
#         return a - b
#
#     @staticmethod
#     def Mul(a, b):
#         return a * b
# f=Fun()
# f.a=100
# f.b=200
# print(f.Add(10,10))
# print(f.Sub(10,10))
# print(f.Mul(10,10))

# class Gym:
#     treadmill="25km"
#     @classmethod
#     def Men(cls):
#         print(cls.treadmill)
#
#     @staticmethod
#     def Women(a):
#         print(a.treadmill)
#
# x=Gym()
# x.Men()
# x.Women(x)



#---------> Constructor

#------> Without parameterised constructor
# class Test:
#     def __init__(self):
#         print("First constructor")
#     def __init__(self):
#         print("Second Constructor")
# a=Test()
# Test.__init__(a)

# class Bank:
#     def __init__(self):
#         Acc=1235435555
#         name="Pooja"
#         ifsc="SBI1234567"
#         loc="Nashik"
#         balance="0"
#         print(f"Account no = {Acc}")
#         print(f"Account holder name = {name}")
#         print(f"Account ifsc = {ifsc}")
#         print(f"Account loc = {loc}")
#         print(f"Account balance = {balance}")
# a=Bank()
# Bank.__init__(a)


# class Bank:
#     def __init__(self,Acc,name,ifsc,loc,balance):
#         print(f"Account no = {Acc}")
#         print(f"Account holder name = {name}")
#         print(f"Account ifsc = {ifsc}")
#         print(f"Account loc = {loc}")
#         print(f"Account balance = {balance}")
#         print()
# a=Bank(123445666,"Pooja","BOB12345","Deolali",10000000)
# Bank.__init__(a,98765543,"Anush","BOI12345","Mini Pakistan",1000000)




