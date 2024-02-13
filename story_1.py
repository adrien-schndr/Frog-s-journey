from constantes import *

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()


GAME_FONT = pygame.freetype.Font("story_font.otf", 32)
TITLE_FONT = pygame.freetype.Font("story_font.otf", 40)

title = """LAYTON"""
texts = [
    """Ah voyageur intrépide, *ribbit* bienvenue dans ces contrées sylvestres. Je suis Layton,""",
    """Chef de la Guilde, gardien de ces marais ancestraux.""",
    """J’entrevois dans vos yeux une lueur de détermination et de bravoure *ribbit*. Je vous""",
    """confie une quête d’une importance capitale, même si vous ne l’avez peut être pas encore""",
    """souhaitée. Vous êtes désigné pour récupérer les dix épées légendaires, symbole de""",
    """pouvoir et de savoir ancien. Je vous servirais de guide n’ayez crainte *ribbit*. Il est""",
    """maintenant l’heure pour vous d’accomplir votre destinée.""",
    """Je vous souhaite bonne chance voyageur *ribbit*."""
]

# Constantes
menu = "images/story_screen.png"


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
        for event in pygame.event.get():
            if (event.type == KEYDOWN and event.key == K_ESCAPE) or event.type == pygame.QUIT:
                pygame.quit()
                running = False  # Quitter la boucle principale si l'utilisateur ferme la fenêtre
            if event.type == MOUSEBUTTONDOWN and event.button == 1:  # Vérifier le clic de souris
                # Récupérer les coordonnées du clic
                clic_x, clic_y = event.pos
                if 1349 < clic_x < 1407 and 854 < clic_y < 959:
                    running = False
                    import main
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


creation_fenetre()
pygame.quit()
