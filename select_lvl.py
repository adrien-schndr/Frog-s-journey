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
                # NIVEAU 1
                if 207 < clic_x < 305 and 853 < clic_y < 988:
                    data['chosen_level'] = 1

                # NIVEAU 2
                if (526 < clic_x < 627 and 724 < clic_y < 854) and (last_unlocked_lvl >= 2 or last_unlocked_lvl == -1):
                    data['chosen_level'] = 2

                # NIVEAU 3
                if (689 < clic_x < 789 and 479 < clic_y < 618) and (last_unlocked_lvl >= 3 or last_unlocked_lvl == -1):
                    data['chosen_level'] = 3

                # NIVEAU 4
                if (1062 < clic_x < 1161 and 427 < clic_y < 559) and (last_unlocked_lvl >= 4 or last_unlocked_lvl == -1):
                    data['chosen_level'] = 4

                # NIVEAU 5
                if (1063 < clic_x < 1164 and 278 < clic_y < 415) and (last_unlocked_lvl >= 5 or last_unlocked_lvl == -1):
                    data['chosen_level'] = 5

                # NIVEAU 6
                if (1420 < clic_x < 1527 and 169 < clic_y < 303) and (last_unlocked_lvl >= 6 or last_unlocked_lvl == -1):
                    data['chosen_level'] = 6

                # NIVEAU 7
                if (1234 < clic_x < 1337 and 15 < clic_y < 158) and (last_unlocked_lvl >= 7 or last_unlocked_lvl == -1):
                    data['chosen_level'] = 7

                # NIVEAU 8
                if (792 < clic_x < 899 and 17 < clic_y < 156) and (last_unlocked_lvl >= 7 or last_unlocked_lvl == -1):
                    data['chosen_level'] = 8

                # NIVEAU 9
                if (466 < clic_x < 566 and 59 < clic_y < 200) and (last_unlocked_lvl >= 9 or last_unlocked_lvl == -1):
                    data['chosen_level'] = 9

                # NIVEAU 10
                if 158 < clic_x < 265 and 165 < clic_y < 303:
                    data['chosen_level'] = 0

                running = False
                with open('save.txt', 'w') as store_data:
                    json.dump(data, store_data)
                from level import level
                level()

    pygame.quit()
