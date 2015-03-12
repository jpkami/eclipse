'''
Created on 11 mars 2015

@author: charles
'''
import unittest
from eclipse_game import Game
from eclipse_research import sacDeTechnologies
from eclipse_player import HegemonieOrion, Human
from eclipse_tile import Tile
from eclipse_spaceship import Intercepteur
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
        print("starting test of defineWinner")
        self.eg.defineWinner()
        print("end of test of defineWinner")
        
    def test_startCombat(self):
        print("starting test of startOfCombat")
        self.eg.tiles.append(Tile(tileId=200))
        self.eg.tiles.append(Tile(tileId=201))
        self.eg.tiles.append(Tile(tileId=202))
        
        print(self.eg.nbPlayers)
        print(len(self.eg.tiles))
        v1=Intercepteur(player=self.eg.players[0],tile=self.eg.tiles[0])
        v2=Intercepteur(player=self.eg.players[1],tile=self.eg.tiles[0])
        v3=Intercepteur(player=self.eg.players[0],tile=self.eg.tiles[1])
        v4=Intercepteur(player=self.eg.players[1],tile=self.eg.tiles[1])
        v5=Intercepteur(player=self.eg.players[0],tile=self.eg.tiles[2])
        v6=Intercepteur(player=self.eg.players[0],tile=self.eg.tiles[2])
        self.eg.tiles[0].vaisseaux.append(v1)
        self.eg.tiles[2].vaisseaux.append(v2)
        self.eg.tiles[1].vaisseaux.append(v3)
        self.eg.tiles[1].vaisseaux.append(v4)
        self.eg.tiles[2].vaisseaux.append(v5)
        self.eg.tiles[2].vaisseaux.append(v6)
        listTiles = self.eg.startOfCombat()
#         for tile in listTiles:
#             print(tile.id)
            
        self.assertTrue(len(listTiles) == 2)
        self.assertTrue(listTiles[0].id == 202)
        self.assertTrue(listTiles[1].id == 201)
        self.eg.tiles.clear()
        print("end of test of startOfCombat")

    def testDrawTechnologies(self):
        
        print("start of test of DrawTechnologies")
        self.eg.drawTechnologies()
        self.assertTrue(len(self.eg.availableTechnologies) == 4)
        print("available techs: ")
        for tech in self.eg.availableTechnologies:
            print(tech.name)
            
        print("remaining techs in sacDeTechno: ")
        for tech in sacDeTechnologies:
            print(tech.name)
        
        print("end of test of DrawTechnologies")

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
