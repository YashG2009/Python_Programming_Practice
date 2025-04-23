# Count no. of alphabets and no. of digits in any given string.

alphabet = "abcdefghijklmnopqrstuvwxyz"
digit = "0123456789"

s = input("Enter a string: ").lower()

alpha_count = 0
digit_count = 0

for i in s :
    if i in alphabet :
        alpha_count += 1
    elif i in digit :
        digit_count += 1

print("Number of alphabets: ", alpha_count)
print("Number of digits: ", digit_count)