# Encapsulation : We cant achieve 100% encapsulation because we cant access private variable outside class.
# Access Specifier :
# 1. Public : No prefix
# 2. Protected : In place of prefix using single underscore (_). You can access only inside class.
# 3. Private : In place of prefix using double underscore (__)


# Public
# class Myclass:
#     a=10
#     def spam(self):
#         print("GM")
#         print(self.a)
# m=Myclass()
# m.spam()
# print(m.a)


# class Day:
#     def __init__(self,marks,sub):
#         self.mark=marks
#         self.sub=sub
#
#     def Total(self):
#         print(self.mark)
#         print(self.sub)
# d=Day(250,"Python")
# d.Total()
# print(d.mark)
# print(d.sub)

# Protected : to do modification we have to  go with Getter, setter and deleter format
# Improper way to do protected access specifier
# class Bank:
#     _ATMpin=1234
#     def Password(self):
#         print(f"my atm pin is {self._ATMpin}")
# b=Bank()
# b.Password()
# b._ATMpin=4321
# b.Password()

# Proper way is using Getter, setter and deleter method
# class Bank:
#     def __init__(self,pinnumber):
#         self._pin=pinnumber
#
#     def _Getter(self):  #getting The value
#         return self._pin
#
#
#     def _setter(self,pinnumber):
#         self._pin=pinnumber
#
# b=Bank(1111)
# print(b._Getter())
# b._setter(4455)
# print(b._Getter())

# class student:
#     def __init__(self,name,marks):
#         self._name=name
#         self._mark=marks
#
#     def Getting(self):
#         return self._name,self._mark
#
#     def Setting_the_value(self,name,marks):
#         self._name=name
#         self._mark=marks
#
#     def deleter(self):
#         del self._name,self._mark
#
# x=student("Prince",250)
# print(x.Getting())
# x.Setting_the_value("Ravi",350)
# print(x.Getting())
# x.deleter()
# print(x._name)


# Private : we can access variable outside class in indirect way using syntax
# obj._classname__varname  and  classname._classname__varname

# class Fun:
#     __name="PYTHON"
#     def spam(self):
#         print(f'my subject name is {self.__name}')
# f=Fun()
# f.spam()
# # print(f.__name)
# # print(Fun.__dict__)
# print(f._Fun__name)   # object._class_name__var_name
# print(Fun._Fun__name) #class_name._classname__var_name

# Example of Access Specifier
# class Information:
#     def __init__(self,room_num,std_count,batch_code):
#         self.rn=room_num
#         self._count=std_count
#         self.__batch=batch_code
#
#     def Getting(self):
#         return (self.rn,self._count,self.__batch)
#
#     def Setting(self,room_num,std_count,batch_code):
#         self.rn=room_num
#         self._count=std_count
#         self.__batch=batch_code
#
#     # def Deleter(self):
#     #     del self.rn,self._count,self.__batch
# i=Information(1,30,"A1")
# print(i.Getting())
# i.Setting(2,25,"A2")
# print(i.Getting())
# # i.Deleter()
# print(i.rn)


# Another format is @property: in built class --------> getter()
# @getter.setter -----> @getter_name.setter_name
# @getter.deleter ----> @getter_name.deleter_name
# class Total:
#      def __init__(self,name):
#          self.name=name
#
#      @property
#      def Getting(self):
#          return self.name
#
#      @Getting.setter
#      def Getting(self,name):
#          self.name=name
#
#      @Getting.deleter
#      def Getting(self):
#          del self.name
# t=Total("XYZ")
# print(t.Getting)
# t.Getting="ABC"
# print(t.Getting)
# del t.Getting
# print(t.Getting)

# class Total:
#     def __init__(self,name,id,sal):
#         self.name=name
#         self.id=id
#         self.sal=sal
#
#
#     @property
#     def Getting(self):
#         return self.name,self.id,self.sal
#
#
#     @Getting.setter
#     def Getting(self,value):
#         self.name,self.id,self.sal=value
#
#
# t=Total("XYZ",121,5000)
# print(t.Getting)
# t.Getting=("abc",131,10000)
# print(t.Getting)

# class Total:
#     def __init__(self,name):
#         self.name=name
#     @property
#     def Getting(self):
#         return self.name
#     @Getting.setter
#     def Getting(self,name):
#         self.name=name
#
#     @Getting.deleter
#     def Getting(self):
#         del self.name
#
# t=Total("XYZ")
# print(t.Getting)
# t.Getting="abc"
# print(t.Getting)
# del t.Getting
# print(t.Getting)  #AttributeError: 'Total' object has no attribute 'name'

# class Total:
#     def __init__(self,name,id,sal):
#         self.name=name
#         self.id=id
#         self.sal=sal
#     @property
#     def Getting(self):
#         return self.name,self.id,self.sal
#     @Getting.setter
#     def Getting(self,value):
#         self.name,self.id,self.sal=value
#
#
#     @Getting.deleter
#     def Getting(self):
#         del self.name,self.id,self.value
#
# t=Total("XYZ",121,5000)
# print(t.Getting)
# t.Getting=("abc",131,10000)
# print(t.Getting)
# del t.Getting
# print(t.Getting)  #AttributeError: 'Total' object has no attribute 'value'


# class ABC:
#     def __init__(self,a,b):
#         self._a=a
#         self.__b=b
#
#     def getters(self):
#         return (self._a,self.__b)
#
#     def seters(self,a,b):
#         self._a = a
#         self.__b = b
#
# o=ABC(10,20)
# print(o.getters())
# o.seters(50,100)
# print(o.getters())



