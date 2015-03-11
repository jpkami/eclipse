'''
Created on 10 mars 2015

@author: Jean Ph
'''
import data.Resources as res
import os
from math import floor, ceil

pygame = res.pygame
class PlayerButton(pygame.sprite.Sprite):
    '''
    classdocs
    '''

    def __init__(self, x,y,surface,color=res.WHITE,factor=(1,1)):
        '''
        Constructor
        '''
        pygame.sprite.Sprite.__init__(self)
        bSize = round(surface.get_rect().h/3)
        self.rect = pygame.Rect((x,y),(round(factor[0]*bSize),round(factor[1]*bSize)))
        self.defaultImage = pygame.surface.Surface((self.rect.w,self.rect.h))
        self.color = color
        self.defaultImage.fill(color)
        self.image = self.defaultImage.copy()
        self.event = pygame.event.Event(res.PLAYEREVENT, {"button":self})
    
    def setText(self,text,fontcolor=res.BLACK):
        self.image=self.defaultImage.copy()
        font = pygame.font.SysFont('helvetica', 30)
        textR = font.render(text, True, fontcolor)
        textRect = textR.get_rect()
        textRect.center = (self.rect.w/2,self.rect.h/2)
#         self.menuSurface.blit(textR, textRect) 
#         print("bsettext : "+text)
        self.image.blit(textR, textRect)
    
    def setImage(self,image):
        tmpImage = self.loadimage(image)
        resizedImage = pygame.transform.smoothscale(tmpImage,(self.rect.w,self.rect.h))
        self.defaultImage = resizedImage
        self.image = self.defaultImage.copy()
        
        pass
    
    def loadimage(self,name):
        return pygame.image.load(os.path.join('data',name+'.png')).convert_alpha()
    
    def setFunction(self,args):
        self.event = pygame.event.Event(res.PLAYEREVENT, args)
        
    
    def onClick(self):
        pygame.event.post(self.event)
        
        
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
#         self.setPortrait("player1")
#         self.setRessources()
#         self.setCubes()
    
    def setPlayer(self,player):
        self.player = player
