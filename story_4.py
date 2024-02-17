
from constantes import *

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()


GAME_FONT = pygame.freetype.Font("story_font.otf", 32)
TITLE_FONT = pygame.freetype.Font("story_font.otf", 40)

title = """LAYTON"""
texts = [
    """Félicitations, voyageur, pour votre avancée dans cette quête *ribbit*. Je remarque que""",
    """fardeau que vous portez semble s'alourdir de plus en plus, signe que vous avez accompli """,
    """des progrès considérables.""",
    """Cependant, le temps est un allié précieux que nous ne pouvons nous permettre de  """,
    """gaspiller. Chaque moment compte dans cette entreprise cruciale *ribbit*. Je vous """,
    """prie donc d'accélérer le pas dans votre exploration des niveaux à venir.""",
    """Je suis contraint de reprendre mes obligations rapidement, mais je vous encourage """,
    """à maintenir votre élan et votre détermination. Que rien ne vous arrête dans votre  """,
    """quête des épées légendaires *ribbit*.""",
    """Poursuivez votre chemin avec vigueur, voyageur. Que votre détermination soit  """,
    """aussi inébranlable que la force du courant. Bonne chance, et que les étoiles  """,
    """vous guident vers la victoire *ribbit*."""
]

# Constantes
menu = "images/story_screen_2.png"


def story_4():
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
                    from select_lvl import select_level
                    select_level()
    pygame.quit()
