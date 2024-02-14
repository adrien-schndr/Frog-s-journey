import pygame
from pygame.locals import *
import pygame.freetype

pygame.init()

last_unlocked_lvl = 1

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


class Frog(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        skin_frog = pygame.image.load("images/skin_menu/frogs/frog26.png").convert_alpha()
        skin_frog = pygame.transform.scale(skin_frog, (100, 100))
        self.image = pygame.Surface((100, 100), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.center = (50, 50)
        self.image.blit(skin_frog, (self.rect.x, self.rect.y))
        self.rect.x = 910

    def move(self, event):
        vitesse = 100

        if event.type == KEYDOWN and event.key == K_LEFT:
            if 0 <= self.rect.x - vitesse <= window_length - 100:
                self.rect.x -= vitesse
        if event.type == KEYDOWN and event.key == K_RIGHT:
            if 0 <= self.rect.x + vitesse <= window_length - 100:
                self.rect.x += vitesse
        if event.type == KEYDOWN and event.key == K_UP:
            if 0 <= self.rect.y - vitesse <= window_height - 100:
                self.rect.y -= vitesse
        if event.type == KEYDOWN and event.key == K_DOWN:
            if 0 <= self.rect.y + vitesse <= window_height - 100:
                self.rect.y += vitesse


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
        self.rect.center = (length/2, height/2)
        self.rect.x, self.rect.y = x, y
        self.dimensions = (length, height)
        self.speed = speed

    def update(self):
        self.rect.x += self.speed
        if self.rect.x >= window_length:
            self.rect.x = -self.dimensions[0]
        if self.isAnimated:
            self.index += 1
            if self.index >= len(self.skin):
                self.index = 0
            self.image = self.skin[self.index]
        return
