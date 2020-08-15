import pygame
import pygame_menu
import sys
from bullets import Bullet
from beings import *
from surfaces import Surface
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
    enemy = Enemy()
    player = Player()
    death_timer = 70
    text = font.render(str(death_timer), True,(0,0,0)) #Declaring just for rect
    text_rect = text.get_rect(center = (windowX//2,windowY//2 - 100))
    # lower_surface = Surface('killsurf')
    # main_surface = Surface('default')

    while True:
        for event in pygame.event.get():
        	if event.type == pygame.QUIT:
        		gamerun = False
        		pygame.quit(),sys.exit()
        		break

        window.fill((41, 64, 59))

        # lower_surface.place(window,0,0)
        # main_surface.place(window,145,145)

        player.teleportation()
        player.shoot(window)
        player.draw(window)
        player.update()
        player.collision()
        if player.out_of_area():
            death_timer -= 1
            timertext_color = (255-death_timer-60,3.6*death_timer,10)
            text = font.render(str(death_timer), True, timertext_color) #Actual text
            window.blit(text,text_rect)
            if death_timer <= 1:
                print('DED')
                break
        else:
            death_timer = 70


        enemy.enemy_shoot(window)
        enemy.draw(window)
        enemy.move('right')

        if enemy.enemy_x >= windowX-10: #That returning thingy
            enemy.enemy_x = 5
        enemy.collision()

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
