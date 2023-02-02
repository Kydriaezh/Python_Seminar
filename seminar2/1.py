# По данному целому неотрицательному n вычислите значение n! Решить задачу используя цикл while

n = int(input('введите число'))
factorial = 1
a = 1
while a <= n:
    factorial = factorial * a
    a = a + 1
print (factorial)

# n = int(input('введите число'))
# factorial = 1
# while n > 0:
#     factorial = factorial * n
#     a = n-1
# print (factorial)