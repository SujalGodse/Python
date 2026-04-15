#wap if the length of string is even then reverse else convert into upper case (take user input)

s = input("Enter the string : ")
if len(s)%2==0:
    print("Reverse is ",s[::-1])
else:
    print("Uppercase is ",s.upper())