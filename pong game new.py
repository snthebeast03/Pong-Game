import pygame
import sys
import random
import time
from pygame.locals import *
pygame.init()

red = random.randint(0,1)
if red == 1:
    black = 0
else:
    black = 1
updown = random.choice([1,2,3,4,5,-1,-2,-3,-4,-5])

WHITE = (255,255,255)
FPS = 60
fps = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))
screen.fill(WHITE)
end_game_screen = pygame.image.load("gameover.jpeg")

class Paddles(pygame.sprite.Sprite):
    def __init__(self, img, pos):
        super().__init__()
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.rect.center = pos
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self == redplayer:
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -10)
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0, 10)
        elif self == blackplayer:
            if pressed_keys[K_w]:
                self.rect.move_ip(0, -10)
            if pressed_keys[K_s]:
                self.rect.move_ip(0, 10)

class Walls(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__() 
        self.image = pygame.image.load("walls2.png")
        self.rect = self.image.get_rect()
        self.rect.center = pos
    def move(self):
        pass
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("balledited.jpg")
        self.rect = self.image.get_rect()
        self.rect.center=(400, 300)

    def move(self):
        global updown
        if red == 1:
            self.rect.move_ip(5,updown)
        elif black == 1:
            self.rect.move_ip(-5,updown)

blackplayer = Paddles("black paddle.jpg", (50,300))
#blackplayer.imge = "black paddle.jpg"
#blackplayer.cent = (50,300)
redplayer = Paddles("red paddle.png", (750,300))
#blackplayer.imge = "red paddle.png"
#blackplayer.cent = (750,300)
upwall = Walls((400,0))
downwall = Walls((400,600))
ball = Ball()

all_sprites = pygame.sprite.Group()
all_sprites.add(redplayer)
all_sprites.add(blackplayer)
all_sprites.add(upwall)
all_sprites.add(downwall)
all_sprites.add(ball)

q = True
while q:
    for event in pygame.event.get():
        if event.type == QUIT:
            screen.blit(end_game_screen, (0,0))
            pygame.display.update()
            time.sleep(2)
            pygame.quit()
            sys.exit()
    screen.fill(WHITE)
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()
    if ball.rect.colliderect(redplayer.rect) or ball.rect.colliderect(blackplayer.rect):
        if red == 1:
            red = 0
            black = 1
        else:
            red = 1
            black = 0
    if ball.rect.colliderect(upwall.rect):
        updown = random.randint(1,5)
    if ball.rect.colliderect(downwall.rect):
        updown = random.randint(-5,-1)

    if ball.rect.center[0] > 820 or ball.rect.center[0] < -20:
        screen.blit(end_game_screen, (0,0))
        pygame.display.update()
        time.sleep(2.5)
        pygame.quit()
        sys.exit()
    pygame.display.update()
    fps.tick(FPS)
