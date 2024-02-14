from constantes import *

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()


GAME_FONT = pygame.freetype.Font("story_font.otf", 32)
TITLE_FONT = pygame.freetype.Font("story_font.otf", 40)

title = """LAYTON"""
texts = [
    """Bienvenue dans la première étape de votre périple, voyageur. Vous êtes désormais sur""",
    """le point de vous aventurer dans les profondeurs de notre royaume, où les défis et""",
    """les mystères abondent. Pour trouver la première des dix épées légendaires, vous devrez """,
    """traverser ce niveau avec diligence et habileté.""",
    """Utilisez les touches fléchées de votre clavier pour vous déplacer à travers ce""",
    """dédale de dangers. Le temps presse, donc ne tardez pas trop. Chaque seconde écoulée""",
    """vous rapproche de l'échec.""",
    """Attention aux obstacles qui jonchent votre chemin. Évitez-les avec agilité pour ne""",
    """pas compromettre votre progression. Seuls les plus habiles et les plus attentifs""",
    """réussiront à atteindre l'épée convoitée.""",
    """N'oubliez pas que votre quête est chronométrée. Le temps file comme le vent, et chaque""",
    """seconde compte. Soyez rapide, mais ne négligez pas la prudence.""",
    """Une fois que vous aurez atteint l'épée, votre aventure ne fera que commencer. Mais""",
    """pour cela, vous devez d'abord surmonter ce premier défi avec succès. Allez, brave""",
    """voyageur, que la chance soit avec vous."""
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
