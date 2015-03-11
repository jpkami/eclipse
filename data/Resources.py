import pygame
import os
import sys
from pygame.locals import *


#Constant of the board of the game
WINDOWWIDTH = 1024
WINDOWHEIGHT =512
CENTERX = round(WINDOWWIDTH/2)
CENTERY = round(WINDOWHEIGHT/2)
HEXMSIZE = round(WINDOWHEIGHT/5)

#Speed of the game constants
FPS = 30
PADDLESPEED = 20

pygame.mixer.pre_init(22050, -16, 2, 1024)
pygame.init()
mainClock = pygame.time.Clock()
#Timers Constants for Power Ups
# TIMER_TICK = USEREVENT +1
BUTTONEVENT = USEREVENT
TILEEVENT = USEREVENT+1
PLAYEREVENT = USEREVENT+2

windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)

pygame.display.set_caption('Eclipse - the Game')


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
WHOLE = pygame.image.load(os.path.join('data','WHole.png')).convert_alpha()
GC = pygame.image.load(os.path.join('data','GC.png')).convert_alpha()
R1 = pygame.image.load(os.path.join('data','R1.png')).convert_alpha()
R2 = pygame.image.load(os.path.join('data','R2.png')).convert_alpha()
BACKGROUND = pygame.image.load(os.path.join('data','galaxy.jpg')).convert()
#Constant Sounds
ALLSOUNDS = []
INTRO = pygame.mixer.Sound(os.path.join('data','Pacman_Intro.wav'))
INTRO.set_volume(0.0)
ALLSOUNDS.append(INTRO)


cubeTable= (28,24,21,18,15,12,10,8,6,4,3,2)
influenceTable = (-30,-25,-21,-17,-10,-7,-5,-3,-2,-1,0,0)
technoReducTable = (0,-1,-2,-3,-4,-6,-8)
technoVPTable = (0,0,0,1,2,3,5)

# pygame.time.set_timer(TIMER_TICK,1000)
displayMenu = False
gameIsPlaying = False
gameInited = False