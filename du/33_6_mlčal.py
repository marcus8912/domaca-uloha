import tkinter
from random import *
canvas=tkinter.Canvas(bg='white',width=500,height=500)
canvas.pack()

def balony(): #funkcia
    x=0
    for i in range(8): #opakovanie
        x=x+40
        farby=['red','green','purple'] c
        canvas.create_oval(40+x,300,100+x,360,fill=choice(farby)) #vykreslenie balonov
        canvas.create_line(70+x,300,250,110) #vykreslenie ciar
balony() #zavolanie funkcie
