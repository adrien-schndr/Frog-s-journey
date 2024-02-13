import pygame.freetype
from constantes import *

pygame.init()
pygame.font.init()


GAME_FONT = pygame.freetype.Font("story_font.otf", 32)
TITLE_FONT = pygame.freetype.Font("story_font.otf", 48)


# Constantes
menu = "images/story_screen.png"


def creation_fenetre():
    """ création d'une fenêtre de taille largeur x hauteur"""
    global fenetre
    fenetre = pygame.display.set_mode((1920, 1080), pygame.SCALED | pygame.FULLSCREEN)
    menu_background = pygame.image.load(menu).convert()
    menu_background = pygame.transform.scale(menu_background, (1920, 1080))
    fenetre.blit(menu_background, (0, 0))
    pygame.display.flip()
    title_surface, rect = GAME_FONT.render("""LAYTON""", (0, 0, 0))
    text_surface, rect = GAME_FONT.render("""Ah voyageur intrépide, *ribbit* bienvenue dans ces contrées sylvestres. Je suis Layton, """, (0, 0, 0))
    text_surface2, rect = GAME_FONT.render("""Chef de la Guilde, gardien de ces marais ancestraux.""", (0, 0, 0))
    screen.blit(title_surface, (125, 675))
    screen.blit(text_surface, (150, 725))
    screen.blit(text_surface2, (150, 775))
    pygame.display.flip()

    running = True  # Variable pour contrôler la boucle principale
    while running:
        fenetre.blit(menu_background, (0, 0))
        for event in pygame.event.get():
            if (event.type == KEYDOWN and event.key == K_ESCAPE) or event.type == pygame.QUIT:
                pygame.quit()
                running = False  # Quitter la boucle principale si l'utilisateur ferme la fenêtre
            if event.type == MOUSEBUTTONDOWN and event.button == 1:  # Vérifier le clic de souris
                # Récupérer les coordonnées du clic
                clic_x, clic_y = event.pos
                if 1349 < clic_x < 1407 and 854 < clic_y < 959:
                    running = False


creation_fenetre()
pygame.quit()
