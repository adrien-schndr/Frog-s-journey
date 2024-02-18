from constantes import *
pygame.init()




# Constantes


def menu():
    with open('save.txt') as load_file:
        data = json.load(load_file)
    print("Menu : ", data)
    menu = "images/menu_background.png"
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
                print(clic_x, clic_y)
                if 735 < clic_x < 1241 and 517 < clic_y < 773:
                    data['last_unlocked_lvl'] = -1
                    with open('save.txt', 'w') as store_data:
                        json.dump(data, store_data)
                    from select_lvl import select_level
                    select_level()
                    running = False
                if 682 < clic_x < 1292 and 806 < clic_y < 1028:
                    data['last_unlocked_lvl'] = 1
                    with open('save.txt', 'w') as store_data:
                        json.dump(data, store_data)
                    running = False
                    from story_full import story
                    story(1)
                if 1727 < clic_x < 1920 and 0 < clic_y < 132:
                    from skin_select import skin_select
                    skin_select()
                    running = False
    pygame.quit()