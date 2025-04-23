def binary(num,i=0):
    if (num > 0):
        if (num >= 2**l[i]):
            b.append(1)
            num -= 2**l[i]
        else :
            b.append(0)
        i += 1
        binary(num,i)
    elif (num == 0 and len(b) < len(l)):
        for j in range(len(l) - len(b)):
            b.append(0)
    return b

n = int(input("Enter a number : "))
l = []
b = []
i = 0
while (n >= 2**i):
    l.append(i)
    i += 1
l.reverse()
print(binary(n))