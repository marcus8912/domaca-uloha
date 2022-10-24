import tkinter
canvas = tkinter.Canvas(height=200,width=200,bg='white')
canvas.pack()

def balon(): #funkcia
    canvas.create_oval(80,50,120,90,fill='blue') #vykreslenie balona
    canvas.create_line(80,75,100,140) #vykreslenie ciari
    canvas.create_line(120,75,100,140) #vykreslenie ciari
    canvas.create_rectangle(90,140,110,150,fill='red') #vykreslenie obdlznika
balon() #zavolanie funkcie
