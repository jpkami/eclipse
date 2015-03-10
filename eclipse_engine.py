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
from test.test_typechecks import Integer
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
    
def manageEvent(event,dMap):
    if event.type == QUIT:
        pygame.quit()
        res.sys.exit()
    if event.type == KEYDOWN:
        onKeyDown(event)
    if event.type == MOUSEBUTTONUP:
        onMouseUp(event)
    if event.type == res.BUTTONEVENT:
        print(str(event))
        if event.chMenu == "playerSelect":
            initHome(homeSurface, 1)
        if isinstance(event.chMenu, int):
            if event.chMenu == 2:
                dMAP[(0,4)].initTile(dMap)
                dMAP[(0,-4)].initTile(dMap)
            elif event.chMenu == 3:
                dMAP[(0,4)].initTile(dMap)
                dMAP[(2,-2)].initTile(dMap)
                dMAP[(-2,-2)].initTile(dMap)
            elif event.chMenu == 4:
                dMAP[(2,2)].initTile(dMap)
                dMAP[(-2,2)].initTile(dMap)
                dMAP[(2,-2)].initTile(dMap)
                dMAP[(-2,-2)].initTile(dMap)
            
            global gameIsPlaying
            gameIsPlaying = True
#             print("nbJoueur = "+str(event.chMenu))
        

def onMouseUp(event):
#     print(str(allSprites.get_sprites_at(event.pos)))
    clickedSprites = allSprites.get_sprites_at(event.pos)
    if len(clickedSprites)>0:
        clickedSprites[-1].onClick()
    
def onKeyDown(event):
    if event.key==pygame.K_DELETE:
        pygame.quit()
        res.sys.exit()    
    if event.key == pygame.K_s:
        global gameIsPlaying
        gameIsPlaying = True
    pass

def drawGame():
    gameSurface.fill(res.BLACK)
    MAP.draw(gameSurface)
    windowSurface.blit(gameSurface,gameSurface.get_rect())
#     allSprites.draw(gameSurface)

def drawMenu():
    gameMenu.draw(windowSurface)

def drawHome():
    windowSurface.blit(homeSurface,homeSurface.get_rect())
    allSprites.draw(homeSurface)

def initGame(gameSurface):
    pass

def initHome(homeSurface,player = 0):
    homeSurface.fill(res.BLACK)
    write('ECLIPSE', 120, res.WINDOWWIDTH/2, res.WINDOWHEIGHT/4,homeSurface)
    write('A new Dawn for the Galaxy', 100, res.WINDOWWIDTH/2, res.WINDOWHEIGHT/2,homeSurface)
#     b= men.Button(res.WINDOWWIDTH/2,3*res.WINDOWHEIGHT/4,100,50)
#     b.writecenter("start", 20, res.BLACK)
#     b.onClick = lambda x="":print("c'est la fonction lambda qui est cliquee")
    if player == 0:
        b= men.Button(res.WINDOWWIDTH/2,3*res.WINDOWHEIGHT/4,100,50,"start", 20,res.BLUE, res.BLACK)
        b.setFunction({"chMenu":"playerSelect"})
        allSprites.add(b)
    if player>0:
        allSprites.empty()
        b2 = men.Button(res.WINDOWWIDTH/4,3*res.WINDOWHEIGHT/4+50,50,50,"2",10,res.RED, res.BLACK)
        b2.setFunction({"chMenu":2})
        allSprites.add(b2)
        b3 = men.Button(2*res.WINDOWWIDTH/4,3*res.WINDOWHEIGHT/4+50,50,50,"3",10,res.RED, res.BLACK)
        b3.setFunction({"chMenu":3})
        allSprites.add(b3)
        b4 = men.Button(3*res.WINDOWWIDTH/4,3*res.WINDOWHEIGHT/4+50,50,50,"4",10,res.RED, res.BLACK)
        b4.setFunction({"chMenu":4})
        allSprites.add(b4)
        write('select the number of players', 40, res.WINDOWWIDTH/2, 3*res.WINDOWHEIGHT/4,homeSurface)
    
dMap = None
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
        gameSurface = windowSurface.copy()
        menuSurface = windowSurface.copy()
        homeSurface = windowSurface.copy()
        initHome(homeSurface)
    
    for event in pygame.event.get():
        manageEvent(event,dMap)
    
    if gameIsPlaying:
        drawGame()        
    elif menuIsShowing:
        drawMenu()
    else:
        drawHome()
        
    pygame.display.update()
    mainClock.tick(FPS)