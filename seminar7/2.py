def same_by(conditions,nums):
    return len(set(map(conditions, nums))) == 1
values = [0,2,10,5]
print(same_by(lambda v: v%2, values))

if same_by(lambda v: v%2, values):
    print('same')
else:
    print('different')    