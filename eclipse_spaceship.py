class Spaceship:
    
    def __init__(self,_type=None, _vitesse=0,_caseAmelioration=[],_player=None):
        self.isSlowedDown = False
        self.casesAmelioration = _caseAmelioration   
        self.player = _player
        self.vitesse =  _vitesse
        self.type = _type
    
    def move(self):
        pass
    
    def attack(self):
        pass
    
    def improve(self):
        pass
    
class Intercepteur(Spaceship):
    
    def __init__(self):
        pass
    
    
class Fregate(Spaceship):
    
    def __init__(self):
        pass
    
    
class Croiseur(Spaceship):
    
    def __init__(self):
        pass
    
    
class BaseStellaire(Spaceship):
    
    def __init__(self):
        pass