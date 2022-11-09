import tkinter
from random import *
canvas = tkinter.Canvas(width=400,height=150)
canvas.pack()

def semafor(x,y):
    a=choice(['red','green','yellow']) #nahodny vyber z urcenych farieb
    b=choice(['red','green','yellow']) #nahodny vyber z urcenych farieb
    c=choice(['red','green','yellow'])#nahodny vyber z urcenych farieb
    canvas.create_rectangle(x,0,x+50,150,fill='black') #vykreslenie obdlznika
    canvas.create_oval(x,y,x+50,y+50,fill=a) #vykreslenie elipsy
    canvas.create_oval(x,y+50,x+50,y+100,fill=b) #vykreslenie elipsy
    canvas.create_oval(x,y+100,x+50,y+150,fill=c) #vykreslenie elipsy
    
for i in range(5):
    semafor(i*55,0) 
