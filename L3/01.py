# Count how many vowels are there in a string. Accept the string from the user.

s = input("Enter a string: ").lower()

vowels = "aeiou"

no_of_vowels = 0

for i in vowels:
    no_of_vowels += s.count(i)

print("Number of vowels: ", no_of_vowels)