import tkinter
from random import *
canvas = tkinter.Canvas(width=400,height=400,bg='white')
canvas.pack()

x=-25
for i in range(25):
    x=x+15 #posuvanie x suradnice
    canvas.create_line(180,180,20+x,0) #vykreslenie ciary
