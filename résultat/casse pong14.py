# script clavier.py
from tkinter import *
from math import *
import random as r
global Arret
#global AbsBalleRouge
#global OrdBalleRouge,OrdBalleRougedepart
#global vitesseX
#global vitesseY
#global DiametreBalles
Arret = True
BonusBouclierBleu=False
BonusBouclierRouge=False
EtatBouclierBleu=0
EtatBouclierRouge=0
vitesseAjoute=0
score=0
CotéDescente=r.randrange(0,2)
DescenteBonus=False
nombrebonus=r.randrange(0,2)
BonusMissileBleu=False
BonusMissileRouge=False
FeuBleu1=False
FeuBleu2=False
FeuRouge1=False
FeuRouge2=False
EtatMissileRouge=0
EtatMissileBleu=0
MissileReussi=False


def RebondPalettes(AbsBalle,OrdBalle,SensDeplacementX,SensDeplacementY):
    

    global BordDroit,BordGauche,DiametreBalles,MilieuHauteurPaletteBleue,MilieuHauteurPaletteRouge
    global vitesseAjoute,EtatBouclierBleu,BonusBouclierBleu
    global EtatBouclierRouge,BonusBouclierRouge,nombrebonus,BonusMissileBleu,BonusMissileRouge,EtatMissileRouge,EtatMissileBleu
    
    if nombrebonus==0:
        if AbsBonus>=BordDroit and OrdBonus<=MilieuHauteurPaletteBleue+50 and OrdBonus>=MilieuHauteurPaletteBleue-50:
            BonusBouclierBleu=True
            EtatBouclierBleu=1
        
        if AbsBonus<=BordGauche and OrdBonus<=MilieuHauteurPaletteRouge+50 and OrdBonus>=MilieuHauteurPaletteRouge-50:
            BonusBouclierRouge=True
            EtatBouclierRouge=1
            
    else :
        if nombrebonus==1:
            if AbsBonus>=BordDroit and OrdBonus<=MilieuHauteurPaletteBleue+50 and OrdBonus>=MilieuHauteurPaletteBleue-50:
                BonusMissileBleu=True
                EtatMissileBleu=1
                
            if AbsBonus<=BordGauche and OrdBonus<=MilieuHauteurPaletteRouge+50 and OrdBonus>=MilieuHauteurPaletteRouge-50:
                BonusMissileRouge=True
                EtatMissileRouge=1
     
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
        
    else:
        if AbsBalle<=BordGauche and EtatBouclierRouge!=0 :
            SensDeplacementX=-SensDeplacementX
            EtatBouclierRouge-=1
        
        if EtatBouclierRouge==0:
            BonusBouclierRouge=False
            
        if  AbsBalle+DiametreBalles>=BordDroit and EtatBouclierBleu!=0 :
            SensDeplacementX=-SensDeplacementX-vitesseAjoute
            EtatBouclierBleu-=1
        
        if EtatBouclierBleu==0:
            BonusBouclierBleu=False
        
        
        
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
    global Hauteur, hauteurBrique,DescenteBonus
    global largeurBrique
    global NbColonneMur
    global AbscisseMur
    
    BriquePositionAbs.clear()
    BriquePositionOrd.clear()
    EtatBrique.clear()
    NbBriqueColonne.clear()
    
    NbColonneMur=4
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
            
