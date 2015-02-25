#from data.Resources import *
import data.Resources as res
import random
import math

pygame=res.pygame
#Classes

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
        
    # The Tile for Map
class TileM(pygame.sprite.Sprite):
    type=0
    h=round(res.HEXMSIZE*math.sqrt(3)/2)
    w=res.HEXMSIZE
    texture = pygame.transform.smoothscale(res.WHEX,(w,h))
    x=0
    y=0
    def __init__(self,type,x,y):
        pygame.sprite.Sprite.__init__(self)
        
        if y%2==0:
            self.l=res.CENTERX+self.w*3*x/4-self.w/2
            self.t=res.CENTERY+self.h*y/2-self.h/2
        else:
            self.l=res.CENTERX+self.w*3*x/4-self.w/2
            self.t=res.CENTERY+self.h*y/2-self.h/2
     
        self.rect = pygame.Rect(self.l,self.t,self.w,self.h)
        self.x = x
        self.y = y
        self.type=abs(x)+abs(y)
        if self.type==2 and abs(x)%2==0 and x !=0:
            self.type+=2
        
        if abs(x)>2 and self.type == 4:
            self.type+=4
        
        if self.type==0:
            self.image= pygame.transform.smoothscale(res.GC,(self.w,self.h))
        elif self.type==2 :
            self.image = pygame.transform.smoothscale(res.R1,(self.w,self.h))
        elif self.type==4 :
            self.image = pygame.transform.smoothscale(res.R2,(self.w,self.h))
        else :
            self.image = self.texture
        print(str(self.rect))
        
    def kill (self):
        pygame.sprite.Sprite.kill(self)
        
        
    # The Bricks
class Brick(pygame.sprite.Sprite):
    color = res.WHITE
    type = 0
    h = res.BRICKSIZE
    w = round(res.BRICKSIZE*1.5)
    texture = pygame.transform.smoothscale(res.WBRICK,(w,h))
    
    def __init__(self,type,l,t):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(l,t,self.w,self.h)
        self.l = l
        self.t = t
        self.type=type
        self.image = self.texture
        self.getColor()
        
    def getColor(self):
        if self.type == 1:
            self.color = res.RED
            self.image = pygame.transform.smoothscale(res.RBRICK,(self.w,self.h))            
        elif self.type == 2:
            self.color = res.GREEN
            self.image = pygame.transform.smoothscale(res.GBRICK,(self.w,self.h))    
        elif self.type == 3:
            self.color = res.YELLOW
            self.image = pygame.transform.smoothscale(res.YBRICK,(self.w,self.h))    
        elif self.type == 4:
            self.color = res.CYAN
            self.image = pygame.transform.smoothscale(res.CBRICK,(self.w,self.h))  
        else:
            self.color = res.WHITE
            self.image = pygame.transform.smoothscale(res.WBRICK,(self.w,self.h))
    
    def setType(self,type):
        self.type = type
        self.getColor()
        
    def destroy(self):
        r = random.randint(0, 100)
        res.BOOM.play()
        a = Animation(res.os.path.join('data','explosion.png'),self,16)
        res.Score.val += (self.type+1)*100
        res.ExplGroup.add(a)
        
        if r > 60 :
            r2 = random.randint(0,4)
            if r2 == 0:
                pu = PUPadWidthUp(r2,self.l + self.w/4,self.rect.bottom)
                pu.getColor()
            elif r2 == 1:
                pu = PUPadSpeedUp(r2,self.l + self.w/4,self.rect.bottom)
                pu.getColor()
            elif r2 == 2:
                pu = PUPadSpeedDown(r2,self.l + self.w/4,self.rect.bottom)
                pu.getColor()
            elif r2 == 3:
                pu = PUMultiBall(r2,self.l + self.w/4,self.rect.bottom)
                pu.getColor()
            elif r2 == 4:
                pu = PULaser(r2,self.l + self.w/4,self.rect.bottom)
                pu.getColor()
            res.PowerUps.add(pu)
    
    def kill (self):
        self.destroy()
        if self.type > 0 :
                self.setType(self.type-1)
        else:
            pygame.sprite.Sprite.kill(self)
            #brick.kill()

            
class MovingBrick(Brick):
    movement = 1
    left=0
    right=res.WINDOWWIDTH
    
    def setBounds(self,left=0,right=res.WINDOWWIDTH):
        self.left=left
        self.right=right
        
    def update(self):
        if self.rect.right >= self.right or self.rect.left <= self.left:
            self.movement *= -1
        self.rect.left += self.movement
    
    
