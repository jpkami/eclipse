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
                 anciens=0, decouverte=False, vaisseaux=None, pointVictoire=0):
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

    def hasCombat(self):
        playerset= set()
        for va in self.vaisseaux:
            playerset.add(va.player)
        if len(playerset) > 1:
            return True
        return False