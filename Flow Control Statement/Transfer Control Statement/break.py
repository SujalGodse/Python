# #wap for checking the username is matching or not
#
# user_name="sujal@123"
# while True:
#     user=input("Enter an Username : ")
#     if user==user_name:
#         print("Login Successful")
#         break
#     else:
#         print("Try Again")
# print()


#wap to check user enters correct otp or not

import random
import time
from time import sleep

num=eval(input("Enter a Contact Number : "))
while True:
    otp=random.randint(1000,9999)
    print(f"Your Contact number is {num} and your OTP is {otp}")
    ver=eval(input("Enter your OTP : "))
    if ver==otp:
        print("Login Successful")
        break
    else:
        print("Incorrect OTP, Please wait for 5sec")
        time.sleep(5)