def create_list(l1,l2):
    l1,l2 = set(l1), set(l2)
    l = list(l1.intersection(l2))
    print(l)

l1 =[123,345,567,789]
l2 = [123,567,890,456]
create_list(l1,l2)