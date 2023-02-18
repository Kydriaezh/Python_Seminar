# На столе лежат n монеток. Некоторые из них лежат вверх решёткой, а некоторые - гербом.
# Выведите минимальное количесвто монет, которые нужно перевернуть.

n = int(input())
count0 = 0
count1 = 0
for i in range(n):
    coin = int(input())
    if coin:
        count0 +=1
    else:
        count1 +=1
if count0 < count1:
    print(f"нужно перевернуть {count0} монетки")
else:
    print(f"нужно перевернуть {count1} монетки")        
    
