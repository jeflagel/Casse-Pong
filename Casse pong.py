# script clavier.py
from tkinter import *

global Arret
global x
global y
global vitesseX
global vitesseY
global r
Arret = TRUE
vitesseAjoute=0

# La fonction affiche les briques a l'écran
def brique():
        largeurBrique=20
        hauteurBrique=30
        a=550
        b=-20
        bi=b
        for loop in range(5):
            a+=largeurBrique+2
            b=bi
            for loop in range(18):
                b+=hauteurBrique+2
                brique = Canevas.create_rectangle(a,b,a+largeurBrique,b+hauteurBrique,outline='red',fill='red')



# Permet de gérer le déplacement des palettes ( chaque palette représente un joueur )
def Clavier(event):
    """ Gestion de l'événement Appui sur une touche du clavier """
    global PosX1,PosX2,PosY1,PosY2,BordDroit,BordGauche
    touche = event.keysym
    print(touche)
    # déplacement vers le bas de la palette rouge
    if touche == 's':
        PosX1 += 20
    # déplacement vers le haut de la palette rouge
    if touche == 'z':
        PosX1 -= 20
    # on dessine le pion à sa nouvelle position
    Canevas.coords(Palette1,PosY1 -5, PosX1 -50, PosY1 +5, PosX1 +50)
    # déplacement vers le bas de la palette blue
    if touche == 'm':
        PosX2 += 20
    # déplacement vers le haut de la palette rouge
    if touche == 'p':
        PosX2 -= 20
    # on dessine le pion à sa nouvelle position
    Canevas.coords(Palette2,PosY2 -5, PosX2 -50, PosY2 +5, PosX2 +50)


def AffichageGeneral():
    Canevas.delete(ALL)
    global Arret
    global x,x2
    global y,y2
    global vitesseX,vitesseX2,vitesseAjoute
    global vitesseY,vitesseY2
    global r
    
    # recreation pallettes+ balle apres reset canevas
    balle1 = Canevas.create_oval(x, y, x+r, y+r, outline='red', fill='red')
    balle2 = Canevas.create_oval(x2, y2, x2+r, y2+r, outline='blue', fill='blue')
    Palette1 = Canevas.create_rectangle(PosY1-5,PosX1-50,PosY1+5,PosX1+50,width=2,outline='red',fill='red')
    Palette2 = Canevas.create_rectangle(PosY2-5,PosX2-50,PosY2+5,PosX2+50,width=2,outline='blue',fill='blue')


    x+=vitesseX
    y+=vitesseY
    x2+=vitesseX2
    y2+=vitesseY2
    if x2==BordDroit and y2<=PosX1+50 and y2>=PosX1-50:
        vitesseX2=-vitesseX2+vitesseAjoute
        #vitesseAjoute=-vitesseAjoute-1
    elif x2+r==BordGauche and y2<=PosX2+50 and y2>=PosX2-50:
        vitesseX2=-vitesseX2-vitesseAjoute
        #vitesseAjoute=vitesseAjoute+1
    elif y2+r>=Hauteur or y2<=0:
        vitesseY2=-vitesseY2
    if x+r==BordDroit and y<=PosX2+50 and y>=PosX2-50:
        vitesseX=-vitesseX-vitesseAjoute
        #vitesseAjoute=vitesseAjoute+1
    elif x==BordGauche and y<=PosX1+50 and y>=PosX1-50:
        vitesseX=-vitesseX+vitesseAjoute
        #vitesseAjoute=-vitesseAjoute-1
    elif y+r>=Hauteur or y<=0:
        vitesseY=-vitesseY
    
    if Arret == False:
        Mafenetre.after(10,AffichageGeneral)
    if x+1.5*r<BordGauche:
        Arret = True
        Frame1 = Frame(Mafenetre,borderwidth=2,relief=GROOVE)
        Frame1.pack(side=LEFT,padx=10,pady=10)
        Label(Frame1,text="Le joueur bleu gagne").pack(padx=10,pady=10)
    if x-r>BordDroit:
        Arret = True
        texte1 = Frame(Mafenetre,borderwidth=2,relief=GROOVE)
        texte1.pack(side=LEFT,padx=10,pady=10)
        Label(texte1,text="Le joueur rouge gagne").pack(padx=10,pady=10)
    
        
        
    
    brique()

