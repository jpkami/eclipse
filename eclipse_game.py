<<<<<<< HEAD
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
zoomFactor = 1
showMenu = False

def setMenu():
    menuSurface = pygame.Surface((round(res.WINDOWWIDTH/2),(round(res.WINDOWHEIGHT/2))))
    menuSurface.fill(pygame.Color(200,50,50,30))
    menuSurfaceRect = menuSurface.get_rect()
    menuSurfaceRect.centerx = windowSurface.get_rect().centerx
    menuSurfaceRect.centery = windowSurface.get_rect().centery
    
    return (menuSurface,menuSurfaceRect)
    
    
def zoomWindow(direction):
    global zoomFactor
    if direction == "in":
        zoomFactor +=0.1
        # s = pygame.transform.smoothscale(ws,(round(res.WINDOWWIDTH*1.5),round(res.WINDOWHEIGHT*1.5)))
        # gameSurface.fill(res.BLACK)
        # gameSurface.blit(s,windowSurface.get_rect())
        print("zoom in")
    elif direction == "out":
        if zoomFactor>0.2:
            zoomFactor -=0.1
        print("zoom out")
    
    #This function draws everything in the game. 
def drawGame(gameIsPlaying,gameMenu,displayMenu):
    # windowSurface.blit(res.BACKGROUND,windowSurface.get_rect())
    windowSurface.fill(res.BLACK)
    if gameIsPlaying:
        gameSurface.fill(res.BLACK)
        MAP.draw(gameSurface)
        writePopUp(popUpText,gameSurface)
        if showMenu:
            menu = setMenu()
            write("ff Working !",20,menu[0].get_rect().centerx,20,menu[0])
            # writePopUp("Working !",menu[0])
            gameSurface.blit(menu[0],menu[1])
        if zoomFactor != 1:
            s = pygame.transform.smoothscale(gameSurface,(round(res.WINDOWWIDTH*zoomFactor),round(res.WINDOWHEIGHT*zoomFactor)))
            r = s.get_rect()
            r.center=gameSurface.get_rect().center
            gameSurface.fill(res.BLACK)
            gameSurface.blit(s,r)
            # gameSurface.blit(s,gameSurface.get_rect())
        windowSurface.blit(gameSurface,windowSurface.get_rect())
        #print("playing")
    if displayMenu:
        gameMenu.draw(windowSurface)     

    #A function for writing a text with the most basic font
def write(text, fontSize, x, y,s=windowSurface, color=res.WHITE):
    font = pygame.font.SysFont(None, fontSize)
    
    textR = font.render(text, True, color)
    textRect = textR.get_rect()
    textRect.centerx = x
    textRect.centery = y
    s.blit(textR, textRect)

def writePopUp(pu,s=windowSurface):
    write(pu,20,res.WINDOWWIDTH/2,20,s)
    
#def onTimerTick(pad):
#    res.PowerUps.update(True)

#Now the core of the game

def onMouseUp(event):
    global popUpText
    if not res.gameIsPlaying:
        1+1
    elif res.gameIsPlaying:
        if event.button == 4:
            zoomWindow("in")
        elif event.button == 5:
            zoomWindow("out")
            
        elif event.button == 1:
            # popUpText = str(event)
            ecartMax=res.HEXMSIZE
            tMax=None
            for t in MAP.get_sprites_at(event.pos):
                # print("gspat ="+str(t.toString()))
            # for t in MAP:
                if t.rect.collidepoint(event.pos):
                    #print(str(t.x)+" "+str(t.y)+" type = "+str(t.type))
                    ecart = abs(t.rect.centerx-event.pos[0])+abs(t.rect.centery-event.pos[1])
                    #print("rect = "+str(t.rect.centerx-event.pos[0])+","+str(t.rect.centery-event.pos[1])+" ecart = "+str(ecart))
                    if ecart<ecartMax :
                        ecartMax = ecart
                        tMax=t
            if tMax != None:
                if tMax.isInitialised:
                    tMax.rotate(-60)
                    tMax.getConnectedNeighbours(dMAP)
                else:
                    tMax.initTile(dMAP)
                popUpText = str(tMax.x)+" "+str(tMax.y)+" edges = "+str(tMax.edges)+" angle = "+str(tMax.angle)


def onKeyDown(event):
    if not res.gameIsPlaying:
        if event.key == ord('s'):
#             mouseEnabled = False
            res.gameIsPlaying = True
        if event.key == ord('m'):
#             mouseEnabled = True
            res.gameIsPlaying = True
        if event.key == ord('c'):
#             mouseEnabled = False
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
        if event.key == K_l:
            res.gameIsPlaying = True
            global showMenu
            showMenu = not showMenu
    
    
        
        
