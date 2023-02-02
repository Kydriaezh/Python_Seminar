

n = int(input())
max_day = cur_day = 0
for i in range (n):
    temp = int(input())
    if temp > 0:
        cur_day +=1
    else:
        if cur_day > max_day:
            max_day = cur_day
        cur_day = 0    
print (max_day)            