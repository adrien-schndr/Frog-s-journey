import pygame.freetype

from constantes import *

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()


GAME_FONT = pygame.freetype.Font("story_font.otf", 32)
TITLE_FONT = pygame.freetype.Font("story_font.otf", 40)

texts = [
    """As darkness falls, the Frog's Journey ends in betrayal.""",
    """Yet in the memory of courage, hope remains.""",
    """May the light guide our steps towards a brighter future."""
]

# Constantes
fond = "images/black.jpg"


def endgame_message():
    menu_background = pygame.image.load(fond).convert()
    menu_background = pygame.transform.scale(menu_background, (1920, 1080))
    screen.blit(menu_background, (0, 0))
    pygame.display.flip()

    longueur = 0
    text_number = 0

    running = True
    while running:
        screen.blit(menu_background, (0, 0))
        clock.tick(20)
        for event in pygame.event.get():
            if (event.type == KEYDOWN and event.key == K_ESCAPE) or event.type == pygame.QUIT:
                running = False  # Quitter la boucle principale si l'utilisateur ferme la fenêtre
        if longueur < len(texts[text_number]):
            text_surface, rect = GAME_FONT.render(texts[text_number][0:longueur], (255, 255, 255))
            screen.blit(text_surface, (150, 725))
            longueur += 1
            pygame.display.flip()
        else:
            pygame.time.wait(2000)  # Attendre 2 secondes avant de passer à la phrase suivante
            longueur = 0
            text_number += 1
            if text_number >= len(texts):
                pygame.time.wait(2000)
                from game_menu import menu
                menu()
                running = False
    pygame.quit()
