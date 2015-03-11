'''
Created on 10 mars 2015

@author: charles
'''
import unittest
import eclipse_player
from eclipse_player import HegemonieOrion, Human
from tkinter import Place

class Test(unittest.TestCase):


    def setUp(self):
        self.joueur = Human()


    def tearDown(self):
        pass


    def test_player_setup(self):
        
        joueur = HegemonieOrion()
#         print(joueur.flotte[0].type)
#         print("joueur.maxmove " +str(joueur.maxMove))
#         print("joueur.tuilescombat " +str(joueur.tuilesCombat))
#         print("joueur.maxreputcombat " +str(joueur.maxReputationCombat))
#         print("joueur.science " +str(joueur.science))
        
        self.assertTrue(joueur.flotte[0].type == "Fregate")
        
        joueur = Human()
#         print(joueur.flotte[0].type)
#         print(joueur.flotte[0])
#         print(joueur.flotte[0].prix)
        
        self.assertTrue(joueur.flotte[0].type == "Intercepteur")

    def test_computeScore(self):
        print(self.joueur.computeScore())
        self.assertTrue(self.joueur.computeScore() == 0)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()