def MissileBrique(SensDeplacement,largeurBrique,DiametreBalles,DeplacementVertical,AbsMissile): #fonction pour destruction brique par missile
    global AbsMissilerouge1,OrdMissileRougeHaut,AbsMissilerouge2,OrdMissileRougeBas,AbsMissileBleu1,OrdMissileBleuHaut,AbsMissileBleu2
    global BonusMissilebleu1,BonusMissilebleu2,OrdMissileBleuBas
    global BonusMissilerouge1,BonusMissilerouge2,score,MissileReussi

    if AbsMissile>=AbscisseMur and AbsMissile<=AbscisseMur+(NbColonneMur*(largeurBrique+2))-2: # partie ou la balle est susceptible de rebondir
        colonne=int((AbsMissile-AbscisseMur)/largeurBrique)    # combien de colonnes entre missile et abscisse mur
        if colonne<=NbColonneMur-1:
            indiceDebut=NbBriqueColonne[colonne]*colonne
            indiceFin=indiceDebut+NbBriqueColonne[colonne]-1
            i=indiceDebut
            while i<=indiceFin:
                print("coucou")
                if AbsMissilerouge1>=BriquePositionAbs[i] and OrdMissileRougeHaut>=BriquePositionOrd[i] and OrdMissileRougeHaut<=BriquePositionOrd[i]+hauteurBrique and EtatBrique[i]>0:
                    EtatBrique[i]=0
                    BriqueEffacer(BriquePositionAbs[i],BriquePositionOrd[i],largeurBrique,hauteurBrique)
                    score+=100
                    #Canevas.delete(BonusMissilerouge1)
                    MissileReussi=True
                if AbsMissilerouge2>=BriquePositionAbs[i] and OrdMissileRougeBas>=BriquePositionOrd[i] and OrdMissileRougeBas<=BriquePositionOrd[i]+hauteurBrique and EtatBrique[i]>0:
                    EtatBrique[i]=0
                    BriqueEffacer(BriquePositionAbs[i],BriquePositionOrd[i],largeurBrique,hauteurBrique)
                    score+=100
                    #Canevas.delete(BonusMissilerouge2)
                    MissileReussi=True
                if AbsMissileBleu1>=BriquePositionAbs[i] and OrdMissileBleuHaut>=BriquePositionOrd[i] and OrdMissileBleuHaut<=BriquePositionOrd[i]+hauteurBrique and EtatBrique[i]>0:
                    EtatBrique[i]=0
                    BriqueEffacer(BriquePositionAbs[i],BriquePositionOrd[i],largeurBrique,hauteurBrique)
                    score+=100
                    #Canevas.delete(BonusMissilebleu1)
                    MissileReussi=True
                if AbsMissileBleu2>=BriquePositionAbs[i] and OrdMissileBleuBas>=BriquePositionOrd[i] and OrdMissileBleuBas<=BriquePositionOrd[i]+hauteurBrique and EtatBrique[i]>0:
                    EtatBrique[i]=0
                    BriqueEffacer(BriquePositionAbs[i],BriquePositionOrd[i],largeurBrique,hauteurBrique)
                    score+=100
                    #Canevas.delete(BonusMissilebleu2) 
                    MissileReussi=True   
                    
                if MissileReussi==True:
                    i=indiceFin
                i+=1     
                    
                    

def RebondBrique(AbsBalle,OrdBalle,SensDeplacement,largeurBrique,DiametreBalles,DeplacementVertical):
    global indiceCoté,Bonus,score,OrdBonus,AbsBonus,CubeBonus,DescenteBonus
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
                        score+=100
                        Bonus=r.randrange(2,6)
                        if Bonus==5:
                            CubeBonus=Canevas.create_image(AbsBonus,OrdBonus,image=photoBonus)
                            DescenteBonus=True
                    else :
                        if DeplacementVertical>0:
                            indiceCoté=i+1                        #indice de la colonne sur laquelle le rebond est testé
                        else:
                            indiceCoté=i-1
                    i=indiceFin
                i+=1     
            
    
    return(SensDeplacement)
   
def BriqueEffacer(Abscisse,ordonnée,largeurb,hauteurb):        # procédure pour effacer les briques

        Canevas.create_rectangle(Abscisse,ordonnée,Abscisse+largeurb,ordonnée+hauteurb,outline='white',fill='white')

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
    global FeuRouge1,FeuRouge2,FeuBleu1,FeuBleu2,EtatMissileRouge,EtatMissileBleu
    touche = event.keysym
    # la touche c et n pour les missiles
    if BonusMissileRouge==True and touche =='c':
        FeuRouge1=True
        FeuRouge2=True
        if EtatMissileRouge>0:
            EtatMissileRouge-=1
    if BonusMissileBleu==True and touche =='n':
        FeuBleu1=True
        FeuBleu2=True
        if EtatMissileRouge>0:
            EtatMissileBleu-=1
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
    BonusBouclierBleu=False
    BonusBouclierRouge=False
    EtatBouclierBleu=0
    EtatBouclierRouge=0
    score=0
    DescenteBonus=False
    BonusMissileBleu=False
    BonusMissileRouge=False
    FeuBleu1=False
    FeuBleu2=False
    FeuRouge1=False
    FeuRouge2=False
    EtatMissileRouge=0
    EtatMissileBleu=0

