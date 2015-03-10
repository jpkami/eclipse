'''
Created on 10 mars 2015

@author: Jean Ph
'''
import unittest
import eclipse_map as emap

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testName(self):
        MAP = emap.setMap()
        for t in MAP[0]:
            print(t.toString())
        for x in MAP[1]:
            print(str(x))
        
        emap.initMapForPlayers(MAP[1], 3)    
        tm = emap.TileM(0,0)
        tm = MAP[1][(0,0)]
        tm.initTile()
        tm = MAP[1][(1,1)]

        tm.initTile()
        tm.getConnectedNeighbours(MAP[1])
        tm.rotate(-60)
        tm.getConnectedNeighbours(MAP[1])
        
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()