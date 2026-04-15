#10.wap to print series of factorial(take user input)

num = eval(input("Enter a number: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print(f"Factorial of {num} is {fact}")