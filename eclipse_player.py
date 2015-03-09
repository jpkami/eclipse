#from data.Resources import *
import data.Resources as res
import random
import math

pygame=res.pygame
#Classes

    # The Player
class Player():
    
    def __init__(self,tile):
        self.ressources[0]= 2
        self.ressources[1]= 2
        self.ressources[2] = 2
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
    
    
      
