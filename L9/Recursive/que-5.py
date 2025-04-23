def power(a,b,apb = 1):
    if (b == 0):
        return apb
    return power(a,b - 1,apb *a)
    
a = int(input("Enter a : "))
b = int(input("Enter b : "))
print(power(a,b))