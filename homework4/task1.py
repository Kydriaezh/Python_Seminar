

a = set(map(int,input("введите первое множество")))
b = set(map(int,input("введите второе множество")))
u = a.union(b)
u = list(u)
u.sort()
u = set(u)
print(u)
