from eclipse_player import Human, HegemonieOrion
from random import randint
from eclipse_research import sacDeTechnologies
from eclipse_tile import Tile
class Game:
    
    def __init__(self):
        self.players = []
        self.tiles = []
        self.turnNumber = 0
        
        self.phase = "action"
        
        self.availableTechnologies = []
    
    def endOfInit(self):
        self.nbPlayers = len(self.players)
        if self.nbPlayers == 2:
            self.remove=4
        else:
            self.remove=self.nbPlayers+3
                
    def endOfAction(self):
        numberOfPlayersThatHavePassed = 0
        for player in self.players:
            if player.hasPassed:
                numberOfPlayersThatHavePassed += 1
        if numberOfPlayersThatHavePassed == len(self.players):
            self.phase = "combat"
        else : 
            self.currentplayer = self.players[(self.players.index(self.currentplayer) + 1) % len(self.players)]
        return self.phase, self.currentplayer
            
    def startOfCombat(self):
        """return all the tiles where there is a combat, in the correct order"""
        #check all the tiles, and see which have ships and put them in combats
        self.combats=[]
        for tile in self.tiles:
            if tile.hasCombat():
                self.combats.append(tile)
        #sort according to id
        
        self.combats.sort(key=lambda tile:tile.id, reverse=True)
        return self.combats
        
    def actionPhase(self):
        # start turn : find first player in players
        self.currentplayer = self.firstPlayer
        
        print("first player is " + str(self.currentplayer))
        self.passed = 0
        while self.passed != len(self.players):
            print(str(self.currentplayer) + "is playing")
            # showInterface, if player passed, show reactions else actions
            action = randint(0, 1)  # InterfaceMethod(self.currentplayer)
            if action == 0:  # should check if player passed
                print(str(self.currentplayer) + "passed")
                if self.passed == 0:  # next actionPhase, the first player will be this one
                    self.firstPlayer = self.currentplayer   
                if self.currentplayer.hasPassed == False:
                    print(str(self.currentplayer) + " first time pass")             
                    self.currentplayer.hasPassed = True         
                    self.passed += 1
            # when action finished, if all passed end phase, else go to next player
            self.currentplayer = self.players[(self.players.index(self.currentplayer) + 1) % len(self.players)]
        
        
        
        print("all players have passed")
    
    def combatPhase(self):
        
        print("turn number:" + str(self.turnNumber) + " combatPhase")
        pass
    def maintenancePhase(self):
        print("turn number:" + str(self.turnNumber) + " maintenancePhase")
        pass
    def cleanupPhase(self):
        print("turn number:" + str(self.turnNumber) + " cleanupPhase")
        # tirez nouvelles tuiles techno
        self.drawTechnologies()
        # chaque joueur reprend les disques influence, les cubes du cimetiere, 
        # retourne les vaisseaux de colons et carte résumé
        for player in self.players:
            player.hasPassed = False
            pass
            pass
        # nouveau tour
        self.turnNumber += 1
        self.combats.clear()
    
    def drawTechnologies(self):
        for i in range(0, self.remove):
            size = len(sacDeTechnologies)
            rand = randint(0,size-1)
            techno = sacDeTechnologies[rand]
            self.availableTechnologies.append(techno)
            del sacDeTechnologies[rand]
    
    def defineWinner(self):
        #count victory points
        self.LeaderBoard = []
        for i,player in enumerate(self.players):
            self.LeaderBoard.append(("joueur "+str(i),player.computeScore()))
        self.LeaderBoard.sort(key=lambda tup: tup[1],reverse=True)
        for play in self.LeaderBoard:
            print(str(play)) 
        print("The winner is:" + str(self.LeaderBoard[0]))
        pass
    
    def numberPlayers(self, *args):
        for player in args:
            self.players.append(player)
        self.currentplayer = self.players[0]
        self.firstPlayer = self.players[0]        
            
    def addPlayers(self, player):
        self.players.append(player)
        self.currentplayer = self.players[0]
        self.firstPlayer = self.players[0]        
            
    # start new game
    def mainGame(self):
        # select number of players
        self.numberPlayers(Human(), HegemonieOrion())  
        self.endOfInit()  
        # choose race for each player
        # callmethodfromengine()
        # start turns
        while self.turnNumber < 9:
            self.actionPhase()
            self.combatPhase()
            self.maintenancePhase()
            self.cleanupPhase()
            
            
        
        self.defineWinner()
