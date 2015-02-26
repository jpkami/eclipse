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

    
    #This function draws everything in the game. 
def drawGame(gameIsPlaying,gameMenu,displayMenu):
    windowSurface.blit(res.BACKGROUND,windowSurface.get_rect())
    
    if gameIsPlaying:
        MAP.draw(windowSurface)
        writePopUp(popUpText)
        #print("playing")
    if displayMenu:
        gameMenu.draw(windowSurface)     

    #A function for writing a text with the most basic font
def write(text, fontSize, x, y, color=res.WHITE):
    font = pygame.font.SysFont(None, fontSize)
    
    textR = font.render(text, True, color)
    textRect = textR.get_rect()
    textRect.centerx = x
    textRect.centery = y
    windowSurface.blit(textR, textRect)

def writePopUp(pu):
    write(pu,20,res.WINDOWWIDTH/2,20)
    
#def onTimerTick(pad):
#    res.PowerUps.update(True)

#Now the core of the game

def onMouseUp(event):
    if not res.gameIsPlaying:
        1+1
    elif res.gameIsPlaying:
        ecartMax=res.HEXMSIZE
        tMax=None
        for t in MAP:
            if t.rect.collidepoint(event.pos):
                #print(str(t.x)+" "+str(t.y)+" type = "+str(t.type))
                ecart = abs(t.rect.centerx-event.pos[0])+abs(t.rect.centery-event.pos[1])
                #print("rect = "+str(t.rect.centerx-event.pos[0])+","+str(t.rect.centery-event.pos[1])+" ecart = "+str(ecart))
                if ecart<ecartMax :
                    ecartMax = ecart
                    tMax=t
        if tMax != None:
            tMax.rotate(60)
            global popUpText
            popUpText = str(tMax.x)+" "+str(tMax.y)+" edges = "+str(tMax.edges)+" angle = "+str(tMax.angle)
            #writePopUp(txt)
            #print(txt)

def onKeyDown(event):
    if not res.gameIsPlaying:
        if event.key == ord('s'):
            mouseEnabled = False
            res.gameIsPlaying = True
        if event.key == ord('m'):
            mouseEnabled = True
            res.gameIsPlaying = True
        if event.key == ord('c'):
            mouseEnabled = False
            res.gameIsPlaying = True
        if event.key == K_p:
            res.gameIsPlaying = True
            res.displayMenu = False
            
    elif res.gameIsPlaying:
        if event.key == K_ESCAPE or event.key == ord('a'):
            res.gameIsPlaying = False
        if event.key == K_p:
            res.gameIsPlaying = False
            res.displayMenu = True
    
    
        
        
while True:
    #offset pour centrer les briques
    if not res.gameInited:
        gameMenu = men.GameMenu()
        MAP= emap.setMap()
        res.gameInited = True
    #if not pygame.mixer.Channel(1).get_busy():
        #pygame.mixer.Channel(1).play(INTRO)
    #This is the "menu"
    while not res.gameIsPlaying:
        for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    res.sys.exit()
                if event.type == KEYDOWN:
                    onKeyDown(event)
                if event.type == KEYUP:
                    if event.key == ord('q'):
                        pygame.quit()
                        res.sys.exit()
        

        drawGame(res.gameIsPlaying,gameMenu,res.displayMenu)
        if not res.displayMenu:
            write('Press s', 120, res.WINDOWWIDTH/4, res.WINDOWHEIGHT/2)
            write('to play!', 120, 3*res.WINDOWWIDTH/4, res.WINDOWHEIGHT/2) 
            
            #write('Press m', 60, res.WINDOWWIDTH/4, res.WINDOWHEIGHT/2+60)
            #write('for mouse control', 60, 3*res.WINDOWWIDTH/4, res.WINDOWHEIGHT/2+60)

            write('Press q', 60, 3*res.WINDOWWIDTH/8, 3*res.WINDOWHEIGHT/4)
            write('to quit.', 60, 5*res.WINDOWWIDTH/8, 3*res.WINDOWHEIGHT/4)
            
            #write('c = AI', 60, res.WINDOWWIDTH - 85, res.WINDOWHEIGHT/4)

        pygame.display.update()
        mainClock.tick(FPS)
        
    #This is the game playing
    while res.gameIsPlaying:
    
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                res.sys.exit()
            if event.type == KEYDOWN:
                onKeyDown(event)
            if event.type == KEYUP:
                1+1
            if event.type == MOUSEBUTTONUP:
                #print("mb up")
                onMouseUp(event)
                
            if event.type == res.TIMER_TICK:
                1+1
                #print("tick")   
                #onTimerTick(paddle1)
                
        drawGame(res.gameIsPlaying,gameMenu,res.displayMenu)
        

        pygame.display.update()
        mainClock.tick(FPS)

    pygame.display.update()
    mainClock.tick(FPS)