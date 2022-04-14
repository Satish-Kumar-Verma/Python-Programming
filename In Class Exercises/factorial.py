
fact = 1
while True:
    n = int(input("Enter a positive integer : "))
    if n >= 0:
        break

for i in range(1, n + 1):
    fact = fact * i

print(f"Factorial of {n}! is {fact}")
