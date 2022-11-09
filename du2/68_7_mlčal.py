import tkinter
from random import *
canvas = tkinter.Canvas(width=400,height=400)
canvas.pack()



kabel=' '
def vyber():
    global kabel
    kabel = choice(('blue','red','yellow','green')) #nahodny vyber z urcenych farieb
vyber()
c=60
def casovac():
    global c,kabel
    canvas.delete('del_cas') #vymazavanie casu
    c=c-1
    canvas.create_rectangle(20,20,380,200,fill='white') #vykreslenie obldznika
    canvas.create_text(200,100,text=c,font='Arial 100',fill='red', tags ='del_cas') #vykreslenie textu
    canvas.after(100,casovac)
    if c==0:
        canvas.create_text(200,300,text='bomba vybuchla') #vykreslenie textu
        c=+1
casovac()

def modra():
    global modra,kabel
    if kabel =='blue':
        canvas.create_text(200,300,text='bomba vybuchla') #vykreslenie textu
    else:
        canvas.create_text(200,300,text='bomba zneskodnena') #vykreslenie textu
def cervena():
    global modra,kabel
    if kabel =='red':
        canvas.create_text(200,300,text='bomba vybuchla') #vykreslenie textu
    else:
        canvas.create_text(200,300,text='bomba zneskodnena') #vykreslenie textu
def zlta():
    global zlta,kabel
    if kabel =='yellow':
        canvas.create_text(200,300,text='bomba vybuchla') #vykreslenie textu
    else:
        canvas.create_text(200,300,text='bomba zneskodnena') #vykreslenie textu
    
def zelena():
    global zelena,kabel
    if kabel =='green':
        canvas.create_text(200,300,text='bomba vybuchla') #vykreslenie textu
    else:
        canvas.create_text(200,300,text='bomba zneskodnena') #vykreslenie textu
    

button1 = tkinter.Button(text='modry kablik',command=modra) #tlacitko
button1.pack()

button2 = tkinter.Button(text='cerveny kablik',command=cervena) #tlacitko
button2.pack()

button3 = tkinter.Button(text='zlty kablik',command=zlta) #tlacitko
button3.pack()

button4 = tkinter.Button(text='zeleny kablik',command=zelena) #tlacitko
button4.pack()
