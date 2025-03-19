# Generate 20 random integers and store them in a list. Accept a number from the user and print position of all occurrences of that number in the list.

import random

l1 = random.choices(range(1,11),k=20)
print(l1)
num = int(input("Enter a number: "))
print(l1.count(num))