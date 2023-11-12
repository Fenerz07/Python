#Importation de programmes

#---}
import tkinter
import time
#---}

#Création de la fenêtre d'animation Tkinter

#---}
fenetre = tkinter.Tk()
fenetre.title("mon animation :)")
zone_graphique = tkinter.Canvas(fenetre, width = 800, height = 600, bg = 'lightblue')
zone_graphique.pack()
#---}

#Classes contenant tout les dessins rangé classe par classe

#---}
class Soleil():
    ''' Cette classe dessine un soleil selon son x , son y et son rayon , de plus elle va lui crée un mouvement avec le m pour l'animation .'''
    def __init__(self,x=50,y=150,rayon=150,m=0.05):
        '''Cette méthode est le constructeur des attributs x, y, rayon et m'''
        self.x=x
        self.y=y
        self.rayon=rayon
        self.m=m
    
    def dessiner_soleil(self):
        '''Cette méthode dessine le soleil. '''
        zone_graphique.create_oval(self.x,self.x,self.y, self.rayon, fill='yellow', outline='')
        
    def mouvement_soleil(self):
        '''Cette méthode permet de donner un mouvement (légère pulsation) au soleil avec la fonction : animation() .'''
        self.y=self.y+self.m
        self.rayon=self.rayon+self.m
        self.x=self.x-self.m
        if self.rayon>=165 or self.rayon<=135 or self.y>=165 or self.y<=135 or self.x<=45 or self.x>=55:
            self.m=-self.m

class Sol():
    ''' Cette classe dessine un sol selon son hauteur et son épaisseur .'''
    def __init__(self,hauteur=600, epaisseur=800):
        '''Cette méthode est le constructeur des attributs hauteur et epaisseur'''
        self.hauteur=hauteur
        self.epaisseur=epaisseur
    
    def dessiner_sol(self):
        '''Cette méthode dessine le sol. '''
        zone_graphique.create_rectangle(self.epaisseur-800, self.hauteur-75, self.epaisseur, self.hauteur, fill='grey', outline='')

class Arbre():
    ''' Cette classe dessine un arbre selon son x , son y , sa hauteur , sa largeur et son rayon .'''
    def __init__(self,x=350, y=450,hauteur=400,largeur=50,rayon=75):
        '''Cette méthode est le constructeur des attributs x, y, hauteur ,largeur et rayon'''
        self.x=x
        self.y=y
        self.hauteur=hauteur
        self.rayon=rayon
        self.largeur=largeur
    
    def dessiner_arbre(self):
        '''Cette méthode dessine l'arbre. '''
        zone_graphique.create_rectangle(700, self.hauteur, self.largeur+700, self.hauteur+125, fill='brown', outline='')
        zone_graphique.create_oval(self.rayon+600, self.x, self.rayon+700, self.y, fill='green', outline='')

class Voiture():
    ''' Cette classe dessine une voiture selon son x , son y , sa longueur , son rayon , de plus elle va lui crée un mouvement avec la vitesse pour l'animation .'''
    def __init__(self,x=150, y=475, longueur=300,rayon=525,vitesse=5):
        '''Cette méthode est le constructeur des attributs x, y, longueur, rayon et vitesse'''
        self.x=x
        self.y=y
        self.longueur=longueur
        self.rayon=rayon
        self.vitesse=vitesse
        
    def dessiner_voiture(self):
        '''Cette méthode dessine la voiture. '''
        zone_graphique.create_rectangle(self.x-50, self.y+25, self.x+200, self.y-50, fill='green')    
        zone_graphique.create_oval(self.x, self.y, self.x+50, self.rayon, fill='white')
        zone_graphique.create_oval(self.x+100, self.y, self.x+150, self.rayon, fill='white')
        zone_graphique.create_rectangle(self.x, self.y-100, self.x+150, self.y-50, fill='lightgreen')
    
    def rouler(self):
        '''Cette méthode permet de donner un mouvement (faire rouler la voiture) à la voiture avec la fonction : animation() .'''
        self.x=self.x+self.vitesse
        if self.x+200==800 or self.x==0+50 :
            self.vitesse=-self.vitesse

class Oiseau():
    ''' Cette classe dessine un oiseau selon son x , son y et son envergure , de plus elle va lui crée un mouvement avec la vitesse pour l'animation .'''
    def __init__(self,x=200, y=200,envergure=25,vitesse=2.5):
        '''Cette méthode est le constructeur des attributs x, y, envergure et vitesse'''
        self.x=x
        self.y=y
        self.envergure=envergure
        self.vitesse=vitesse
        
    def dessiner_oiseau(self):
        '''Cette méthode dessine l'oiseau. '''
        zone_graphique.create_line(self.x, self.y, self.x+self.envergure, self.y+self.envergure)
        zone_graphique.create_line(self.x+25, self.y+25, self.x+self.envergure+25, self.y)
    
    def voler(self):
        '''Cette méthode permet de donner un mouvement (faire voler l'oiseau) à l'oiseau avec la fonction : animation() . '''
        self.x=self.x+self.vitesse
        if self.x+50==800 or self.x==0:
            self.vitesse=-self.vitesse
#---}    
    
    
#Instanciation

#---}
soleil=Soleil()
sol=Sol()
voiture=Voiture()
oiseau=Oiseau()
arbre=Arbre()
#---}

#Fonction pour l'animation Tkinter

#---}
def animation():
    '''Cette fonction permet l'animation des "dessins" .'''
    running = True
    while running == True :
        zone_graphique.delete('all') # ---> rend la zone_graphique vide en supprimant tout les anciens dessins
        soleil.dessiner_soleil() 
        soleil.mouvement_soleil()
        sol.dessiner_sol()
        arbre.dessiner_arbre()
        voiture.dessiner_voiture()
        voiture.rouler()
        oiseau.dessiner_oiseau()
        oiseau.voler()
        zone_graphique.update() #---> Mise à jour à chaque "tour" de la zone_graphique
        time.sleep(0.000001) #---> repos très rapide permettant d'avoir une animation fluide 

animation()
#---}

#Mise à jour de la fenêtre Tkinter

#---}
fenetre.mainloop()
#---}
