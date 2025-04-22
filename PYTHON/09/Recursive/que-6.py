def sanitizes(l, i = 0):
    if (i < len(l)):
        l[i] = 0 if l[i] < 0 else l[i]
        return sanitizes(l,i + 1)
    return l
        
lst = [2,-5,8,1,-12,-23,7,18,43]
print(sanitizes(lst))