'''
Created on 9 mars 2015

@author: Jean Ph
'''

class Research():
    '''
    classdocs
    Class for research tiles
    '''
    name = ""
    cost = ""
    maxReducedCost = ""
    #0:military, 1:advanced, 2:nano
    type = 0

    def __init__(self, name,type, cost,maxRC):
        '''
        Constructor
        '''
        self.name = name
        self.type = type
        self.cost = cost
        self.maxReducedCost = maxRC
    