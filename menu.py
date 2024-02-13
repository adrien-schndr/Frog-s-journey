import pygame
from pygame.locals import *
pygame.init()

# Constantes
menu = "images/menu_background.png"


def creation_fenetre():
    """ création d'une fenêtre de taille largeur x hauteur"""
    global fenetre
    fenetre = pygame.display.set_mode((1920, 1080), pygame.SCALED | pygame.FULLSCREEN)
    menu_background = pygame.image.load(menu).convert()
    menu_background = pygame.transform.scale(menu_background, (1920, 1080))
    fenetre.blit(menu_background, (0, 0))
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
                print(clic_x, clic_y)
                if 735 < clic_x < 1241 and 517 < clic_y < 773:
                    running = False
                    # import ...
                if 682 < clic_x < 1292 and 806 < clic_y < 1028:
                    running = False
                    # import ...


creation_fenetre()
pygame.quit()
