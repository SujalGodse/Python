# # Number Protocols
# class Product:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def __add__(self, other):
#         return (self.a+other.a,self.b+other.b)
#
#     #if we access using class name then it will show output in object add. To avoid it we use __str__().
#     # def __add__(self, other):
#     #     return Product(self.a+other.a,self.b+other.b)
#     # def __str__(self):                                  #To avoid obj add
#     #     return f'{self.a} and {self.b}'
#
#     def __sub__(self, other):
#         return (self.a-other.a,self.b-other.b)
#
#     def __mul__(self, other):
#         return (self.a*other.a,self.b*other.b)
#
#     def __floordiv__(self, other):
#         return (self.a//other.a,self.b//other.b)
#
#     def __gt__(self, other):
#         return (self.a>other.a,self.b>other.b)
#
#     def __lt__(self, other):
#         return (self.a<other.a,self.b<other.b)
#
#     def __eq__(self, other):
#         return (self.a==other.a,self.b==other.b)
#
# p=Product(10,2)
# p1=Product(4,5)
# print(p.__add__(p1))
# print(p.__sub__(p1))
# print(p.__mul__(p1))
# print(p.__floordiv__(p1))
# print(p.__gt__(p1))
# print(p.__lt__(p1))
# print(p.__eq__(p1))