# Permet de commencer la partie

def Demarrer():
    global Arret,Pause
    if Arret == True:
        Arret = False
        Brique()
        AffichageGeneral()
        BoutonGo["text"] = "Démarrer"

# Met la partie en pause        
def Pause():
    global Arret,Pause
    
    Arret = True
    BoutonGo["text"] = "Reprendre"
#-------------------------------------------------------------------------------
#
#                 PROGRAMME PRINCIPAL
#
#-------------------------------------------------------------------------------    
# Création de la fenêtre principale
Mafenetre = Toplevel()
Mafenetre.title('Casse Pong')

# position initiale des palettes
# Palette1 = rouge
# Palette2 = bleu
MilieuHauteurPaletteRouge = 300
MilieuLargeurPaletteRouge = 20
MilieuHauteurPaletteBleue =300
MilieuLargeurPaletteBleue =1260

BordDroit=MilieuLargeurPaletteBleue-5
BordGauche=MilieuLargeurPaletteRouge+5

# Position initiale des balles/ordballe et abs balle doit etre un multiple de vitesse sinon bug
AbsBalleRouge=29
AbsBalleBleue=1231
Hauteur = 600
OrdBalleRouge=Hauteur/2-10
OrdBalleBleue=Hauteur/2-10
AbsBonus=640
OrdBonus=r.randrange(1,600)
#AbsMissileBleuDepart=MilieuLargeurPaletteBleue
#AbsMissilerougeDepart=MilieuLargeurPaletteRouge
AbsMissileBleu1=MilieuLargeurPaletteBleue
AbsMissileBleu2=MilieuLargeurPaletteBleue
AbsMissilerouge1=MilieuLargeurPaletteRouge
AbsMissilerouge2=MilieuLargeurPaletteRouge
OrdMissileBleuHaut=400-72
OrdMissileRougeHaut=400-72
OrdMissileBleuBas=400+72
OrdMissileRougeBas=400+72

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
Canevas = Canvas(Mafenetre, width = Largeur, height =Hauteur, bg ='black')
DiametreBalles = 20


# Affichage des textures

photoBrique=PhotoImage(file="C:\\Users\\jeremy\\Desktop\\Projet\\ImagesISN\\Brique.gif")
photoBalleBleue=PhotoImage(file="C:\\Users\\jeremy\\Desktop\\Projet\\ImagesISN\\BalleBleu.gif")
photoBalleRouge=PhotoImage(file="C:\\Users\\jeremy\\Desktop\\Projet\\ImagesISN\\BalleRouge.gif")
photoPaletteBleu=PhotoImage(file="C:\\Users\\jeremy\\Desktop\\Projet\\ImagesISN\\paletteLaserBleue2.gif")
photoPaletteRouge=PhotoImage(file="C:\\Users\\jeremy\\Desktop\\Projet\\ImagesISN\\paletteLaserRouge2.gif")
photoBonus=PhotoImage(file="C:\\Users\\jeremy\\Desktop\\Projet\\ImagesISN\\Bonus.gif")
photoMissileRouge=PhotoImage(file="C:\\Users\\jeremy\\Desktop\\Projet\\ImagesISN\\missileRouge2.gif")
photoMissileBleu=PhotoImage(file="C:\\Users\\jeremy\\Desktop\\Projet\\ImagesISN\\missileBleue2.gif")

