# Create a dictionary with dept no, employee roll no. and salary. Find out department wise min and maximum of salary.

# roll no.: [dept no., salary]
d= {1: [1, 1000], 
    2: [2, 2000], 
    3: [1, 3000], 
    4: [1, 1000], 
    5: [2, 5000], 
    6: [2, 6000],}

# sorting by dept
dept = {}
temp_list = []
for k,v in d.items():
    dept.setdefault(v[0],[]).append(v[1])
    temp_list = []

max_dict = {}
min_dict = {}
for k,v in dept.items():
    max_dict[k] = max(v)
    min_dict[k] = min(v)

print("Minimum:",min_dict)
print("Maximum:",max_dict)