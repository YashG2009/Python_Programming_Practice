# Write a program to create three dictionaries and concatenate them to create fourth dictionary.

d1 = {1: 123}
d2 = {2: 234}
d3 = {3: 543}
d4 = {**d1,**d2,**d3}

print(d4)