# Print nCr and nPr.

n = int(input("Enter n: "))
r = int(input("Enter r: "))

def ncr(n,r):
    return fact(n)//(fact(r)*fact(n-r))

def npr(n,r):
    return fact(n)//(fact(n-r))

def fact(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

print("nCr: ", ncr(n,r))
print("nPr: ", npr(n,r))