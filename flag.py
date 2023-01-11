import turtle as t

MOON_COLOR = "#FFFFF0"
NIGHT_COLOR = "red"

def moon(size=400):
    t.penup()
    t.color(MOON_COLOR, MOON_COLOR)
    t.dot(size)
    t.forward(size*.4)
    t.color(NIGHT_COLOR, NIGHT_COLOR)
    t.dot(7*size/8)

def star(size=200):
    t.left(24)
    t.fillcolor(MOON_COLOR)
    t.begin_fill()

    for side in range(5):
        t.forward(size)
        t.right(144)
        t.forward(size)
        t.right(72 - 144)

    t.end_fill()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000

t.Screen().screensize(SCREEN_WIDTH, SCREEN_HEIGHT)
t.Screen().setworldcoordinates(-SCREEN_WIDTH, -
                               SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT)
t.Screen().bgcolor("red")

x, y = t.position()
t.goto(x-250, y)
moon()
t.goto(x+250, y+120)
star()

breakpoint()