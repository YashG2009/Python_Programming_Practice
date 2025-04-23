# Delete an element of a tuple.

tup = ("b1", "g1", "b2", "g2", "b3", "g3")

del_ele = "g2"

tup = list(tup)
tup.remove("g2")
tup = tuple(tup)

print(tup)