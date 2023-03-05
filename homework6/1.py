# Заполните массив элементами арифмитеско прогресси. Её первы элемент, разность и колиество элементов нужно
# ввести с клавиатуры.

first = int(input())
sub = int(input())
count = int(input())

for i in range(count):
    print(first + i * sub, end=" ")