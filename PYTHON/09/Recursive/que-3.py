def count_vowels(s,v = 0,i = 0):
    l = ["a","e","i","o","u","A","E","I","O","U"]
    if (i < len(l)):
        v += st.count(l[i])
        i += 1
        return count_vowels(s,v,i)
    return v

st = input("Enter a string : ")
print("Number of vowels :",count_vowels(st))