#WAP to check whether a given year is a leap year or not. if leap year, print leap year or else not a leap year.

year = eval(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")