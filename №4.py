# Задание №4

a = input('Введите предложение: ')

a = a.split()

# b = len(a)
# for i in range(b):
#     print(f'{i + 1}. {a[i][:10]}')

for i, e in enumerate(a, 1):
    print(f'{i}. {e[:10]}')
