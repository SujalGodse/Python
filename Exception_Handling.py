#UserdefinedError
# class NegativeError(Exception):
#     pass
# def Number(x):
#     if x>0:
#         print("Its +ve")
#     else:
#         raise NegativeError
# Number(-34)
from codecs import replace_errors

#using return keyword
# class NegativeError(Exception):
#     pass
# def Number(x):
#     if x>0:
#         return "Its +ve"
#     raise NegativeError
# print(Number(-34))

#wap to check palindrome. if not palindrome raise an userdefined error
# class PalindromeError(Exception):
#     pass
# def Pal(x):
#     if x==x[::-1]:
#         return "Its Palindrome"
#     raise PalindromeError
# print(Pal("AnushkakhsunA"))

#w.a.p to check pass length. If len is less then 5 raise error
# class InvalidPassword(Exception):
#     pass
# def Check(x):
#     if len(x)>5:
#         print("Valid Password")
#     else:
#         raise InvalidPassword
# Check("anish@30feb")
# Check("anish")

#w.a.p to check valid age if age is less then 0 and greater then 120 we have to raise error invalidage
# class InvalidAge(Exception):
#     pass
# def Age(x):
#     if 0<x<120:
#         print("Valid Age")
#     else:
#         raise InvalidAge
# Age(12)
# Age(150)

#w.a.f for a basic login system. raise a error if username and password is not matched
# class CustomError(Exception):
#     pass
# def Login(user,pwd):
#     if user=="virat" and pwd=="1234":
#         print("Login Successfull")
#     else:
#         raise CustomError
# # Login("virat","1234")
# Login("anish","1234")

#waf that checks if username is valid (eg. length between 5 and 15 ) . raise a custom error if the uasername is invalid
# class UsernameError(Exception):
#     pass
# def Login(user):
#     if 5<len(user)<15:
#         print("Valid Username")
#     else:
#         raise UsernameError
# Login("Anushka")
# Login("anish")

#waf that withdraws money from a ban account. Define a custom error if there are insuffient funds
# class FundError(Exception):
#     pass
# def fund(x):
#     if x<500:
#         print("Sufficient Balance")
#     else:
#         raise FundError
# fund(100)
# fund(1000)

