import tkinter
canvas=tkinter.Canvas(width=600,height=300,bg='white')
canvas.pack()

pocetradov = 10
VEL = 40
busx, busy = 50,50
def zafarbi(sedadlo, farba): #funkcia na farbenie sedadiel
    canvas.itemconfig('sedadlo_'+str(sedadlo),fill=farba) #meni farbu policiek

def kresli(x, y, pocet): #funkcia na vykreslenie policok
    cislo = 0
    for i in range(pocet):
        for j in range(4):
            cislo += 1
            canvas.create_rectangle(x+i*VEL, y+j*VEL, x+(i+1)*VEL-10, y+(j+1)*VEL-10, tags='sedadlo_'+str(cislo),fill='lightgreen') #vykreslenie stvorcekov
            canvas.create_text(x+i*VEL+VEL/2-5, y+j*VEL+VEL/2-5, text=cislo) #vykreslenie textu vo stvorcekochä

def obsad(sedadlo):  
    global red, green
    index = green.index(sedadlo)
    green.pop(index)
    red.append(sedadlo)
    zafarbi(sedadlo, 'red') #zafarbi sedadlo na cervno

def uvolni(sedadlo): 
    global red, green
    index = red.index(sedadlo)
    red.pop(index)
    green.append(sedadlo)
    zafarbi(sedadlo, 'lightgreen') #zafarbi sedadlo na zeleno

def info(): #funkcia na zobrazenie informacii
    canvas.delete('info')
    canvas.create_text(busx, 220, text='Počet voľných: '+str(len(green)),tags='info', anchor='nw') #vykresli text pocet volnych
    canvas.create_text(busx, 240,text='Počet obsadených: '+str(len(red)),tags='info', anchor='nw') #vykresli text pocet obsadenych
    volne_pri_ulicke = 0
    for sedadlo in green:
        if 2 <=sedadlo % 4 <= 3: #podmienka ak sedadlo bude v ulicke
            volne_pri_ulicke += 1
    canvas.create_text(busx, 260, text='Počet voľných pri uličke: '+str(volne_pri_ulicke), tags='info', anchor='nw') #vykresli text pocet volnych pri ulicke

def klik(event): #fukncia na klikanie
    global a,b,c,d
    if (busx < event.x < busx + VEL * pocetradov and
        busy < event.y < busy + VEL * 4):
        ix = (event.x - busy) // VEL
        iy = (event.y - busy) // VEL
        sedadlo = ix * 4 + iy + 1
        zafarbi(sedadlo, 'red')
        if sedadlo in green:
            obsad(sedadlo)
        else:
            uvolni(sedadlo)
        info()

def save(): #funkcia na ulozenie 
    with open('subor.txt', 'a') as subor:
        for j in range(1, 5):
            riadok = ''
            for i in range(j, pocetradov*4+1, 4):
                if i in green:
                    riadok += '{:2} '.format(i)
                else:
                    riadok += ' X' + ' '
            riadok = riadok[:-1] + '\n'
            subor.write(riadok)
        subor.close()       

kresli(busx, busy, pocetradov) #privolanie suradnic a pocet radov
canvas.bind('<Button-1>', klik) #nabindovanie kliknutia
red = []
green = []

for i in range(pocetradov*4): #zafarbi vsetky na zeleno na zaciatku
    green.append(i+1)
    zafarbi(i+1, 'lightgreen') 

button1 = tkinter.Button(text='save', command=save) #tlacitko na ulozenie 
button1.pack()
info()
