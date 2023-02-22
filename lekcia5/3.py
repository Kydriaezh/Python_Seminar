# Пользователь вводит исло н, необходимо вывести н первых исел ленов последовательности фибонаи.

def fib(n):
    if n in [1,2]:
        return 1
    return fib(n-1) + fib(n-2)

list = []
for i in range(1,5):
    list.append(fib(i))
print(list)    