import pygame
import os
import sys
from pygame.locals import *

#Constant of the board of the game
WINDOWWIDTH = 1024
WINDOWHEIGHT = 768
CENTERX = round(WINDOWWIDTH/2)
CENTERY = round(WINDOWHEIGHT/2)
SIZESIDES = 10
BRICKSIZE = 30
HEXMSIZE = round(WINDOWHEIGHT/5)

#Speed of the game constants
FPS = 30
PADDLESPEED = 20

pygame.mixer.pre_init(22050, -16, 2, 1024)
pygame.init()
mainClock = pygame.time.Clock()
#Timers Constants for Power Ups
TIMER_TICK = USEREVENT +1
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)

pygame.display.set_caption('Running_window')
#Rects of the board of the game
TOPSIDE = pygame.Rect(0, 0, WINDOWWIDTH, SIZESIDES)
BOTTOMSIDE = pygame.Rect(0, WINDOWHEIGHT - SIZESIDES, WINDOWWIDTH, SIZESIDES) 

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DKBLUE = (0, 0, 128)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)

#Constant Surfaces
WHEX = pygame.image.load(os.path.join('data','wHex.png')).convert_alpha()
GC = pygame.image.load(os.path.join('data','GC.png')).convert_alpha()
R1 = pygame.image.load(os.path.join('data','R1.png')).convert_alpha()
R2 = pygame.image.load(os.path.join('data','R2.png')).convert_alpha()
WBRICK = pygame.image.load(os.path.join('data','whiteBrick.png')).convert()
RBRICK = pygame.image.load(os.path.join('data','redBrick.png')).convert()
GBRICK = pygame.image.load(os.path.join('data','greenBrick.png')).convert()
YBRICK = pygame.image.load(os.path.join('data','yellowBrick.png')).convert()
CBRICK = pygame.image.load(os.path.join('data','cyanBrick.png')).convert()
BACKGROUND = pygame.image.load(os.path.join('data','galaxy.jpg')).convert()
PADDLE = pygame.image.load(os.path.join('data','pad.png')).convert()
PADDLE.set_colorkey(BLACK)
#Constant Sounds
ALLSOUNDS = []
INTRO = pygame.mixer.Sound(os.path.join('data','Pacman_Intro.wav'))
INTRO.set_volume(0.0)
ALLSOUNDS.append(INTRO)
BONG = pygame.mixer.Sound(os.path.join('data','bong.wav'))
BONG.set_volume(0.0)
ALLSOUNDS.append(BONG)
BOOM = pygame.mixer.Sound(os.path.join('data','Explosion1.wav'))
BOOM.set_volume(0.0)
ALLSOUNDS.append(BOOM)
SPLASH = pygame.mixer.Sound(os.path.join('data','Splash.wav'))
SPLASH.set_volume(0.0)
ALLSOUNDS.append(SPLASH)
POWERUP = pygame.mixer.Sound(os.path.join('data','Powerup.wav'))
POWERUP.set_volume(0.0)
ALLSOUNDS.append(POWERUP)

#These are used to print the scores
LEVEL =[
'''       
       
       
       
       
       
   W   ''',
'''       
       
       
       
       
       
   Y   ''',
'''RRRRRRR
 WWWWW 
 W   W 
 W G W 
 W G W 
 W   W 
WWWWWWW''',
'''RRRRRRR
 WWWWW 
RW   WR
 W G W 
GW G WG
 WGGGW 
RRRRRRR'''
]

ExplGroup = pygame.sprite.Group()
Balls = pygame.sprite.Group()
PowerUps = pygame.sprite.Group()
Shots = pygame.sprite.Group()
LvlNum = 0
class GameScore:
    val = 0
    def __init__(self,val):
        self.val=val
        
Score = GameScore(0)
pygame.time.set_timer(TIMER_TICK,1000)
displayMenu = False
gameIsPlaying = False
gameInited = False