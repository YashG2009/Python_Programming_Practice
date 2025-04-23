# A list contains names of boys and girls as its elements. Boys’ names are stored as tuples. Write a program to find out number of boys and girls in the list. (Hint: use isinstance(ele,tuple))

names = [("b1",), "g1", ("b2",), "g2", ("b3","b4"), "g3"]

boys_count=0
girls_count=0
for name in names:
    if isinstance(name, tuple):
        boys_count+=len(name)
    else:
        girls_count+=1

print(f"Number of boys: {boys_count}")
print("Number of girls:", girls_count)