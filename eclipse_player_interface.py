'''
Created on 10 mars 2015

@author: Jean Ph
'''
import pygame
import data.Resources as res
import os

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
        self.rect = pygame.Rect((0,0),(sRect.w,round(sRect.h/8)))
        self.image = pygame.surface.Surface((self.rect.w,self.rect.h))
        self.image.fill((45,45,100))
#         self.image.set_alpha(80)
        self.setPortrait("player1")
    
    def setPortrait(self,image):
        tmpPortrait = self.loadimage(image)
        tmpRect = tmpPortrait.get_rect()
        tmpW = round(self.rect.h*tmpRect.w/tmpRect.h)
        resizedPortrait = pygame.transform.smoothscale(tmpPortrait,(tmpW,self.rect.h))
        resizedRect = resizedPortrait.get_rect()
        resizedRect.topleft = (0,0)
        self.image.blit(resizedPortrait, resizedRect)
        pass
    
    def loadimage(self,name):
        return pygame.image.load(os.path.join('data',name+'.png')).convert_alpha()
        
    def onClick(self):
        pass