class PowerUp(Brick):
    color = res.WHITE
    type = 0
    h = round(res.BRICKSIZE /2)
    w = round(res.BRICKSIZE*1.5/2)
    texture = pygame.transform.smoothscale(res.WBRICK,(w,h))
    duration = -1
    def update(self,timer=False):
        if timer:
            if self.duration > 0:
                self.duration -= 1
            elif self.duration == 0:
                self.kill()
        else:
            self.move()
        
    def setAction(self,duration=15,object=None):
        self.duration = duration
          
    def destroy(self):
        return
    
    def kill(self):
        pygame.sprite.Sprite.kill(self)
    
    def move(self):
        self.rect.centery += 5

class PUPadSpeedUp(PowerUp):
    pad = None
    def setAction(self,object=None,duration=15):
        self.duration = duration
        if object.__class__.__name__ == "Paddle":
            self.pad = object
            self.pad.padSpeed += 5
             
    def kill(self):
        if self.pad is not None:
            self.pad.padSpeed -= 5
        pygame.sprite.Sprite.kill(self)

class PUPadSpeedDown(PowerUp):
    pad = None
    def setAction(self,object=None,duration=15):
        self.duration = duration
        if object.__class__.__name__ == "Paddle":
            self.pad = object
            self.pad.padSpeed -= 5
                
    def kill(self):
        if self.pad is not None:
            self.pad.padSpeed += 5
        pygame.sprite.Sprite.kill(self)
        
class PUPadWidthUp(PowerUp):
    pad = None
    def setAction(self,object=None,duration=15):
        self.duration = duration
        if object.__class__.__name__ == "Paddle":
            self.pad = object
            self.pad.w += 30  
    
    def kill(self):
        if self.pad is not None:
            self.pad.w -= 30
        pygame.sprite.Sprite.kill(self)

class PULaser(PowerUp):
    pad = None
    def setAction(self,object=None,duration=15):
        self.duration = duration
        if object.__class__.__name__ == "Paddle":
            self.pad = object
            self.pad.canShoot = True
            
    def update(self,timer=False):
        if self.pad is not None:
            self.pad.canShoot = True
        PowerUp.update(self,timer)  
        
    
    def kill(self):
        if self.pad is not None:
            self.pad.canShoot = False
        pygame.sprite.Sprite.kill(self)
        
class PUMultiBall(PowerUp):
    ball = None
    # def setAction(self,Balls, object=None,duration=-1):
        # self.duration = duration
        # if object.__class__.__name__ == "Ball":
            # Balls.add(Ball(object.rect.centerx, object.rect.centery, 15, 15, object.speed[0]+3, object.speed[1]))
            # Balls.add(Ball(object.rect.centerx, object.rect.centery, 15, 15, object.speed[0]-3, object.speed[1]))
    def setAction(self, object=None,duration=-1):
        self.duration = duration
        if object.__class__.__name__ == "Group":
            ind = random.randint(0,len(object.sprites())-1)
            b = (object.sprites())[ind]
            res.Balls.add(Ball(b.rect.centerx, b.rect.centery, 15, 15, b.speed[0]+3, b.speed[1]))
            res.Balls.add(Ball(b.rect.centerx, b.rect.centery, 15, 15, b.speed[0]-3, b.speed[1]))        
    
    def kill(self):
        pygame.sprite.Sprite.kill(self)
                
    #The paddles
class Paddle:
    lives = 3
    rect = pygame.Rect(0, 0, 0, 0)
    movement = 0
    padSpeed = 20
    canShoot = False
    def __init__(self, l, t, w, h):
        self.l = l
        self.t = t
        self.w = w
        self.h = h
    def setRect(self):
        self.rect = pygame.Rect(self.l, self.t, self.w, self.h)

    def setPosition(self):
        self.position = self.l
    def setMovement(self, y):
        self.movement = y
    def move(self):
        self.l = self.l + self.movement*self.padSpeed
        self.setPosition()
        self.setRect()
    def draw(self):
        texture = pygame.transform.smoothscale(res.PADDLE,(self.w,self.h))
        res.windowSurface.blit(texture, self.rect)
    def collideWithSide(self, leftSide, rightSide):
        if (self.l + self.w) > rightSide:
            self.setMovement(0)
        if (self.l) < leftSide:
            self.setMovement(0)
            
    def collideWithPU(self,Balls,ball):
        pu = pygame.sprite.spritecollideany(self,res.PowerUps)
        if pu is not None:
            res.POWERUP.play()
            if pu.type == 3:
                #pu.setAction(Balls,ball)
                pu.setAction(Balls)
            else:
                pu.setAction(self)
            
            if pu.type == 2:
                res.Score.val -= 500
            else:
                res.Score.val += 500
            
            pu.image = pygame.surface.Surface((0,0))
            pu.rect = pygame.Rect(0,0,1,1)
    
    def shoot(self,shots):
        if self.canShoot:
            shots.add(Shot(self.rect.centerx,self.rect.centery))
	
