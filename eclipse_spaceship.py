class Spaceship:
    
    def __init__(self,player,spaceshipType="",model):
        
        canons = []
        missiles = []
        init=0
        precision=0
        bouclier=0
        vie=0
        deplacement=0
        energie=0
        for amelio in model:
            if amelio.type == "canon":
                canons.append(amelio.degats)
            elif amelio.type == "missile":
                missiles.append(amelio.degats)            
            energie += amelio.energie
            init += amelio.init
            precision += amelio.precision
            bouclier += amelio.bouclier
            vie += amelio.vie
            deplacement += amelio.deplacement    
        
        self.isSlowedDown = False
        self.player = player
        self.type = type
        self.canons =  canons
        self.missiles =  missiles
        self.init = init
        self.precision = precision
        self.bouclier = bouclier
        self.vie = vie
        self.deplacement = deplacement
        self.energie = energie
        self.Type = spaceshipType
    
    def move(self):
        pass
    
    def attack(self):
        pass
    
    def improve(self):
        pass
    
class Intercepteur(Spaceship):
     
    def __init__(self,player):    
        Spaceship.__init__(self,player,"Intercepteur",player.modeleIntercepteur)
    
    
class Fregate(Spaceship):
    
    def __init__(self,player):
        Spaceship.__init__(self,player,"Fregate",player.modeleIntercepteur)
    
    
class Croiseur(Spaceship):
    
    def __init__(self):
        pass
    
    
class BaseStellaire(Spaceship):
    
    def __init__(self):
        pass