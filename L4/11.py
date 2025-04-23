# Calculate sin(x); x is a radian value. The formula is as under:
# sin𝑥=𝑥− 𝑥3/3!+ 𝑥5/5!− 𝑥7/7!…
# (hint: degrees can be converted into radians by 3.14159 / 180.)

x = int(input("Enter x in radian : "))
x = x * (3.14159 / 180)

def fact(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

sinx = x
for n in range(1, 50):
    sign = (-1) ** (n)
    sinx += sign * ((x ** (2*n + 1)) / fact((2*n + 1)))

print(round(sinx,5))