while True:
    #offset pour centrer les briques
    if not res.gameInited:
        gameMenu = men.GameMenu()
        tmpMAP= emap.setMap()
        MAP=tmpMAP[0]
        dMAP=tmpMAP[1]
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
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                pygame.quit()
                res.sys.exit()
            if event.type == KEYDOWN:
                onKeyDown(event)
            if event.type == KEYUP:
                1+1
            if event.type == MOUSEBUTTONUP:
                #print("mb up")
                print("events"+str(events))
                onMouseUp(event)
                
            if event.type == res.TIMER_TICK:
                1+1
                #print("tick")   
                #onTimerTick(paddle1)
                
        drawGame(res.gameIsPlaying,gameMenu,res.displayMenu)
        

        pygame.display.update()
        mainClock.tick(FPS)

    pygame.display.update()
=======
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
zoomFactor = 1 
showMenu = False

def setMenu():
    menuSurface = pygame.Surface((round(res.WINDOWWIDTH/2),(round(res.WINDOWHEIGHT/2))))
    menuSurface.fill(pygame.Color(200,50,50,30))
    menuSurfaceRect = menuSurface.get_rect()
    menuSurfaceRect.centerx = windowSurface.get_rect().centerx
    menuSurfaceRect.centery = windowSurface.get_rect().centery
    
    return (menuSurface,menuSurfaceRect)
    
    
def zoomWindow(direction):
    global zoomFactor
    if direction == "in":
        zoomFactor +=0.1
        # s = pygame.transform.smoothscale(ws,(round(res.WINDOWWIDTH*1.5),round(res.WINDOWHEIGHT*1.5)))
        # gameSurface.fill(res.BLACK)
        # gameSurface.blit(s,windowSurface.get_rect())
        print("zoom in")
    elif direction == "out":
        if zoomFactor>0.2:
            zoomFactor -=0.1
        print("zoom out")
    
    #This function draws everything in the game. 
def drawGame(gameIsPlaying,gameMenu,displayMenu):
    # windowSurface.blit(res.BACKGROUND,windowSurface.get_rect())
    windowSurface.fill(res.BLACK)
    if gameIsPlaying:
        gameSurface.fill(res.BLACK)
        MAP.draw(gameSurface)
        writePopUp(popUpText,gameSurface)
        if showMenu:
            menu = setMenu()
            write("ff Working !",20,menu[0].get_rect().centerx,20,menu[0])
            # writePopUp("Working !",menu[0])
            gameSurface.blit(menu[0],menu[1])
        if zoomFactor != 1:
            s = pygame.transform.smoothscale(gameSurface,(round(res.WINDOWWIDTH*zoomFactor),round(res.WINDOWHEIGHT*zoomFactor)))
            r = s.get_rect()
            r.center=gameSurface.get_rect().center
            gameSurface.fill(res.BLACK)
            gameSurface.blit(s,r)
            # gameSurface.blit(s,gameSurface.get_rect())
        windowSurface.blit(gameSurface,windowSurface.get_rect())
        #print("playing")
    if displayMenu:
        gameMenu.draw(windowSurface)     

    #A function for writing a text with the most basic font
def write(text, fontSize, x, y,s=windowSurface, color=res.WHITE):
    font = pygame.font.SysFont(None, fontSize)
    
    textR = font.render(text, True, color)
    textRect = textR.get_rect()
    textRect.centerx = x
    textRect.centery = y
    s.blit(textR, textRect)

def writePopUp(pu,s=windowSurface):
    write(pu,20,res.WINDOWWIDTH/2,20,s)
    
#def onTimerTick(pad):
#    res.PowerUps.update(True)

#Now the core of the game

def onMouseUp(event):
    global popUpText
    if not res.gameIsPlaying:
        1+1
    elif res.gameIsPlaying:
        if event.button == 4:
            zoomWindow("in")
        elif event.button == 5:
            zoomWindow("out")
            
        elif event.button == 1:
            # popUpText = str(event)
            ecartMax=res.HEXMSIZE
            tMax=None
            for t in MAP.get_sprites_at(event.pos):
                # print("gspat ="+str(t.toString()))
            # for t in MAP:
                if t.rect.collidepoint(event.pos):
                    #print(str(t.x)+" "+str(t.y)+" type = "+str(t.type))
                    ecart = abs(t.rect.centerx-event.pos[0])+abs(t.rect.centery-event.pos[1])
                    #print("rect = "+str(t.rect.centerx-event.pos[0])+","+str(t.rect.centery-event.pos[1])+" ecart = "+str(ecart))
                    if ecart<ecartMax :
                        ecartMax = ecart
                        tMax=t
            if tMax != None:
                if tMax.isInitialised:
                    tMax.rotate(-60)
                    tMax.getConnectedNeighbours(dMAP)
                else:
                    tMax.initTile(dMAP)
                popUpText = str(tMax.x)+" "+str(tMax.y)+" edges = "+str(tMax.edges)+" angle = "+str(tMax.angle)


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
        if event.key == K_l:
            res.gameIsPlaying = True
            global showMenu
            showMenu = not showMenu
    
    
        
        
while True:
    #offset pour centrer les briques
    if not res.gameInited:
        gameMenu = men.GameMenu()
        tmpMAP= emap.setMap()
        MAP=tmpMAP[0]
        dMAP=tmpMAP[1]
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
>>>>>>> branch 'master' of https://github.com/jpkami/eclipse.git
    mainClock.tick(FPS)
