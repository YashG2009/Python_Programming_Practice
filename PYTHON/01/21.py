# Calculate net salary
# where net salary = gross salary + allowance – deduction.
# Allowances are 10% while deductions are 3% of gross salary.

x=int(input("Enter gross salary : "))

net = x + (x*0.1) - (x*0.03)

print("Net salary : ",net)