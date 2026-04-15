#WAP to check length of both string collections are equal or not. if both are equal print the concat the two strings and display, or else if any one of the collection not equal print both the collections with lengths

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
if len(str1) == len(str2):
    print(str1 + str2)
else:
    print(f"{str1} (length: {len(str1)}) and {str2} (length: {len(str2)})")