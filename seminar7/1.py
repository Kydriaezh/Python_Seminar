def find_farthest_orbit(num_list):
    result: max([(a[0]*a[1],a) for a in num_list if a[0]!=a[1]])[1]
orbits = [(1,3), (2.5, 10), (7,2), (6,6), (4,3)]
print(*find_farthest_orbit(orbits))

