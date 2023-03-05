data = [1, 2, 3, 5, 8, 15, 23, 38]
res = list()

for i in data:
    if i % 2 == 0:
        res.appened((i, i**2))
print(res)        


def select(f,col):
    return[f(y) for y in col]

def where(f, col):
    return[y for y in col if f(y)]
data = [1, 2, 3, 5, 8, 15, 23, 38]
res = select(int, data)
res = where(lambda y: y%2 == 0, res)
print(res)
res = list(select(lambda y: (y, y**2), res))