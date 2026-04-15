# Multithreading-----> Multitasking ---> executing multiple tasks
# Types---> 1) Process Behind Multitasking 2) Thread Behind Multitasking

import threading
import time
# print("The name of the thread is ",threading.currentThread().name)
# print()
# print("The name of the thread is ",threading.currentThread().getName())

# from threading import *
# # print("The name of the thread is ",currentThread().getName())
# # print()
# # print("The name of the thread is ",currentThread().name)

# to change current name
from threading import *
# print("Current name of the thread is ",threading.currentThread().getName())
# current_thread().setName("PYTHON")
# print("Updated name of the thread is ",threading.currentThread().getName())

# How to create thread or what are ways

#1. creating thread without using any class
# from threading import *
# def demo():
#     for j in range(5):
#         print("Child Thread")
# # Syntax-----> new_var=Thread(target=fun_name)
# t=Thread(target=demo)
# t.start()
# for i in range(5):
#     print("Main Thread")

#2. creating thread with using class
# from threading import *
# class Myclass:
#     def demo(self):
#         for i in range(3):
#             print("Child Thread")
# m=Myclass()
# # Syntax-----> new_var=Thread(target=fun_name)
# t=Thread(target=m.demo)
# t.start()
# for i in range(5):
#     print("Main Thread")

#3.creating thread with extending thread class
# from threading import *
# class Myclass(Thread):
#     def run(self):
#         print("Main Thread")
# m=Myclass()
# m.start()
#
# without threading concept
# def double(numbers):
#     for i in numbers:
#         print(i*2,end=" ")
#     print()
# def square(numbers):
#     for i in numbers:
#         print(i*i,end=" ")
# numbers=[1,2,3,4]
# double([1,2,3,4])
# square([1,2,3,4])

# with threading concept
# from threading import *
# import time
# def double(numbers):
#     for i in numbers:
#         time.sleep(2)
#         print(i*2,end=" ")
#     print()
# def square(numbers):
#     for i in numbers:
#         time.sleep(2)
#         print(i*i,end=" ")
# numbers=[1,2,3,4,5,6]
# t=Thread(target=double,args=(numbers,))
# t1=Thread(target=square,args=(numbers,))
# t.start()
# t1.start()

# # How to get thread number
# from threading import *
# def demo():
#     print("Main Thread")
# t=Thread(target=demo)
# t.start()
# print(t.ident)

# To get count of active threads in program we use active_count()
# from threading import *
# import time
# from time import sleep
# def check():
#     print(current_thread().name,"Started")
#     time,sleep(3)
#     print(current_thread().name,"Ended")
# print("Total number of active threads ",active_count())
# t=Thread(target=check,name="Child_Thread1")
# t1=Thread(target=check,name="Child_Thread2")
# t2=Thread(target=check,name="Child_Thread3")
# t.start()
# t1.start()
# t2.start()
# print("Total number of active threads ",active_count())
# time.sleep(3)
# print("Total number of active threads ",active_count())

# is_alive()---> to check whether thread is active or not
# from threading import *
# import time
# def Fun():
#     print(current_thread().name,"Started")
#     time.sleep(5)
#     print(current_thread().name,"Ended")
# t=Thread(target=Fun,name="T1")
# t1=Thread(target=Fun,name="T2")
# t2=Thread(target=Fun,name="T3")
# t3=Thread(target=Fun,name="T4")
# t.start()
# t1.start()
# t2.start()
# t3.start()
# print(t.name," Isalive ",t.is_alive())
# print(t1.name," Isalive ",t1.is_alive())
# print(t2.name," Isalive ",t2.is_alive())
# print(t3.name," Isalive ",t3.is_alive())
# time.sleep(5)
# print(t.name," Isalive ",t.is_alive())
# print(t1.name," Isalive ",t1.is_alive())
# print(t2.name," Isalive ",t2.is_alive())
# print(t3.name," Isalive ",t3.is_alive())

# join()
# from threading import *
# def check():
#     for i in range(4):
#         time.sleep(3)
#         print("Child")
# t=Thread(target=check)
# t.start()
# t.join(2)
# for i in range(4):
#     print("Main")

# daemon----> Always work in background and gives support to main thread
# nondaemon--->
# from threading import *
# print(current_thread().isDaemon())
# print(current_thread().setDaemon(True))
# we cant change daemon once thread is active. We can change it before thread is active

# from threading import *
# import  time
# l=Lock()      #to execute all thread in sequence
#
# def wish(name):
#     l.acquire()
#     for i in range(3):
#         print("Good Morning ",end="")
#         time.sleep(2)
#         print(name)
#     l.release()
# t=Thread(target=wish,args=("Anushka",))
# t1=Thread(target=wish,args=("Roshan",))
# t1.start()
# t.start()

#
# new=Lock()
# print("first thread is working")
# new.acquire()
# print("Second thread is started")
# new.acquire()
# print("Third thread is working.......")
# new.release()
# new.release()

