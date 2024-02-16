import pygame.freetype
from constantes import *

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()

# Définition des constantes
fond = "images/final.png"
font = pygame.font.Font("story_font.otf", 34)

# Textes à afficher
texts = [
    """Dans la tranquillité des marais, le voyageur, après d'innombrables épreuves,""",
    """atteignit enfin son objectif ultime. Il rassembla les dix épées légendaires, leur""",
    """lueur éclatant dans la pénombre de la nuit. Layton, qui l'avait guidé à travers""",
    """chaque défi, observait avec satisfaction cet accomplissement.""",
    """ """,
    """ """,
    """Mais alors que le voyageur, épuisé mais triomphant, se retournait pour partager son""",
    """succès avec Layton, il fut frappé  par une trahison inattendue. Le regard de Layton avait""",
    """changé, devenant froid et impitoyable. Sans un mot, Layton dégaina une lame, l'une des dix""",
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


def story_final():

    # Charger l'image de fond
    menu_background = pygame.image.load(fond).convert()
    menu_background = pygame.transform.scale(menu_background, (window_length, window_height))
    screen.blit(menu_background, (0, 0))

    pygame.display.flip()

    running = True

    while running:
        hauteur_texte = window_height // 2 - len(texts) * font.get_height() // 2
        for texte in texts:
            texte_surface = font.render(texte, True, (0, 0, 0))
            x_position = window_length // 2 - texte_surface.get_width() // 2
            for lettre in texte:
                lettre_surface = font.render(lettre, True, (0, 0, 0))
                screen.blit(lettre_surface, (x_position, hauteur_texte))
                pygame.display.flip()
                pygame.time.wait(25)
                x_position += lettre_surface.get_width()
                for event in pygame.event.get():
                    if (event.type == KEYDOWN and event.key == K_ESCAPE) or event.type == pygame.QUIT:
                        running = False
                        pygame.quit()
                    if event.type == pygame.QUIT:
                        running = False
                        pygame.quit()
            hauteur_texte += font.get_height()
        pygame.time.wait(3000)
        from endgame_message import endgame_message
        running = False
        endgame_message()
    pygame.quit()
