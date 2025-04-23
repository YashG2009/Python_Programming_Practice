# Given three points (x1,y1), (x2,y2) and (x3,y3), check if all the three points fall on one straight line.

p = [int(input("Enter the x point of p: ")), int(input("Enter the y point of p: "))]
q = [int(input("Enter the x point of q: ")), int(input("Enter the y point of q: "))]
r = [int(input("Enter the x point of r: ")), int(input("Enter the y point of r: "))]

area = 0.5*(p[0]*(q[1]-r[1]) + q[0]*(r[1]-p[1]) + r[0]*(p[1]-q[1]))

if area == 0:
    print("The three points fall on one straight line.")
else:
    print("The three points do not fall on one straight line.")