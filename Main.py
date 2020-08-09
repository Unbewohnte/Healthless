import pygame
import pygame_menu
import sys
import random
import time
from bullets import Bullet
from player import Player
from enemy import Enemy
from surfaces import Surface

######## Set up things that will not change
pygame.init()
pygame.display.set_caption('Healthless')
windowX = 640
windowY = 640
window = pygame.display.set_mode((windowX,windowY))
icon = pygame.image.load('pics/logo.png')
pygame.display.set_icon(icon)


bullet_image = pygame.image.load('pics/second_bullet.png')
enemy_bul_img = pygame.image.load('pics/bullet.png')
enemy_image = pygame.image.load('pics/32x64.png')
player_image = pygame.image.load('pics/32x64.png')
########

################################################################
def play():
    FPS = 70
    clock = pygame.time.Clock()
    start_color = (0,0,0)
    pygame.mouse.set_visible(False)
    enemy = Enemy()
    player = Player()
    test_surface = Surface()

    while True:
        for event in pygame.event.get():
        	if event.type == pygame.QUIT:
        		gamerun = False
        		pygame.quit(),sys.exit()
        		break

        window.fill((41, 64, 59)) # (41,64,59)

        test_surface.place(window,100,100)

        player.teleportation()
        player.shoot(window,start_color,bullet_image)
        player.draw(window,start_color,player_image)
        player.update(window,start_color,bullet_image)


        enemy.enemy_shoot(window,start_color,enemy_bul_img)
        enemy.draw(window,start_color,enemy_image)
        enemy.update()
        enemy.collision(enemy)

        if player.out_of_area():
            print(player.x, player.y)
            break

        if enemy.out_of_area():
            print('Random is on our side')
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
