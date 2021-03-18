import turtle
import random
win = turtle.Screen()
win.title("Avaneesh turtle games")
win.setup(width=500,height=500)
win.bgcolor("black")
win.delay(50)
print(win.getshapes())
turtle.shape("turtle")
turtle.color('white')
"""turtle.left(90)
turtle.fd(100)
turtle.speed()
turtle.circle(80)"""
def disable_keys():
    win.clear()
def enable_keys():
    win.listen()
    win.onkeypress(draw_triangle, "Up")
    win.onkeypress(draw_square, "Down")
    win.onkeypress(draw_pentagon, "Right")
    win.onkeypress(draw_hexagon, "Left")
    win.onkeypress(draw_circle, "c")

def draw_polygon(sides,length):
    disable_keys()
    colors = ["red","blue","black","purple","teal","chocolate"]
    turtle.fillcolor(random.choice(colors))
    turtle.begin_fill()
    for i in range(sides):
        turtle.forward(length)
        turtle.left(360/sides)
    turtle.end_fill()
    enable_keys()
#draw_polygon(3,10)
def draw_triangle():
    draw_polygon(3,100)
def draw_square():
    draw_polygon(4,100)
def draw_pentagon():
    draw_polygon(5,100)
def draw_hexagon():
    draw_polygon(6,100)
def draw_circle():
    draw_polygon(100,3)

enable_keys()
win.mainloop()