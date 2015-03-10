'''
Created on 10 mars 2015

@author: Jean Ph
'''
import pygame
import data.Resources as res
import os
from math import floor, ceil

class PlayerButton(pygame.sprite.Sprite):
    '''
    classdocs
    '''

    def __init__(self, x,y,surface,color):
        '''
        Constructor
        '''
        pygame.sprite.Sprite.__init__(self)
        bSize = round(surface.get_rect().h/3)
        self.rect = pygame.Rect((x,y),(bSize*2,bSize))
        self.image = pygame.surface.Surface((self.rect.w,self.rect.h))
        self.color = color
        self.image.fill(color)
        self.defaultImage = self.image.copy()
        self.event = pygame.event.Event(res.PLAYEREVENT, {"button":self})
    
    def setText(self,text):
        font = pygame.font.SysFont('helvetica', 30)
        textR = font.render(text, True, res.BLACK)
        textRect = textR.get_rect()
        textRect.center = (self.rect.w/2,self.rect.h/2)
#         self.menuSurface.blit(textR, textRect) 
   
        self.image.blit(textR, textRect)
    
    def setImage(self,image):
        tmpImage = self.loadimage(image)
        resizedImage = pygame.transform.smoothscale(tmpImage,(self.rect.w,self.rect.h))
        self.image = resizedImage
        self.defaultImage = self.image.copy()
        
        pass
    
    def loadimage(self,name):
        return pygame.image.load(os.path.join('data',name+'.png')).convert_alpha()
    
    def setFunction(self,args):
        self.event = pygame.event.Event(res.PLAYEREVENT, args)
        
    
    def onClick(self):
        pygame.event.post(self.event)
        self.image=self.defaultImage.copy()
        self.setText("clique")
        print("button clicked : color = "+str(self.color))
        
        
class PlayerInterface(pygame.sprite.Sprite):
    '''
    classdocs
    '''


    def __init__(self, windowSurface):
        '''
        Constructor
        '''
        pygame.sprite.Sprite.__init__(self)
        sRect = windowSurface.get_rect()
        self.rect = pygame.Rect((0,0),(sRect.w,round(sRect.h/6)))
        self.image = pygame.surface.Surface((self.rect.w,self.rect.h))
        self.image.fill((45,45,100))
        
        self.items = pygame.sprite.Group()
#         self.image.set_alpha(80)
        self.setPortrait("player1")
        self.setRessources()
        self.setCubes()
    
    def setPlayer(self,player):
        self.player = player
#         self.setPortrait("player1")
#         self.items.empty()
        self.setRessources((self.player.credits,self.player.science,self.player.materiaux))
        self.setCubes((self.player.cubesCredit,self.player.cubesScience,self.player.cubesMateriaux))
        print("player set : "+str(self.player.cubesCredit))
    
    def setPortrait(self,image):
        tmpPortrait = self.loadimage(image)
        tmpRect = tmpPortrait.get_rect()
        tmpW = round(self.rect.h*tmpRect.w/tmpRect.h)
        resizedPortrait = pygame.transform.smoothscale(tmpPortrait,(tmpW,self.rect.h))
        resizedRect = resizedPortrait.get_rect()
        resizedRect.topleft = (0,0)
        self.portrait = resizedPortrait
        self.image.blit(resizedPortrait, resizedRect)
        self.portraitOffset = tmpW+5
        
    def setRessources(self,args=(0,0,0)):
        bc = PlayerButton(self.portraitOffset,0,self.image,(235,110,0))
        bc.setImage("resC")
        bc.setText(str(args[0]))
        self.items.add(bc)
        bs = PlayerButton(self.portraitOffset,bc.rect.h,self.image,(240,170,180))
        bs.setImage("resS")
        bs.setText(str(args[1]))
        self.items.add(bs)
        bm = PlayerButton(self.portraitOffset,2*bc.rect.h,self.image,(145,80,45))
        bm.setImage("resM")
        bm.setText(str(args[2]))
        self.items.add(bm)
        self.ResOffset = bs.rect.w +5
        
        
        
    def setCubes(self,args=(0,0,0)):
        bc = PlayerButton(self.portraitOffset+self.ResOffset,0,self.image,(235,110,0))
        bc.setText(str(args[0]))
        self.items.add(bc)
        bs = PlayerButton(self.portraitOffset+self.ResOffset,bc.rect.h,self.image,(240,170,180))
        bs.setText(str(args[1]))
        self.items.add(bs)
        bm = PlayerButton(self.portraitOffset+self.ResOffset,2*bc.rect.h,self.image,(145,80,45))
        bm.setText(str(args[2]))
        self.items.add(bm)    
        
    def getItems(self):
        return self.items
        
    def loadimage(self,name):
        return pygame.image.load(os.path.join('data',name+'.png')).convert_alpha()
        
    def onClick(self):
        pass