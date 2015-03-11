'''
Created on 11 mars 2015

@author: charles
'''
import unittest
from eclipse_game import Game
from eclipse_research import sacDeTechnologies
from eclipse_player import HegemonieOrion, Human
class Test(unittest.TestCase):

    def setUp(self):
        self.eg = Game()
        self.eg.addPlayers(Human())
        self.eg.addPlayers(HegemonieOrion())
        self.eg.endOfInit()

    def testEclipse_game(self):
#         self.eg.mainGame()
        pass
    
    def test_defineWinner(self):
        self.eg.defineWinner()

    def testDrawTechnologies(self):
        self.eg.drawTechnologies()
        self.assertTrue(len(self.eg.availableTechnologies) == 4)
        print("available techs: ")
        for tech in self.eg.availableTechnologies:
            print(tech.name)
            
        print("remaining techs in sacDeTechno: ")
        for tech in sacDeTechnologies:
            print(tech.name)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
