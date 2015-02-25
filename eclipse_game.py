#from data.Resources import *
import data.Resources as res
import eclipse_classes as cla
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

    # return a list with the rect to draw, drawn later with drawGame()
def setMap(w=7,h=9):
    if w%2==0:
        w+=1
    if h%2==0:
        h+=1
    rectList = pygame.sprite.Group()
    for x in range(-round(w/2),round(w/2)+1,2):
        for y in range(-round(h/2),round(h/2)+1,2):
            print("x= "+str(x)+" y= "+str(y))
            rectList.add(cla.TileM(0,x,y))
    
    for x in range(1-round(w/2),round(w/2),2):
        for y in range(1-round(h/2),round(h/2),2):
            print("x= "+str(x)+" y= "+str(y))
            rectList.add(cla.TileM(0,x,y))
                
    return rectList
    
    #This function draws everything in the game. 
def drawGame(gameIsPlaying,gameMenu,displayMenu):
    windowSurface.blit(res.BACKGROUND,windowSurface.get_rect())
    
    if gameIsPlaying:
        MAP.draw(windowSurface)
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

#def onTimerTick(pad):
#    res.PowerUps.update(True)

#Now the core of the game

while True:
    #offset pour centrer les briques
    if not res.gameInited:
        gameMenu = men.GameMenu()
        MAP=setMap()
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
                    if event.key == ord('s'):
                        mouseEnabled = False
                        res.gameIsPlaying = True
                    if event.key == ord('m'):
                        mouseEnabled = True
                        res.gameIsPlaying = True
                    if event.key == ord('c'):
                        paddle1 = cla.AI(res.WINDOWWIDTH/2 - 40, res.WINDOWHEIGHT - 35, 80, 15)
                        mouseEnabled = False
                        res.gameIsPlaying = True
                    if event.key == K_p:
                        res.gameIsPlaying = True
                        res.displayMenu = False
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
                if event.key == K_ESCAPE or event.key == ord('a'):
                    res.gameIsPlaying = False
                if event.key == K_p:
                    res.gameIsPlaying = False
                    res.displayMenu = True
            if event.type == KEYUP:
                print("up")
            if event.type == MOUSEBUTTONUP:
                #print("mb up")
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
                    print(str(tMax.x)+" "+str(tMax.y)+" type = "+str(tMax.type))
                
            if event.type == res.TIMER_TICK:
                1+1
                #print("tick")   
                #onTimerTick(paddle1)
                
        drawGame(res.gameIsPlaying,gameMenu,res.displayMenu)


        pygame.display.update()
        mainClock.tick(FPS)

    pygame.display.update()
    mainClock.tick(FPS)