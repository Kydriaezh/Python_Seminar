#Петя помогает Кате по математике. Он задумывает два натуральных числа, а Катя должна их отгадать.
# Петя делает две подскзки. Он называет сумму этих чисел и их произведение. Помогите Кате отгадать задуманные Петей числа

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