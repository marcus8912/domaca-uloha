import tkinter
from random import *
canvas = tkinter.Canvas(height=200,width=300,bg='white') 
canvas.pack()

def ciarovykod(): #funkcia
    x=0
    a=0
    for i in range(1,20): #opakovanie 19 krat
        a=randint(1,7) #nahodne hrubky
        x=x+7 #posuvanie ciar
        canvas.create_line(x+10,10,x+10,120,width=a) #vykreslenie ciar 
        print(a) #vypisanie hrubky do shellu
ciarovykod() #zavolanie funkcie 
