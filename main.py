import pygame, sys
import button
from pygame.locals import *

pygame.init()
        

#setup display resolution
width, height = 800,600
screen = pygame.display.set_mode((width, height))

class gameScreen():
    def __init__(self, image, x, y, scale):
        
        self.image =  pygame.transform.scale(image,(width, height))
        self.rect = self.image.get_rect()
        self.rect = self.topleft = (x,y)
    def get_Screen(self):
        screen.blit(self.image,(self.rect.x,self.rect.y))


#game variable
game_pause = False
game_state = "main"
clock = pygame.time.Clock()

#load button image
start_image = pygame.image.load("image\start2.png").convert_alpha()
exit_image = pygame.image.load("image\exit.png").convert_alpha()

#create button instance
button_start = button.Button(200,300, start_image, 0.6)
button_exit = button.Button(400,300, exit_image, 0.6)

#name of game
pygame.display.set_caption("Dungeon Hell")

#library color
red = (255, 0, 0)
black = (255, 255, 255)

#load background
bg_img = pygame.image.load("image\galaxy.png")
map_img = pygame.image.load("image\chess.png")

#creat background
main_Menu = gameScreen(width, height, bg_img)
board = gameScreen(width, height)

#library text font
manual_font = pygame.font.SysFont("arial", 14)

#setup first page
i = 0
st = 1;                               
while True:                         
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
        if st == True:
            screen.blit(bg_img, (i, 0))
    if button_start.draw(screen) == True:
        print("true")
        screen.blit(map_img, (0, 0))
        st = False
    if button_exit.draw(screen) == True:
        pygame.quit()
        sys.exit()
    
    pygame.display.update()