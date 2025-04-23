def compute(n):
    sum = 0
    for i in range(1,n+1):
        sum += int(str(n)*i)
    return sum

for n in range(4,8):
    print(n,compute(n),sep=' : ')