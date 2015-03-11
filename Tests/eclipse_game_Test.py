'''
Created on 11 mars 2015

@author: charles
'''
import unittest
from eclipse_game import Game

class Test(unittest.TestCase):


    def testEclipse_game(self):
        eg = Game()
        eg.mainGame()
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()