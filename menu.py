from constantes import *
pygame.init()

# Constantes
menu = "images/menu_background.png"


def creation_fenetre():
    menu_background = pygame.image.load(menu).convert()
    menu_background = pygame.transform.scale(menu_background, (1920, 1080))
    screen.blit(menu_background, (0, 0))
    pygame.display.flip()

    running = True  # Variable pour contrôler la boucle principale
    while running:
        for event in pygame.event.get():
            if (event.type == KEYDOWN and event.key == K_ESCAPE) or event.type == pygame.QUIT:
                pygame.quit()
                running = False  # Quitter la boucle principale si l'utilisateur ferme la fenêtre
            if event.type == MOUSEBUTTONDOWN and event.button == 1:  # Vérifier le clic de souris
                # Récupérer les coordonnées du clic
                clic_x, clic_y = event.pos
                if 735 < clic_x < 1241 and 517 < clic_y < 773:
                    last_unlocked_lvl = -1
                    import select_lvl
                    running = False
                if 682 < clic_x < 1292 and 806 < clic_y < 1028:
                    last_unlocked_lvl = 0
                    import story_1
                    running = False


creation_fenetre()
pygame.quit()
