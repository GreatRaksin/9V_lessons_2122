from turtle import *

t = Turtle()
t.shape('turtle')
lines = 12

for figure in range(lines):
    t.fd(100)
    t.stamp()
    t.bk(100)
    t.lt(360 / lines)


