class Game:
    
    def __init__(self):
        self.players = []
        self.tiles = []
        self.turnNumber = 0
        self.currentplayer = 0
        
    def defineWinner(self):
        print("The winner is:" + str(self.players[self.currentplayer]))
        pass
    
    def numberPlayers(self, *args):
        for player in enumerate(args):
            self.players.append(player)
            
            
    def actionPhase(self):
        # start turn : find first player in players
        for count, player in self.players:
            if True: #player.isfirst():
                self.currentplayer = count
                break
        
        print("first player is " + str(self.players[self.currentplayer]))
        self.passed = 0
        while self.passed != len(self.players):
            print(str(self.players[self.currentplayer]) + "is playing")
            # showInterface, if player passed, show reactions else actions
            action = True  # InterfaceMethod(self.players[self.currentplayer])
            if action == True:  # should check if player passed
                print(str(self.players[self.currentplayer]) + "passed")           
                self.passed += 1
            # when action finished, if all passed end phase, else go to next player
            self.currentplayer = (self.currentplayer + 1) % len(self.players)
        
        
        
        print("all players have passed")
    
    def combatPhase(self):
        print("turn number:" + str(self.turnNumber) + " combatPhase")
        pass
    def maintenancePhase(self):
        print("turn number:" + str(self.turnNumber) + " maintenancePhase")
        pass
    def cleanupPhase(self):
        print("turn number:" +  str(self.turnNumber) + " cleanupPhase")
        pass
    
    # start new game
    def mainGame(self):
        # select number of players
        self.numberPlayers("A", "B", "C")    
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
