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

######## Load Images
bullet_image = pygame.image.load('pics/second_bullet.png')
enemy_image = pygame.image.load('pics/enemy.png')
player_image = pygame.image.load('pics/player.png')
########
#rand_color = (int(random.randint(0,254)),int(random.randint(0,254)) ,int(random.randint(0,254)))

################################################################
def play():
    FPS = 70
    clock = pygame.time.Clock()
    start_color = (0,0,0)
    pygame.mouse.set_visible(False)
    enemy = Enemy(10,random.randint(10,250),30,60,30,30) #(100,100,30,60,30,30) x,y,width,height, damage and health ???
    player = Player(300,300,10,64,32,100) #(300,300,10,64,32,100) x,y,vel,height,width, health ???

    while True:
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

        if player.y == 0: #Just to try a "death"
            break

        clock.tick(FPS)
        pygame.display.update()
        pass

##################################################################
def quit():
    pygame_menu.events.EXIT
    sys.exit()

while True:
    for event in pygame.event.get():
    	if event.type == pygame.QUIT:
    		pygame.quit(),sys.exit()
    		break

    menu = pygame_menu.Menu(windowX,windowY,'Healthless',theme = pygame_menu.themes.THEME_BLUE)
    menu.add_button('Play', play)
    menu.add_button('Quit', quit)
    menu.mainloop(window)
