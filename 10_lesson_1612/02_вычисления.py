# программа суммирует 5 чисел, которые вводятся пользователем
summary = 0

for i in range(5):
    n = int(input('Введите число: '))
    summary += n

"""
Инкремент - увеличение с присваиванием (+=, *=, **=)
Декремент - уменьшение с присваиванием (-=, /=, //=, %=)

x = 2 
x *= 6 (x = 12)
x += 7 (x = 19) 
x -= 3 (x = 16) 
x /= 2 (x = 8)
"""

x = 1210
y = x
for i in range(10):
    x %= 3
    y /= 3
    print('y ', y)
    print('x ', x)

