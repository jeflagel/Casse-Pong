# script clavier.py
from tkinter import *
from math import *
global Arret
#global AbsBalleRouge
#global OrdBalleRouge,OrdBalleRougedepart
#global vitesseX
#global vitesseY
#global DiametreBalles
Arret = TRUE
vitesseAjoute=0

def RebondPalettes(AbsBalle,OrdBalle,SensDeplacementX,SensDeplacementY):
    

    global BordDroit,BordGauche,DiametreBalles,MilieuHauteurPaletteBleue,MilieuHauteurPaletteRouge
    global vitesseAjoute
    
    if AbsBalle+DiametreBalles>=BordDroit and OrdBalle<=MilieuHauteurPaletteBleue+20 and OrdBalle>=MilieuHauteurPaletteBleue-20:
        SensDeplacementX=-SensDeplacementX-vitesseAjoute
        
    elif AbsBalle+DiametreBalles>=BordDroit and OrdBalle<=MilieuHauteurPaletteBleue+50 and OrdBalle>=MilieuHauteurPaletteBleue+20:
        SensDeplacementX=5
        SensDeplacementY=7
        SensDeplacementX=-SensDeplacementX
        
    elif AbsBalle+DiametreBalles>=BordDroit and OrdBalle<=MilieuHauteurPaletteBleue-20 and OrdBalle>=MilieuHauteurPaletteBleue-50:
        SensDeplacementX=5
        SensDeplacementY=-7
        SensDeplacementX=-SensDeplacementX-vitesseAjoute
        
        
    elif AbsBalle==BordGauche and OrdBalle<=MilieuHauteurPaletteRouge+20 and OrdBalle>=MilieuHauteurPaletteRouge-20:
          SensDeplacementX=-SensDeplacementX
          
    elif AbsBalle==BordGauche and OrdBalle<=MilieuHauteurPaletteRouge+50 and OrdBalle>=MilieuHauteurPaletteRouge+20:
        SensDeplacementX=5
        SensDeplacementY=7
        SensDeplacementX=-SensDeplacementX
        
    elif AbsBalle==BordGauche and OrdBalle<=MilieuHauteurPaletteRouge-20 and OrdBalle>=MilieuHauteurPaletteRouge-50:
        SensDeplacementX=5
        SensDeplacementY=-7
        SensDeplacementX=SensDeplacementX-vitesseAjoute
        
    return(SensDeplacementX,SensDeplacementY)
        
def RebondHautBas(OrdBalle,SensDeplacement):
    
    
    global DiametreBalles,Hauteur
        
    if OrdBalle+(DiametreBalles/2)>=Hauteur or OrdBalle-(DiametreBalles/2)<=0:
        SensDeplacement=-SensDeplacement
    return(SensDeplacement)
    
    

# La fonction affiche les briques a l'écran/les briques doivent etre positionnés proportionellement a la vitesse

                
                
                
TransparenteBriquePositionAbs=[]
TransparenteBriquePositionOrd=[]
BriquePositionAbs=[]
BriquePositionOrd=[]
NbBriqueColonne=[]
EtatBrique=[]
# -----------------------------------------------------------------------------------
#    
# --------------------------------------------------------------------------------
def Brique():
    global TransparenteBriquePositionAbs
    global TransparenteBriquePositionOrd
    global BriquePositionAbs
    global BriquePositionOrd
    global Hauteur, hauteurBrique
    global largeurBrique
    global NbColonneMur
    global AbscisseMur
    
    BriquePositionAbs.clear()
    BriquePositionOrd.clear()
    EtatBrique.clear()
    NbBriqueColonne.clear()
    
    NbColonneMur=6
    largeurBrique=20
    hauteurBrique=30
    
    AbscisseInitiale=(Largeur/2)-((largeurBrique+2)*(NbColonneMur/2))-1
    AbscisseMur=AbscisseInitiale
    OrdonneeInitiale=0
    ValeurDepart=OrdonneeInitiale
    nbbrique=int(Hauteur/(hauteurBrique+2))        #ajustement de taille des briques pour remplir la hauteur de l'ecran
    hauteurBrique=(Hauteur-(2*(nbbrique-1)))/nbbrique
    
    for loop in range(NbColonneMur):
        OrdonneeInitiale=ValeurDepart
        NbBriqueColonne.append(nbbrique)
        for loop in range(nbbrique):                                     # on fait nbbrique par colonne
            BriquePositionAbs.append(AbscisseInitiale)
            BriquePositionOrd.append(OrdonneeInitiale)
            EtatBrique.append(1)                           # 1=afficher et 0=effacer (nb de rebond nécessaire pour détruire)
            OrdonneeInitiale+=hauteurBrique+2
        AbscisseInitiale+=largeurBrique+2
            

