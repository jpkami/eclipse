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
        pass


    def tearDown(self):
        pass


    def test_player_setup(self):
        
        joueur = HegemonieOrion()
        print(joueur.flotte[0].type)
        print(joueur.flotte[0].canons)
        self.assertTrue(joueur.flotte[0].type == "Fregate")
        
        joueur = Human()
        print(joueur.flotte[0].type)
        print(joueur.flotte[0])
        print(joueur.flotte[0].prix)
        
        self.assertTrue(joueur.flotte[0].type == "Intercepteur")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()