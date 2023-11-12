# ► Importation de programmes

#╔════════════
import tkinter    #programme Tkinter pour l'animation et le dessin
import time       #programme Time pour le temps ( ici , utlisé pour faire une pause dans l'animation )
#╚════════════

# ► Classes du programme contenant les différent(e)s dessins/animations et l'interface .

#╔═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
class Interface():
    ''' Cette classe correspond à l'interface de la fenêtre d'animation permettant de dessiner et d'animer les autres classes . '''
    
    def __init__(self,fenetre = tkinter.Tk(),zone_graphique = tkinter.Canvas(width = 800, height = 600, bg = 'lightblue')):
        '''Cette méthode est le constructeur des attributs de l'interface de la fenêtre (titre,zone graphique,dimensions de la fenêtre, ...)'''
        self.fenetre = fenetre
        self.fenetre.title(" Animation D'Hugo.M ")
        self.zone_graphique=zone_graphique
        self.zone_graphique.pack()
    
    def instancier(self):
        '''Cette méthode instancie les autres classes'''
        self.soleil=Soleil(50,150,150,0.05,self.zone_graphique)
        self.sol=Sol(275,800,self.zone_graphique)
        self.voiture=Voiture(150,475,200,50,5,self.zone_graphique)
        self.oiseau=Oiseau(200,200,15,2.5,1,self.zone_graphique)
        self.arbre=Arbre(700,525,100,50,75,1,self.zone_graphique)
        
    def dessiner(self):
        '''Cette méthode dessine les autres classes'''
        self.soleil.dessiner_soleil()
        self.sol.dessiner_sol()
        self.arbre.dessiner_arbre()
        self.voiture.dessiner_voiture()
        self.oiseau.dessiner_oiseau()
        
    def animation(self):
        '''Cette méthode construit l'animation des dessins (déjà construit grâce à la méthode "dessiner()") '''
        running = True
        while running == True :
            self.zone_graphique.delete('all') # ---> rend la zone_graphique vide en supprimant tout les anciens dessins
            self.dessiner()
            self.voiture.rouler()
            self.oiseau.voler()
            self.oiseau.ailes()
            self.soleil.mouvement_soleil()
            self.zone_graphique.update() #---> Mise à jour à chaque "tour" de la zone_graphique
            time.sleep(0.000001) #---> repos très rapide permettant d'avoir une animation fluide 
        
class Soleil():
    ''' Cette classe dessine un soleil selon son x , son y et son rayon , de plus elle va lui crée un mouvement avec le m pour l'animation .'''
    
    def __init__(self,x,y,rayon,m,zone_graphique):
        '''Cette méthode est le constructeur des attributs x, y, rayon et m'''
        self.x=x
        self.y=y
        self.rayon=rayon
        self.m=m
        self.zone_graphique=zone_graphique
    
    def dessiner_soleil(self):
        '''Cette méthode dessine le soleil. '''
        self.zone_graphique.create_oval(self.x,self.x,self.y, self.rayon, fill='yellow', outline='')
        
    def mouvement_soleil(self):
        '''Cette méthode permet de donner un mouvement (légère pulsation) au soleil avec la fonction : animation() .'''
        self.y=self.y+self.m
        self.rayon=self.rayon+self.m
        self.x=self.x-self.m
        if self.rayon>=165 or self.rayon<=135 or self.y>=165 or self.y<=135 or self.x<=45 or self.x>=55:
            self.m=-self.m

class Sol():
    ''' Cette classe dessine un sol selon son hauteur et son épaisseur .'''
    
    def __init__(self,hauteur, epaisseur,zone_graphique):
        '''Cette méthode est le constructeur des attributs hauteur et epaisseur'''
        self.hauteur=hauteur
        self.epaisseur=epaisseur
        self.zone_graphique=zone_graphique
    
    def dessiner_sol(self):
        '''Cette méthode dessine le sol. '''
        self.zone_graphique.create_rectangle(self.epaisseur-800, 800-self.hauteur, self.epaisseur, 800, fill='grey')

