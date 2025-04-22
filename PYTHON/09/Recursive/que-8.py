def length(s, l = 0, i = 0):
    if (i >= len(s)):
        return l
    else :
        return length(s,l + 1, i + 1)

st = "HJ2DBw5nT6g@sty"
print(length(st))