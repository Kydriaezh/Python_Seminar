# напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень В
# с помощью рекурсии.

a = int(input())
b = int(input())
def st (a,b):
    if b == 1:
        return a
    if b != 1:
        return (a * st(a, b-1))
print(st(a,b))  