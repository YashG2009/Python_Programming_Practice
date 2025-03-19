# Print factorial of a given number.

def fact(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

n = int(input("Enter a number: "))
print(f"Factorial of {n} is", fact(n))