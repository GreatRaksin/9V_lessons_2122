n = int(input('Введите число: '))
count = 0

while n >= 1:
    n //= 10
    count += 1

print(f'Всего {count} цифр')

