# Abstraction : Hiding the complexity of feature but displaying required property to the end user

# from abc import ABC, abstractmethod

# class Myclass:
#     def spam(self):                    #declaration
#         print("Its spam method")       #implementation
# m=Myclass()
# m.spam()

# Abstract Class : partial implementation of class
# class Test(ABC):
#     pass
# t=Test()

# Abstract Method : sometime we dont know about implementation but we declare some method
# class Test1(ABC):
#     @abstractmethod
#     def spam(self):         #declaration
#         pass                #no implementation
# t=Test1()


# We can achieve abstraction using inheritance
# from abc import ABC, abstractmethod

# class Pyspider(ABC):
#     @abstractmethod
#     def Subject1(self,sub1):
#         pass
#     @abstractmethod
#     def Subject2(self, sub2):
#         pass
# class Classroom(Pyspider):
#     def Subject1(self,sub1):
#         print(f"My 1st Subject name is {sub1}")
#     def Subject2(self,sub2):
#         print(f"My 2nd Subject name is {sub2}")
# c=Classroom()
# c.Subject1("Python")
# c.Subject2("PowerBI")


# from abc import ABC, abstractmethod
# class Bank(ABC):
#     @abstractmethod
#     def balance(self):
#         pass
#     @abstractmethod
#     def deposite(self,amount):
#         pass
#     @abstractmethod
#     def withdrawal(self,amount):
#         pass
# class ATM(Bank):
#     def __init__(self,bank_name,bal):
#         self.name=bank_name
#         self.bal=bal
#     def balance(self):
#         print(f"Total amount in my account is {self.bal}")
#     def deposite(self,amount):
#         print(f"Total amount in my account is {self.bal}")
#         self.bal+=amount
#         print(f"Total balance after depositing {amount} amount is {self.bal}")
#     def withdrawal(self,amount):
#         print(f"Total amount in my account is {self.bal}")
#         self.bal-=amount
#         print(f"Total balance after depositing {amount} amount is {self.bal}")
# a=ATM("XYZ",1000)
# a.balance()
# a.deposite(500)
# a.withdrawal(500)


# from abc import ABC, abstractmethod
# class Student(ABC):
#     @abstractmethod
#     def Std1(self,mark1):
#         ...
#     def Std2(self,mark2):
#         ...
# class Total_MArks(Student):
#     def __init__(self,name,loc):
#         self.clg_name=name
#         self.loc=loc
#     def Details(self,name):
#         print(f"My name is {name}. My clg name is {self.clg_name} located in {self.loc}")
#     def Std1(self,mark1):
#         print(f"Marks obtained by std1 are {mark1}")
#     def Std2(self,mark2):
#         print(f"Marks obtained by std2 are {mark2}")
# t=Total_MArks("XYZ","Pune")
# t.Std1(98)
# t.Std2(89)


from abc import ABC, abstractmethod
class Theater(ABC):
    @abstractmethod
    def Theater_Name(self,tname):
        pass
    @abstractmethod
    def Movie(self,mname):
        pass
    @abstractmethod
    def Cost(self,cost):
        pass
    @abstractmethod
    def Snacks(self,snack1,snack2):
        pass
class Details(Theater):
    def __init__(self,runtime):
        self.time=runtime
    def Theater_Name(self,tname):
        print(f"Name of theater is {tname}")
    def Movie(self,mname):
        self.mname=mname
        print(f"Movie name is {self.mname} and its runtime is {self.time}")
    def Cost(self,cost):
        print(f"The cost of movie {self.mname} is {cost}")
    def Snacks(self,snack1,snack2):
        print(f"The snacks ordered are {snack1} and {snack2}")
d=Details("2.5h")
d.Theater_Name("Vijay Mamta")
d.Movie("Mission impossible")
d.Cost("250Rs")
d.Snacks("Popcorn","Beer")


