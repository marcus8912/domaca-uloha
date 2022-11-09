import tkinter
from random import *
canvas = tkinter.Canvas(width=400,height=400)
canvas.pack()


x=5
y=5
def bosorka1():
    global x,y
    r=randint(0,10) #nahodne cislo od 0 po 10
    canvas.delete('all') #vymazavanie platna
    canvas.create_rectangle(x-5,y-5,x+10,y+20) #vykreslenie obldznika 
    canvas.create_oval(x-5,y-20,x+10,y-5) #vykreslenie elipsy
    canvas.create_line(x-20,y+10,x+20,y+10) #vykreslenie ciary
    x+=5
    y+=5
    if y<400: #ak bosorka bude na mensej pozicii ako je y 400 tak sa bude vykreslovat
        canvas.after(r,bosorka1)
    y1=0
    for i in range (8):
        y1=y1+5
        canvas.create_line(x-40,y-20+y1,x-20,y+5) #vykreslenie ciary
bosorka1()
xx=5
yy=5
def bosorka2():
    global xx,yy
    rr=randint(0,10)#nahodne cislo od 0 po 10
    canvas.delete('all')#vymazavanie platna
    canvas.create_rectangle(xx-5,yy-5,xx+10,yy+20) #vykreslenie obldznika 
    canvas.create_oval(xx-5,yy-20,xx+10,yy-5) #vykreslenie elipsy
    canvas.create_line(xx-20,yy+10,xx+20,yy+10) #vykreslenie ciary
    xx+=5
    yy+=5
    if yy<400:
        canvas.after(rr,bosorka2)
    y2=0
    for i in range (8):
        y2=y2+5
        canvas.create_line(xx-40,yy-20+y2,xx-20,yy+5) #vykreslenie ciary
bosorka2()
