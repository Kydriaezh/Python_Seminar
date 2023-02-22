# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные на минимальные.


def max_ti_min(list):
    Min = min(list) 
    Max = max(list) 
    return [Min if i == Max else i for i in list]
print(max_ti_min([int(i) for i in input().split()]))
