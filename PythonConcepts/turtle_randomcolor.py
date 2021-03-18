import turtle
import random
win = turtle.Screen()
win.title("Avaneesh turtle games")
win.setup(width=500,height=500)
digits = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
final = "#"
for i in range(6):
    x = random.randint(0,15)
    final+=digits[x]
win.bgcolor(final)
win.mainloop()