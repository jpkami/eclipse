import data.Resources as res
pygame = res.pygame

class Button(pygame.sprite.Sprite):
    #buttonSurface = None
    x=0
    y=0
    w=0
    h=0

    def __init__(self,x,y,w,h,text=None,fontSize=10,color = res.BLUE,tColor=res.WHITE):
        pygame.sprite.Sprite.__init__(self)
#         self.image=None
        buttonSurface = pygame.Surface((w,h))
        buttonSurface.fill(color)
        self.image = buttonSurface
        r = pygame.Rect(x,y,w,h)
        r.center=(x,y)
        self.rect = r
        self.event = pygame.event.Event(res.BUTTONEVENT, {})
        if text is not None:
            self.writecenter(text, fontSize, tColor)
    
    def write(self, text, fontSize, x, y, color=res.WHITE):
    
        font = pygame.font.SysFont('helvetica', fontSize)
        textR = font.render(text, True, color)
        textRect = textR.get_rect()
        textRect.centerx = x
        textRect.centery = y
#         self.menuSurface.blit(textR, textRect)    
        self.image.blit(textR, textRect)    
        
    def writecenter(self, text, fontSize, color=res.WHITE):    
        font = pygame.font.SysFont('helvetica', fontSize)
        textR = font.render(text, True, color)
        textRect = textR.get_rect()
        textRect.center = (self.rect.w/2,self.rect.h/2)
#         self.menuSurface.blit(textR, textRect)    
        self.image.blit(textR, textRect)   
    
    def setFunction(self,args):
        self.event = pygame.event.Event(res.BUTTONEVENT, args)
    
    def onClick(self):
        pygame.event.post(self.event)
         
class GameMenu(pygame.sprite.Sprite):
    menuSurface = None
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.surface = pygame.Surface((abs(res.WINDOWWIDTH*7/8),abs(res.WINDOWHEIGHT*7/8)))
        self.surface.fill(res.DKBLUE)
        self.surface.set_alpha(200)
        self.rect = self.surface.get_rect()
        self.rect.centerx = pygame.display.get_surface().get_rect().centerx
        self.rect.centery = pygame.display.get_surface().get_rect().centery
    
    def initInterface(self):
        1+1
    
    def setSFXVolume(self,vol):
        for sound in res.ALLSOUNDS:
            sound.set_volume(vol)
    
    def write(self, text, fontSize, x, y, color=res.WHITE):
        font = pygame.font.SysFont('helvetica', fontSize)
        textR = font.render(text, True, color)
        textRect = textR.get_rect()
        textRect.centerx = x
        textRect.centery = y
        self.surface.blit(textR, textRect)
    
    def draw(self,surface):
        surface.blit(self.surface,self.rect)