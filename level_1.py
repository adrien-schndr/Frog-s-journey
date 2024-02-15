from constantes import *


def creation_fenetre(frog_skin, screen=screen):

    pygame.init()
    clock = pygame.time.Clock()
    player = Frog(frog_skin)

    # Chargement objets
    rondin_bois_1 = Obstacle(0, 200, 200, 100, wooden_log_textures, 7.5)
    caillou = Obstacle(910, 400, 100, 100, "rock", 0)
    rondin_bois_2 = Obstacle(0, 500, 200, 100, wooden_log_textures, 9)
    rondin_bois_2_1 = Obstacle(300, 500, 200, 100, wooden_log_textures, 9)
    rondin_bois_3 = Obstacle(0, 600, 200, 100, wooden_log_textures, 11)
    rondin_bois_3_1 = Obstacle(400, 600, 200, 100, wooden_log_textures, 11)
    win_sword = Obstacle(910, 900, 100, 180, "win_sword", 0)
    obsctacle_group = pygame.sprite.Group(rondin_bois_1, caillou, rondin_bois_2, rondin_bois_2_1, rondin_bois_3, rondin_bois_3_1, win_sword)

    # Chargement du background
    background_png = pygame.image.load("images/lvl_1_bg.png").convert_alpha()
    scroll = 0

    running = True
    while running:
        # Rafraichissement fen^tre
        screen.blit(background_png, (0, 0))
        pygame.sprite.Group(player).draw(screen)
        obsctacle_group.draw(screen)
        pygame.display.update()
        clock.tick(60)
        obsctacle_group.update()

        if pygame.sprite.spritecollide(player, obsctacle_group, False):
            player.rect.x, player.rect.y = 910, 0

        # Quitter le jeu
        for event in pygame.event.get():
            player.move(event)
            if (event.type == KEYDOWN and event.key == K_ESCAPE) or event.type == pygame.QUIT:
                pygame.quit()
                running = False


creation_fenetre("frog27")


pygame.quit()
