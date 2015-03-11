# from data.Resources import *
import data.Resources as res
import random
import math
from eclipse_spaceship import Spaceship, Intercepteur, Fregate
from eclipse_amelioration import *
from eclipse_map import TileM
from eclipse_research import BaseStellaire, BouclierGauss, BombeNeutron
from eclipse_tile import Tile

pygame = res.pygame
# Classes

    # The Player
class Player():
    
    def __init__(self, playerCredits=2, science=2, materiaux=2, cubesCredit=11, cubesScience=11, cubesMateriaux=11,
                 disquesInfluence=16, modeleIntercepteur=[CanonPlasma()], tiles=[],
                 modeleFregate=[CanonPlasma()], modeleCroiseur=[CanonPlasma()], modeleBaseStellaire=[CanonPlasma()],
                 flotte=[], prixIntercepteur=2, prixFregate=4, prixCroiseur=8, maxMove=3, maxBuild=2, maxImprove=2,
                 maxColons=3, maxReputationCombat=4, tauxChange=2, maxExplore=1, maxRecherche=1, technoInitiales=[]):
        
        self.credits = playerCredits
        self.science = science
        self.materiaux = materiaux
        self.cubesCredit = cubesCredit
        self.cubesScience = cubesScience
        self.cubesMateriaux = cubesMateriaux
        self.disquesInfluence = disquesInfluence
        self.tiles = tiles
        self.tuilesCombat = []
        
        self.intercepteurs = 8
        self.fregate = 4
        self.croiseur = 2
        self.base_stellaire = 4 
        
        self.tuilesAmbassadeur = 4
        
        self.prixIntercepteur = prixIntercepteur
        self.prixFregate = prixFregate
        self.prixCroiseur = prixCroiseur
        
        self.modeleIntercepteur = modeleIntercepteur
        self.modeleFregate = modeleFregate
        self.modeleCroiseur = modeleCroiseur
        self.modeleBaseStellaire = modeleBaseStellaire        
        
        self.flotte = flotte
        
        self.maxMove = maxMove
        self.maxBuild = maxBuild
        self.maxImprove = maxImprove
        self.maxColons = maxColons
        self.maxReputationCombat = maxReputationCombat
        self.tauxChange = tauxChange
        self.maxExplore = maxExplore
        self.maxRecherche = maxRecherche
        self.technoInitiales = technoInitiales
        
        self.hasPassed = False
        pass
    
    def newTurn(self):
        self.hasPassed = False
        pass
    
    def addHex(self, hexM):
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
    
    def build(self, what, where):
        if what.type == "Orbitale" or  what.type == "Monolithe" :
            pass
        else :
            what.tile = where
            self.flotte.append(what) 
    
    def move(self):
        pass
    
    def playerPass(self):
        self.hasPassed = True
        pass
    
    def canBuild(self, what):
        return what.prix <= self.materiaux
      
class Human(Player):
    def __init__(self,tileId=221):
        Player.__init__(self, technoInitiales=[BaseStellaire()]) 
        self.tiles = [Tile(tileId=tileId)]
        self.modeleIntercepteur = [BaseIntercepteurHumain(), CanonPlasma(), Vide(), Vide()]
        
        self.flotte = [Intercepteur(player=self, tile=self.tiles[0])]

class HegemonieOrion(Player):
    def __init__(self, tile=None):
        Player.__init__(self, maxReputationCombat=5, maxMove=2, tauxChange=4, playerCredits=3,
                        science=3, materiaux=5, technoInitiales=[BouclierGauss(), BombeNeutron()])
        self.modeleFregate = [CanonPlasma(), CanonPlasma()]
        # TODO modeles
        self.tiles = [Tile(tileId=232)]
        self.flotte = [Fregate(player=self, tile=self.tiles[0])]
