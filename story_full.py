from constantes import *


title = """LAYTON"""
story_dict = {
    "story_1": [
        """Ah voyageur intrépide, *ribbit* bienvenue dans ces contrées sylvestres. Je suis Layton,""",
        """Chef de la Guilde, gardien de ces marais ancestraux. J’entrevois dans vos yeux une lueur""",
        """de détermination et de bravoure *ribbit*. Je vous confie une quête d’une importance""",
        """capitale, même si vous ne l’avez peut être pas encore souhaitée. Vous êtes désigné pour""",
        """récupérer les dix épées légendaires, symbole de pouvoir et de savoir ancien. Je vous""",
        """servirais de guide n’ayez crainte *ribbit*. Il est maintenant l’heure pour vous """,
        """d’accomplir votre destinée. Je vous souhaite bonne chance voyageur *ribbit*."""
    ],
    "story_2": [
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
        """Faites attention aux courants, ne leur accordez pas votre confiance et sortez de """,
        """l'eau au plus vite. Soyez rapide, mais ne négligez pas la prudence.""",
        """Une fois que vous aurez atteint l'épée, votre aventure ne fera que commencer. Mais""",
        """pour cela, vous devez d'abord surmonter ce premier défi avec succès. Allez, brave""",
        """voyageur, que la chance soit avec vous."""
    ],
    "story_3": [
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
    ],
    "story_4": [
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
}

background = "images/story_screen.png"
background_game = "images/story_screen_2.png"

GAME_FONT = pygame.freetype.Font("story_font.otf", 32)
TITLE_FONT = pygame.freetype.Font("story_font.otf", 40)


def story(id_story):
    if id_story == 1:
        menu_background = pygame.image.load(background).convert()
    else:
        menu_background = pygame.image.load(background_game).convert()
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
            text_surface0, rect = GAME_FONT.render(story_dict["story_" + str(id_story)][text_number][0:longueur], (0, 0, 0))
            screen.blit(text_surface0, (150, 725))
            longueur += 1
        if longueur >= len(story_dict["story_" + str(id_story)][text_number]) and text_number < len(story_dict["story_" + str(id_story)]) - 1:
            text_number += 1
            longueur = 0
        if text_number >= 1:
            text_surface0, rect = GAME_FONT.render(story_dict["story_" + str(id_story)][text_number - 1], (0, 0, 0))
            text_surface1, rect = GAME_FONT.render(story_dict["story_" + str(id_story)][text_number][0:longueur], (0, 0, 0))
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
                    if id_story == 1:
                        story(2)
                    elif id_story == 2 or id_story == 3 or id_story == 4:
                        from select_lvl import select_level
                        select_level()
