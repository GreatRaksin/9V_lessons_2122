""" Функция range() - генератор арифметических последовательностей
range(x) - 0...x - 1 (x не входит)
range(y, x) - y...x - 1
range(1, 9, 3) - 1, 4, 7
"""
for n in range(5):
    print(n, end=', ')

print()

for n in range(35, 50):
    print(n, end=', ')

print()

for n in range(1, 10, 2):
    print(n, end=', ')

print()

for n in range(10, -1, -1):
    print(n, end=', ')