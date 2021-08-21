# Задание №3

month = int(input('Введите порядковое число месяца: '))

season = ('зима', 'весна', 'лето', 'осень')
# season = ['зима', 'весна', 'лето', 'осень']
if (month <= 2) or (month == 12):
    print(season[0])
elif (month >= 3) and (month < 6):
    print(season[1])
elif (month >= 6) and (month < 9):
    print(season[2])
elif (month >= 9) and (month < 12):
    print(season[3])
else:
    print('Такого месяца нет!')