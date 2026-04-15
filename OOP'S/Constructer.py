#Constructor ---->  __init__   (Magic Method)  special member of class.

# class fun:
#     def __init__(self):
#         print("Constructor")
#
#     def demo(self):
#         print("Function")
# f=fun()
# f.demo()
# fun.__init__(f)
# fun.demo(f)

# without Parameterized constructor
# class Bank:
#     def __init__(self):
#         name="Rohit"
#         acc_num=12345678
#         bal=10000
#         loc="mumbai"
#         print(f'my name is {name} and mine account number {acc_num} and total bal  {bal}  '
#               f'and current location is {loc}')
# b=Bank()
# b1=Bank()
# b2=Bank()

# with Parameterized constructor
# class Bank:
#     def __init__(self,name,acc_num,bal,loc):
#         print(f'my name is {name} and mine account number {acc_num} and total bal  {bal}  '
#               f'and current location is {loc}')
#
# b=Bank("Rohit",1234567,12345678,"mumbai")
# print()
# b1=Bank("ravi",43268427425,500000,"pune")
# print()
# Bank.__init__(b,"vikas",234567,44444,"pune1")

# modification in without parameterized
# class Bank:
#     def __init__(self):
#         self.name="Rohit"   #self.new_vn=value
#         self.acc_num=12345678
#         self.bal=10000
#         self.loc="mumbai"
#     def details(self):
#         print(f'my name is {self.name} and account number {self.acc_num} '
#               f'total balance is {self.bal} and current location is {self.loc}')
# b=Bank()
# b.details()

# modification with parenthesis
# class Bank:
#     def __init__(self,name,acc_num,bal,loc):
#         self.name=name
#         self.acc_num=acc_num
#         self.bal=bal
#         self.loc=loc
#     def details(self):
#         print(f'my name is {self.name} and account number {self.acc_num} '
#               f'total balance is {self.bal} and current location is {self.loc}')
# b=Bank("XYZ",234567898765,555555,"pune")
# b.details()
#
# class Bank:
#     def __init__(self,name,acc_num,bal,loc):
#         self.a=name
#         self.b=acc_num
#         self.c=bal
#         self.d=loc
#     def details(self):
#         print(f'my name is {self.a} and account number {self.b} '
#               f'total balance is {self.c} and current location is {self.d}')
#
# b=Bank("abc",234567898765,555555,"pune")
# b.details()

#modificaation in without parenthesis
# class Bank:
#     def __init__(self):
#         self.bal=0.0
#
#     def deposit(self,amount):
#         self.bal+=amount
#         print(f'total balance is {self.bal}')
# b=Bank()
# Bank.bal=5000
# print(b.bal)
# b.deposit(5000)

# multiple constructor in class
# class Joy:
#     def __init__(self):
#         print("constructor class one")
#     def __init__(self):
#         print("constructor class two")
# j=Joy()

# class Test:
#     def __init__(self,a=0,b=0,c=0):
#         print(a+b+c)
# t=Test()   # 0+0+0
# t1=Test(1)  #1+0+0
# t2=Test(1,2) #1+2+0
# t3=Test(1,2,3) #1+2+3


# class Dim:
#     def __init__(self):
#         print("constructor1")
#     def __init__(self, a):
#         print("constructor2")
#     def __init__(self,a=0, b=0):
#         print("constructor3")
#         print(a+b)
# d = Dim(10)
# constructor3
# 10