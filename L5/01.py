# Create a list of 5 odd integers using random nos. Similarly create a list of 4 even integers using random nos. Replace the third element of odd integers with a list of 4 even integers. Flattern, sort and print the list. Provide appropriate message at each stage.

import random
l1 = random.choices(range(1,100,2),k=5)
l2 = random.choices(range(2,100,2),k=4)

print("Two lists:",l1,l2,sep='\n')

# l1[2] = l2
# print('After replacing',l1,l2,sep='\n')

new_l = l1[:2] + l2 + l1[3:]
print('After adding, flattening and sorting',new_l,sep='\n')