# Write a function that removes one string from another string, if present. E.g. Onestring = “abcdef”, removestring = “cd”. The finalstring should contain “abef”.

s = input("Enter a string: ").lower()
s1 = input("Enter a string to be removed: ").lower()

s = s.replace(s1, "")
print(s)