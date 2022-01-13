def say_hello(name):  # определение функции
    msg = f'Hello, {name}!'  # тело функции
    return msg  # возврат результата


def pow(num, p=2):
    res = 1
    for i in range(p):
        res *= num
    return res

print(pow(2, 3))  # позиционные аргументы
print(pow(p=3, num=2))  # именованные аргументы
print(pow(10))  # p=2
print(pow(2, 9))  # p=9

greet = say_hello('Zakhar')  # сохранение результата работы функции в переменной
print(greet)
print(greet[0])


