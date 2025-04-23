def average(l, sum = 0, i = 0):
    if (i < len(l)):
        sum += l[i]
        return average(l,sum, i + 1)
    return (sum / len(l))

lst = [1,3,8,6,10,20,27,5]
print("Average of elements of entered list is :",average(lst))