import pygame
import random
import math

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
dark_red = (200, 0, 0)
dark_green = (0, 200, 0)
blue = (0, 0, 255)

# sounds
point = pygame.mixer.Sound("point.wav")
hit = pygame.mixer.Sound("hit.wav")
pygame.mixer.music.load("background.wav")
# window
game_display = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Box Moving')
# background image
background_img = pygame.image.load('background.jpg')


def button(msg, x, y, w, h, ic, ac, text_x, text_y, action):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    pygame.draw.rect(game_display, ac, (x, y, w, h))
    all_font = pygame.font.Font('freesansbold.ttf', 15)
    all_display = all_font.render(msg, True, black)
    game_display.blit(all_display, (text_x, text_y))
    if x < mouse[0] < x+w and y < mouse[1] < y+h:
        pygame.draw.rect(game_display, ic, (x, y, w, h))
        game_display.blit(all_display, (text_x, text_y))
        if click[0] == 1 and action == 's':
            game_loop()
        if click[0] == 1 and action == 'e':
            pygame.quit()
            quit()
        if click[0] == 1 and action == 'c':
            unpaused()


pause = True


def unpaused():
    pygame.mixer.music.unpause()
    global pause
    pause = False


def paused():
    pygame.mixer.music.pause()
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    unpaused()
                if event.key == pygame.K_e:
                    pygame.quit()
                    quit()

        # border
        pygame.draw.line(game_display, black, (0, 0), (0, 600), 10)
        pygame.draw.line(game_display, black, (0, 600), (600, 600), 15)
        pygame.draw.line(game_display, black, (600, 600), (600, 0), 15)
        pygame.draw.line(game_display, black, (600, 0), (0, 0), 15)
        game_start_font = pygame.font.Font('freesansbold.ttf', 30)
        game_start_x = 200
        game_start_y = 80
        game_start_display = game_start_font.render('GAME PAUSED', True, red)
        game_display.blit(game_start_display, (game_start_x, game_start_y))
        button('CONTINUE', 170, 270, 90, 40, red, dark_red, 175, 285, 'c')
        button('EXIT', 400, 270, 60, 40, green, dark_green, 410, 285, 'e')

        pygame.display.update()


def gameintro():
    game_display.fill(white)
    pygame.display.set_caption('GAME')
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    game_loop()
                if event.key == pygame.K_e:
                    pygame.quit()
                    quit()

        # border
        pygame.draw.line(game_display, black, (0, 0), (0, 600), 10)
        pygame.draw.line(game_display, black, (0, 600), (600, 600), 15)
        pygame.draw.line(game_display, black, (600, 600), (600, 0), 15)
        pygame.draw.line(game_display, black, (600, 0), (0, 0), 15)
        game_start_font = pygame.font.Font('freesansbold.ttf', 30)
        game_start_x = 200
        game_start_y = 80
        game_start_display = game_start_font.render('GAME START', True, red)
        game_display.blit(game_start_display, (game_start_x, game_start_y))
        button('START', 170, 270, 60, 40, red, dark_red, 175, 285, 's')
        button('EXIT', 400, 270, 60, 40, green, dark_green, 410, 285, 'e')

        pygame.display.update()


# score text display
def scoreandliveandlevel(score, live, level):
    score_font = pygame.font.Font('freesansbold.ttf', 20)
    score_x = 10
    score_y = 10
    live_x = 10
    live_y = 30
    level_x = 10
    level_y = 50
    score_display = score_font.render('Score:'+str(score), True, (100, 0, 0))
    game_display.blit(score_display, (score_x, score_y))
    score_display = score_font.render('Live : '+str(live), True, (100, 0, 0))
    game_display.blit(score_display, (live_x, live_y))
    score_display = score_font.render('Level :'+str(level), True, (100, 0, 0))
    game_display.blit(score_display, (level_x, level_y))


def gameover():
    pygame.mixer.music.pause()
    gameover_font = pygame.font.Font('freesansbold.ttf', 50)
    gameover_display = gameover_font.render(
        'GAME OVER', True, (100, 200, 0))
    game_display.blit(gameover_display, (150, 200))


def scores(score):
    scores_font = pygame.font.Font('freesansbold.ttf', 50)
    scores_display = scores_font.render(
        'Score : '+str(score), True, (red))
    game_display.blit(scores_display, (190, 240))


def game_loop():
    enemy_other_y = 0
    enemy_red = random.randint(0, 255)
    enemy_green = random.randint(0, 255)
    enemy_blue = random.randint(0, 255)
    enemy_color = (100, 0, 30)
    pygame.mixer.music.play(-1)
    #score and live
    score = 0
    live = 3
    level = 1
    # player coordinates
    player_x = 250
    player_y = 500
    player_change_x = 0
    # player color
    Player_img = pygame.image.load("player.png")
    # enemy coordinates
    enemy_x = 32
    enemy_y = 28
    loop = True
    while loop:
        game_display.blit(background_img, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_change_x -= 5
                if event.key == pygame.K_RIGHT:
                    player_change_x = 5
                if event.key == pygame.K_e:
                    pygame.quit()
                    quit()
                if live > 0:
                    if event.key == pygame.K_p:
                        global pause
                        pause = True
                        paused()
                if live == 0:
                    if event.key == pygame.K_r:
                        game_loop()

            if event.type == pygame.KEYUP:
                player_change_x = 0
        player_x += player_change_x
        if player_x <= 6:
            player_x = 6
        if player_x >= 523:
            player_x = 523
        # border
        pygame.draw.line(game_display, black, (0, 0), (0, 600), 10)
        pygame.draw.line(game_display, black, (0, 600), (600, 600), 15)
        pygame.draw.line(game_display, black, (600, 600), (600, 0), 15)
        pygame.draw.line(game_display, black, (600, 0), (0, 0), 15)
        # player
        game_display.blit(Player_img, (player_x, player_y))
        scoreandliveandlevel(score, '', '')
        scoreandliveandlevel('', live, '')
        scoreandliveandlevel('', '', level)
        # enemy
        if enemy_y >= 570:
            point.play()
            enemy_y = 0
            enemy_x = random.randint(32, 573)
            score += 1
            scoreandliveandlevel(score, '', '')
            enemy_red += random.randint(0, 255)
            enemy_blue += 20
            enemy_green += random.randint(100, 200)
            if enemy_red <= 0 or enemy_green <= 0 or enemy_blue <= 0 or enemy_red >= 255 or enemy_green >= 255 or enemy_blue >= 255:
                enemy_red = random.randint(0, 255)
                enemy_green = random.randint(0, 255)
                enemy_blue = random.randint(0, 255)
            enemy_color = (enemy_red, enemy_green, enemy_blue)
            if score >= 20*level:
                enemy_other_y += 1
                level += 1
                scoreandliveandlevel('', '', level)
                if enemy_other_y >= 10:
                    enemy_other_y = 2
        enemy_y += enemy_other_y+3
        # collision
        collision = math.sqrt(math.pow(enemy_x-player_x, 2) +
                              math.pow(enemy_y-player_y, 2))
        if collision < 43.5:
            hit.play()
            enemy_x = random.randint(32, 573)
            enemy_y = 0
            live -= 1
            if live <= 0:
                live = 0
            scoreandliveandlevel('', live, '')
        if live == 0:
            gameover()
            scores(score)
            enemy_y = -100
            player_y = -300
        # enemy
        pygame.draw.rect(game_display, enemy_color, (enemy_x, enemy_y, 40, 40))

        pygame.display.update()


gameintro()
game_loop()
pygame.quit()
quit()
