#WAP to check whether the given two input numbers are divisible by 3 and 5. If it is divisible, print “Good Morning”, if it is not divisible print “Good Evening”.

x = eval(input("Enter a number: "))
if x % 3 == 0 and x % 5 == 0:
    print("Good Morning")
else:
    print("Good Evening")