# Permet de recommencer une nouvelle partie
def Reinitialiser():
    global x
    global y 
    global r 
    global PosX1,PosY1,PosX2,PosY2
    Pause()
    x=xdepart
    y=ydepart
    x2=x2depart
    y2=y2depart
    Canevas.delete(ALL)
    PosX1 = 310
    PosY1 = 20
    PosX2 =310
    PosY2 =1260
    Palette1 = Canevas.create_rectangle(PosY1-5,PosX1-50,PosY1+5,PosX1+50,width=2,outline='red',fill='red')
    Palette2 = Canevas.create_rectangle(PosY2-5,PosX2-50,PosY2+5,PosX2+50,width=2,outline='blue',fill='blue')
    balle = Canevas.create_oval(x, y, x+r, y+r, outline='red', fill='red')
    balle2 = Canevas.create_oval(x2, y2, x2+r, y2+r, outline='blue', fill='blue')

# Permet de commencer la partie
def Demarrer():
    global Arret
    #Canevas.delete(ALL)
    if Arret == True:
        Arret = False
        AffichageGeneral()

# Met la partie en pause        
def Pause():
    global Arret
    Arret = True
    
    
# Création de la fenêtre principale
Mafenetre = Tk()
Mafenetre.title('Casse Pong')

# position initiale des palettes
# Palette1 = rouge
# Palette2 = bleu
PosX1 = 300
PosY1 = 20
PosX2 =310
PosY2 =1260

BordDroit=PosY2-5
BordGauche=PosY1+5

# Position initiale des balles
x=25
x2=1234
y=Hauteur/2
y2=Hauteur/2

# Sauvegarde des position des balles
xdepart=x
ydepart=y
x2depart=x2
y2depart=y2

# Sens et vitesse de déplacement des balles
vitesseX = 5
vitesseX2=-5
vitesseY2=5
vitesseY = 5

# Création d'un widget Canvas (fenetre de jeu)
Largeur = 1280 #1280
Hauteur = 600 #720
Canevas = Canvas(Mafenetre, width = Largeur, height =Hauteur, bg ='white')
r = 20

Palette1 = Canevas.create_rectangle(PosY1-5,PosX1-50,PosY1+5,PosX1+50,width=2,outline='red',fill='red')
Palette2 = Canevas.create_rectangle(PosY2-5,PosX2-50,PosY2+5,PosX2+50,width=2,outline='blue',fill='blue')
balle = Canevas.create_oval(x, y, x+r, y+r, outline='red', fill='red')
balle2 = Canevas.create_oval(x2, y2, x2+r, y2+r, outline='blue', fill='blue')
#palletes anciennes positions
Canevas.focus_set()
Canevas.bind('<Key>',Clavier)
Canevas.pack(padx =5, pady =5)

# Création de widgets Button 
Button(Mafenetre, text ='Quitter', command = Mafenetre.destroy).pack(side=LEFT,padx=5,pady=5)

BoutonBrique = Button(Mafenetre, text ='brique', command =brique)
BoutonBrique.pack(side = LEFT, padx = 15, pady = 15)


BoutonGo = Button(Mafenetre, text ='Démarrer', command = Demarrer)
BoutonGo.pack(side = LEFT, padx = 10, pady = 10)

BoutonPause = Button(Mafenetre, text ='Pause', command = Pause)
BoutonPause.pack(side = LEFT, padx = 5, pady = 5)

BoutonReinitialiser = Button(Mafenetre, text='Reinitialiser', command = Reinitialiser)
BoutonReinitialiser.pack(side=LEFT, padx = 5,pady = 5)

Mafenetre.mainloop()