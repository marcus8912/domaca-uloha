import tkinter
canvas = tkinter.Canvas(height=200,width=200,bg='white') 
canvas.pack()

def strom(): #funkcia
    canvas.create_rectangle(80,80,120,150,fill='brown') #vykreslenie kmena
    canvas.create_oval(60,10,140,90,fill='green') #vykreslenie koruny
    canvas.create_line(120,30,110,50,width='2') #vykreslenie ciari
    canvas.create_line(120,30,130,50,width='2') #vykreslenie ciari
    canvas.create_oval(105,50,115,60,fill='red') #vykreslenie ceresne lavej
    canvas.create_oval(125,50,135,60,fill='red') #vykreslenie ceresne pravej 
strom() #zavolanie funkcie 