def RebondBrique(AbsBalle,OrdBalle,SensDeplacement,largeurBrique,DiametreBalles,DeplacementVertical):
    global indiceCoté
    if SensDeplacement>0:
        AbsBalle+=DiametreBalles
    else :
        AbsBalle-=largeurBrique
    if AbsBalle>=AbscisseMur and AbsBalle<=AbscisseMur+(NbColonneMur*(largeurBrique+2))-2: # partie ou la balle est susceptible de rebondir
        colonne=int((AbsBalle-AbscisseMur)/largeurBrique)    # combien de colonnes entre balle et abscisse mur
        if colonne<=NbColonneMur-1:
            indiceDebut=NbBriqueColonne[colonne]*colonne
            indiceFin=indiceDebut+NbBriqueColonne[colonne]-1
            i=indiceDebut
            while i<=indiceFin:
                if OrdBalle>=BriquePositionOrd[i] and OrdBalle<=BriquePositionOrd[i]+hauteurBrique :
                    if EtatBrique[i]>0:
                        SensDeplacement=-SensDeplacement
                        EtatBrique[i]=0
                        BriqueEffacer(BriquePositionAbs[i],BriquePositionOrd[i],largeurBrique,hauteurBrique)
                    else :
                        if DeplacementVertical>0:
                            indiceCoté=i+1
                        else:
                            indiceCoté=i-1
                    i=indiceFin
                i+=1     
            
    
    return(SensDeplacement)
   
def BriqueEffacer(Abscisse,ordonnée,largeurb,hauteurb):        # procédure pour effacer les briques

        Canevas.create_rectangle(Abscisse,ordonnée,Abscisse+largeurb,ordonnée+hauteurb,outline='white',fill='white')
        
def affichageBriques():
    global BriquePositionOrd,BriquePositionAbs
    global largeurBrique,hauteurBrique
    
    nb=len(BriquePositionAbs)
    for i in range(nb):
        if EtatBrique[i]>0:
            Canevas.create_rectangle(BriquePositionAbs[i],BriquePositionOrd[i],BriquePositionAbs[i]+largeurBrique,BriquePositionOrd[i]+hauteurBrique,outline='red',fill='red')

