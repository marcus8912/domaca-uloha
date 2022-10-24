import tkinter
canvas = tkinter.Canvas(height=200,width=200,bg='white') 
canvas.pack()

def kornutik(): #funkcia
    canvas.create_oval(80,10,120,50,fill='red') #vykreslenie cerveneho kornutika
    canvas.create_oval(70,25,110,65,fill='yellow') #vykreslenie zlteho kornutika
    canvas.create_oval(90,25,130,65,fill='green') ##vykreslenie zeleneho kornutika
    canvas.create_rectangle(70,40,130,70,fill='white') ##vykreslenie obdlznika pod kornutikami
    canvas.create_line(70,70,100,120,width='2') #vykreslenie ciary 
    canvas.create_line(100,120,130,70,width='2') #vykreslenie ciary 
kornutik() #zavolanie funkcie
