import pygame
import pygame_menu
import sys
import random
import time
from bullets import *
from player import *
from enemy import *

pygame.init()
pygame.display.set_caption('Healthless')
windowX = 600
windowY = 600
window = pygame.display.set_mode((windowX,windowY))
icon = pygame.image.load('pics/logo.png')
pygame.display.set_icon(icon)

######## Images
bullet_image = pygame.image.load('pics/second_bullet.png')
enemy_image = pygame.image.load('pics/enemy.png')
player_image = pygame.image.load('pics/player.png')
arrow_img = pygame.image.load('pics/arrow.png')
#######
#rand_color = (int(random.randint(0,254)),int(random.randint(0,254)) ,int(random.randint(0,254)))

#################################################### Variables
FPS = 70
clock = pygame.time.Clock()
start_color = (0,0,0)
pygame.mouse.set_visible(False)
enemy = Enemy(100,100,30,60,30,30)
player = Player(300,300,10,64,32,100)
#######################################################
################################################################ MAINLOOP START
def play():
    gamerun = True
    while gamerun == True:
        for event in pygame.event.get():
        	if event.type == pygame.QUIT:
        		gamerun = False
        		pygame.quit(),sys.exit()
        		break

        window.fill((0,70,80))

        player.debug()
        player.shoot(window,start_color,bullet_image)
        player.draw(window,start_color,player_image)
        player.update(window,start_color,bullet_image)

        enemy.draw(window,start_color,enemy_image)
        enemy.update()

        clock.tick(FPS)
        pygame.display.update() #Update a display
        pass
################################################################## MAINLOOP END
def quit():
    pygame_menu.events.EXIT
    sys.exit()

menu_bool = True
while menu_bool == True:
    for event in pygame.event.get():
    	if event.type == pygame.QUIT:
    		menu_bool = False
    		pygame.quit(),sys.exit()
    		break

    menu = pygame_menu.Menu(windowX,windowY,'Healthless',theme = pygame_menu.themes.THEME_BLUE)
    menu.add_button('Play', play)
    menu.add_button('Quit', quit)
    menu.mainloop(window)