balle1 = Canevas.create_image((AbsBalleRouge+AbsBalleRouge+DiametreBalles)/2,(OrdBalleRouge+OrdBalleRouge+DiametreBalles)/2,image=photoBalleRouge)
balle2 = Canevas.create_image((AbsBalleBleue+AbsBalleBleue+DiametreBalles)/2,(OrdBalleBleue+OrdBalleBleue+DiametreBalles)/2,image=photoBalleBleue)
Palette1 = Canevas.create_image((MilieuLargeurPaletteRouge-5+MilieuLargeurPaletteRouge+5)/2,(MilieuHauteurPaletteRouge-50+MilieuHauteurPaletteRouge+50)/2,image=photoPaletteRouge)
Palette2 = Canevas.create_image((MilieuLargeurPaletteBleue-5+MilieuLargeurPaletteBleue+5)/2,(MilieuHauteurPaletteBleue-50+MilieuHauteurPaletteBleue+50)/2,image=photoPaletteBleu)
#affichage des missiles

if BonusMissileBleu==True and FeuBleu1==True and FeuBleu2==True and EtatMissileBleu>=0:
    BonusMissilebleu1=Canevas.create_image(AbsMissileBleuDepart,OrdMissileBleuHaut,image=photoMissileBleu)
    BonusMissilebleu2=Canevas.create_image(AbsMissileBleuDepart,OrdMissileBleuBas,image=photoMissileBleu)
    
if BonusMissileRouge==True and EtatMissileRouge>=0 and FeuRouge1==True and FeuRouge2==True :
    BonusMissilerouge1=Canevas.create_image(AbsMissilerougeDepart,OrdMissileRougeHaut,image=photoMissileRouge)
    BonusMissilerouge2=Canevas.create_image(AbsMissilerougeDepart,OrdMissileRougeBas,image=photoMissileRouge)
     
#affichage des boucliers

if BonusBouclierBleu==True:
    BonusBouclierBleu1 =                            Canevas.create_rectangle(MilieuLargeurPaletteBleue-1,MilieuHauteurPaletteBleue-1000,MilieuLargeurPaletteBleue+1,MilieuHauteurPaletteBleue+1000,width=1,outline='#33ef00',fill='#33ef00')
    
if BonusBouclierRouge==True:
    BonusBouclierRouge1 =                            Canevas.create_rectangle(MilieuLargeurPaletteRouge-1,MilieuHauteurPaletteRouge-1000,MilieuLargeurPaletteRouge+1,MilieuHauteurPaletteRouge+1000,width=1,outline='#33ef00',fill='#33ef00')    
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


        
def affichageBriques():
    global BriquePositionOrd,BriquePositionAbs
    global largeurBrique,hauteurBrique
    
    nb=len(BriquePositionAbs)
    for i in range(nb):
        if EtatBrique[i]>0:
            Canevas.create_image((BriquePositionAbs[i]+BriquePositionAbs[i]+largeurBrique)/2,(BriquePositionOrd[i]+BriquePositionOrd[i]+hauteurBrique)/2,image=photoBrique)
            #Canevas.create_rectangle(BriquePositionAbs[i],BriquePositionOrd[i],BriquePositionAbs[i]+largeurBrique,BriquePositionOrd[i]+hauteurBrique,outline='red',fill='red')
            
