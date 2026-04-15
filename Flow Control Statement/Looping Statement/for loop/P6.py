#6.wap to print the count of alphabets and numbers and space in the given string s="india got the independence in the year 1947"

s = "india got the independence in the year 1947"
alpha_count = 0
num_count = 0
space_count = 0
for char in s:
    if char.isalpha():
        alpha_count += 1
    elif char.isdigit():
        num_count += 1
    elif char.isspace():
        space_count += 1
print("Count of Alphabets:", alpha_count)
print("Count of Numbers:", num_count)
print("Count of Spaces:", space_count)
