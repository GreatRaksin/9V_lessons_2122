"""
Методы списков:
1. .append(x) <- добавляет х в список
2. .pop(i) <- удаляет элемент с индексом i из списка
3. .sort() <- сортирует значения списка по возрастанию
"""
import random as r  # импортирую библиотеку рандом

my_list = []  # пустой список
for number in range(20):  # хочу наполнить список 20 числами
    my_list.append(r.randint(1, 200))
    # randint(a, b) - генерирует случайное целое число в диапазоне от a до b включительно

my_list.sort()
print(my_list)
