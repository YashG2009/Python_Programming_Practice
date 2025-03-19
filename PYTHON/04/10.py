# Generate N numbers of Fibonacci series.

n = int(input("Enter a number: "))

a, b = 0, 1

for i in range(n):
    print(a)
    a, b = b, a + b