# дано натуральное число N  и последовательность из N элементов.
#Требуется вывести эту последовательност в обратном порядке. Не использовать массивы и циклы

# n = input()
# nums = input()
# print(nums[::-1])


def rev_num(num):
    if num == 0:
        return ""
    nums = input()
    return rev_num(num - 1) + f"{nums}"
print(rev_num(int(input())))