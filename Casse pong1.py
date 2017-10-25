# script clavier.py
from tkinter import *

global Arret
#global OrdBalleRouge
#global AbsBalleRouge,AbsBalleRougedepart
#global vitesseX
#global vitesseY
#global DiametreBalles
Arret = TRUE
vitesseAjoute=0

def RebondPalettes(AbsBalle,OrdBalle,DeplacementVertical,DeplacementHorizontal):
    
    global BordDroit,BordGauche,DiametreBalles,MilieuHauteurPaletteBleue,MilieuHauteurPaletteRouge
    global vitesseAjoute,Hauteur
    
    if OrdBalle+DiametreBalles==BordDroit and AbsBalle<=MilieuHauteurPaletteBleue+50                      and AbsBalle>=MilieuHauteurPaletteBleue-50:
        vitesseX=-vitesseX-vitesseAjoute
        #vitesseAjoute=vitesseAjoute+1
    elif OrdBalle==BordGauche and AbsBalle<=MilieuHauteurPaletteRouge+50 and AbsBalle>=MilieuHauteurPaletteRouge-50:
        vitesseX=-vitesseX+vitesseAjoute
        #vitesseAjoute=-vitesseAjoute-1
    elif AbsBalle+DiametreBalles>=Hauteur or AbsBalle<=0:
        DeplacementHorizontal=-DeplacementHorizontal
        

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
    global MilieuHauteurPaletteRouge,MilieuHauteurPaletteBleue,MilieuLargeurPaletteRouge,MilieuLargeurPaletteBleu,BordDroit,BordGauche
    touche = event.keysym
    print(touche)
    # déplacement vers le bas de la palette rouge
    if touche == 's':
        MilieuHauteurPaletteRouge += 20
    # déplacement vers le haut de la palette rouge
    if touche == 'z':
        MilieuHauteurPaletteRouge -= 20
    # on dessine le pion à sa nouvelle position
    Canevas.coords(Palette1,MilieuLargeurPaletteRouge -5, MilieuHauteurPaletteRouge -50, MilieuLargeurPaletteRouge +5, MilieuHauteurPaletteRouge +50)
    # déplacement vers le bas de la palette blue
    if touche == 'm':
        MilieuHauteurPaletteBleue += 20
    # déplacement vers le haut de la palette rouge
    if touche == 'p':
        MilieuHauteurPaletteBleue -= 20
    # on dessine le pion à sa nouvelle position
    Canevas.coords(Palette2,MilieuLargeurPaletteBleu -5, MilieuHauteurPaletteBleue -50, MilieuLargeurPaletteBleu +5, MilieuHauteurPaletteBleue +50)


def AffichageGeneral():
    Canevas.delete(ALL)
    global Arret
    global OrdBalleRouge,OrdBalleBleue
    global AbsBalleRouge,AbsBalleBleue
    global vitesseX,vitesseX2,vitesseAjoute
    global vitesseY,vitesseY2
    global DiametreBalles
    
    # recreation pallettes+ balles apres reset canevas pour eviter trace de la balle
    balle1 = Canevas.create_oval(OrdBalleRouge, AbsBalleRouge, OrdBalleRouge+DiametreBalles, AbsBalleRouge+DiametreBalles, outline='red', fill='red')
    balle2 = Canevas.create_oval(OrdBalleBleue, AbsBalleBleue, OrdBalleBleue+DiametreBalles, AbsBalleBleue+DiametreBalles, outline='blue', fill='blue')
    Palette1 = Canevas.create_rectangle(MilieuLargeurPaletteRouge-5,MilieuHauteurPaletteRouge-50,MilieuLargeurPaletteRouge+5,MilieuHauteurPaletteRouge+50,width=2,outline='red',fill='red')
    Palette2 = Canevas.create_rectangle(MilieuLargeurPaletteBleu-5,MilieuHauteurPaletteBleue-50,MilieuLargeurPaletteBleu+5,MilieuHauteurPaletteBleue+50,width=2,outline='blue',fill='blue')

