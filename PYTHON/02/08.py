# Check whether a triangle is valid or not, when the three angles of the triangle are entered through the keyboard. A triangle is valid if te sum of all the three angles is equal to 180 degrees.

a = int(input("Enter first angle: "))
b = int(input("Enter second angle: "))
c = int(input("Enter third angle: "))

if a + b + c == 180:
    print("The triangle is valid.")
else:
    print("The triangle is not valid.")