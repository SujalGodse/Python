#9.wap to create a dictionary and traverse into it and if the length is even print as it else reverse it names=["apple","google","yahoo","microsoft","gmai l","walmart"]

names=["apple","google","yahoo","microsoft","gmail","walmart"]
dictionary={}
for i in names:
    if len(i)%2==0:
        dictionary[i]=i
    else:
        dictionary[i]=i[::-1]
print("Dictionary : ",dictionary)