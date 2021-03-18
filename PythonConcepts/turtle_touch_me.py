import turtle
import random
import time
def lvl_1():
    ball.delay = 1.5
    ball.turtlesize(2)
    ball.cornor = 20
    ball.start = True
def lvl_2():
    ball.delay = 1
    ball.cornor = 10
    ball.start = True
    ball.turtlesize(1)
    ball.color("silver")
def lvl_3():
    ball.delay = 0.5
    ball.turtlesize(0.5)
    ball.cornor = 5
    ball.start = True
    ball.color("dim gray")
def win_pause():
    reset()
def windows ():
    win.title("Touch Me Avaneesh")
    win.setup(width=500,height=500)
    win.listen()
    win.bgcolor("black")
def reset():
    win.reset()
    windows()
    win.listen()
    draw_line()
    create_ball()
    enable_key()
    s()
    create_pen()
    ball.color("#FFFFFF")
def draw_line():
    line = turtle.Turtle()
    line.hideturtle()
    line.goto(-240,220)
    line.pencolor("white")
    line.goto(240,220)
def create_ball():
    ball.shape("circle")
    ball.color("white")
    ball.penup()
    ball.touch = 0
    ball.miss = 0
    ball.delay = 2
    ball.turtlesize(2)
    ball.start = False
def mouse_click(x,y):
    my_distance = ball.distance(x,y)
    print(my_distance)
    if my_distance <= ball.cornor:
        ball.touch += 1
    else:
        ball.miss += 1
def move():
    ball.goto(random.randint(-220,220),random.randint(-220,220))
def start():
    ball.start = True
    win.onscreenclick(mouse_click)
def stop():
    ball.start = False
def enable_key():
    win.onscreenclick(mouse_click)
    win.onkeypress(lvl_1,"1")
    win.onkeypress(lvl_2,"2")
    win.onkeypress(lvl_3,"3")
def create_pen():
    pen.hideturtle()
    pen.penup()
    pen.goto(0,230)
    pen.color("white")
    pen.write(f"click:{ball.touch}  miss:{ball.miss}",align="center")
def update_text():
    pen.clear()
    pen.write(f"click:{ball.touch}  miss:{ball.miss}", align="center")
def s ():
    win.onkeypress(win_pause,"s")
win = turtle.Screen()
ball = turtle.Turtle()
pen = turtle.Turtle()
reset()
while True:
    update_text()
    win.update()
    if ball.start == True:
        move()
        time.sleep(ball.delay)
    update_text()
win.mainloop()