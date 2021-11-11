import random as r

r_list = []
for i in range(10):
    num = r.randint(1, 20)
    if num not in r_list:
        r_list.append(num)

print(r_list)

