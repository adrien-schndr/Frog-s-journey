
import pygame.freetype
from constantes import *

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()

# Définition des constantes
fond = "images/final.png"
TEXT_COLOR = (0, 0, 0)
TEXT_START_POSITION = (350, 50)
TEXT_LINE_SPACING = 20  # Espacement vertical entre chaque ligne de texte

# Charger les polices
GAME_FONT = pygame.freetype.Font("story_font.otf", 32)

# Textes à afficher
texts = [
    """Dans la tranquillité des marais, le voyageur, après d'innombrables épreuves,""",
    """atteignit enfin son objectif ultime. Il rassembla les dix épées légendaires, leur """,
    """lueur éclatant dans la pénombre de la nuit. Layton, qui l'avait guidé à travers """,
    """chaque défi, observait avec satisfaction cet accomplissement.""",
    """ """,
    """ """,
    """Mais alors que le voyageur, épuisé mais triomphant, se retournait pour partager son""",
    """succès avec Layton, il fut frappé  par une trahison inattendue. Le regard de Layton avait""",
    """changé, devenant froid et impitoyable. Sans un mot, Layton dégaina une lame, l'une des dix """,
    """épées autrefois convoitées, et l'abattit avec une précision mortelle sur le voyageur.""",
    """ """,
    """Le bruit du métal contre la chair déchira la quiétude de la nuit, alors que le voyageur tombait""",
    """au sol, sa vie s'échappant de lui. Layton, désormais révélé comme un traître, contempla froidement""",
    """son acte, son regard dénué de remords.""",
    """ """,
    """Pendant tout ce temps, les épées légendaires n'étaient pas un symbole de protection, mais un moyen""",
    """pour Layton de s'emparer du pouvoir absolu, même au prix du sang de ceux qu'il avait guidés. Avec le""",
    """voyageur gisant sans vie à ses pieds, Layton tenait désormais entre ses mains l'ultime pouvoir, prêt""",
    """à plonger le royaume dans les ténèbres."""
    """ """,
    """ """,
    """Ainsi se termina l'histoire de la quête des dix épées légendaires, un récit de courage, de trahison et""",
    """de destinée tragique, laissant le royaume plongé dans une obscurité sans fin."""
]


def creation_fenetre():

    # Charger l'image de fond
    menu_background = pygame.image.load(fond).convert()
    menu_background = pygame.transform.scale(menu_background, (window_length, window_height))
    screen.blit(menu_background, (0, 0))

    pygame.display.flip()

    line_number = 0
    longueur = 0
    running = True

    while running:
        screen.blit(menu_background, (0, 0))
        clock.tick(20)
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_ESCAPE or event.type == pygame.QUIT:
                running = False
        if line_number == 0:
            text_surface0, rect = GAME_FONT.render(texts[line_number][0:longueur], (0, 0, 0))
            screen.blit(text_surface0, (150, 725))
            longueur += 1
        pygame.display.flip()


    # while running:
    #     screen.blit(menu_background, (0, 0))
    #     clock.tick(20)
    #
    #     for event in pygame.event.get():
    #         if event.type == KEYDOWN and event.key == K_ESCAPE or event.type == pygame.QUIT:
    #             running = False
    #
    #     # Affichage du texte
    #     y_position = TEXT_START_POSITION[1]  # Position verticale du texte
    #     for i in range(text_number + 1):
    #         text_surface, rect = GAME_FONT.render(texts[i], TEXT_COLOR)
    #         text_width, text_height = rect.size
    #         x_position = (window_length - text_width) // 2  # Calculer la position horizontale pour centrer le texte
    #         screen.blit(text_surface, (x_position, y_position))
    #         y_position += text_height + TEXT_LINE_SPACING  # Mettre à jour la position verticale pour le prochain texte
    #
    #     pygame.display.flip()
    #
    #     pygame.time.wait(500)
    #     text_number += 1
    #
    #     for ligne in texts:
    #         for lettre in ligne:
    #
    #
    #     if text_number >= len(texts):
    #         pygame.time.wait(2000)
    #         running = False
    #         import endgame_message

    pygame.quit()


creation_fenetre()
