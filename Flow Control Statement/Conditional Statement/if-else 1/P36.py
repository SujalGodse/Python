#WAP to check whether a given value is a string or not and length of the value should be more than 7, if condition is satisfied to append the new string in the middle of the given string or else to perform the replications with 3 and display the result.

string = input("Enter a string: ")
if isinstance(string, str) and len(string) > 7:
    middle = len(string) // 2
    new_string = string[:middle] + "new" + string[middle:]
    print(new_string)
else:
    print(string * 3)