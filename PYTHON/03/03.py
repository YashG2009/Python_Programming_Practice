# Accept two strings. Check whether one string is there in another string.

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if s1 in s2:
    print(f"The {s1} is there in the {s2}.")
else:
    print(f"The {s1} is not there in the {s2}.")