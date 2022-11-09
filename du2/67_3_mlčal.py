import tkinter
from random import *
canvas=tkinter.Canvas(width=400,height=400)
canvas.pack()

def kocky():
    global x,y
    canvas.delete('k') #vymazavanie cisel
    x=randint(1,6) #nahodny vyber cisel od 1 po 6
    y=randint(1,6) #nahodny vyber cisel od 1 po 6
    canvas.create_text(200,50,text='pocet bodov:')#vykreslenie textu
    canvas.create_text(150,200,text=x,font='Arial 25',tags='k')#vykreslenie textu
    canvas.create_text(250,200,text=y,font='Arial 25',tags='k')#vykreslenie textu
    canvas.create_rectangle(130,180,170,220) #vykreslenie obldznika
    canvas.create_rectangle(230,180,270,220) #vykreslenie obldznika
    canvas.after(1000,kocky) #nastavenie casu animacie
kocky()


def body():
    canvas.delete('a') #vymazavanie cisel
    global b
    if x==y: #podmienka
        b=b+2
    if x!=y: #podmienka 
        b=b-2 
    canvas.create_text(250,50,text=b,tags='a') #vykreslenie textu
b=0

button1 = tkinter.Button(text='Rovnaké',command=body)
button1.pack()
