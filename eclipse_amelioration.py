'''
Created on 10 mars 2015

@author: charles
'''

class Amelioration:
    '''
    classdocs
    '''


    def __init__(self, init=0, precision=0, bouclier=0, vie=0, deplacement=0, energie=0, ameliotype="", degats=0):
        '''
        Constructor
        '''
        self.init = init
        self.precision = precision
        self.bouclier = bouclier
        self.vie = vie
        self.deplacement = deplacement
        self.energie = energie
        self.type = ameliotype
        self.degats = degats


class CanonPlasma(Amelioration):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        Amelioration.__init__(self, ameliotype="canon", degats=2, energie=-2)
    
    
    
    