def AffichageGeneral():
    Canevas.delete(ALL)
    global Arret
    global AbsBalleRouge,AbsBalleBleue
    global OrdBalleRouge,OrdBalleBleue
    global vitesseX,vitesseX2,vitesseAjoute
    global vitesseY,vitesseY2
    global vitesseXInitiale,vitesseX2Initiale
    global vitesseYInitiale,vitesseY2Initiale
    global DiametreBalles,AbsBonus,OrdBonus,DescenteBonus,CubeBonus,CotéDescente
    global AbsMissileBleu1,AbsMissileBleu2,AbsMissilerouge1,AbsMissilerouge2
    
    # recreation pallettes+ balles apres reset canevas pour eviter trace de la balle
    balle1 = Canevas.create_image((AbsBalleRouge+AbsBalleRouge+DiametreBalles)/2,(OrdBalleRouge+OrdBalleRouge+DiametreBalles)/2,image=photoBalleRouge)
    balle2 = Canevas.create_image((AbsBalleBleue+AbsBalleBleue+DiametreBalles)/2,(OrdBalleBleue+OrdBalleBleue+DiametreBalles)/2,image=photoBalleBleue)
    Palette1 = Canevas.create_image((MilieuLargeurPaletteRouge-5+MilieuLargeurPaletteRouge+5)/2,(MilieuHauteurPaletteRouge-50+MilieuHauteurPaletteRouge+50)/2,image=photoPaletteRouge)
    Palette2 = Canevas.create_image((MilieuLargeurPaletteBleue-5+MilieuLargeurPaletteBleue+5)/2,(MilieuHauteurPaletteBleue-50+MilieuHauteurPaletteBleue+50)/2,image=photoPaletteBleu)
    #bonus bouclier
    if BonusBouclierBleu==True:
        BonusBouclierBleu1 =                            Canevas.create_rectangle(MilieuLargeurPaletteBleue-1,MilieuHauteurPaletteBleue-1000,MilieuLargeurPaletteBleue+1,MilieuHauteurPaletteBleue+1000,width=1,outline='#33ef00',fill='#33ef00')
        
    if BonusBouclierRouge==True:
        BonusBouclierRouge1 =                            Canevas.create_rectangle(MilieuLargeurPaletteRouge-1,MilieuHauteurPaletteRouge-1000,MilieuLargeurPaletteRouge+1,MilieuHauteurPaletteRouge+1000,width=1,outline='#33ef00',fill='#33ef00')
        
    #bonus missile
    if BonusMissileBleu==True and FeuBleu1==True and EtatMissileBleu>=0:
        AbsMissileBleu1-=3
        BonusMissilebleu1=Canevas.create_image(AbsMissileBleu1,OrdMissileBleuHaut,image=photoMissileBleu)
        
        
    if BonusMissileBleu==True and FeuBleu2==True and EtatMissileBleu>=0: 
        AbsMissileBleu2-=3
        BonusMissilebleu2=Canevas.create_image(AbsMissileBleu2,OrdMissileBleuBas,image=photoMissileBleu)
        
    if BonusMissileRouge==True and EtatMissileRouge>=0 and FeuRouge1==True :
        AbsMissilerouge1+=3
        BonusMissilerouge1=Canevas.create_image(AbsMissilerouge1,OrdMissileRougeHaut,image=photoMissileRouge)
    
    if BonusMissileRouge==True and EtatMissileRouge>=0 and FeuRouge2==True :
        AbsMissilerouge2+=3
        BonusMissilerouge2=Canevas.create_image(AbsMissilerouge2,OrdMissileRougeBas,image=photoMissileRouge)
        
    if DescenteBonus==True :
        if CotéDescente==0:
            AbsBonus-=3
            CubeBonus=Canevas.create_image(AbsBonus,OrdBonus,image=photoBonus)
            if AbsBonus<0:
                DescenteBonus=False
                AbsBonus=640
                OrdBonus=r.randrange(1,600)
                CotéDescente=r.randrange(0,2)
                nombrebonus=r.randrange(0,3)
                
        else:
            AbsBonus+=3
            CubeBonus=Canevas.create_image(AbsBonus,OrdBonus,image=photoBonus)
            if AbsBonus>1280:
                DescenteBonus=False
                AbsBonus=640
                OrdBonus=r.randrange(1,600)
                CotéDescente=r.randrange(0,2)
                nombrebonus=r.randrange(0,3)
            
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
    
    
    MissileBrique(vitesseX2,largeurBrique,DiametreBalles,vitesseY2,AbsMissileBleu1)
    MissileBrique(vitesseX,largeurBrique,DiametreBalles,vitesseY,AbsMissilerouge1)
   
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
    
   # Frame2 = Frame(Mafenetre,borderwidth=1,relief=GROOVE)
    #Frame2.pack(side=LEFT,padx=10,pady=10)
    #Label(Frame2,text=score).pack(padx=10,pady=10)
    

Mafenetre.mainloop()
