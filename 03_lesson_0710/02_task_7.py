from turtle import *

t = Turtle()
t.shape('turtle')
steps = 5

for figure in range(50):
    t.fd(steps)
    t.rt(90)
    steps = steps + 5



