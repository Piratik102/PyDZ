# Задание №5 вариант 1
# a = []
# n = int(input('Введите сколько чисел вы хотите ввести в список: '))
# for i in range(n):
#     a.append(input())

a = [7, 5, 3, 3, 2]

b = int(input('Введите число: '))
a.append(b)

a.sort(reverse=True)
# a = sorted(a, reverse=True)

print(a)
