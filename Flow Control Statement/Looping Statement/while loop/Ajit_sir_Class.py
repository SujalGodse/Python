#wap for l=["Python.py","Prog.html","Text.txt"]
#otp=["py","html","txt"]

l=["Python.py","Prog.html","Text.txt"]
otp=[]
for i in l:
    a=i.split(".")
    otp.append(a[-1])
print(otp)
