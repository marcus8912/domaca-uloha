import tkinter
from random import *
canvas=tkinter.Canvas(width=600,height=400,bg='white')
canvas.pack()

x=0
for i in range(300):
    y=randint(20,70)
    x=x+2
    canvas.create_line(0+x,0,0+x,y,fill='green',width=2) #vykreslenie travy
    canvas.create_line(0+x,400-y,0+x,400,fill='green',width=2) #vykreslenie travy 

for i in range(10):
    c=randint(10,50)
    b=randint(0,600)
    a=randint(150,250)
    canvas.create_oval(b-c,a-c,b+c,a+c,fill='blue') #vykreslenie mlak
t=0
for i in range(11):
    t=t+50
    canvas.create_rectangle(0+t-50,270,50+t,320) #vykreslenie rebrika
