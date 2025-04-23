# A list contains 5 strings. Convert all these strings to uppercase.

l = ['abc', 'def', 'ghi', 'jkl', 'mno']
# l = [input("Enter 1st string"), input("Enter 2nd string"), input("Enter 3rd string"), input("Enter 4th string"), input("Enter 5th string")]

for i in range(len(l)):
    l[i] = l[i].upper()

print(l)