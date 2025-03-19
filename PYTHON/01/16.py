# Calculate interest where I = PRN/100.

p=int(input("Enter principal amount P : "))
r=int(input("Enter rate of interest R : "))
n=int(input("Enter number of years N : "))

y=(p*r*n)/100

print("Interest : ",y)
