#Using premade template

import pygame
import random


WIDTH=480
HEIGHT=600
FPS=60

#colors
WHITE=(255,255,255)
BLACK=(0,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
RED=(255,0,0)
YELLOW=(255,255,0)
#initializing pygame and creating the window
pygame.init()
pygame.mixer.init() #this is used for sounds
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tis My SHMUP")
clock=pygame.time.Clock()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((50, 40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx=0
    def update(self):
        self.speedx=0
        keystate=pygame.key.get_pressed()
        #movement and checks for button presses
        if keystate[pygame.K_LEFT]:
            self.speedx=-5
        if keystate[pygame.K_RIGHT]:
            self.speedx=5
        self.rect.x+=self.speedx
        if self.rect.right>WIDTH:
            self.rect.right=WIDTH
        if self.rect.left<0:
            self.rect.left=0
            
    def shoot(self):
        bullet=Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        all_bullets.add(bullet)        
        
class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((40,50))
        self.image.fill(RED)
        self.rect=self.image.get_rect()
        self.rect.x=random.randrange(0,WIDTH-self.rect.width)
        self.rect.y=random.randrange(-100, -40)
        self.speedy=random.randrange(1,5)
        self.speedx=random.randrange(-3,3)
    def update(self):
        self.rect.y+=self.speedy
        self.rect.x+=self.speedx
        if self.rect.top>HEIGHT+10 or self.rect.left<-25 or self.rect.right>WIDTH+20:
            self.rect.x=random.randrange(0,WIDTH-self.rect.width)
            self.rect.y=random.randrange(-100, -40)
            self.speedy=random.randrange(1,5)


        
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((10,20))
        self.image.fill(YELLOW)
        self.rect=self.image.get_rect()
        self.rect.bottom=y
        self.rect.centerx=x
        self.speedy=-10
    def update(self):
        self.rect.y+=self.speedy
        #will kill if movess off top of screen
        if self.rect.bottom<0:
            self.kill()
    
    
all_sprites=pygame.sprite.Group()
player=Player()
all_sprites.add(player)
all_bullets=pygame.sprite.Group()

all_mobs=pygame.sprite.Group()

for i in range(8):
    m=Mob()
    all_sprites.add(m)
    all_mobs.add(m)
    
#Game loop (main loop)
running=True

while running:
    #keep loop running at the right speed
    clock.tick(FPS)
    #process input (events)
    for event in pygame.event.get():
        #check for closing of the window
        if event.type==pygame.QUIT:
            running=False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                player.shoot()
                
    #update
    all_sprites.update()
    #check for collisions
    hits=pygame.sprite.spritecollide(player, all_mobs, False)
    if hits:
        running=False
    #check to see if bullet hit a mob
    hits=pygame.sprite.groupcollide(all_mobs, all_bullets, True, True)
    for hit in hits:
        m=Mob()
        all_sprites.add(m)
        all_mobs.add(m)
    #draw/render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    #AFTER drawing everything, flip the display
    pygame.display.flip() #whiteboard anaology
    
pygame.quit()
