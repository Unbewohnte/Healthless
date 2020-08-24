import pygame
import pygame_menu
import sys
from settings import windowX,windowY, DEBUG, window_caption,logo,gamefont, FPS
from bullets import Bullet
from beings import *
from surfaces import SlowTimeSurf, BuffRandomSurf
from particles import *

pygame.init()
pygame.display.set_caption(window_caption)
window = pygame.display.set_mode((windowX,windowY))
pygame.display.set_icon(logo)
font = pygame.font.Font(gamefont, 46)

################################################################
def play():
    if DEBUG == True:
        from bullets import player_bullets_on_screen,enemy_bul_on_screen
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(False)
    slowsurf = SlowTimeSurf(384,64)
    randsurf = BuffRandomSurf(540,64)
    enemy = Enemy(100,100)
    enemy2 = Enemy(windowX,200)
    enemies_on_screen.append(enemy)
    enemies_on_screen.append(enemy2)
    print(enemies_on_screen)
    player = Player()
    
    death_timer = 1.5
    death_timer_calculation = (death_timer/70)/death_timer
    SCORE = 0
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
            #print('power_of_random: ',player.power_of_random)
            print('bullets_on_screen: ', str(len(player_bullets_on_screen + enemy_bul_on_screen)))


########################## LAYER 0 END

########################## LAYER 1
        if slowsurf.switch == True:
            slowsurf.place(window)
            if slowsurf.collide(player.player_rect):
                print("<Sakuya slows the flow of time !>")
                slowsurf.switch = False
        else:
            #for enemy in enemies_on_screen: #Doesn`t work and I don`t know why
            slowsurf.activate(enemy)
            slowsurf.activate(enemy2)

        if randsurf.switch == True:
            randsurf.place(window)
            if randsurf.collide(player.player_rect):
                print('<Randoumu no pawa~ !>')
                randsurf.switch = False
        else:
            randsurf.activate(player)



        player.teleportation()
        player.shoot(window)
        player.draw(window)
        player.update()
        player.collision(window)

        if player.out_of_area():
            death_timer -= death_timer_calculation
            timertext_color = (255-death_timer*150,170*death_timer,10)
            text = font.render(str(round(death_timer,2)), True, timertext_color)
            window.blit(text,(windowX//2,windowY//2 - 100))
            if death_timer < 0.1:
                print('DED')
                if DEBUG == True:
                    print('TOTAL {}'.format(time.time()-start))
                break
        else:
            if DEBUG == True:
                start = time.time()
            death_timer = 1.5

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
