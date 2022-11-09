import tkinter
canvas=tkinter.Canvas(width=400,height=400)
canvas.pack()

def studenti(suradnice):
    a=str(entry1.get()) #vkladanie nazvu ziaka
    x=suradnice.x #suradnice x-ovej osi
    y=suradnice.y #suradnice y-ovej osi
    canvas.create_rectangle(x,y,x+30,y+35) #vykreslenie obldznika 
    canvas.create_text(x+15,y+40,text=a) #vykreslenie textu
    canvas.create_oval(x,y-30,x+30,y) #vykreslenie elipsy
canvas.bind('<Button-1>',studenti) #nabindovane tlacitko na mysi 
entry1 = tkinter.Entry() 
entry1.pack()
