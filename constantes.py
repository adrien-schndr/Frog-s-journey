import pygame
# noinspection PyUnresolvedReferences
import json
from pygame.locals import *
import pygame.freetype

pygame.init()


clock = pygame.time.Clock()


# Fenêtre
window_length, window_height = 1920, 1080
screen = pygame.display.set_mode((window_length, window_height), pygame.SCALED | pygame.FULLSCREEN)


# Textures
wooden_log_textures = []
for image in range(0, 18):
    texture = pygame.image.load("images/wood/wood_log_" + str(image) + ".png")
    texture = pygame.transform.scale(texture, (100, 100))
    wooden_log_textures.append(texture)

reverse_wooden_log_textures = []
for image in range(0, 18):
    texture = pygame.image.load("images/wood/wood_log_" + str(17-image) + ".png")
    texture = pygame.transform.scale(texture, (100, 100))
    reverse_wooden_log_textures.append(texture)

rabbit_textures = []
for image in range(0, 16):
    texture = pygame.image.load("images/rabbit/rabbit_" + str(image) + ".png")
    texture = pygame.transform.scale(texture, (100, 100))
    rabbit_textures.append(texture)

menu_background = "images/menu_background.png"


class Frog(pygame.sprite.Sprite):
    def __init__(self, chosen_skin):
        super().__init__()
        skin_frog = pygame.image.load("images/skin_menu/frogs/" + chosen_skin + ".png").convert_alpha()
        skin_frog = pygame.transform.scale(skin_frog, (100, 100))
        self.image = pygame.Surface((100, 100), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.center = (50, 50)
        self.image.blit(skin_frog, (self.rect.x, self.rect.y))
        self.rect.x = 900

    def move(self, event, direction=""):
        vitesse = 100

        if (event.type == KEYDOWN and event.key == K_LEFT) or direction == "left":
            direction = "left"
            if 0 <= self.rect.x - vitesse <= window_length - 100:
                self.rect.x -= vitesse
                return direction
        if (event.type == KEYDOWN and event.key == K_RIGHT) or direction == "right":
            direction = "right"
            if 0 <= self.rect.x + vitesse <= window_length - 100:
                self.rect.x += vitesse
                return direction
        if (event.type == KEYDOWN and event.key == K_UP) or direction == "up":
            direction = "up"
            if 0 <= self.rect.y - vitesse <= window_height - 100:
                self.rect.y -= vitesse
                return direction
        if (event.type == KEYDOWN and event.key == K_DOWN) or direction == "down":
            direction = "down"
            if 0 <= self.rect.y + vitesse <= window_height - 100:
                self.rect.y += vitesse
                return direction


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, length, height, skin, speed):
        super().__init__()
        self.image = pygame.Surface((length, height), pygame.SRCALPHA)
        self.skin = skin
        if type(self.skin) is str:  # Non animé
            self.isAnimated = False
            skin_obstacle = pygame.image.load("images/" + self.skin + ".png").convert_alpha()
            skin_obstacle = pygame.transform.scale(skin_obstacle, (length, height))
            self.image.blit(skin_obstacle, (0, 0))
        if type(self.skin) is list:
            self.index = 0
            self.isAnimated = True
            self.images = []
            for image in skin:
                self.images.append(image)
            self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.init_position = (x, y)
        self.rect.center = (length/2, height/2)
        self.rect.x, self.rect.y = x, y
        self.dimensions = (length, height)
        self.speed = speed

    def update(self):
        self.rect.x += self.speed
        if self.rect.x >= window_length and self.speed > 0:
            self.rect.x = -self.dimensions[0]
        if self.rect.x < 0-self.dimensions[0] and self.speed < 0:
            self.rect.x = 1920
        if self.isAnimated:
            self.index += 1
            if self.index >= len(self.skin):
                self.index = 0
            self.image = self.skin[self.index]
        return
