year = int(input('Введите год: '))

# год делится на 4, не делится на 100 или делится на 400
if ((year % 4 == 0) and not(year % 100 == 0)) or (year % 400 == 0):
    print('YES')
else:
    print('NO')


