#from data.Resources import *
#import data.Resources as res
import random
import math
from eclipse_spaceship import Spaceship, Intercepteur, Fregate
from eclipse_amelioration import *
#from eclipse_map import TileM

#pygame=res.pygame
#Classes

    # The Player
class Player():
    
    def __init__(self,tile,playerCredits=2,science=2,materiaux=2,cubesCredit=11,cubesScience=11,cubesMateriaux=11,
                 disquesInfluence=16):
        self.credits= playerCredits
        self.science= science
        self.materiaux = materiaux
        self.cubesCredit = cubesCredit
        self.cubesScience = cubesScience
        self.cubesMateriaux = cubesMateriaux
        self.disquesInfluence = disquesInfluence
        self.tuilesCombat= [0]*4
        self.intercepteurs = 8
        self.fregate = 4
        self.croiseur = 2
        self.base_stellaire = 4 
        self.tuilesAmbassadeur = 3
#        self.hexTable = pygame.sprite.Group()
#        self.hexTable.add(tile)
        self.modeleIntercepteur = [CanonPlasma()]
        self.modeleFregate = [CanonPlasma()]
        self.modeleCroiseur = []
        self.modeleBaseStellaire = []
        
        
        self.flotte = []
        self.flotte.append(Intercepteur(player=self))
        self.hasPassed =False
        pass
    
    def newTurn(self):
        self.hasPassed = False
        pass
    
    def addHex(self,hexM):
        self.hexTable.add(hexM)
        pass
        
    def explore(self):
        pass
    
    def influence(self):
        pass
    
    def research(self):
        pass
    
    def upgrade(self):
        pass
    
    def build(self):
        pass
    
    def move(self):
        pass
    
    def playerPass(self):
        self.hasPassed = True
        pass
    
    
      
class Human(Player):
    def __init__(self,tile):
        Player.__init__(self, tile) 

class HegemonieOrion(Player):
    def __init__(self):
        Player.__init__(self, None)
        del(self.flotte[-1])
        self.flotte.append(Fregate(player=self)) 
    
    def move(self):#TODO override
        Player.move(self)