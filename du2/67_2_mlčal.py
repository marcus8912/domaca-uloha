import tkinter
canvas=tkinter.Canvas(width=400,height=400)
canvas.pack()

canvas.create_rectangle(0,300,400,400,fill='blue')#vykreslenie modreho obldznika 
def lodicky(suradnice):
    x=suradnice.x #suradnice x-ovej osi
    y=suradnice.y #suradnice y-ovej osi
    if y<300:
        canvas.create_rectangle(x,y,x+15,y+15)#vykreslenie obldznika 
        canvas.create_oval(x,y-30,x+15,y-15)#vykreslenie elipsy
        canvas.create_line(x,y-20,x+7,y) #vykreslenie ciary
        canvas.create_line(x+15,y-20,x+7,y)#vykreslenie ciary
    else:
        canvas.create_rectangle(x,y,x+20,y+10)#vykreslenie obldznika 
        canvas.create_line(x+15,y-10,x+15,y)#vykreslenie ciary
canvas.bind('<Button-1>',lodicky)
