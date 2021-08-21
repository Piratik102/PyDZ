# Задание №2
a = []
n = int(input('Введите сколько элементов вы хотите ввести в список: '))
for i in range(n):
    a.append(input())

# print(a)
a_copy = a.copy()
b = len(a)
i = 0

while i < (b-1):
    a_copy.pop(i)
    a_copy.insert((i + 1), a[i])
    i += 2

print(a_copy)
