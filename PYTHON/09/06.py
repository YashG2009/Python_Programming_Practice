def ind(end):
    l = []
    for x in range(1,end+1):
        l.append((x,x*x,x**3))
    return l

end = int(input("Enter the end number: "))
print(ind(end))