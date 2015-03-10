class Spaceship:
    
    def __init__(self,player,model,spaceshipType="",tile=None):
        canons = []
        missiles = []
        init=0
        precision=0
        bouclier=0
        vie=0
        deplacement=0
        energie=0
        prix=0
        for amelio in model:
            if amelio.type == "canon":
                canons.append(amelio.degats)
            elif amelio.type == "missile":
                missiles.append(amelio.degats)  
            elif amelio.type == "base":
                prix = amelio.prix
            energie += amelio.energie
            init += amelio.init
            precision += amelio.precision
            bouclier += amelio.bouclier
            vie += amelio.vie
            deplacement += amelio.deplacement
        
        self.tile = tile
        self.isSlowedDown = False
        self.player = player
        self.canons =  canons
        self.missiles =  missiles
        self.init = init
        self.precision = precision
        self.bouclier = bouclier
        self.vie = vie
        self.deplacement = deplacement
        self.energie = energie
        self.type = spaceshipType
        self.prix = prix
        
    def move(self):
        pass
    
    def attack(self):
        pass
    
    def improve(self):
        pass
    
class Intercepteur(Spaceship):
     
    def __init__(self,player,tile):    
        Spaceship.__init__(self,player,spaceshipType="Intercepteur",model=player.modeleIntercepteur)
    
    
class Fregate(Spaceship):
    
    def __init__(self,player,tile):
        Spaceship.__init__(self,player,spaceshipType="Fregate",model=player.modeleFregate)
    
    
class Croiseur(Spaceship):
    
    def __init__(self):
        pass
    
    
class BaseStellaire(Spaceship):
    
    def __init__(self):
        pass