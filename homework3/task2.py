import random
num = []
n = int(input())
for i in range(n):
    num.append(random.randint(0,12))
print(num)    
x = int(input())
number=0
for i in range(len(num)):
    if (x - num[i]) == 1 or (x - num[i]) == -1 :
        number=i
    elif (x - num[i]) == 2 or (x - num[i]) == -2 :
        number=i
    elif (x - num[i]) == 3 or (x - num[i]) == -3 :
        number=i
    elif (x - num[i]) == 4 or (x - num[i]) == -4 :
        number=i
   
         
print(num[number])