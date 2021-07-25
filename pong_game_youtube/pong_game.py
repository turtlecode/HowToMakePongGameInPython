from random import choice, random
from turtle import *

import screen as screen
from freegames import vector
def value():
    return (3+random()*2) * choice([1,-1])
state = {1:0, 2:0}
ball = vector(0,0)
aim = vector(value(),value())
bgcolor("green")
def move(player, change):
    state[player] += change

def rectangle(x, y, width, height):
    up()
    goto(x, y)
    down()
    begin_fill()
    for count in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)
    end_fill()

def draw():
    clear()
    rectangle(-400, state[1], 10, 150)
    rectangle(380, state[2], 10, 150)
    ball.move(aim)
    x = ball.x
    y = ball.y
    up()
    goto(x,y)
    dot(10)
    if y<-400 or y>400:
        aim.y = -aim.y
    if x<-370:
        low = state[1]
        high = state[1]+150
        if low <=y <= high:
            aim.x = -aim.x
        else:
            return
    if x>370:
        low = state[2]
        high = state[2]+150
        if low <= y <=high:
            aim.x = -aim.x
        else:
            return
    ontimer(draw,15)

setup(840,840,370,0)
hideturtle()
tracer(False)
draw()
listen()
onkey(lambda : move(1,50), 'e')
onkey(lambda : move(1,-50), 'd')
onkey(lambda : move(2,50), 'o')
onkey(lambda : move(2,-50), 'l')

done()