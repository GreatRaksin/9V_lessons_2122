age = int(input('Сколько тебе лет? '))

if age <= 4:  # если
    print('Low level')
elif age < 18:  # ИНАЧЕ если (если первое выражение - ложь)
    print('Medium level')
else:
    print('High level')