def RapportVitesseHorizontale(AbsBalle,OrdBalle,SensDeplacement):   # procédure pour gérer la vitesse a l'approche d'un obstacle
    coeff=1
    if SensDeplacement>0:
        AbsBalle+=DiametreBalles
    else :
        AbsBalle-=largeurBrique
    if AbsBalle>AbscisseMur-fabs(SensDeplacement) and AbsBalle<AbscisseMur+(NbColonneMur*(largeurBrique+2)-2)+fabs(SensDeplacement): 
        colonne=int(fabs(AbsBalle-AbscisseMur)/largeurBrique)
        if AbsBalle!=BriquePositionAbs[colonne]:
            if fabs(BriquePositionAbs[colonne]-(AbsBalle))<fabs(SensDeplacement):
                coeff=fabs(BriquePositionAbs[colonne]-AbsBalle)/fabs(SensDeplacement)
    else:
        if AbsBalle-DiametreBalles != BordDroit:
            if fabs(BordDroit-AbsBalle+DiametreBalles)<fabs(SensDeplacement) and OrdBalle<=MilieuHauteurPaletteBleue+50 and OrdBalle>=MilieuHauteurPaletteBleue-50:
                coeff=fabs(BordDroit-AbsBalle+DiametreBalles)/fabs(SensDeplacement)
        if AbsBalle + largeurBrique != BordGauche:
            if fabs(BordGauche-AbsBalle- largeurBrique)<fabs(SensDeplacement) and OrdBalle<=MilieuHauteurPaletteRouge+50 and OrdBalle>=MilieuHauteurPaletteRouge-50:
                coeff=fabs(BordGauche-AbsBalle-largeurBrique)/fabs(SensDeplacement)
        
          
    return(coeff)
    
def RapportVitesseVerticale(AbsBalle,OrdBalle,SensDeplacement):   # procédure pour gérer la vitesse a l'approche d'un obstacle
    coeff=1
    if SensDeplacement>0:
       OrdBalle+=(DiametreBalles/2) 
    else :
        OrdBalle-=(DiametreBalles/2)+hauteurBrique
    if OrdBalle>BriquePositionOrd[indiceCoté]-fabs(SensDeplacement):
        if fabs(BriquePositionOrd[indiceCoté] - OrdBalle)<fabs(SensDeplacement):
            coeff=fabs(BriquePositionOrd[indiceCoté]-OrdBalle)/fabs(SensDeplacement)

    return(coeff)
    

# Permet de gérer le déplacement des palettes ( chaque palette représente un joueur )
def Clavier(event):
    """ Gestion de l'événement Appui sur une touche du clavier """
    global MilieuHauteurPaletteRouge,MilieuHauteurPaletteBleue,MilieuLargeurPaletteRouge,MilieuLargeurPaletteBleue,BordDroit,BordGauche
    touche = event.keysym
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
    Canevas.coords(Palette2,MilieuLargeurPaletteBleue -5, MilieuHauteurPaletteBleue -50, MilieuLargeurPaletteBleue +5, MilieuHauteurPaletteBleue +50)


def AffichageGeneral():
    Canevas.delete(ALL)
    global Arret
    global AbsBalleRouge,AbsBalleBleue
    global OrdBalleRouge,OrdBalleBleue
    global vitesseX,vitesseX2,vitesseAjoute
    global vitesseY,vitesseY2
    global vitesseXInitiale,vitesseX2Initiale
    global vitesseYInitiale,vitesseY2Initiale
    global DiametreBalles
    
    # recreation pallettes+ balles apres reset canevas pour eviter trace de la balle
    balle1 = Canevas.create_oval(AbsBalleRouge, OrdBalleRouge, AbsBalleRouge+DiametreBalles, OrdBalleRouge+DiametreBalles, outline='red', fill='red')
    balle2 = Canevas.create_oval(AbsBalleBleue, OrdBalleBleue, AbsBalleBleue+DiametreBalles, OrdBalleBleue+DiametreBalles, outline='blue', fill='blue')
    Palette1 = Canevas.create_rectangle(MilieuLargeurPaletteRouge-5,MilieuHauteurPaletteRouge-50,MilieuLargeurPaletteRouge+5,MilieuHauteurPaletteRouge+50,width=2,outline='red',fill='red')
    Palette2 = Canevas.create_rectangle(MilieuLargeurPaletteBleue-5,MilieuHauteurPaletteBleue-50,MilieuLargeurPaletteBleue+5,MilieuHauteurPaletteBleue+50,width=2,outline='blue',fill='blue')

    affichageBriques()
