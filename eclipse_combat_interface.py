'''
Created on 12 mars 2015

@author: charles
'''
from eclipse_player_interface import PlayerButton
import data.Resources as res
pygame = res.pygame
class CombatInterface(pygame.sprite.Sprite):
    CombatSurface = None
    def __init__(self):
#         
#         pygame.sprite.Sprite.__init__(self)
#         sRect = windowSurface.get_rect()
#         self.rect = pygame.Rect((0,0),(sRect.w,round(sRect.h/6)))
#         self.image = pygame.surface.Surface((self.rect.w,self.rect.h))
#         self.image.fill((45,45,100))
#         
#         self.items = pygame.sprite.Group()

        pygame.sprite.Sprite.__init__(self)
        self.surface = pygame.Surface((abs(res.WINDOWWIDTH*7/8),abs(res.WINDOWHEIGHT*7/8)))
        self.surface.fill(res.RED)
        self.surface.set_alpha(200)
        self.rect = self.surface.get_rect()
        self.rect.centerx = pygame.display.get_surface().get_rect().centerx
        self.rect.centery = pygame.display.get_surface().get_rect().centery
        
        self.items = pygame.sprite.Group()
        
        bp = PlayerButton(self.rect.w/3,0,self.surface,res.WHITE,(3,1))
        br = PlayerButton(self.rect.w/3,bp.rect.h,self.surface,(130,130,130),(3,1))
        br.setText("Combaaaaat",res.BLACK)
        self.items.add(br)
        br.setFunction({"button":self,"action":"none"})
        
    
    
    def initInterface(self):
        1+1
    
    def setSFXVolume(self,vol):
        for sound in res.ALLSOUNDS:
            sound.set_volume(vol)
    
    def write(self, text, fontSize, x, y, color=res.WHITE):
        font = pygame.font.SysFont('helvetica', fontSize)
        textR = font.render(text, True, color)
        textRect = textR.get_rect()
        textRect.centerx = x
        textRect.centery = y
        self.surface.blit(textR, textRect)
    
    def draw(self,surface):
        
        surface.blit(self.surface,self.rect)