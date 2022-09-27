import tkinter
canvas = tkinter.Canvas(width=450,height=180,bg='white') #vytvorenie platna 
canvas.pack()

def kresli(): #vykresli stvorceky
    for i in range(len(farby)): #vykresli tolko kolko je farieb
        canvas.create_rectangle(x+i*vel,y,x+i*vel+vel-1,y+vel-1,fill=farby[i],outline='') 

def klik(sur): #zaznamenavanie klikania na stvorceky
    if y < sur.y < y + vel:
        poradie = (sur.x - x) // vel
        if 0 <=poradie < len(farby):
            print(poradie) #vypise poradie
            student = entry1.get()
            if student != '': 
                subor = open ('vyber_jedla.txt', 'a') #otvori subor
                subor.write(student+' '+skratky[poradie]+'\n') #napise do suboru studenta + skratky farby kociek
                subor.close() #zatvori subor

canvas.create_text(220,20,text='VYBER JEDLA', font='Arial 20',fill='red') #vypise na platne text vyber jedla
subor = open('vyber_jedla.txt','w') #otvory subor
subor.close() #zavre subor
farby = ('green','red','blue','orange') #v premenej zaevidovane farby
skratky = 'zcmo' #nastavene skratky
x,y,vel = 20,50,100 #nastavene velkosti od ktorych sa budu kocky vykreslovat
kresli() #spustenie funkcie vykresli
canvas.bind('<Button-1>',klik) #nabindovanie na lave tlacitko
labell = tkinter.Label(text='kod studenta:') 
labell.pack()
entry1 = tkinter.Entry() #pole do ktoreho sa zadava kod studenta
entry1.pack()
