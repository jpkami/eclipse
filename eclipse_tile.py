'''
Created on 10 mars 2015

@author: charles
'''
from builtins import set

class Tile(object):
    '''
    classdocs
    '''


    def __init__(self, tileId=0, casesScience=0, casesMateriaux=0, casesCredits=0, casesGrises=0,
                 casesScienceAvance=0, casesMateriauxAvance=0, casesCreditsAvance=0, orbitale=False, monolithe=False,
                 anciens=0, decouverte=False, vaisseaux=None, pointVictoire=0,artefact=False):
        '''
        Constructor
        '''
        self.id = tileId
        self.casesScience = casesScience
        self.casesScienceAvance = casesScienceAvance
        self.casesMateriaux = casesMateriaux
        self.casesMateriauxAvance = casesMateriauxAvance
        self.casesCredits = casesCredits
        self.casesCreditsAvance = casesCreditsAvance
        self.casesGrises = casesGrises
        self.orbitale = orbitale
        self.monolithe = monolithe
        self.vaisseaux = vaisseaux if vaisseaux is not None else []
        self.anciens = anciens
        self.pointVictoire = pointVictoire
        self.decouverte = decouverte
        self.artefact = artefact
        self.isSet = False

    def hasCombat(self):
        playerset= set()
        for va in self.vaisseaux:
            playerset.add(va.player)
        if len(playerset) > 1:
            return True
        return False
    
    def setTile(self,tileM):
        self.tileM = tileM
        self.isSet = True
    
class StartingTile(Tile):
    
    def __init__(self,tileId):
        Tile.__init__(self, tileId, casesScience=1, casesMateriaux=1, casesCredits=1, casesScienceAvance=1, casesCreditsAvance=1, pointVictoire=3, artefact=True)
        
    
class CenterOfGalaxy(Tile):
    
    def __init__(self):
        Tile.__init__(self,tileId="001", casesScience=1,casesCredits=1, casesScienceAvance=1,casesCreditsAvance=1,casesGrises=2,decouverte=True,pointVictoire=4,artefact=True)
#         self.    