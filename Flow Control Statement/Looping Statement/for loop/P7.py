#7.wap to check how many words are present in the given sentence s="hello world sentence"

s = "hello world sentence"
count=1
for word in s:
    if word == " ":
        count += 1
print("Number of words:", count)



#by using split
print("\n***************************\n")
w_count=0
for i in s.split():
    w_count+=1
print("Count : ",w_count)
