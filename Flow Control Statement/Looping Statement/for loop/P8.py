#8.wap to create a dictionary and print the characters  and its Ascii value pair s="hello world output:--> {"h":ascii value,"e":ascii value........}

s="hello world"
dictionary={}
for i in s:
    dictionary[i]=ord(i)
print("Dictionary : ",dictionary)