#vitesses et sens de deplacements des balles 
    coefficient=RapportVitesseHorizontale(AbsBalleRouge,OrdBalleRouge,vitesseX)
    AbsBalleRouge+=vitesseX*coefficient
    OrdBalleRouge+=vitesseY*coefficient
    coefficient=RapportVitesseHorizontale(AbsBalleBleue,OrdBalleBleue,vitesseX2)
    AbsBalleBleue+=vitesseX2*coefficient
    OrdBalleBleue+=vitesseY2*coefficient
    
    
   
    vitesseX,vitesseY= RebondPalettes(AbsBalleRouge,OrdBalleRouge,vitesseX,vitesseY)
    
    vitesseY=RebondHautBas(OrdBalleRouge,vitesseY)
   
    vitesseX2,vitesseY2= RebondPalettes(AbsBalleBleue,OrdBalleBleue,vitesseX2,vitesseY2)
    vitesseY2=RebondHautBas(OrdBalleBleue,vitesseY2)
    
    
    vitesseX2=RebondBrique(AbsBalleBleue,OrdBalleBleue,vitesseX2,largeurBrique,DiametreBalles,vitesseY2)
    vitesseX=RebondBrique(AbsBalleRouge,OrdBalleRouge,vitesseX,largeurBrique,DiametreBalles,vitesseY)
   
    #toutes les dix millisecondes appel a affichage
    if Arret == False:
        Mafenetre.after(10,AffichageGeneral)
    if AbsBalleRouge+1.5*DiametreBalles<=BordGauche:
        Arret = True
        Frame1 = Frame(Mafenetre,borderwidth=1,relief=GROOVE)
        Frame1.pack(side=LEFT,padx=10,pady=10)
        Label(Frame1,text="Le joueur bleu gagne").pack(padx=10,pady=10)
    elif AbsBalleRouge-DiametreBalles>=BordDroit:
        Arret = True
        texte1 = Frame(Mafenetre,borderwidth=1,relief=GROOVE)
        texte1.pack(side=LEFT,padx=10,pady=10)
        Label(texte1,text="Le joueur rouge gagne").pack(padx=10,pady=10)
    elif AbsBalleBleue+1.5*DiametreBalles<=BordGauche:
        Arret = True
        Frame1 = Frame(Mafenetre,borderwidth=1,relief=GROOVE)
        Frame1.pack(side=LEFT,padx=10,pady=10)
        Label(Frame1,text="Le joueur bleu gagne").pack(padx=10,pady=10)
    elif AbsBalleBleue-DiametreBalles>=BordDroit:
        Arret = True
        texte1 = Frame(Mafenetre,borderwidth=1,relief=GROOVE)
        texte1.pack(side=LEFT,padx=10,pady=10)
        Label(texte1,text="Le joueur rouge gagne").pack(padx=10,pady=10)
    


    
    

# Permet de recommencer une nouvelle partie
def Reinitialiser():
    global AbsBalleRouge
    global OrdBalleRouge,OrdBalleRougedepart
    global AbsBalleBleue
    global OrdBalleBleue,OrdBalleBleuedepart
    global DiametreBalles 
    global MilieuHauteurPaletteRouge,MilieuLargeurPaletteRouge
    global MilieuHauteurPaletteBleue,MilieuLargeurPaletteBleue
    global vitesseX
    global vitesseX2
    global vitesseY2
    global vitesseY
    Pause()
    AbsBalleRouge=AbsBalleRougedepart
    OrdBalleRouge=OrdBalleRougedepart
    AbsBalleBleue=AbsBalleBleuedepart
    OrdBalleBleue=OrdBalleBleuedepart
    Canevas.delete(ALL)
    MilieuHauteurPaletteRouge = 310
    MilieuLargeurPaletteRouge = 20
    MilieuHauteurPaletteBleue =310
    MilieuLargeurPaletteBleue =1260
    vitesseX = 5
    vitesseX2=-5
    vitesseY2=5
    vitesseY = 5

