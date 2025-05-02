import pygame, sys
from random import choice
from player import Player
from ball import Ball

# Initialize pygame
pygame.init()
clock = pygame.time.Clock()

score = 0

# Setting screen
screen = pygame.display.set_mode((900, 700))
pygame.display.set_caption("Play game")
font = pygame.font.Font("Catcher/fonts/Bangers/Bangers-Regular.ttf", 50)

bg_pic = pygame.image.load("Catcher/images/background.png")
game_over_sound = pygame.mixer.Sound("Catcher/audio/game_over.wav")
bg_music = pygame.mixer.Sound("Catcher/audio/background.mp3")
bg_music.play(loops= -1)

catch_sound = pygame.mixer.Sound("Catcher/audio/catch.mp3")

# Intro screen
game_title = font.render("Press Space to start", False, "#1F1717")
game_title_rect = game_title.get_rect(center=(450, 300))


# Player
basket = pygame.sprite.GroupSingle()
basket.add(Player())

# Ball
obstacle = pygame.sprite.Group()


def display_score():
        score_surf = font.render(f"Score: {score}", False, (64, 64, 64))
        score_rect = score_surf.get_rect(center=(800, 30))
        screen.blit(score_surf, score_rect)


def collision():
    for enemy in obstacle:
        if pygame.sprite.spritecollideany(basket.sprite, obstacle):
            obstacle.remove(enemy)
            global score
            score += 1
            catch_sound.play()
    return True

# Timer
obstacle_speed = 2000
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, obstacle_speed)


# game active
game_active = False
while True:

    # Game events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # Intro screen 
        if not game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active = True
        else:
            if event.type == obstacle_timer:
                obstacle.add(Ball(choice(['ball1', 'ball2', 'ball3'])))

    if game_active:
        # Drawing the background, player and ball
        screen.blit(bg_pic, (0, 0))


        basket.draw(screen)
        basket.update()

        obstacle.draw(screen)
        obstacle.update()   

        game_active = collision()

        display_score()

                
        # game over state
        for enemy in obstacle:
            if enemy.rect.y >= 670:
                obstacle.remove(enemy)
                game_over_sound.play()
                game_active = False
                
    else:
        screen.blit(bg_pic, (0, 0))
        screen.blit(game_title, game_title_rect)
        score = 0
        obstacle.empty()
    

    pygame.display.update()
    clock.tick(60)