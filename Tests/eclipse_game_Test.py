'''
Created on 11 mars 2015

@author: charles
'''
import unittest
from eclipse_game import Game
from eclipse_research import sacDeTechnologies

class Test(unittest.TestCase):

    def setUp(self):
        self.eg = Game()



    def testEclipse_game(self):
#         self.eg.mainGame()
        pass
    
    def testDrawTechnologies(self):
        self.eg.drawTechnologies(2)
        self.assertTrue(len(self.eg.availableTechnologies) == 4)
        print("available techs: ")
        for tech in self.eg.availableTechnologies:
            print(tech.name)
            
        print("remaining techs in sacDeTechno: ")
        for tech in sacDeTechnologies:
            print(tech.name)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()