# Permet de commencer la partie
def Demarrer():
    global Arret
    if Arret == True:
        Arret = False
        Brique()
        AffichageGeneral()

# Met la partie en pause        
def Pause():
    global Arret
    Arret = True
    
#-------------------------------------------------------------------------------
#
#                 PROGRAMME PRINCIPAL
#
#-------------------------------------------------------------------------------    
# Création de la fenêtre principale
Mafenetre = Tk()
Mafenetre.title('Casse Pong')

# position initiale des palettes
# Palette1 = rouge
# Palette2 = bleu
MilieuHauteurPaletteRouge = 300
MilieuLargeurPaletteRouge = 20
MilieuHauteurPaletteBleue =310
MilieuLargeurPaletteBleue =1260

BordDroit=MilieuLargeurPaletteBleue-5
BordGauche=MilieuLargeurPaletteRouge+5

# Position initiale des balles/ordballe et abs balle doit etre un multiple de vitesse sinon bug
AbsBalleRouge=25
AbsBalleBleue=1235
Hauteur = 600
OrdBalleRouge=Hauteur/2
OrdBalleBleue=Hauteur/2

# Sauvegarde des position des balles
AbsBalleRougedepart=AbsBalleRouge
OrdBalleRougedepart=OrdBalleRouge
AbsBalleBleuedepart=AbsBalleBleue
OrdBalleBleuedepart=OrdBalleBleue

# Sens et vitesse de déplacement des balles
vitesseX = 5
vitesseX2=-5
vitesseY2=5
vitesseY = 5
vitesseXInitiale=vitesseX
vitesseX2Initiale=vitesseX2
vitesseYInitiale=vitesseY
vitesseY2Initiale=vitesseY2

# Création d'un widget Canvas (fenetre de jeu)
Largeur = 1280 #1280
Hauteur = 600 #720
Canevas = Canvas(Mafenetre, width = Largeur, height =Hauteur, bg ='white')
DiametreBalles = 20

Palette1 = Canevas.create_rectangle(MilieuLargeurPaletteRouge-5,MilieuHauteurPaletteRouge-50,MilieuLargeurPaletteRouge+5,MilieuHauteurPaletteRouge+50,width=2,outline='red',fill='red')
Palette2 = Canevas.create_rectangle(MilieuLargeurPaletteBleue-5,MilieuHauteurPaletteBleue-50,MilieuLargeurPaletteBleue+5,MilieuHauteurPaletteBleue+50,width=2,outline='blue',fill='blue')
balle1 = Canevas.create_oval(AbsBalleRouge, OrdBalleRouge, AbsBalleRouge+DiametreBalles, OrdBalleRouge+DiametreBalles, outline='red', fill='red')
balle2 = Canevas.create_oval(AbsBalleBleue, OrdBalleBleue, AbsBalleBleue+DiametreBalles, OrdBalleBleue+DiametreBalles, outline='blue', fill='blue')
#palletes anciennes positions
Canevas.focus_set()
Canevas.bind('<Key>',Clavier)
Canevas.pack(padx =5, pady =5)

# Création de widgets Button 
Button(Mafenetre, text ='Quitter', command = Mafenetre.destroy).pack(side=LEFT,padx=5,pady=5)

BoutonBrique = Button(Mafenetre, text ='brique', command =Brique)
BoutonBrique.pack(side = LEFT, padx = 15, pady = 15)


BoutonGo = Button(Mafenetre, text ='Démarrer', command = Demarrer)
BoutonGo.pack(side = LEFT, padx = 10, pady = 10)

BoutonPause = Button(Mafenetre, text ='Pause', command = Pause)
BoutonPause.pack(side = LEFT, padx = 5, pady = 5)

BoutonReinitialiser = Button(Mafenetre, text='Reinitialiser', command = Reinitialiser)
BoutonReinitialiser.pack(side=LEFT, padx = 5,pady = 5)

Mafenetre.mainloop()