#         self.setPortrait("player1")
#         print(str(self.items))
        self.items.empty()
        self.setPortrait(player.portrait, self.player.color)
        self.setRessources((self.player.credits,self.player.science,self.player.materiaux))
        self.setCubes((self.player.cubesCredit,self.player.cubesScience,self.player.cubesMateriaux))
        self.setActionsButtons()
        self.setReactionsButtons()
        self.setPassButtons()
        print("player set : "+str(self.player.cubesCredit))
    
    def setPortrait(self,image,color=(45,45,100)):
        tmpPortrait = self.loadimage(image)
        tmpRect = tmpPortrait.get_rect()
        tmpW = round(self.rect.h*tmpRect.w/tmpRect.h)
        resizedPortrait = pygame.transform.smoothscale(tmpPortrait,(tmpW,self.rect.h))
        resizedRect = resizedPortrait.get_rect()
        resizedRect.topleft = (0,0)
        self.image.fill(color)
        self.portrait = resizedPortrait
        self.image.blit(resizedPortrait, resizedRect)
        self.portraitOffset = tmpW+5
        
    def setRessources(self,args=(0,0,0)):
        bc = PlayerButton(self.portraitOffset,0,self.image,(235,110,0))
        bc.setImage("resC")
        bc.setText(str(args[0]))
        print("credit = "+str(args[0]))
        self.items.add(bc)
        bs = PlayerButton(self.portraitOffset,bc.rect.h,self.image,(240,170,180))
        bs.setImage("resS")
        print("science = "+str(args[1]))
        bs.setText(str(args[1]))
        self.items.add(bs)
        bm = PlayerButton(self.portraitOffset,2*bc.rect.h,self.image,(145,80,45))
        bm.setImage("resM")
        print("materiaux = "+str(args[2]))
        bm.setText(str(args[2]))
        self.items.add(bm)
        self.ResOffset = bs.rect.w +5
        
        
        
    def setCubes(self,args=(0,0,0)):
        bc = PlayerButton(self.portraitOffset+self.ResOffset,0,self.image,(235,110,0))
        bc.setText(str(res.cubeTable[args[0]])+"/"+str(res.cubeTable[args[0]-1]))
        self.items.add(bc)
        bs = PlayerButton(self.portraitOffset+self.ResOffset,bc.rect.h,self.image,(240,170,180))
        bs.setText(str(res.cubeTable[args[1]])+"/"+str(res.cubeTable[args[1]-1]))
        self.items.add(bs)
        bm = PlayerButton(self.portraitOffset+self.ResOffset,2*bc.rect.h,self.image,(145,80,45))
        bm.setText(str(res.cubeTable[args[2]])+"/"+str(res.cubeTable[args[2]-1]))
        self.items.add(bm)    
    
    def setPassButtons(self):
        bp = PlayerButton(self.rect.w-3*(self.ResOffset-5),0,self.image,res.WHITE,(3,1))
        bp.setText("PASS")
        bp.setFunction({"button":self,"action":"pass","player":self.player})
        self.items.add(bp)
    
    def setReactionsButtons(self):
        bp = PlayerButton(self.rect.w-3*(self.ResOffset-5),0,self.image,res.WHITE,(3,1))
        br = PlayerButton(self.rect.w-3*(self.ResOffset-5),bp.rect.h,self.image,(130,130,130),(3,1))
        br.setText("REACTION",res.BLACK)
        self.items.add(br)
        br.setFunction({"button":self,"action":"none"})
        bra = PlayerButton(self.rect.w-3*(self.ResOffset-5),2*bp.rect.h,self.image)
        bra.setFunction({"button":self,"action":"Rupgrade","player":self.player})
        bra.setImage("rupg")
        self.items.add(bra)
        
        brc = PlayerButton(self.rect.w-2*(self.ResOffset-5),2*bp.rect.h,self.image)
        brc.setFunction({"button":self,"action":"Rconstruct","player":self.player})
        brc.setImage("Rcon")
        self.items.add(brc)
        brm = PlayerButton(self.rect.w-brc.rect.w,2*bp.rect.h,self.image)
        brm.setFunction({"button":self,"action":"Rmove","player":self.player})
        brm.setImage("rmov")
        self.items.add(brm)
        
    
    def setActionsButtons(self):
        bp = PlayerButton(0,0,self.image)
        be = PlayerButton(self.rect.w-round(7.5*bp.rect.w)-5,0,self.image,factor=(1.5,1.5))
        be.setImage("exp")
        be.setFunction({"button":self,"action":"explore","player":self.player})
        self.items.add(be)
        bi = PlayerButton(self.rect.w-round(6*bp.rect.w)-5,0,self.image,factor=(1.5,1.5))
        bi.setImage("inf")
        bi.setFunction({"button":self,"action":"influence","player":self.player})
        self.items.add(bi)
        bu = PlayerButton(self.rect.w-round(4.5*bp.rect.w)-5,0,self.image,factor=(1.5,1.5))
        bu.setImage("upg")
        bu.setFunction({"button":self,"action":"upgrade","player":self.player})
        self.items.add(bu)
        
        br = PlayerButton(self.rect.w-round(7.5*bp.rect.w)-5,bu.rect.h,self.image,factor=(1.5,1.5))
        br.setImage("res")
        br.setFunction({"button":self,"action":"research","player":self.player})
        self.items.add(br)
        bc = PlayerButton(self.rect.w-round(6*bp.rect.w)-5,bu.rect.h,self.image,factor=(1.5,1.5))
        bc.setImage("cons")
        bc.setFunction({"button":self,"action":"construct","player":self.player})
        self.items.add(bc)
        bm = PlayerButton(self.rect.w-round(4.5*bp.rect.w)-5,bu.rect.h,self.image,factor=(1.5,1.5))
        bm.setImage("mov")
        bm.setFunction({"button":self,"action":"move","player":self.player})
        self.items.add(bm)
        pass
        
    def getItems(self):
        return self.items
        
    def loadimage(self,name):
        return pygame.image.load(os.path.join('data',name+'.png')).convert_alpha()
        
    def onClick(self):
        pass