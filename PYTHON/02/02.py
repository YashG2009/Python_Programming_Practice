# Print largest and smallest values out of three.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest number is: ", a)
elif b >= a and b >= c:
    print("Largest number is: ", b)
else:
    print("Largest number is: ", c)

if a <= b and a <= c:
    print("Smallest number is: ", a)
elif b <= a and b <= c:
    print("Smallest number is: ", b)
else:
    print("Smallest number is: ", c)