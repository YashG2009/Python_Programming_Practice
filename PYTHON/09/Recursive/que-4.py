def reverse_list(l,i = 0):
    if (i <= len(l) - 1):
        rev.append(l[len(l) - i -1])
        i += 1
        reverse_list(l,i)
    return rev

lst = [0,8,6,4,7,5,1,3,2]
rev = []
print(reverse_list(lst))