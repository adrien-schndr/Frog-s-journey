import pygame
from pygame.locals import *

# Fenêtre
window_length = 1920
window_height = 1080
screen = pygame.display.set_mode((window_length, window_height), pygame.SCALED | pygame.FULLSCREEN)


# Textures
wooden_log_textures = []
for image in range(0, 18):
    texture = pygame.image.load("images/wood/wood_log_" + str(image) + ".png")
    texture = pygame.transform.scale(texture, (100, 100))
    wooden_log_textures.append(texture)

menu_background = "images/menu_background.png"
