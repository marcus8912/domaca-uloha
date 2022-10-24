import tkinter
from random import *
canvas=tkinter.Canvas(width=600,height=500,bg='white')
canvas.pack()

def trava():
    canvas.create_line(0,500,600,500,width=35,fill='green')#vykreslenie spodku travy
    x=0
    y=0
    for i in range(100):
        x=x+3
        canvas.create_line(x+3+x,y+500,x+3+x,y+475,fill='green',width=2) #vykreslenie travy
trava() #zavolanie funkcie
def muchotravka():
    canvas.create_oval(100,320,200,420,fill='red',outline='') #vykreslenie kruznice
    canvas.create_rectangle(100,370,210,420,fill='white',outline='') #vykreslenie obdlznika
    canvas.create_rectangle(135,370,165,460,fill='sienna',outline='')
    canvas.create_oval(135,450,165,470,fill='sienna',outline='')#vykreslenie kruznice
    canvas.create_oval(120,340,130,350,fill='white',outline='')#vykreslenie kruznice
    canvas.create_oval(170,340,180,350,fill='white',outline='')#vykreslenie kruznice
    canvas.create_oval(150,335,160,340,fill='white',outline='')#vykreslenie kruznice
    canvas.create_oval(145,350,150,350,fill='white',outline='')#vykreslenie kruznice
muchotravka() #zavolanie funkcie
def luce():
    for i in range(40):
        x=randint(1,100)
        y= randint(1,100)
        canvas.create_line(0,0,x,y,fill='yellow',width=2) #vykreslenie lucov
luce() #zavolanie funkcie
a=0
b=0
c=0
x=0
for i in range(5):
    a=randint(10,50)#vyber nahodneho cila od 10 po 50 
    b=randint(10,50)#vyber nahodneho cila od 10 po 50 
    c=randint(10,50) #vyber nahodneho cila od 10 po 50 
    x=x+60
    canvas.create_rectangle(250+x,150,250+a+x,150+a)#vykreslenie obdlznika
    canvas.create_rectangle(250+x,210,250+b+x,210+b)#vykreslenie obdlznika
    canvas.create_rectangle(250+x,270,250+c+x,270+c)#vykreslenie obdlznika

x=380
y=320
x1=500
y1=440
for i in range(20):
    x=x+5
    y=y+5
    x1=x1-5
    y1=y1-5
    canvas.create_oval(x,y,x1,y1,outline='blue') #vykreslenie kruznice

