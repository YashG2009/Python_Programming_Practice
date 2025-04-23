# Modify an element of a tuple.

tup = ("b1", "g1", "b2", "g2", "b3", "g3")
after_repl_tup = ("b4", "g4", "b5", "g5", "b6", "g6")

for i in range(len(tup)):
    tup = list(tup)
    after_repl_tup = list(after_repl_tup)
    tup[i] = after_repl_tup[i]
    tup = tuple(tup)
    after_repl_tup = tuple(after_repl_tup)

print(tup)