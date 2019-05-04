from turtle import *
from random import *

def drawSnow():
    hideturtle()
    pensize(2)
    for i in range(100):
        r, g, b = random(), random(), random()
        pencolor((r, g, b))
        penup()
        setx(randint(-350,350))
        sety(randint(1,270))
        pendown()
        dens = randint(8,12)
        snowsize = randint(10,14)
        for j in range(dens):
            forward(snowsize)
            backward(snowsize)
            right(360/dens)

def drawGround():
    hideturtle()
    for i in range(400):
        pensize(randint(5,10))
        x = randint(-400,350)
        y = randint(-280,-1)
        r, g, b = -y/280, -y/280, -y/280
        pencolor((r, g, b))
        penup()
        goto(x, y)
        pendown()
        forward(randint(40,100))

setup(800, 600)
tracer(False)
bgcolor("black")
drawSnow()
drawGround()
done()