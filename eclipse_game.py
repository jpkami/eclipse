from eclipse_player import Human,HegemonieOrion
from random import randint

class Game:
    
    def __init__(self):
        self.players = []
        self.tiles = []
        self.turnNumber = 0
        
    def defineWinner(self):
        print("The winner is:" + str(self.currentplayer))
        pass
    
    def numberPlayers(self, *args):
        for player in args:
            self.players.append(player)
        self.currentplayer = self.players[0]
        self.firstPlayer = self.players[0]        
            
    def actionPhase(self):
        # start turn : find first player in players
        self.currentplayer = self.firstPlayer
        
        print("first player is " + str(self.currentplayer))
        self.passed = 0
        while self.passed != len(self.players):
            print(str(self.currentplayer) + "is playing")
            # showInterface, if player passed, show reactions else actions
            action = randint(0,1)  # InterfaceMethod(self.currentplayer)
            if action == 0:  # should check if player passed
                print(str(self.currentplayer) + "passed")
                if self.passed == 0: # next actionPhase, the first player will be this one
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
        print("turn number:" +  str(self.turnNumber) + " cleanupPhase")
        for player in self.players:
            player.hasPassed = False
        pass
    
    # start new game
    def mainGame(self):
        # select number of players
        self.numberPlayers(Human(),HegemonieOrion())    
        # choose race for each player
        # callmethodfromengine()
        # start turns
        while self.turnNumber < 9:
            self.actionPhase()
            self.combatPhase()
            self.maintenancePhase()
            self.cleanupPhase()
            
            self.turnNumber += 1
        
        self.defineWinner()
