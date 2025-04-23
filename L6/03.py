# Suppose a date is represented as a tuple (d, m, y). Create two date tuples and find the number of days between the two dates.

import datetime

print("Enter start date: ")
d1 = (int(input("Enter day: ")),int(input("Enter month: ")),int(input("Enter year: ")))
print("Enter end date: ")
d2 = (int(input("Enter day: ")),int(input("Enter month: ")),int(input("Enter year: ")))

# d1 = datetime.date(d1[2],d1[1],d1[0])
# d2 = datetime.date(d2[2],d2[1],d2[0])

# print((d2-d1).days)

days_diff = 0

if d1[1] != d2[1]:
    days_diff += abs(d1[1]-d2[1])*30

if d1[2] != d2[2]:
    days_diff += abs(d1[2]-d2[2])*365
    print(days_diff)

days_diff = abs(days_diff - d1[0] + d2[0])

print(days_diff)