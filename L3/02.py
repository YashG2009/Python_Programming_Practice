# Write your own functions (without using built-in functions) to convert all characters of a string into lower case/upper case/toggle case.

cap = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
small = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def my_lower(s):

    for let in s :
        if let in cap:
            ind = cap.index(let)
            s = s.replace(let, small[ind])
    return s

def my_upper(s):
    for let in s :
        if let in small:
            ind = small.index(let)
            s = s.replace(let, cap[ind])
    return s

def my_toggle(s):
    for let in s :
        if let in cap:
            ind = cap.index(let)
            s = s.replace(let, small[ind])
        elif let in small:
            ind = small.index(let)
            s = s.replace(let, cap[ind])
    return s

s = input("Enter a string: ")
print(my_toggle(s))