#WAP to read the age of a candidate and determine whether it is eligible for his/her own vote or not.it eligible print age and eligible messages or else print not eligible.

age = eval(input("Enter age: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible")