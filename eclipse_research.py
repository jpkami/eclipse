'''
Created on 9 mars 2015

@author: Jean Ph
'''

class Research():
    '''
    classdocs
    Class for research tiles
    '''
    def __init__(self, name,ResearchType, cost,maxRC):
        '''
        Constructor
        '''
        self.name = name
        self.type = type
        self.cost = cost
        self.maxReducedCost = maxRC
    
class BombeNeutron(Research):
    def __init__(self):
        Research.__init__(self, "BombeNeutron", "Militaire", 2, 2)

class BouclierGauss(Research):
    def __init__(self):
        Research.__init__(self, "BouclierGauss", "Avancee", 2, 2)
            
class BaseStellaire(Research):
    def __init__(self):
        Research.__init__(self, "BaseStellaire", "Militaire", 4, 3)
        
                
sacDeTechnologies=[BombeNeutron(),BouclierGauss(),BaseStellaire(),BaseStellaire(),
                   BouclierGauss(),BouclierGauss(),BouclierGauss(),BouclierGauss(),
                   BouclierGauss(),BouclierGauss(),BouclierGauss()]
        