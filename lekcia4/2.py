list1 = [y for y in range(1,10)]
print(list1)
list1 = list(map(lambda y: y+10, list1))
print(list1)