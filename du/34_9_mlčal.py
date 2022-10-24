import tkinter
canvas = tkinter.Canvas(width=600,height=300,bg='white')
canvas.pack()

x=0
y=0

for i in range(10):
    x=x+5 #posuvanie x suradnice o 5
    y=y+20 #posuvanie y sudaradnice o 20
    canvas.create_line(20,20,80,250) #vykreslenie ciary
    canvas.create_line(60,20,120,250) #vykreslenie ciary
    canvas.create_line(10+x,30+y,80+x,30+y) #vykreslenie ciary
    canvas.create_line(300,20,240,250) #vykreslenie ciary
    canvas.create_line(340,20,280,250) #vykreslenie ciary
    canvas.create_line(350-x,30+y,280-x,30+y) #vykreslenie ciary
