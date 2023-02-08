#Дана последовательность из N целых чисел и число k. Необходимо всю последовательность 
# (сдвиг циклический) на к элементов впрао, к - положительное число.

# list = [1, 2, 3, 4, 5]
# k = 3
# result = list[(k % len(list)):] + list[:(k % len(list))]
# print (result)

list = [1, 2, 3, 4, 5]
k = 2
for i in range(k-1):
    list.insert(0,list.pop(-1))
print(list)    