import string as s
import random as r

letters = s.ascii_letters  # генерация английского алфавита
symb = []  # пустой список

for i in range(20):  # повторить 20 раз
    char = r.choice(letters)   # выбрать случайную букву из строки
    symb.append(char)  # и добавить его

for index in range(len(symb)):  # повторить <длина_списка> раз | 0...n
    print(symb[index], end=', ')  # вывести символ по индексу в списке
    # end - это то, чем заканчивается вывод списка


