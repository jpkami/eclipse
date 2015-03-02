#from data.Resources import *
import data.Resources as res
import random
import math
import os

pygame=res.pygame
HexW = res.HEXMSIZE
HexH = round(HexW*math.sqrt(3/4))

# coordonees dans le rectangle des centre des cotes + l'angle
#     0
#     __
#  5 /  \ 1
#  4 \__/ 2
#     3
# a cause de pygame, la rotation differente de 90° fait un agrandissement
# theorie : edgesCenter = [(round(HexW/2),0,0), (round(7*HexW/8),round(HexH/4),-60), (round(7*HexW/8),round(3*HexH/4),-120), (round(HexW/2),HexH,180), (round(HexW/8),round(3*HexH/4),120), (round(HexW/8),round(HexH/4),60)]
# TODO : ameliorer
edgesCenter = [(round(HexW/2),0,0), (round(7*HexW/8)-5,round(HexH/4)+5,-60), (round(7*HexW/8)-5,round(3*HexH/4)-5,-120), (round(HexW/2),HexH,180), (round(HexW/8)+5,round(3*HexH/4)-5,120), (round(HexW/8)+5,round(HexH/4)+5,60)]
WHimage = pygame.transform.smoothscale(res.WHOLE,(round(HexW/16),round(HexH/16)))
#Classes
    # return a list with the rect to draw, drawn later with drawGame(), and and dict to get the Tiles from coordinates
def setMap(w=7,h=9):
    if w%2==0:
        w+=1
    if h%2==0:
        h+=1
    tileGroup = pygame.sprite.LayeredUpdates()
    tileDict = dict()
    for x in range(-round(w/2),round(w/2)+1,2):
        for y in range(-round(h/2),round(h/2)+1,2):
            t= TileM(x,y)
            tileGroup.add(t)
            tileDict[(x,y)]=t
    
    for x in range(1-round(w/2),round(w/2),2):
        for y in range(1-round(h/2),round(h/2),2):
            t= TileM(x,y)
            tileGroup.add(t)
            tileDict[(x,y)]=t
                
    return (tileGroup,tileDict)
 
 
    # The Tile for Map
