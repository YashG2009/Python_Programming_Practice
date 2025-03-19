# Take two lists of numbers. Create third list of numbers for only those numbers from first list which are not there in 2nd list (use list comprehension).

list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]
list3 = []

for num in list1:
    if num not in list2:
        list3.append(num)

print(list3)