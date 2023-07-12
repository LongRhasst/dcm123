import pygame, sys
from pygame.locals import *

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("hello")



red = (0,0,255)

def draw_board():
    for i in range(32):
        column = i % 4
        row = i // 4
        if row % 2 == 0:
            pygame.draw.rect(screen, "light gray", [600 - (column*200), row * 100, 100, 100])
        else:
            pygame.draw.rect(screen, "light gray", [700 - (column*200), row * 100, 100, 100])


#setup character abilities
hp_hero = 80
mana_hero = 100
class hero_abilities():
    def __init__(self, image, x, y):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.x = self.rect.x
        self.y = self.rect.y
        self.left_press =  False
        self.right_press=  False
        self.up_press   =  False
        self.down_press =  False
    def draw(self):
        screen.blit(self.image, (self.x, self.y))
    def update(self):
        if self.left_press == True:
            self.x -= 100
            screen.blit(self.image, (self.x, self.y))
            self.left_press = False
        if self.right_press == True:
            self.x += 100
            screen.blit(self.image, (self.x, self.y))
            self.right_press = False
        if self.up_press == True:
            self.y -= 1
            screen.blit(self.image, (self.x, self.y))
        if self.down_press == True:
            self.y += 1
            screen.blit(self.image, (self.x, self.y))
            

hero = hero_abilities("image\character.png", 25, 25)

run = True
check = True
while run:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    if event.type == KEYDOWN:
        if event.key == pygame.K_LEFT and check == True:
            hero.left_press = True
            check = False
        if event.key == pygame.K_RIGHT and check == True:
            hero.right_press = True
            check = False
        if event.key == pygame.K_UP:
            hero.up_press = True
        if event.key == pygame.K_DOWN:
            hero.down_press = True
    if event.type == KEYUP:
        if event.key == pygame.K_LEFT and check == False:
            hero.left_press = False
            check = True
        if event.key == pygame.K_RIGHT and check == False:
            hero.right_press = False
            check = True
        if event.key == pygame.K_UP:
            hero.up_press = False
        if event.key == pygame.K_DOWN:
            hero.down_press = False
    
    screen.fill("dark gray")
    draw_board()
    
    #setup moving
    
            
    hero.draw()
    hero.update()
    
    pygame.display.flip()