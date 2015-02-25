#from data.Resources import *
import data.Resources as res
import random
import math

pygame=res.pygame
#Classes

class GameScore:
    val = 0
    def __init__(self,val):
        self.val=val
        
class Animation(pygame.sprite.Sprite):
    fullImage = 0
    fullX = 0
    fullY = 0
    nbIt = 0
    nbImage = 16
    def __init__(self,filename,dest,nbImage=16):
        pygame.sprite.Sprite.__init__(self)
        self.fullImage = pygame.image.load(filename).convert()
        self.rect = dest
        self.nbImage = nbImage
        #TODO :
        self.fullX = self.fullImage.get_rect().w
        self.fullY = self.fullImage.get_rect().h
        self.image = pygame.Surface((self.fullX/self.nbImage,self.fullY))
        self.image.blit(self.fullImage,self.image.get_rect(),pygame.Rect(0,0,self.fullX/self.nbImage,self.fullY))
        self.image = pygame.transform.smoothscale(self.image,(self.rect.w,self.rect.h))
        self.image.set_colorkey(res.BLACK)    
    def update(self):
        if self.nbIt < self.nbImage:
            tmpImage = pygame.Surface((self.fullX/self.nbImage,self.fullY))
            tmpImage.blit(self.fullImage,pygame.Rect(0,0,self.fullX/self.nbImage,self.fullY),
                pygame.Rect(self.nbIt*self.fullX/self.nbImage,0,self.fullX/self.nbImage,self.fullY))
            self.image = pygame.transform.smoothscale(tmpImage,(self.rect.w,self.rect.h))
            self.image.set_colorkey(res.BLACK)            
            self.nbIt +=1
        else:
            self.kill()
    
    def setCoord(self,x,y):
        self.rect.centerx = x
        self.rect.centery = y
        
    # The Tile for Map
class TileM(pygame.sprite.Sprite):
    type=0
    h=round(res.HEXMSIZE*math.sqrt(3)/2)
    w=res.HEXMSIZE
    texture = pygame.transform.smoothscale(res.WHEX,(w,h))
    x=0
    y=0
    def __init__(self,type,x,y):
        pygame.sprite.Sprite.__init__(self)
        
        if y%2==0:
            self.l=res.CENTERX+self.w*3*x/4-self.w/2
            self.t=res.CENTERY+self.h*y/2-self.h/2
        else:
            self.l=res.CENTERX+self.w*3*x/4-self.w/2
            self.t=res.CENTERY+self.h*y/2-self.h/2
     
        self.rect = pygame.Rect(self.l,self.t,self.w,self.h)
        self.x = x
        self.y = y
        # TODO: type a specifier au moment de la creation de la map ... et verifier les cas particulliers
        self.type=abs(x)+abs(y)
        if self.type==2 and abs(x)%2==0 and x !=0:
            self.type+=2
        
        if abs(x)>2 and self.type == 4:
            self.type+=4
        
        if self.type==0:
            self.image= pygame.transform.smoothscale(res.GC,(self.w,self.h))
        elif self.type==2 :
            self.image = pygame.transform.smoothscale(res.R1,(self.w,self.h))
        elif self.type==4 :
            self.image = pygame.transform.smoothscale(res.R2,(self.w,self.h))
        else :
            self.image = self.texture
        print(str(self.rect))
        
    def kill (self):
        pygame.sprite.Sprite.kill(self)
        
        
        # res.BOOM.play()
        # a = Animation(res.os.path.join('data','explosion.png'),self,16)
