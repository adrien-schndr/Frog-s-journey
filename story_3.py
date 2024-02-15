from constantes import *

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()


GAME_FONT = pygame.freetype.Font("story_font.otf", 32)
TITLE_FONT = pygame.freetype.Font("story_font.otf", 40)

title = """LAYTON"""
texts = [
    """Bravo, voyageur ! Vous avez franchi avec succès les épreuves de ce premier niveau.""",
    """Votre agilité et votre détermination sont remarquables *ribbit*. Continuez ainsi sur""",
    """cette voie, et vous accomplirez des exploits encore plus grands. """,
    """Malheureusement, le devoir m'appelle. Je dois m'absenter pour ne pas être en retard""",
    """à mon thé avec la Reine des Nénuphars *ribbit*. Mais ne vous inquiétez pas, je serai""",
    """toujours là pour vous guider à distance, tel un phare dans l'obscurité.""",
    """Quant aux épées que vous cherchez, elles ne sont pas de simples armes *ribbit*. Elles""",
    """renferment un pouvoir ancestral, capable de déverrouiller les portes des dimensions""",
    """oubliées et de protéger notre royaume contre les forces du mal *ribbit*. Leur utilité """,
    """dépasse de loin leur simple aspect de trésor. Elles sont les gardiennes de notre """,
    """histoire et de notre avenir.""",
    """Continuez votre quête avec courage et persévérance, voyageur *ribbit*. Puissent """,
    """ces épées vous guider vers la victoire et l'accomplissement de votre destinée *ribbit*."""
]

# Constantes
menu = "images/story_screen_2.png"


def creation_fenetre():
    menu_background = pygame.image.load(menu).convert()
    menu_background = pygame.transform.scale(menu_background, (1920, 1080))
    screen.blit(menu_background, (0, 0))
    pygame.display.flip()

    pygame.display.flip()
    longueur = 0
    text_number = 0

    running = True  # Variable pour contrôler la boucle principale
    while running:
        screen.blit(menu_background, (0, 0))
        clock.tick(20)
        title_surface, rect = TITLE_FONT.render(title, (0, 0, 0))
        screen.blit(title_surface, (125, 665))
        if text_number == 0:
            text_surface0, rect = GAME_FONT.render(texts[text_number][0:longueur], (0, 0, 0))
            screen.blit(text_surface0, (150, 725))
            longueur += 1
        if longueur >= len(texts[text_number]) and text_number < len(texts)-1:
            text_number += 1
            longueur = 0
        if text_number >= 1:
            text_surface0, rect = GAME_FONT.render(texts[text_number-1], (0, 0, 0))
            text_surface1, rect = GAME_FONT.render(texts[text_number][0:longueur], (0, 0, 0))
            screen.blit(text_surface0, (150, 725))
            screen.blit(text_surface1, (150, 775))
            longueur += 1
        pygame.display.flip()
        for event in pygame.event.get():
            if (event.type == KEYDOWN and event.key == K_ESCAPE) or event.type == pygame.QUIT:
                running = False  # Quitter la boucle principale si l'utilisateur ferme la fenêtre
                pygame.quit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1:  # Vérifier le clic de souris
                # Récupérer les coordonnées du clic
                clic_x, clic_y = event.pos
                print(clic_x, clic_y)
                if 1313 < clic_x < 1366 and 828 < clic_y < 941:
                    running = False
                    import select_lvl
    pygame.quit()

creation_fenetre()