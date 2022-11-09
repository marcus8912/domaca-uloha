import tkinter
from random import *
canvas = tkinter.Canvas(height=500,width=500)
canvas.pack()

word=' '
x=250
y=0
def slovo():
    global y,x,word,s,n
    canvas.delete('txt') #vymazavanie textu
    s=choice(('auto','oblak','chodník','zeleň','jablko')) #nahodny vyber
    n=choice(('zelezo','zalud','myska','mobyl','hri')) #nahodny vyber
    canvas.create_text(x,y,text=word,tags='txt') #vykreslovanie textu
    y=y+10
    if y>=500:
        y=0
        word=choice((s,n)) #nahodny vyber
    canvas.after(50,slovo)
slovo()


sn=0
def klik(suradnice):
    global sn
    canvas.delete('cislo')  #vymazavanie cisla    
    canvas.create_text(50,50,text=sn,tags='cislo')#vykreslenie textu
    if word==s:
        sn=sn+1
    elif word==n:
        sn=sn-2
    cena=choice(('telefón','lístky do divadla','knihu')) #nahodny vyber 
    if sn>=10:
        canvas.create_text(80,70,text='vyhrali ste a získali ste cenu:') #vykreslenie textu
        canvas.create_text(80,80,text=cena) #vykreslenie textu
canvas.bind('<Button-1>', klik) #nabidnovane tlacitko 
 
