# Факториал числа n - произведение всех натуральных чисел от 1 до n
# 5! = 1 * 2 * 3 * 4 * 5 = 120


num = int(input('Введите число: '))
factorial = 1
while num > 1:
    factorial *= num
    num -= 1

print(factorial)

