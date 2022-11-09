import tkinter
from random import *
canvas = tkinter.Canvas(width=400,height=400)
canvas.pack()

entry1 = tkinter.Entry()
entry1.pack()

def zmaz():
    canvas.delete("all") #mazanie platna

def setric():
    a=10
    canvas.delete('all') #mazanie platna
    x=randint(0,400) #nahodny vyber cisel od 0 po 400
    y=randint(0,400) #nahodny vyber cisel od 0 po 400
    if a>90:
        a=10
    canvas.create_text(x,y,text=str(entry1.get()),angle=a) #vykreslenie textu
    a=a+10
    canvas.after(1000,setric)
setric()

canvas.bind('<Button-1>',zmaz)

