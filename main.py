from calendar import month
import pygame
import random
from pygame.examples.go_over_there import screen, running

pygame.init()
running = True
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Игра Тир")

icon = pygame.image.load("img/png-transparent-infographic-shooting-target.png")
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/target.png")
target_width = 80
target_height = 80

target_x = random.randint(0,SCREEN_WIDTH-target_width)
target_y = random.randint(0, SCREEN_HEIGHT-target_height)
color = 133
score = 0

while running:
    screen.fill(color)
    font = pygame.font.SysFont('couriernew', 20)
    text = font.render(str(score), True, 'green')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x< target_x+target_width and target_y < mouse_y< target_y+target_width:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                score = score+1

#Отрисовка мишени
    screen.blit(target_img, (target_x, target_y))
#Отрисовка счетчика попаданий
    screen.blit(text, (750, 10))
    pygame.display.update()

pygame.quit()