class TileM(pygame.sprite.Sprite):
    isInitialised = False
    dmap = dict()
    edges = dict()
    conNeigh = dict()
    type=0
    h=round(res.HEXMSIZE*math.sqrt(3)/2)
    w=res.HEXMSIZE
    texture = pygame.transform.smoothscale(res.WHEX,(w,h))
    angle = 0
    x=0
    y=0
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        
        self.l=res.CENTERX+self.w*3*x/4-self.w/2
        self.t=res.CENTERY+self.h*y/2-self.h/2
        self.rect = pygame.Rect(self.l,self.t,self.w,self.h)
        self.x = x
        self.y = y
        # TODO: type a specifier au moment de la creation de la map ... et verifier les cas particulliers
        self.type=abs(x)+abs(y)
        if self.type==2 and abs(x)%2==0 and x !=0:
            self.type+=2
        
        if abs(x)>2 and self.type == 4:
            self.type+=4

        # self.image = pygame.transform.smoothscale(self.loadimage("wHex"),(self.w,self.h))
        self.image = self.texture
    
    def getCoord(self):
        return (self.x,self.y)
    
    def getConnectedNeighbours(self,tmap):
        pos=((0,-2),(1,-1),(1,1),(0,2),(-1,1),(-1,-1))
        d=dict()
        for e in self.edges:
            p=pos[int(e)]
            sp = (self.x+p[0],self.y+p[1])
            if sp in tmap and tmap[sp].isInitialised:
                print("adjacent teste "+str(tmap[sp].toString()))
                matchingedge = int(e)+3
                if matchingedge>5:
                    matchingedge-=6
                if str(matchingedge) in tmap[sp].edges:
                    d[e]=tmap[sp]
        self.conNeigh = d        
        print(str(self.conNeigh))
    
    def loadimage(self,name):
        return pygame.image.load(os.path.join('data',name+'.png')).convert_alpha()
     
    def initTile(self,dmap):
        if not self.isInitialised:
            if self.type==0:
                self.image= pygame.transform.smoothscale(self.loadimage("GC"),(self.w,self.h))
            elif self.type==2 :
                self.image = pygame.transform.smoothscale(self.loadimage("R1"),(self.w,self.h))
            elif self.type==4 :
                self.image = pygame.transform.smoothscale(self.loadimage("R2"),(self.w,self.h))
            else :
                self.image = pygame.transform.smoothscale(self.loadimage("wHex"),(self.w,self.h))
            self.initWHoles()
            self.dmap = dmap
            self.isInitialised = True
     
    def initWHoles(self):
        d = dict()
        min=1
        max=6
        if self.type == 0 :
            min=6
        elif self.type == 2:
            min=2
            max=4
        elif self.type == 4:
            max=3
        else :
            max=2
        print("min = "+str(min)+" max = "+str(max))
        nbWH = random.randint(min,max)
        print("len ="+str(len(d))+" nbWH "+str(nbWH))
        while len(d)<nbWH:
            seg = random.randint(0,5)
            if str(seg) not in d:
                print("a")
                d[str(seg)]=(edgesCenter[seg]) 
        
        self.edges = d.copy()
        
        for wh in self.edges:
            iwh = int(wh)
            ri = pygame.transform.rotate(WHimage,edgesCenter[iwh][2])
            r=ri.get_rect()
            r.centerx = edgesCenter[iwh][0]
            r.centery = edgesCenter[iwh][1]
            self.image.blit(ri,r) 
         
        print(self.toString())
           
    def toString(self):
        s = "("+str(self.x)+","+str(self.y)+") type="+str(self.type)+" edges="+str(len(self.edges))
        return s
    
    def rotate(self,angle):
        #s = self.image.copy()        
        if angle%60 == 0:
            ri = pygame.transform.rotate(self.image,angle)
            r = ri.get_rect()
            r.centerx = self.rect.centerx
            r.centery = self.rect.centery
            self.image = ri
            self.rect = r
            self.angle += angle
            
            tmpdict = dict()
            for e in self.edges:
                newE = int(e)-int(angle/60)
                if newE>5:
                    newE -=6
                if newE<0:
                    newE +=6
                tmpdict[str(newE)] = self.edges[e]
            self.edges = tmpdict
            
            if abs(self.angle) == 360:
                self.angle = 0
    
    def draw(self):            
        pygame.sprite.Sprite.draw(self)
    
    def kill (self):
        pygame.sprite.Sprite.kill(self)
 

 
class GameScore:
    val = 0
    def __init__(self,val):
        self.val=val
        
class Animation(pygame.sprite.Sprite):
    fullImage = 0
    fullX = 0
    fullY = 0
    nbIt = 0
    nbImage = 16
    def __init__(self,filename,dest,nbImage=16):
        pygame.sprite.Sprite.__init__(self)
        self.fullImage = pygame.image.load(filename).convert()
        self.rect = dest
        self.nbImage = nbImage
        #TODO :
        self.fullX = self.fullImage.get_rect().w
        self.fullY = self.fullImage.get_rect().h
        self.image = pygame.Surface((self.fullX/self.nbImage,self.fullY))
        self.image.blit(self.fullImage,self.image.get_rect(),pygame.Rect(0,0,self.fullX/self.nbImage,self.fullY))
        self.image = pygame.transform.smoothscale(self.image,(self.rect.w,self.rect.h))
        self.image.set_colorkey(res.BLACK)    
    def update(self):
        if self.nbIt < self.nbImage:
            tmpImage = pygame.Surface((self.fullX/self.nbImage,self.fullY))
            tmpImage.blit(self.fullImage,pygame.Rect(0,0,self.fullX/self.nbImage,self.fullY),
                pygame.Rect(self.nbIt*self.fullX/self.nbImage,0,self.fullX/self.nbImage,self.fullY))
            self.image = pygame.transform.smoothscale(tmpImage,(self.rect.w,self.rect.h))
            self.image.set_colorkey(res.BLACK)            
            self.nbIt +=1
        else:
            self.kill()
    
    def setCoord(self,x,y):
        self.rect.centerx = x
        self.rect.centery = y       
        # res.BOOM.play()
        # a = Animation(res.os.path.join('data','explosion.png'),self,16)
