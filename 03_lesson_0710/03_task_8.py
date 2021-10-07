from turtle import *

t = Turtle()
t.shape('turtle')
steps = 1

for figure in range(100):
    t.fd(steps)
    t.rt(36)
    steps = steps + 0.5



