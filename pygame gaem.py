import pygame
import sys
import random
import os
import time
from pygame.locals import *
#init and stuff
pygame.init()
WHITE = (255,255,255)
BLACK = (0,0,0)
FPS = 60
FramePerSec = pygame.time.Clock()
#screen 
screen = pygame.display.set_mode((800, 600))
screen.fill(WHITE)
global redstart
global blackstart
redstart = random.randint(0,1)
global q
q = True
#side the ball deflects to when game starts
if redstart == 1:
    blackstart = 0
if redstart == 0:
    blackstart = 1
global collided
collided = 1
global side 
side = random.randint(-5,5)
#gameover screen
gameover = pygame.image.load("gameover.jpeg")

#red paddle
class Redplayer(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("red paddle.png")
        self.rect = self.image.get_rect()
        self.rect.center=(750, 300)
 
      def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -10)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 10)
    
#black paddle
class Blackplayer(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("black paddle.jpg")
        self.rect = self.image.get_rect()
        self.rect.center=(50, 300)
 
      def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_w]:
            self.rect.move_ip(0, -10)
        if pressed_keys[K_s]:
            self.rect.move_ip(0, 10)

#walls
class Wallup(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("walls2.png")
        self.rect = self.image.get_rect()
        self.rect.center=(400, 0)
      def move(self):
          pass

class Walldown(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("walls2.png")
        self.rect = self.image.get_rect()
        self.rect.center=(400, 600)
      def move(self):
          pass


#ball duh
class Ball(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("balledited.jpg")
        self.rect = self.image.get_rect()
        self.rect.center=(400, 300)

      def move(self):
        global redstart
        global blackstart
        global collided
        global side
        global q
        if redstart == 1:
            self.rect.move_ip(5, side)
        if blackstart == 1:
            self.rect.move_ip(-5, side)
        
#creating sprites
blackplayer = Blackplayer()
redplayer = Redplayer()
ball = Ball()
wallu = Wallup()
walld = Walldown()

paddles = pygame.sprite.Group()
paddles.add(redplayer)
paddles.add(blackplayer)

wallup = pygame.sprite.Group()
wallup.add(wallu)

walldown = pygame.sprite.Group()
walldown.add(walld)

sprites = pygame.sprite.Group()
sprites.add(redplayer)
sprites.add(blackplayer)
sprites.add(ball)
sprites.add(wallu)
sprites.add(walld)


#main loop

while q:
    collided = 0
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill(WHITE)
    for entity in sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()
    #collision detection
    if pygame.sprite.spritecollideany(ball, paddles):
        if redstart == 1:
            redstart = 0
            blackstart = 1
        else:
            redstart = 1
            blackstart = 0
    if pygame.sprite.spritecollideany(ball, wallup):
        side = random.randint(1,5)
    if pygame.sprite.spritecollideany(ball, walldown):
        side = random.randint(-5,-1)

    if ball.rect.center[0] > 820 or ball.rect.center[0] < -20:
        screen.blit(gameover, (0,0))
        pygame.display.update()
        time.sleep(2.5)
        pygame.quit()
        sys.exit()
    pygame.display.update()
    FramePerSec.tick(FPS)
