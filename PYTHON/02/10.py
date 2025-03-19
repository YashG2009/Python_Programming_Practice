# Given the length and breadth of a rectangle, write a program to find whether the area of the rectangle is greater than its perimeter.

l = int(input("Enter length: "))
b = int(input("Enter breadth: "))

area = l*b
perimeter = 2*(l+b)

if area > perimeter:
    print("Area is greater than perimeter.")
else:
    print("Perimeter is greater than area.")