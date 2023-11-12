#Appel des modules externes tkinter(modélisation) et random(aléatoire)
from tkinter import *
from random import randrange

def tableau():
    '''
    fonction finale appelant la fonction calculer() et modifplan() et ouvre la fenêtre tkinter pour l'affichage 
    '''
    calculer()
    modifplan()
    window.after(1,tableau)

def plan():
    '''
    construction du plan fait en rectangles morts de couleurs noir
    '''
    for y in range(hauteur):
        for x in range(largeur):
            grille[x][y] = mort
            grilletemp[x][y] = mort
            cellule[x][y] = canvas.create_rectangle((x*cote, y*cote,(x+1)*cote, (y+1)*cote), outline="Black")
    #boucle pour donner les cases de départ aléatoire des rectangles vivants selon la taille du plan
    for i in range(largeur*hauteur//4):
        grille[randrange(largeur)][randrange(hauteur)] = vivant

def calculer():
    '''
    Calcul pour savoir combien un rectangle possède de voisins selon la fonction compte_voisins(x,y)
    '''
    for y in range(hauteur):
        for x in range(largeur):
            nombre_voisins = compte_voisins(x,y)
            
            if grille[x][y] == vivant and (nombre_voisins < 2 or nombre_voisins > 3):
                grilletemp[x][y] = mort
            
            if grille[x][y] == vivant and (nombre_voisins == 2 or nombre_voisins == 3):
                grilletemp[x][y] = vivant

            if grille[x][y] == mort and nombre_voisins == 3:
                grilletemp[x][y] = vivant

    #Quand tout est fait on échange grille et grille temporaire
    for y in range(hauteur):
        for x in range(largeur):
            grille[x][y] = grilletemp[x][y]

def compte_voisins(x,y):
    '''
    compte pour chaque rectangle son nombre de voisins grâce à un accumulateur
    :return: nombre_voisins qui donne le nombre de voisins d'un rectangle en position x,y
    '''
    nombre_voisins = 0

    if grille[(x-1)%largeur][(y+1)%hauteur] == 1:
        nombre_voisins += 1

    if grille[x][(y+1)%hauteur] == 1:
        nombre_voisins += 1

    if grille[(x+1)%largeur][(y+1)%hauteur] == 1:
        nombre_voisins += 1

    if grille[(x-1)%largeur][y] == 1:
        nombre_voisins += 1

    if grille[(x+1)%largeur][y] == 1:
        nombre_voisins += 1

    if grille[(x-1)%largeur][(y-1)%hauteur] == 1:
        nombre_voisins += 1

    if grille[x][(y-1)%hauteur] == 1:
        nombre_voisins += 1

    if grille[(x+1)%largeur][(y-1)%hauteur] == 1:
        nombre_voisins += 1

    return nombre_voisins

def modifplan():
    '''
    modifie le canvas selon le calcul
    '''
    for y in range(hauteur):
        for x in range(largeur):
            if grille[x][y]==0:
                couleur = "black"
            else:
                couleur = "blue"
            canvas.itemconfig(cellule[x][y], fill=couleur)

#mesures de bases
hauteur = 50
largeur = 50
cote = 15 #taille des rectangles
vivant = 1 #numéro assigné à un rectangle vivant
mort = 0 # /         /        /   mort

cellule = [[0 for row in range(hauteur)] for col in range(largeur)]
grille = [[mort for row in range(hauteur)] for col in range(largeur)]
grilletemp = [[mort for row in range(hauteur)] for col in range(largeur)]

#initialisation du Tkinter
window = Tk()
window.title("JDLV")
canvas = Canvas(window, width=cote*largeur, height=cote*hauteur)
canvas.pack()

#appel des fonctions principales
plan()
tableau()

window.mainloop()