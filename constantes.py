import pygame
# noinspection PyUnresolvedReferences
import json
from pygame.locals import *
import pygame.freetype

pygame.init()


clock = pygame.time.Clock()

with open('save.txt') as load_file:
    data = json.load(load_file)
frog_skin = data['frog_skin']
last_unlocked_lvl = data['last_unlocked_lvl']

# Fenêtre
window_length, window_height = 1920, 1080
screen = pygame.display.set_mode((window_length, window_height), pygame.SCALED | pygame.FULLSCREEN)