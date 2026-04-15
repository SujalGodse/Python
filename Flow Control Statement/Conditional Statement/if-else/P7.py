#.wap to check whether the first character in the given string is starting with uppercase or Not if it is not Then capitalize it

s="python"
if s[0].isupper():
    print("The first character in the given string is starting with uppercase")
else:
    print(s.capitalize())