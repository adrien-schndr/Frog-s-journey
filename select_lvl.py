from constantes import *

pygame.init()
clock = pygame.time.Clock()


def select_level():
    menu = "images/level_selection_bg.png"
    lock_positions = [(582, 805), (582, 801), (747, 563), (1123, 511), (1122, 360), (1485, 243), (1296, 97), (856, 97),
                      (525, 137), (221, 248)]

    with open('save.txt') as load_file:
        data = json.load(load_file)
    last_unlocked_lvl = data['last_unlocked_lvl']
    print(data)
    print(last_unlocked_lvl)

    menu_background = pygame.image.load(menu).convert()
    menu_background = pygame.transform.scale(menu_background, (1920, 1080))
    screen.blit(menu_background, (0, 0))

    lock_texture = pygame.image.load("images/lock.png").convert_alpha()
    lock_texture = pygame.transform.scale(lock_texture, (25, 40))
    if last_unlocked_lvl != -1:
        for niveau in range(last_unlocked_lvl, len(lock_positions)):
            screen.blit(lock_texture, lock_positions[niveau])

    pygame.display.flip()

    running = True  # Variable pour contrôler la boucle principale
    while running:
        # screen.blit(menu_background, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if (event.type == KEYDOWN and event.key == K_ESCAPE) or event.type == pygame.QUIT:
                pygame.quit()
                running = False  # Quitter la boucle principale si l'utilisateur ferme la fenêtre
            if event.type == MOUSEBUTTONDOWN and event.button == 1:  # Vérifier le clic de souris
                # Récupérer les coordonnées du clic
                clic_x, clic_y = event.pos
                print(clic_x, clic_y)
                # NIVEAU 1
                if 207 < clic_x < 305 and 853 < clic_y < 988:
                    from level_1 import level_1
                    level_1()
                    running = False

                # NIVEAU 2
                if (526 < clic_x < 627 and 724 < clic_y < 854) and (last_unlocked_lvl >= 2 or last_unlocked_lvl == -1):
                    from level_2 import level_2
                    level_2()
                    running = False

                # NIVEAU 3
                if (689 < clic_x < 789 and 479 < clic_y < 618) and (last_unlocked_lvl >= 3 or last_unlocked_lvl == -1):
                    from level_3 import level_3
                    level_3()
                    running = False

                # NIVEAU 4
                if (1062 < clic_x < 1161 and 427 < clic_y < 559) and (last_unlocked_lvl >= 4 or last_unlocked_lvl == -1):
                    from level_4 import level_4
                    level_4()
                    running = False

                # ENDGAME
                if 158 < clic_x < 265 and 165 < clic_y < 303:
                    from story_final import story_final
                    story_final()
                    running = False


    pygame.quit()
