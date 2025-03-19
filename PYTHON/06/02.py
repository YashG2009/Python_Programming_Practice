# A list contains tuples containing roll no., name and age of student. Write a python program to create three lists separately for roll no., name and age

main_list = [('roll1','n1','age1'),('roll2','n2','age2'),('roll3','n3','age3'),('roll4','n4','age4'),('roll5','n5','age5')]

roll = []
name = []
age = []

for i in main_list:
    roll.append(i[0])
    name.append(i[1])
    age.append(i[2])

print(f"Roll no.: {roll}",f"Name: {name}",f"Age: {age}",sep="\n")