class Arbre():
    ''' Cette classe dessine un arbre selon son x , son y , sa hauteur , sa largeur et son rayon .'''
    
    def __init__(self,x, y,hauteur,largeur,rayon,vitesse,zone_graphique):
        '''Cette méthode est le constructeur des attributs x, y, hauteur ,largeur et rayon'''
        self.x=x
        self.y=y
        self.hauteur=hauteur
        self.rayon=rayon
        self.largeur=largeur
        self.vitesse=vitesse
        self.zone_graphique=zone_graphique
    
    def dessiner_arbre(self):
        '''Cette méthode dessine l'arbre. '''
        self.zone_graphique.create_rectangle(self.x, self.y, self.x+self.largeur, self.y-self.hauteur, fill='brown', outline='')
        self.zone_graphique.create_oval(self.x-25, self.x-350, self.x+self.rayon, self.y+self.rayon-150, fill='green', outline='')
        
class Voiture():
    ''' Cette classe dessine une voiture selon son x , son y , sa longueur , son rayon , de plus elle va lui crée un mouvement avec la vitesse pour l'animation .'''
    
    def __init__(self,x, y, longueur,rayon,vitesse,zone_graphique):
        '''Cette méthode est le constructeur des attributs x, y, longueur, rayon et vitesse'''
        self.x=x
        self.y=y
        self.longueur=longueur
        self.rayon=rayon
        self.vitesse=vitesse
        self.zone_graphique=zone_graphique
        
    def dessiner_voiture(self):
        '''Cette méthode dessine la voiture. '''
        self.zone_graphique.create_rectangle(self.x-50, self.y+25, self.x+self.longueur, self.y-50, fill='green')    
        self.zone_graphique.create_oval(self.x, self.y, self.x+self.rayon, self.y+self.rayon, fill='white')
        self.zone_graphique.create_oval(self.x+100, self.y, self.x+self.rayon+100, self.y+self.rayon, fill='white')
        self.zone_graphique.create_rectangle(self.x, self.y-100, self.x+self.longueur-50, self.y-50, fill='lightgreen')
    
    def rouler(self):
        '''Cette méthode permet de donner un mouvement (faire rouler la voiture) à la voiture avec la fonction : animation() .'''
        self.x=self.x+self.vitesse
        if self.x+self.longueur==800 or self.x==0+50 :
            self.vitesse=-self.vitesse

class Oiseau():
    ''' Cette classe dessine un oiseau selon son x , son y et son envergure , de plus elle va lui crée un mouvement avec la vitesse pour l'animation .'''
    
    def __init__(self,x, y,envergure,vitesse,battements,zone_graphique):
        '''Cette méthode est le constructeur des attributs x, y, envergure et vitesse'''
        self.x=x
        self.y=y
        self.envergure=envergure
        self.vitesse=vitesse
        self.battements=battements
        self.zone_graphique=zone_graphique
        
    def dessiner_oiseau(self):
        '''Cette méthode dessine l'oiseau. '''
        self.zone_graphique.create_line(self.x-self.envergure, self.y-self.envergure, self.x+self.envergure, self.y+self.envergure)
        self.zone_graphique.create_line(self.x+self.envergure, self.y+self.envergure, self.x+3*self.envergure, self.y-self.envergure)
    
    def voler(self):
        '''Cette méthode permet de donner un mouvement (faire voler l'oiseau) à l'oiseau avec la fonction : animation() . '''
        self.x=self.x+self.vitesse
        if self.x+50==800 or self.x-20==0:
            self.vitesse=-self.vitesse
            
    def ailes(self):
        '''Cette méthode permet de donner un mouvement de battement d'ailes à l'oiseau avec la fonction : animation() .'''
        self.y=self.y+self.battements
        if self.y+50==300 or self.y==200 :
            self.battements=-self.battements
#╚═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════    
    
# ► Instanciation de la classe Interface

#╔════════════════════
interface=Interface()

interface.instancier()
interface.dessiner()
interface.animation()
#╚════════════════════

# ► Mise à jour de la fenêtre Tkinter

#╔════════════════
fenetre.mainloop()
#╚════════════════
