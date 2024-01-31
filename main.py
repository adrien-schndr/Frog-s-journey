import pygame
from pygame.locals import *


class Frog(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        skin_frog = "images/green_frog.png"
        skin_frog = pygame.image.load(skin_frog).convert_alpha()
        skin_frog = pygame.transform.scale(skin_frog, (100, 100))
        self.image = pygame.Surface((100, 100), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.center = (50, 50)
        self.image.blit(skin_frog, (self.rect.x, self.rect.y))

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


pygame.init()
screen = pygame.display.set_mode((1920, 1080), pygame.SCALED | pygame.FULLSCREEN)
clock = pygame.time.Clock()

joueur = Frog()

background_png = "images/background.png"
background_png = pygame.image.load(background_png).convert_alpha()

running = True
while running:
    joueur.deplacer_joueur()
    screen.blit(background_png, (0, 0))
    pygame.sprite.Group(joueur).draw(screen)
    pygame.display.flip()
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            running = False
        if event.type == pygame.QUIT:
            running = False


pygame.quit()
