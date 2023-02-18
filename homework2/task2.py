import math

b = int (input())
c = int (input())
a = 1
D = b**2 - 4*a*c 
if D > 0:
    x1 = (b + math.sqrt(D)) / 2*1
    x2 = (b - math.sqrt(D)) / 2*1
    print (x1, x2)
elif D == 0:
    x1 = (b + math.sqrt(D)) / 2*1
    print (x1)     
else:
    print ("нет корней")