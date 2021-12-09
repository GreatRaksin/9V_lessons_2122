for i in range(1, 11):
    if i == 5:
        continue  # пропуск повторения цикла
    elif i == 8:
        break  # выход из цикла
    print(f'2 * {i} = {2 * i}')