class Shot(pygame.sprite.Sprite):
    h = 15
    w = 2
    shotspeed = 10
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x,y,self.w,self.h)
        self.image = pygame.Surface((self.w,self.h))
        self.image.fill(res.WHITE)
    
    def move(self):
        self.rect.top -= self.shotspeed
    
    def collideWithBrick(self,lvl):
        if pygame.sprite.spritecollide(self,lvl,True):
            self.kill()
    
    def update(self,lvl):
        self.move()
        self.collideWithBrick(lvl)
        
    #AI
class AI(Paddle):
    def move(self, ball):
		
        if ball.rect.centerx< self.rect.left:
            self.movement = -1
        elif ball.rect.centerx> self.rect.right:
            self.movement = 1
        else:
            self.movement = 0
        
        self.l = self.l + self.movement*self.padSpeed
        self.setPosition()
        self.setRect() 
	
	
    #The ball
class Ball(pygame.sprite.Sprite):
    rect = pygame.Rect(0, 0, 0, 0)
    main = False
    rectList = []
    position = [0, 0]
    def __init__(self, l, t, w, h, x, y):
        self.speed = [x, y]
        self.l = l
        self.t = t
        self.w = w
        self.h = h
        self.image = pygame.Surface((1, 1))
        pygame.sprite.Sprite.__init__(self)
    def setRect(self):
        self.rect = pygame.Rect(self.l, self.t, self.w, self.h)
    def setPosition(self):
        self.position = [self.l, self.t]
    def setSpeed(self, x, y):
        self.speed = [x, y]
    def draw(self):
        pygame.draw.circle(res.windowSurface, res.WHITE, self.rect.center,round(self.w/2))
        
    def move(self):
        #vecteur ball
        self.rectList = []
        vectY = abs(round(self.speed[1]/2))
        vectY = vectY if vectY != 0 else 1
        signeY = (round(self.speed[1]/2))/vectY
        for i in range(0, vectY):
            self.rectList.append(pygame.Rect(self.l + self.speed[0]*i/vectY, self.t + (signeY*i*2), 2, 2))
        self.l = self.l + self.speed[0]
        self.t = self.t + self.speed[1]
        self.setRect()
        self.setPosition()
        
    def bounce(self, paddle):
        if paddle.rect.collidelist(self.rectList) != -1:
            res.Score.val -= 10
            self.setSpeed(self.speed[0] + (self.l - paddle.l - paddle.w/2)/5, -self.speed[1] )
            rectinter = self.rectList[paddle.rect.collidelist(self.rectList)-1]
            res.BONG.play()
            if self.t > res.WINDOWHEIGHT/2:
                self.t = res.WINDOWHEIGHT - 40
            else:
                self.t = res.WINDOWHEIGHT -10
                
    def collideWithBricks(self, Level):
        brick = pygame.sprite.spritecollideany(self,Level)
        if brick is not None:
            res.BONG.play()
            if self.rect.centery>=brick.rect.bottom-2 or self.rect.centery<=brick.rect.top+2:
                self.setSpeed(self.speed[0], -self.speed[1])
            elif self.rect.centerx<=brick.rect.left+2 or self.rect.centerx >= brick.rect.right -2:
                self.setSpeed(-self.speed[0] , self.speed[1] )
            else:
                self.setSpeed(-self.speed[0] , -self.speed[1] )
            brick.kill()
        
        return
        
    def collideWithSide(self, leftSide, rightSide,topSide):
        if (self.l + self.w) > rightSide or (self.l) < leftSide:
            res.Score.val -= 10
            self.setSpeed(-self.speed[0], self.speed[1])
            res.BONG.play()
        if self.t < topSide :
            res.Score.val -= 10
            self.setSpeed(self.speed[0], -self.speed[1])
            self.t = 5
            res.BONG.play()
    def setMain(self,main):
        self.main = main
    def update (self,Level,Pad,leftSide,rightSide,topSide):
        self.bounce(Pad)
        self.collideWithSide(leftSide,rightSide,topSide)
        self.collideWithBricks(Level)
        self.move()
        self.draw()
        if self.t > res.WINDOWHEIGHT:    
            res.SPLASH.play()
            self.kill()