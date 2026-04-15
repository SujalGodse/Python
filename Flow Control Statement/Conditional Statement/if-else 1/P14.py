#WAP to check whether the student has passed or failed. If the student got more than 40 marks, print ‘PASS’ along with those marks, if it is not printed ‘FAIL’ along with those marks.

marks = eval(input("Enter marks: "))
if marks > 40:
    print("PASS with",marks,"marks.")
else:
    print("FAIL with",marks,"marks.")