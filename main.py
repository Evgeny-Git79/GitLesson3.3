import pygame
<<<<<<< HEAD
=======
import random
>>>>>>> Part_Const_Code
from pygame.examples.go_over_there import screen, running

pygame.init()
running = True
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Игра Тир")
<<<<<<< HEAD
icon = pygame.image.load()
=======
icon = pygame.image.load("img/png-transparent-infographic-shooting-target.png")
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/target.png")
target_width = 80
target_height = 80

target_x = random.randint(0,SCREEN_WIDTH-target_width)
target_y = random.randint(0, SCREEN_HEIGHT-target_height)



>>>>>>> Part_Const_Code
while running:
    pass

pygame.quit()