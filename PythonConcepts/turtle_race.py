import turtle
import random
def change():
    win.start = True
def window ():
    win.title("Turtle Race Avaneesh")
    win.bgcolor("light yellow")
    win.setup(width=500,height=600)
    win.listen()
def draw_line():
    line = turtle.Turtle()
    line.hideturtle()
    line.color("red")
    #line.shape("turtle")
    line.penup()
    line.pensize(3)
    line.goto(-240,260)
    line.pendown()
    line.goto(240,260)
def create_turtles():
    startx = [-220,-160,-100,-40,20,80,140,200]
    number = [i for i in range(8)]
    count = 7
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
    final = "#"
    final_colors = []
    for i in range(8):
        for i in range(6):
            x = random.randint(0, 15)
            final += digits[x]
        final_colors.append(final)
        final = "#"
    for i in range(8):
        t = turtle.Turtle()
        t.penup()
        t.turtlesize(2)
        t.settiltangle(90)
        t.shape("turtle")
        t.color(final_colors[i-1])
        place = random.randint(0,count)
        y = number[place]
        number.remove(y)
        t.goto(startx[y],-260)
        turtles.append(t)
        count -= 1
def show_winner(t):
    win.start = False
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.penup()
    pen.goto(-240,270)
    pen.color(t.pencolor())
    l = t.pencolor()
    pen.write(f"winner is {l[0]} turtle")
def move():
    for t in turtles:
        y = t.ycor()+random.randint(1,20)
        if y >= 250:
            y = 248
            t.sety(y)
            show_winner(t)
        t.sety(y)
def start():
    win.listen()
    win.onkeypress(change,"Up")
win = turtle.Screen()
win.start = False
turtles = []
win.listen()
window()
draw_line()
create_turtles()
start()
while True:
    win.update()
    if win.start:
        move()





win.mainloop()