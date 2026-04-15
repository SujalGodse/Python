#wap to check if the given character is alphabets or Not ,if it is alphabet create a replica of it for 2 times. (take user input)

char = input("Enter a character : ")
if char.isalpha():
    print("Replica :",char*2)
else:
    print("Not an alphabet.")