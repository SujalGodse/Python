# INHERITANCE:- (IS - A - RELATIONSHIP)
# Child class will take properties from parent class
# aquiring properties from one class from another class
#
# 1.Single level inheritance
# 2.Multilevel inheritance
# 3.Multiple inheritance
# 4.Hierarchical inheritance
# 5.Hybrid inheritance
#
# """
# """
# 1.Single level inheritance:-
# Only we have two class
# child class will take properties from parent class
# if you done any modification in parent class it will affect to child class
# if you done any modification in child class it won't affect to parent class
# We are creating object only for child class not for parent class
# class Parent:
#     def villa(self):
#         print("dad's gift")
#
# class Child(Parent):
#     def Party(self):
#         print("no amount")
#
#     def demo(self):
#         print("demo")
#
# x=Child()
# x.villa()
# x.Party()
# print(dir(Parent))
# print()
# print(dir(Child))

# In the constructor if we have to access the data from parent to child class then use
# super().Method_name() ---->Superclass
# Method chaining:- When we use super class in method
# Class chaining:- When we use super class in  class
#
# We can inherit the parent properties in child without inheritance using HAS - A - RELATIONSHIP
# class Dad:
#     def __init__(self):
#         print("dad class")
#
# class child(Dad):
#     def __init__(self):
#         super().__init__()
#         print("child class")
# x=child()


# class Dad:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         print(f'my name is {self.name} and mine age is {self.age}')
#
# class Child(Dad):
#     def __init__(self,loc,sal):
#         super().__init__(name="xyz",age=23)
#         self.loc=loc
#         self.sal=sal
#         print(f'mine current location is {self.loc} and total salary is {self.sal}')
#
# c=Child("Pune",100000)


# class Dad:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         print(f'my name is {self.name} and mine age is {self.age}')
#
# class Child(Dad):
#     def __init__(self,name,age,loc,sal):
#         super().__init__(name,age)
#         self.loc=loc
#         self.sal=sal
#         print(f'mine current location is {self.loc} and total salary is {self.sal}')
#
# c=Child("abc",23,"pune",25000)


# Multilevel inheritance
# class GrandFather:
#     def villa(self):
#         print("villa")
# class Father(GrandFather):
#     def BMW(self):
#         print("BMW")
#     def TVS(self):
#         print("TVS PRO")
# class Child(Father):
#     def TVS(self):
#         super().TVS()
#         print("Tvs")
#     def villa(self):
#         super().villa()
#         print("villa--->***")
#
# c=Child()
# c.villa()
# c.BMW()
# c.TVS()

# Multiple Inheritance
# class Dad:
#     def Bike(self):
#         print("gift")
#     def demo(self):
#         print("33")
# class Mom:
#         def Car(self):
#             print("car gift")
#
#         def demo(self):
#             print("45")
# class child(Mom,Dad):
#       def Party(self):
#           print("*********************")
#
# x=child()
# x.Party()
# x.Bike()
# x.Car()
# x.demo()
# print(child.__mro__)


# #MRO------> error
# class A:
#     a=10
#     b=20
#
# class B(A):
#     s=90
#     d=89
#
# class C(B):
#     w=900
#
# class D(A,B):
#     p=900
#
# d=D()
# print(d.w)


#
# # Hierarchical Inheritance
# class Dad:
#     def Amount(self):
#         print("2lac")
#
#
# class Child1(Dad):
#     def Party(self):
#         print("50-------> T+C")
#
#
# class Child2(Dad):
#     def Party2(self):
#         print("50k ------>>***")
#
# class Child3(Dad):
#     def fun(self):
#         print("funday")
#
# x=Child1()
# x.Amount()
# x.Party()
#
# y=Child2()
# y.Amount()
# y.Party2()
#
# z=Child3()
# z.Amount()
# z.fun()


# # Hybrid Inheritance
# class Person:
#     def show_person(self):
#         print("I am a person")
#
# class Student(Person):
#     def show_student(self):
#         print("I am a student")
#
# class Teacher(Person):         # hiearachical inheritance 2 child inherit from 1 part
#     def show_teacher(self):
#         print("I am a teacher")
#
# class UG_Student(Student):
#     def show_UG_student(self):
#         print("I am UG student")
#
# class Staff(Teacher):
#     def show_staff(self):
#         print("I am a staff")
#
# class Project(UG_Student,Staff):        #multiple inheritance
#     def show_project(self):
#         print("I am working in a final year project")
#
# x=Project()
# x.show_staff()
# x.show_person()
# x.show_teacher()
# x.show_project()
# x.show_UG_student()

