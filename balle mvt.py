from tkinter import *
import random

def Cercle():
    """ Dessine un cercle de centre (x,y) et de rayon r """
    Canevas.delete(ALL)
    global Arret
    global x
    global y
    global vitesseX
    global vitesseY
    global r
    Canevas.create_oval(x, y, x+r, y+r, outline='blue', fill='blue')
    x+=vitesseX
    y+=vitesseY
    if x+r>=Largeur or x<=0:
        vitesseX=-vitesseX
    if y+r>=Hauteur or y<=0:
        vitesseY=-vitesseY
    if Arret == False:
        Mafenetre.after(50,Cercle)

        
def Arreter():
    global Arret
    Arret = True
    
def Reinitialiser():
    global x
    global y 
    global r
    Arreter()
    x=xdepart
    y=ydepart
    Canevas.delete(ALL)
    Canevas.create_oval(xdepart, ydepart, xdepart+r, ydepart+r, outline='blue', fill='blue')

def Demarrer():
    global Arret
    Canevas.delete(ALL)
    if Arret == True:
        Arret = False
        Cercle()
        
        
Arret = True

Mafenetre = Tk()
Mafenetre.title('Animation')

Largeur = 600
Hauteur = 320
x = 600/2
y = 320/2
xdepart=x
ydepart=y
vitesseX = 5
vitesseY = 5
Canevas = Canvas(Mafenetre, width = Largeur, height =Hauteur, bg ='white')
Canevas.pack(padx =5, pady =5)

r = 20
Canevas.create_oval(x, y, x+r, y+r, outline='blue', fill='blue')


BoutonGo = Button(Mafenetre, text ='Démarrer', command = Demarrer)
BoutonGo.pack(side = LEFT, padx = 10, pady = 10)

BoutonArreter = Button(Mafenetre, text ='Arrêter', command = Arreter)
BoutonArreter.pack(side = LEFT, padx = 5, pady = 5)

BoutonReinitialiser = Button(Mafenetre, text='Reinitialiser', command = Reinitialiser)
BoutonReinitialiser.pack(side=LEFT, padx = 5,pady = 5)

BoutonQuitter = Button(Mafenetre, text ='Quitter', command = Mafenetre.destroy)
BoutonQuitter.pack(side = LEFT, padx = 5, pady = 5)

Mafenetre.mainloop()