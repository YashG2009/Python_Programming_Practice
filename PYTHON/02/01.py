# Print largest and smallest values out of two.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a >= b:
    print("Largest number is: ", a)
else:
    print("Largest number is: ", b)

if a <= b:
    print("Smallest number is: ", a)
else:
    print("Smallest number is: ", b)