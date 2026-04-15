#2.wap to extract vowels and digits in a string s="hello123"

s = "hello123"
vowels = []
digits = []
for i in s:
    if i in "aeiouAEIOU":
        vowels.append(i)
    if i.isdigit():
        digits.append(i)
print("Vowels:", vowels)
print("Digits:", digits)