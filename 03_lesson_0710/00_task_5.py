from turtle import *


t = Turtle()
t.shape('turtle')
steps = 10

for figure in range(15):

    # тут я рисую квадраты
    for square in range(4):
        t.rt(90)
        t.fd(steps)

    # а тут я отступаю от каждого квадрата
    t.up()
    t.lt(45)
    t.fd(10)
    t.rt(45)
    t.down()

    # увеличиваю сторону
    steps += 15

