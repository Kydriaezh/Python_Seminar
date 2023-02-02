

n = int (input())
max = min = int(input('ves'))
for _ in range(n-1): # если переменная i нигде не фигурирует, то ставим безымянную переменную _
    count = int (input())
    if count > max:
        max = count
    if count < min:
       min = count
print (min, max)           


