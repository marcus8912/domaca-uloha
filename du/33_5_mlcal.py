import tkinter
canvas=tkinter.Canvas(bg='white',width=500,height=500)
canvas.pack()

def dom(): #funkcia
    canvas.create_line(50,200,150,200)
    canvas.create_line(150,200,95,135)
    canvas.create_line(50,200,95,135)
    canvas.create_rectangle(50,200,150,350,fill='lawn green') #vykreslenie zeleneho domu
    canvas.create_rectangle(85,300,115,350,fill='brown') #vykreslenie dveri
    canvas.create_rectangle(70,230,90,250,fill='blue') #vykreslenie okna
    canvas.create_rectangle(110,230,130,250,fill='blue') #vykreslenie okna
    canvas.create_rectangle(70,260,90,280,fill='blue') #vykreslenie okna
    canvas.create_rectangle(110,260,130,280,fill='blue') #vykreslenie okna
    canvas.create_rectangle(150,300,280,350,fill='coral') #vykreslenie druheho domu
    canvas.create_rectangle(160,310,175,325,fill='blue') #vykreslenie okna
    canvas.create_rectangle(200,310,215,325,fill='blue') #vykreslenie okna
    canvas.create_rectangle(240,325,260,350,fill='black') #vykreslenie dveri 
    canvas.create_rectangle(340,310,350,350,fill='brown') #vykreslenie kmena
    canvas.create_oval(320,260,370,310,fill='green') #vykreslenie koruny
    canvas.create_rectangle(400,310,410,350,fill='brown') #vykreslenie kmena
    canvas.create_oval(380,260,430,310,fill='green')  #vykreslenie koruny
dom() #privolanie funkcie 
