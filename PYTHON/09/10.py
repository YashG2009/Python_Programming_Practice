def frequency(s):
    l = s.split()
    l.sort()
    d = {}
    for ele in l :
        d[ele] = l.count(ele)
    for k,v in d.items():
        print(f"{k}: {v}")

frequency("apple apple orange orange orange apple guava guava")