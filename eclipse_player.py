#from data.Resources import *
import data.Resources as res
import random
import math

pygame=res.pygame
#Classes

    # The Player
class Player():
    
    def __init__(self,tile):
        self.credits= 2
        self.science= 2
        self.materiaux = 2
        self.cubesCredit = 15
        self.cubesScience = 15
        self.cubesMateriaux = 15
        self.disquesInfluence = 15
        self.tuilesCombat= [0]*4
        self.intercepteurs = 0
        self.fregate = 0
        self.croiseur = 0
        self.base_stellaire = 0
        self.hexTable = pygame.sprite.Group()
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
    
    
      
