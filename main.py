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

    def deplacer_joueur(self):
        vitesse = 10
        touches_clavier = pygame.key.get_pressed()
        if touches_clavier[pygame.K_LEFT]:
            if 0 <= self.rect.x - vitesse <= 1920 - 100:
                self.rect.x -= vitesse
        if touches_clavier[pygame.K_RIGHT]:
            if 0 <= self.rect.x + vitesse <= 1920 - 100:
                self.rect.x += vitesse
        if touches_clavier[pygame.K_UP]:
            if 0 <= self.rect.y - vitesse <= 1080 - 100:
                self.rect.y -= vitesse
        if touches_clavier[pygame.K_DOWN]:
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


pygame.init()
screen = pygame.display.set_mode((1920, 1080), pygame.SCALED | pygame.FULLSCREEN)
clock = pygame.time.Clock()

joueur = Frog()

liste_obstacles = []
train = Obstacle(0, 100, 800, 100, "train", 10)
pink_car = Obstacle(0, 200, 200, 100, "pink_car", 5)
liste_obstacles.append(train)
liste_obstacles.append(pink_car)


# Chargement du background
background_png = pygame.image.load("images/background.png").convert_alpha()
scroll = 0
tiles = math.ceil(1080 / background_png.get_height()) + 1


def collision(objet1, objet2) -> bool:
    return objet1.rect.colliderect(objet2.rect)


running = True
while running:
    # Rafraichissement fen^tre
    joueur.deplacer_joueur()
    pygame.sprite.Group(joueur).draw(screen)
    pygame.sprite.Group(liste_obstacles).draw(screen)
    pygame.display.flip()
    clock.tick(60)

    if pygame.sprite.spritecollide(joueur, liste_obstacles, False):
        joueur.rect.x, joueur.rect.y = 910, 0

    for obstacle in liste_obstacles:
        obstacle.rect.x += obstacle.speed
        if obstacle.rect.x >= 1920:
            obstacle.rect.x = -obstacle.dimensions[0]

    # Déplacement background
    i = 0
    while i < tiles:
        screen.blit(background_png, (0, background_png.get_height() * i + scroll))
        i += 1
    scroll -= 0.75
    if abs(scroll) > background_png.get_height():
        scroll = 0

    # Quitter le jeu
    for event in pygame.event.get():
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            running = False
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
