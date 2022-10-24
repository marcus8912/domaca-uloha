import tkinter
from random import *
canvas=tkinter.Canvas(bg='white',width=500,height=500)
canvas.pack()

def balony(): #funkcia
    x=0
    for i in range(8):  #opakovanie
        x=x+40
        farby=['red','green','purple']  #opakovanie
        canvas.create_oval(40+x,150,100+x,210,fill=choice(farby)) #vykreslenie balonov
        canvas.create_line(70+x,210,250,320) #vykreslenie ciar
balony() #zavolanie funkcie
 
