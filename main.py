import pygame
import sys
from pygame.locals import *

# Colours
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)

# Left bat properties
left_bat = 200
left_bat_speed = 0

# Right bat properties
right_bat = 200
right_bat_speed = 0

# Ball properties
ball_x = 320
ball_y = 240
ball_speed_x = 3
ball_speed_y = 3

# Frame rate
fps = 30
fps_clock = pygame.time.Clock()

# Scores
score = [0, 0]

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Pong')

# The font
font = pygame.font.SysFont("Helvetica", 60)
font.set_bold(True)

# Game Loop
while True:
    # Background
    screen.fill(black)

    # Draw ball
    pygame.draw.circle(screen, white, (int(ball_x), int(ball_y)), 10)

    # Draw Left bat
    pygame.draw.rect(screen, red, (0, left_bat, 20, 80))

    # Draw right bat
    pygame.draw.rect(screen, red, (620, right_bat, 20, 80))
    # Print scores
    left_score = font.render(str(score[0]), True, red)
    right_score = font.render(str(score[1]), True, red)
    left_score_rect = left_score.get_rect()
    right_score_rect = right_score.get_rect()
    left_score_rect.center = (40, 40)
    left_score_rect.center = (600, 40)

    screen.blit(left_score, left_score_rect)
    screen.blit(right_score, right_score_rect)


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_a:
                left_bat_speed = -5
            elif event.key == K_z:
                left_bat_speed = 5
            elif event.key == K_k:
                right_bat_speed = -5
            elif event.key == K_m:
                right_bat_speed = 5
        if event.type == KEYUP:
            if event.key == K_a or event.key == K_z:
                left_bat_speed = 0
            elif event.key == K_k or event.key == K_m:
                right_bat_speed = 0

    # move left bat ensuring it stays on the screen
    if left_bat >= 0 and left_bat_speed < 0:
        left_bat += left_bat_speed
    elif left_bat <= 400 and left_bat_speed > 0:
        left_bat += left_bat_speed

    # move right bat ensuring it stays on the screen
    if right_bat >= 0 and right_bat_speed < 0:
        right_bat += right_bat_speed
    elif right_bat <= 400 and right_bat_speed > 0:
        right_bat += right_bat_speed

    # check to see if ball hits edge of screen and bounce if it does
    if ball_y < 10 or ball_y > 470:
        ball_speed_y *= - 1

    # move ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # check if bat hits ball or if it has gone out of court
    if ball_x < 30:
        if pygame.Rect(0, left_bat, 20, 80).colliderect((ball_x-10, ball_y+10, 20, 20)):
            ball_speed_x *= -1.1
            ball_speed_y *= 1.1
        elif ball_speed_x < 0:
            score[1] += 1
            ball_x = 320
            ball_y = 240
            ball_speed_x = 3
            ball_speed_y = 3
    if ball_x > 610:
        if pygame.Rect(620, right_bat, 20, 80).colliderect((ball_x-10, ball_y+10, 20, 20)):
            ball_speed_x *= -1.1
            ball_speed_y *= 1.1
        elif ball_speed_x > 0:
            score[0] += 1
            ball_x = 320
            ball_y = 240
            ball_speed_x = 3
            ball_speed_y = 3



    pygame.display.update()

    # Tick at desired frame rate
    fps_clock.tick(fps)
