'''
Created on 9 mars 2015

@author: Jean Ph
'''

#from data.Resources import *
import data.Resources as res
import eclipse_map as emap
import eclipse_menu as men
import time
import random
pygame=res.pygame
windowSurface = res.windowSurface
mainClock = res.mainClock
FPS = res.FPS
from pygame.locals import *
MAP = pygame.sprite.Group()
#Functions
popUpText =""
gameSurface = windowSurface.copy()

def write(text, fontSize, x, y,s=windowSurface, color=res.WHITE):
    font = pygame.font.SysFont(None, fontSize)
    
    textR = font.render(text, True, color)
    textRect = textR.get_rect()
    textRect.centerx = x
    textRect.centery = y
    s.blit(textR, textRect)
    
def manageEvent(event):
    if event.type == QUIT:
        pygame.quit()
        res.sys.exit()
    if event.type == KEYDOWN:
        onKeyDown(event)
    if event.type == MOUSEBUTTONUP:
        onMouseUp(event)

def onMouseUp(event):
    print(str(allSprites.get_sprites_at(event.pos)))
    
def onKeyDown(event):
    pass

def drawGame():
    pass

def drawMenu():
    gameMenu.draw(windowSurface)

def drawHome():
    write('ECLIPSE', 120, res.WINDOWWIDTH/2, res.WINDOWHEIGHT/4)
    write('A new Dawn for the Galaxy', 100, res.WINDOWWIDTH/2, res.WINDOWHEIGHT/2) 
    b= men.Button(res.WINDOWWIDTH/2,3*res.WINDOWHEIGHT/4,100,50)
    b.writecenter("start", 20, res.BLACK)
    if b not in allSprites:
        allSprites.add(b)
    allSprites.draw(windowSurface)
    write('press s to start', 40, res.WINDOWWIDTH/2, res.WINDOWHEIGHT-40)

def initGame():
    pass

while True:
    if not res.gameInited:
        gameMenu = men.GameMenu()
        tmpMAP= emap.setMap()
        MAP=tmpMAP[0]
        dMAP=tmpMAP[1]
        res.gameInited = True
        gameIsPlaying = False
        menuIsShowing = False
        allSprites = pygame.sprite.LayeredUpdates()
    
    for event in pygame.event.get():
        manageEvent(event)
    
    if gameIsPlaying:
        drawGame()        
    elif menuIsShowing:
        drawMenu()
    else:
        drawHome()
        
    pygame.display.update()
    mainClock.tick(FPS)