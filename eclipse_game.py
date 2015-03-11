from eclipse_player import Human, HegemonieOrion
from random import randint
from eclipse_research import sacDeTechnologies
class Game:
    
    def __init__(self):
        self.players = []
        self.tiles = []
        self.turnNumber = 0
        
        self.phase = "action"
        
        self.availableTechnologies = []
    
            
    def endOfAction(self):
        numberOfPlayersThatHavePassed = 0
        for player in self.players:
            if player.hasPassed():
                numberOfPlayersThatHavePassed += 1
        if numberOfPlayersThatHavePassed == len(self.players):
            self.phase = "Combat"
        else : 
            self.currentplayer = self.players[(self.players.index(self.currentplayer) + 1) % len(self.players)]
        return self.phase, self.currentplayer
            
    
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
        
        # chaque joueur reprend les disques influence, les cubes du cimetiere, 
        # retourne les vaisseaux de colons et carte résumé
        for player in self.players:
            player.hasPassed = False
        
        # nouveau tour
        self.turnNumber += 1
    
    def drawTechnologies(self, nbPlayers):
        if nbPlayers == 2:
            remove=4
        else:
            remove=nbPlayers+3
        
        for i in range(0, remove):
            size = len(sacDeTechnologies)
            rand = randint(0,size-1)
            techno = sacDeTechnologies[rand]
            self.availableTechnologies.append(techno)
            del sacDeTechnologies[rand]
    
    def defineWinner(self):
        print("The winner is:" + str(self.currentplayer))
        pass
    
    def numberPlayers(self, *args):
        for player in args:
            self.players.append(player)
        self.currentplayer = self.players[0]
        self.firstPlayer = self.players[0]        
            
    
    # start new game
    def mainGame(self):
        # select number of players
        self.numberPlayers(Human(), HegemonieOrion())    
        # choose race for each player
        # callmethodfromengine()
        # start turns
        while self.turnNumber < 9:
            self.actionPhase()
            self.combatPhase()
            self.maintenancePhase()
            self.cleanupPhase()
            
            
        
        self.defineWinner()
