import pygame
import pygame_menu
import sys
from settings import windowX,windowY, DEBUG, window_caption,logo,gamefont
from bullets import Bullet
from beings import *
from surfaces import SlowTimeSurf
from particles import *

pygame.init()
pygame.display.set_caption(window_caption)
window = pygame.display.set_mode((windowX,windowY))
pygame.display.set_icon(logo)
font = pygame.font.Font(gamefont, 46)

################################################################
def play():
    FPS = 70
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(False)
    slowsurf = SlowTimeSurf(384,64)
    enemy = Enemy(100,100)
    #enemies_on_screen.append(enemy)
    enemy2 = Enemy(windowX,200)
    #enemies_on_screen.append(enemy2)
    player = Player()
    death_timer = 70
    SCORE = 0
    ppp = False
########################## LAYER 0
    while True:
        for event in pygame.event.get():
        	if event.type == pygame.QUIT:
        		pygame.quit(),sys.exit()
        		break

        window.fill((41, 64, 59))
        pygame.draw.rect(window,(0,0,0),(0,720,windowX,5))

        if DEBUG == True:
            for row in range(0,windowX,32):
                pygame.draw.rect(window,(184, 227, 179, 1),(row,0,2,windowY))
            for column in range(0,windowY,64):
                pygame.draw.rect(window,(184, 227, 179),(0,column,windowX,2))


########################## LAYER 0 END

########################## LAYER 1
        if slowsurf.switch == True:
            slowsurf.place(window)
            if slowsurf.collide(player.player_rect):
                print("Colliding !")
                slowsurf.switch = False
        else:
            if slowsurf.activation_timer >= 0:
                slowsurf.activation_timer -= 1
                enemy.vel = 3 - 2
                enemy2.vel = 3 - 2
                enemy.bul_cooldown += 1.5
                enemy2.bul_cooldown += 1.5
            else:
                enemy.refresh()
                enemy2.refresh()


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

########################## LAYER 1 END

########################## LAYER 2
        if enemy.alive == True:
            enemy.draw(window)
            enemy.move('right')
            enemy.enemy_shoot(window)
            enemy.collision(window)
            if enemy.enemy_x >= windowX-10: #That returning thingy
                enemy.enemy_x = 5

        if enemy2.alive == True:
            enemy2.draw(window)
            enemy2.enemy_shoot(window)
            enemy2.move('left')
            enemy2.collision(window)
            if enemy2.enemy_x <= 5: #That returning thingy
                enemy2.enemy_x = windowX

        if enemy.out_of_area() and enemy.alive == True or enemy.enemy_y + enemy.en_height >= 720 and enemy.alive == True:
            enemy.alive = False
            SCORE += 1
        if enemy2.out_of_area() and enemy2.alive == True or enemy2.enemy_y + enemy2.en_height >= 720 and enemy2.alive == True:
            enemy2.alive = False
            SCORE += 1

        if enemy.alive == False and enemy2.alive == False:
            print('Win-win')
            break

        # for enemy in enemies_on_screen:
        #     if enemy[0].alive == True:
        #         enemy[0].move('right')
        #         enemy[0].enemy_shoot(window)
        #         enemy[0].draw(window)
        #         enemy[0].collision(window)
        #     else:
        #         enemy[0].draw(window)
########################## LAYER 2 END

########################## LAYER 3
        score_font = font.render(str(SCORE), True, (114, 150, 47))
        window.blit(score_font,(100,100))
########################## LAYER 3 END
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
