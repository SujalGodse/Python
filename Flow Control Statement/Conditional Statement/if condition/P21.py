#wap to check whether a character is in the alphabet or not,if it is alphabet,store the value inside a dict(key as a character and value as a ascii value)

char = input("Enter the character : ")
a = {}
if char.isalpha():
    a.update({char:ord(char)})
    # a[char]=ord(char)
    print("Dictionary",a)