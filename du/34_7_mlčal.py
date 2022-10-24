import tkinter
from random import *
canvas=tkinter.Canvas(width=200,height=200,bg='white')
canvas.pack()



y=0
y1=0
for i in range (0,100):
    farby=['red','green','purple','yellow','orange'] #vyber farieb
    y=randint(0,400) #nahodna pozicia pre y
    y1=randint(0,400) #nahodna pozicia pre y1
    canvas.create_line(0,y,500,y1,fill=choice(farby),width=2) #vykreslenie ciar
