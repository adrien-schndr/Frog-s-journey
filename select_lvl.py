from constantes import *
pygame.init()

# Constantes
menu = "images/level_selection_bg.png"
lock_positions = [(227, 866), (546, 743), (716, 500), (1099, 449), (1090, 287), (1453, 173), (1243, 27), (812, 27), (477, 77), (171, 175)]


def creation_fenetre():
    """ création d'une fenêtre de taille largeur x hauteur"""
    global fenetre
    fenetre = pygame.display.set_mode((1920, 1080), pygame.SCALED | pygame.FULLSCREEN)
    menu_background = pygame.image.load(menu).convert()
    menu_background = pygame.transform.scale(menu_background, (1920, 1080))
    fenetre.blit(menu_background, (0, 0))

    lock_texture = pygame.image.load("images/lock.png").convert_alpha()
    for niveau in range(last_unlocked_lvl, len(lock_positions)):
        fenetre.blit(lock_texture, lock_positions[niveau])

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


creation_fenetre()
pygame.quit()
