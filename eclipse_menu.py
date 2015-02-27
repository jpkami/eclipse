import data.Resources as res
pygame = res.pygame

class button(pygame.sprite.Sprite):
    buttonSurface = None
    x=0
    y=0
    w=0
    h=0
    
    def __init__(self,DestSurface,x,y,w,h,color = res.WHITE):
     
        self.buttonSurface = pygame.Surface((w,h))
        self.buttonSurface.fill(color)
        
    def write(self, text, fontSize, x, y, color=res.WHITE):
    
        font = pygame.font.SysFont('helvetica', fontSize)
        textR = font.render(text, True, color)
        textRect = textR.get_rect()
        textRect.centerx = x
        textRect.centery = y
        self.menuSurface.blit(textR, textRect)    
        
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