import math
def prime(num):
    if num == 1 or num == 0:
        return 0
    for i in range(2,int(math.sqrt(num)) + 1):
        if num % i == 0:
            return 0
    return 1

def prime_fact(num,i = 2):
    if num % i == 0:
        if prime(i):
            s.add(i)
        num = num // i
    if num > 1 and i*i <= num:
        prime_fact(num, i+1)
    elif num > 1:
        s.add(num)

n = int(input("Enter a number : "))
original_num = n
s = set()
prime_fact(n)
print(sorted(s))