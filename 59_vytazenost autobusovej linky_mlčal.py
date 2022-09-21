import tkinter
canvas=tkinter.Canvas(width=400,height=400,bg='white')
canvas.pack()



y = 5 #suradnica kde to bude zacinat
def tlacitko(event): #ked sa stlaci tlacitko tak vykresli stupnicu
    global y
    if len(zastavky) > 0:
        canvas.create_rectangle(100,y + 2,200, y +15)
        current = zastavky.pop(0)
        if current > kapacita:
            canvas.create_rectangle(100,y + 2, 100 + 100 * current /kapacita,y + 15,fill='red')
        else:
            canvas.create_rectangle(100,y + 2, 100 + 100 * current /kapacita,y + 15,fill='green')
        y += 20

subor = open('vytazenost_autobusovej_linky.txt') #otvori subor 
kapacita = 0
zastavky = []
pocet = 0

for riadok in subor: #precita subor
    if kapacita == 0:
        kapacita = int(riadok)
    else:
        a = riadok.split()
        pocet +=int(a[0])
        pocet -=int(a[1])
        zastavky.append(pocet)
        canvas.create_text(5 , y, text = ' '.join(a[2:]), anchor='nw') #vykresli text 
        y += 20

y=5
subor.close()
canvas.bind_all('<Key>',tlacitko)

        
