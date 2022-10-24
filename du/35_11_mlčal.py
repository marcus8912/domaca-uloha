import tkinter
from random import *
canvas = tkinter.Canvas(bg='white',width=1000,height=400)
canvas.pack()

a=0
c=0
for i in range(0,20):
    a=randint(10,30) #nahodny vyber od 10 po 30
    c=c+40 #posuvanie kruznic
    farba=['red','green','blue'] #zadefinovane farby
    canvas.create_oval(0-a+c,50-a,0+a+c,50+a,width=3,outline=choice(farba)) #vykreslovanie kruznic
