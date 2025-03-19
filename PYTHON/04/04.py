# Check whether a given number is prime, is perfect, is Armstrong, is palindrome, is automorphic.

n = int(input("Enter a number: "))

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum == n

def is_armstrong(n):
    sum = 0
    for dig in str(n):
        dig = int(dig)
        sum += dig ** len(str(n))
    return sum == n

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def is_automorphic(n):
    sqr = n ** 2
    return str(n) == str(sqr)[-len(str(n)):]

print("is prime number." if is_prime(n) else "Not prime number.", "Is perfect number." if is_perfect(n) else "Not perfect number.","Is Armstrong number." if is_armstrong(n) else "Not Armstrong number.","Is palindrome number." if is_palindrome(n) else "Not palindrome number.","Is automorphic number." if is_automorphic(n) else "Not automorphic number.", sep="\n")