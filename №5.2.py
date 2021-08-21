# Задание №5 вариант 2
# a = []
# n = int(input('Введите сколько чисел вы хотите ввести в список: '))
# for i in range(n):
#     a.append(input())

a = [7, 5, 3, 3, 2]
a.sort(reverse=True)

b = int(input('Введите число: '))
count = a.count(b)
if count != 0:
    a.insert((a.index(b)+count), b)
else:
    a.append(b)
    a.sort(reverse=True)

print(a)
