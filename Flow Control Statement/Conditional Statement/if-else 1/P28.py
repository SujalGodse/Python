#WAP to check whether a given length of the string is even or not. if even, to append the new string called "bye" or else print the first and last characters.

string = input("Enter a string: ")
if len(string) % 2 == 0:
    print(string + "bye")
else:
    print(f"First and Last characters:",string[0],"and",string[-1])