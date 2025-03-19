# Remove empty tuple(s) from the list of tuples.

names = [("b1",), "g1", ("b2",), "g2", ("b3",), "g3", ()]

for name in names:
    if name == ():
        names.remove(name)
print(names)