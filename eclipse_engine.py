'''
Created on 9 mars 2015

@author: Jean Ph
'''

#from data.Resources import *
import data.Resources as res
import eclipse_map as emap
import eclipse_menu as men
import eclipse_combat_interface as combat
import eclipse_player_interface as epintf
import eclipse_player as eplayer
import eclipse_game as g
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
game = g.Game()
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
    if event.type == res.BUTTONEVENT:
        onButtonEvent(event)
    if event.type == res.TILEEVENT:
        onTileEvent(event)
    if event.type == res.PLAYEREVENT:
        onPlayerEvent(event)
    
def onKeyDown(event):
    global gameIsPlaying
    global menuIsShowing
    global combatIsShowing
    if event.key==pygame.K_DELETE:
        pygame.quit()
        res.sys.exit()    
    if event.key == pygame.K_h:
        gameIsPlaying = False
        menuIsShowing = False
        combatIsShowing = False
        
    if event.key == pygame.K_j:        
        gameIsPlaying = False
        combatIsShowing = True
        menuIsShowing = False
    pass

def onMouseUp(event):
#     print(str(allHomeSprites.get_sprites_at(event.pos)))
    clickedSprites = None
    if not gameIsPlaying and not menuIsShowing:
        clickedSprites = allHomeSprites.get_sprites_at(event.pos)
    elif gameIsPlaying:
        clickedSprites = allMapSprites.get_sprites_at(event.pos)
    
    if len(clickedSprites)>0:
        clickedSprites[-1].onClick()
       
def onButtonEvent(event):
#         print(str(event))
    if event.chMenu == "playerSelect":
        initHome(homeSurface, 1)
    if isinstance(event.chMenu, int):
        pl = (eplayer.Human(111,(45,45,100)),eplayer.Human(111,res.RED),eplayer.Human(111,res.GREEN),eplayer.Human(111,res.YELLOW))
        l = emap.initMapForPlayers(dMAP, event.chMenu)
        for p in range(event.chMenu):
            print(str(l[p]))
            pl[p].tiles.append(l[p])
            allMapSprites.add(l[p].planetTable)
            print(str(allMapSprites))
            game.addPlayers(pl[p])
#             game.numberPlayers(eplayer.Human(111,(45,45,100)),eplayer.Human(111,res.RED),eplayer.Human(111,res.GREEN))
        
        allMapSprites.remove(intf.items)
        intf.setPlayer(pl[0])
        allMapSprites.add(intf.items)
        global gameIsPlaying
        gameIsPlaying = True
        
def onTileEvent(event):
    if isinstance(event.tile, emap.TileM):
            if event.canRotate:
                event.tile.rotate(-60)
#                 event.tile.setdMap(dMAP)
#                 event.tile.highlightPossibleNeighbours()
            if "selected" in event.__dict__:
                if event.selected:
                    event.tile.initTile()
                    for t in MAP:
                        if isinstance(t, emap.TileM) and t is not event.tile:
                            t.restore()
                    pygame.event.post(pygame.event.Event(res.PLAYEREVENT, {"action":"endOfAction"}))
            else:
#                 event.tile.highlight()
                pass

def onPlayerEvent(event): 
    if "action" in event.__dict__:
        if event.action == "pass":
            event.player.hasPassed = True
            pygame.event.post(pygame.event.Event(res.PLAYEREVENT, {"action":"endOfAction"}))
        if event.action =="explore":
            print(str(event.player.tiles))
            for t in event.player.tiles:
                t.highlightPossibleNeighbours()
            
#             pygame.event.post(pygame.event.Event(res.PLAYEREVENT, {"action":"endOfAction"}))
        print("action = "+str(event.action))
        
        if event.action == "endOfAction":
            result = game.endOfAction()
            
            if result[0] =="action":
                allMapSprites.remove(intf.getItems())
                intf.setPlayer(result[1])
                allMapSprites.add(intf.getItems())
    else:
        pass

def drawGame():
    gameSurface.fill(res.BLACK)
#     MAP.draw(gameSurface)
    allMapSprites.draw(gameSurface)
    windowSurface.blit(gameSurface,gameSurface.get_rect())
#     allHomeSprites.draw(gameSurface)

def drawMenu():
    gameMenu.draw(windowSurface)

def drawCombat():
        
    gameCombat.draw(windowSurface)
    gameCombat.items.draw(windowSurface)
    
def drawHome():
    windowSurface.blit(homeSurface,homeSurface.get_rect())
    allHomeSprites.draw(homeSurface)

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
        allHomeSprites.add(b)
    if player>0:
        allHomeSprites.empty()
        b2 = men.Button(res.WINDOWWIDTH/4,3*res.WINDOWHEIGHT/4+50,50,50,"2",10,res.RED, res.BLACK)
        b2.setFunction({"chMenu":2})
        allHomeSprites.add(b2)
        b3 = men.Button(2*res.WINDOWWIDTH/4,3*res.WINDOWHEIGHT/4+50,50,50,"3",10,res.RED, res.BLACK)
        b3.setFunction({"chMenu":3})
        allHomeSprites.add(b3)
        b4 = men.Button(3*res.WINDOWWIDTH/4,3*res.WINDOWHEIGHT/4+50,50,50,"4",10,res.RED, res.BLACK)
        b4.setFunction({"chMenu":4})
        allHomeSprites.add(b4)
        write('select the number of players', 40, res.WINDOWWIDTH/2, 3*res.WINDOWHEIGHT/4,homeSurface)

while True:
    if not res.gameInited:
        gameMenu = men.GameMenu()
        gameCombat = combat.CombatInterface()
        tmpMAP= emap.setMap()
        MAP=tmpMAP[0]
        dMAP=tmpMAP[1]
        res.gameInited = True
        gameIsPlaying = False
        menuIsShowing = False    
        combatIsShowing = False       
        gameSurface = windowSurface.copy()
        menuSurface = windowSurface.copy()
        combatSurface = windowSurface.copy()
        homeSurface = windowSurface.copy()
        allHomeSprites = pygame.sprite.LayeredUpdates()
        allCombatSprites = pygame.sprite.LayeredUpdates()
        allMapSprites = MAP
#         print(str(allMapSprites.sprites())) 
        intf = epintf.PlayerInterface(gameSurface)
        allMapSprites.add(intf) 
#         print(str(intf.getItems().sprites())) 
#         allMapSprites.add(intf.getItems())
        initHome(homeSurface)
    
    for event in pygame.event.get():
        manageEvent(event)
    
    if gameIsPlaying:
        drawGame()        
    elif menuIsShowing:
        drawMenu()
    elif combatIsShowing:
        drawCombat()
    else:
        drawHome()
        
    pygame.display.update()
    mainClock.tick(FPS)