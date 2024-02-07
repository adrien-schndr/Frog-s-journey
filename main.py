import math
import pygame
from pygame.locals import *


class Frog(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        skin_frog = pygame.image.load("images/green_frog.png").convert_alpha()
        skin_frog = pygame.transform.scale(skin_frog, (100, 100))
        self.image = pygame.Surface((100, 100), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.center = (50, 50)
        self.image.blit(skin_frog, (self.rect.x, self.rect.y))
        self.rect.x = 910

    def move(self, event):
        vitesse = 100

        if event.type == KEYDOWN and event.key == K_LEFT:
            if 0 <= self.rect.x - vitesse <= 1920 - 100:
                self.rect.x -= vitesse
        if event.type == KEYDOWN and event.key == K_RIGHT:
            if 0 <= self.rect.x + vitesse <= 1920 - 100:
                self.rect.x += vitesse
        if event.type == KEYDOWN and event.key == K_UP:
            if 0 <= self.rect.y - vitesse <= 1080 - 100:
                self.rect.y -= vitesse
        if event.type == KEYDOWN and event.key == K_DOWN:
            if 0 <= self.rect.y + vitesse <= 1080 - 100:
                self.rect.y += vitesse


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, length, height, skin, speed):
        super().__init__()
        skin_obstacle = pygame.image.load("images/" + skin + ".png").convert_alpha()
        skin_obstacle = pygame.transform.scale(skin_obstacle, (length, height))
        self.image = pygame.Surface((length, height), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.center = (length/2, height/2)
        self.image.blit(skin_obstacle, (0, 0))
        self.rect.x, self.rect.y = x, y
        self.dimensions = (length, height)
        self.speed = speed

    def move(self):
        self.rect.x += self.speed
        if self.rect.x >= 1920:
            self.rect.x = -self.dimensions[0]
        return


pygame.init()
screen = pygame.display.set_mode((1920, 1080), pygame.SCALED | pygame.FULLSCREEN)
clock = pygame.time.Clock()

player = Frog()

grille_lvl_1 = [
    [Obstacle(0, 100, 800, 100, "train", 10)],
    [Obstacle(0, 200, 200, 100, "yellow_car", 5)],
    [Obstacle(0, 300, 200, 100, "blue_car", 15), Obstacle(500, 300, 200, 100, "blue_car", 15), Obstacle(800, 300, 200, 100, "blue_car", 15)],
    [],
    [],
    [],
    [],
    [],
    []
]


# Chargement du background
background_png = pygame.image.load("images/background.png").convert_alpha()
scroll = 0
tiles = math.ceil(1080 / background_png.get_height()) + 1


running = True
while running:
    # Rafraichissement fen^tre
    screen.blit(background_png, (0, 0))
    pygame.sprite.Group(player).draw(screen)
    pygame.sprite.Group(ligne_obstacle for ligne_obstacle in grille_lvl_1).draw(screen)
    pygame.display.flip()
    clock.tick(60)

    for ligne_obstacle in grille_lvl_1:
        pygame.sprite.Group(ligne_obstacle).draw(screen)

        if pygame.sprite.spritecollide(player, ligne_obstacle, False):
            player.rect.x, player.rect.y = 910, 0

        for obstacle in ligne_obstacle:
            obstacle.move()

    # Quitter le jeu
    for event in pygame.event.get():
        player.move(event)
        if (event.type == KEYDOWN and event.key == K_ESCAPE) or event.type == pygame.QUIT:
            pygame.quit()
            running = False

pygame.quit()

# # Déplacement background
# i = 0
# while i < tiles:
#     screen.blit(background_png, (0, background_png.get_height() * i + scroll))
#     i += 1
# scroll -= 0.75
# if abs(scroll) > background_png.get_height():
#     scroll = 0
