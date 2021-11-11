import random as r

r_list = []  # создаю пустой список
while len(r_list) < 10:  # пока длина списка меньше 10
    num = r.randint(1, 20)  # сгенерировать число
    if num not in r_list:  # если числа нет в списке
        r_list.append(num)  # добавить число в список

print(r_list)  # вывести список

