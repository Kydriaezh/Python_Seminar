import random
list = []
n = int(input())
for i in range(n):
    list.append(random.randint(0,12))
print(list)    
x = int(input())
num = list[0] 
for i in list:
    if abs(x - i) < abs(x - num):
        num = i
    
print(num)