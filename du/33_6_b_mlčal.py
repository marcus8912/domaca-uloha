import tkinter
from random import *
canvas=tkinter.Canvas(bg='white',width=500,height=500)
canvas.pack()

x=0
for i in range(8):
    x=x+40
    farby=['red','green','purple']
    canvas.create_oval(40+x,300,100+x,360,fill=choice(farby))
    canvas.create_line(70+x,300,250,110)
