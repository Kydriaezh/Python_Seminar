# напишите функцию, которая принимает одно число и проверякет, является ли оно простым
# простое число - это то, которое имеет два делителя: 1 и n(само число)

def prime(n):
    if n == 2:
        return True
    elif n == 1 or n % 2 == 0:
        return False
    for i in range(3, int((n ** 0.5) + 1), 2):
            if (n %1 == 0):
                return False
    return True    
print(prime(int(input())))