import tkinter
canvas=tkinter.Canvas(width=400,height=400)
canvas.pack()

x=400
def titulky():
    global x
    canvas.delete('all') #mazanie platna
    x=x-5 #odpocet po 5 od x
    canvas.create_text(x,370,text=entry1.get()) #vykreslenie textu
    if x<0:
        x=400
    canvas.after(100,titulky)
entry1 = tkinter.Entry()
entry1.pack()
titulky()
