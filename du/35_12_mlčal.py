import tkinter
from random import *
canvas=tkinter.Canvas(bg='white',width=500,height=500)
canvas.pack()

x=0
for i in range(52):
    x=x+10
    canvas.create_line(0+x,0,0+x,500) #vykreslenie ciary
    canvas.create_line(0,0+x,500,0+x) #vykreslenie ciary