#vitesses et sens de deplacements des balles 
    OrdBalleRouge+=vitesseX
    AbsBalleRouge+=vitesseY
    OrdBalleBleue+=vitesseX2
    AbsBalleBleue+=vitesseY2
    
    #RebondPalettes(AbsBalleBleue,OrdBalleBleue)
    print (vitesseX)
    RebondPalettes(AbsBalleRouge,OrdBalleRouge,vitesseX,vitesseY)
    print("apres")
    print(vitesseX)
    #toutes les dix millisecondes appel a affichage
    if Arret == False:
        Mafenetre.after(10,AffichageGeneral)
    if OrdBalleRouge+1.5*DiametreBalles<BordGauche:
        Arret = True
        Frame1 = Frame(Mafenetre,borderwidth=2,relief=GROOVE)
        Frame1.pack(side=LEFT,padx=10,pady=10)
        Label(Frame1,text="Le joueur bleu gagne").pack(padx=10,pady=10)
    if OrdBalleRouge-DiametreBalles>BordDroit:
        Arret = True
        texte1 = Frame(Mafenetre,borderwidth=2,relief=GROOVE)
        texte1.pack(side=LEFT,padx=10,pady=10)
        Label(texte1,text="Le joueur rouge gagne").pack(padx=10,pady=10)
    
        
        
    
    brique()

# Permet de recommencer une nouvelle partie
def Reinitialiser():
    global OrdBalleRouge
    global AbsBalleRouge,AbsBalleRougedepart
    global DiametreBalles 
    global MilieuHauteurPaletteRouge,MilieuLargeurPaletteRouge
    global MilieuHauteurPaletteBleue,MilieuLargeurPaletteBleu
    Pause()
    OrdBalleRouge=OrdBalleRougedepart
    AbsBalleRouge=AbsBalleRougedepart
    OrdBalleBleue=OrdBalleBleuedepart
    AbsBalleBleue=AbsBalleBleuedepart
    Canevas.delete(ALL)
    MilieuHauteurPaletteRouge = 310
    MilieuLargeurPaletteRouge = 20
    MilieuHauteurPaletteBleue =310
    MilieuLargeurPaletteBleu =1260
    Palette1 = Canevas.create_rectangle(MilieuLargeurPaletteRouge-5,MilieuHauteurPaletteRouge-50,MilieuLargeurPaletteRouge+5,MilieuHauteurPaletteRouge+50,width=2,outline='red',fill='red')
    Palette2 = Canevas.create_rectangle(MilieuLargeurPaletteBleu-5,MilieuHauteurPaletteBleue-50,MilieuLargeurPaletteBleu+5,MilieuHauteurPaletteBleue+50,width=2,outline='blue',fill='blue')
    balle = Canevas.create_oval(OrdBalleRouge, AbsBalleRouge, OrdBalleRouge+DiametreBalles, AbsBalleRouge+DiametreBalles, outline='red', fill='red')
    balle2 = Canevas.create_oval(OrdBalleBleue, AbsBalleBleue, OrdBalleBleue+DiametreBalles, AbsBalleBleue+DiametreBalles, outline='blue', fill='blue')

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
MilieuHauteurPaletteRouge = 300
MilieuLargeurPaletteRouge = 20
MilieuHauteurPaletteBleue =310
MilieuLargeurPaletteBleu =1260

BordDroit=MilieuLargeurPaletteBleu-5
BordGauche=MilieuLargeurPaletteRouge+5

# Position initiale des balles
OrdBalleRouge=25
OrdBalleBleue=1234
AbsBalleRouge=Hauteur/2
AbsBalleBleue=Hauteur/2

# Sauvegarde des position des balles
OrdBalleRougedepart=OrdBalleRouge
AbsBalleRougedepart=AbsBalleRouge
OrdBalleBleuedepart=OrdBalleBleue
AbsBalleBleuedepart=AbsBalleBleue

# Sens et vitesse de déplacement des balles
vitesseX = 5
vitesseX2=-5
vitesseY2=5
vitesseY = 5

# Création d'un widget Canvas (fenetre de jeu)
Largeur = 1280 #1280
Hauteur = 600 #720
Canevas = Canvas(Mafenetre, width = Largeur, height =Hauteur, bg ='white')
DiametreBalles = 20

Palette1 = Canevas.create_rectangle(MilieuLargeurPaletteRouge-5,MilieuHauteurPaletteRouge-50,MilieuLargeurPaletteRouge+5,MilieuHauteurPaletteRouge+50,width=2,outline='red',fill='red')
Palette2 = Canevas.create_rectangle(MilieuLargeurPaletteBleu-5,MilieuHauteurPaletteBleue-50,MilieuLargeurPaletteBleu+5,MilieuHauteurPaletteBleue+50,width=2,outline='blue',fill='blue')
balle = Canevas.create_oval(OrdBalleRouge, AbsBalleRouge, OrdBalleRouge+DiametreBalles, AbsBalleRouge+DiametreBalles, outline='red', fill='red')
balle2 = Canevas.create_oval(OrdBalleBleue, AbsBalleBleue, OrdBalleBleue+DiametreBalles, AbsBalleBleue+DiametreBalles, outline='blue', fill='blue')
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