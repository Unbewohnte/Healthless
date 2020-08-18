import pygame
import pygame_menu
import sys
from bullets import Bullet
from beings import *
from surfaces import Surface
from particles import *
######## Set up things that will not change
pygame.init()
pygame.display.set_caption('Healthless')
windowX = 832
windowY = 832
window = pygame.display.set_mode((windowX,windowY))
icon = pygame.image.load('pics/logo.png')
pygame.display.set_icon(icon)
font = pygame.font.Font('freesansbold.ttf', 46)
########

################################################################
def play():
    FPS = 70
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(False)
    enemy = Enemy(100,100)
    enemy2 = Enemy(windowX,200)
    player = Player()
    death_timer = 70
##########################
    while True:
        for event in pygame.event.get():
        	if event.type == pygame.QUIT:
        		gamerun = False
        		pygame.quit(),sys.exit()
        		break

        window.fill((41, 64, 59))
        pygame.draw.rect(window,(0,0,0),(0,720,windowX,5))
##########################

#PPPPPPPPPPPPPPPPPPPPPPPPP
        player.teleportation()
        player.shoot(window)
        player.draw(window)
        player.update()
        player.collision(window)
        if player.out_of_area():
            death_timer -= 1
            timertext_color = (255-death_timer-60,3.6*death_timer,10)
            text = font.render(str(death_timer), True, timertext_color)
            window.blit(text,(windowX//2,windowY//2 - 100))
            if death_timer <= 1:
                print('DED')
                break
        else:
            death_timer = 70
#PPPPPPPPPPPPPPPPPPPPPPPPP

#EEEEEEEEEEEEEEEEEEEEEEEEE
        if enemy.alive == True:
            enemy.enemy_shoot(window)
            enemy.draw(window)
            enemy.move('right')
            enemy.collision(window)
            if enemy.enemy_x >= windowX-10: #That returning thingy
                enemy.enemy_x = 5

        if enemy2.alive == True:
            enemy2.enemy_shoot(window)
            enemy2.move('left')
            enemy2.draw(window)
            enemy2.collision(window)
            if enemy2.enemy_x <= 5: #That returning thingy
                enemy2.enemy_x = windowX

        if enemy.out_of_area() or enemy.enemy_y + enemy.en_height >= 720:
            enemy.alive = False
        if enemy2.out_of_area() or enemy2.enemy_y + enemy2.en_height >= 720:
            enemy2.alive = False

        if enemy.alive == False and enemy2.alive == False:
            print('Win-win')
            break
#EEEEEEEEEEEEEEEEEEEEEEEEE

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
