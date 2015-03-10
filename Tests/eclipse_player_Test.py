'''
Created on 10 mars 2015

@author: charles
'''
import unittest
import eclipse_player
from eclipse_player import HegemonieOrion

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_player_setup(self):
        
        joueur = HegemonieOrion()
        print(joueur.flotte[0])


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()