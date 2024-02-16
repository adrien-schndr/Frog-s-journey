from constantes import *


def creation_fenetre(frog_skin, screen=screen):
    start = False

    pygame.init()
    clock = pygame.time.Clock()
    player = Frog(frog_skin)

    enemies = [
        # Ligne 0
        Obstacle(000, 100, 200, 100, wooden_log_textures, 7),
        # Ligne 1
        Obstacle(000, 200, 200, 100, wooden_log_textures, 9),
        # Obstacle(300, 200, 200, 100, wooden_log_textures, 9),
        Obstacle(600, 200, 200, 100, wooden_log_textures, 9),
        # Obstacle(900, 200, 200, 100, wooden_log_textures, 9),
        Obstacle(1200, 200, 200, 100, wooden_log_textures, 9),
        # Obstacle(1500, 200, 200, 100, wooden_log_textures, 9),
        Obstacle(1800, 200, 200, 100, wooden_log_textures, 9),
        # Ligne 2
        Obstacle(100, 300, 200, 100, wooden_log_textures, 11),
        Obstacle(500, 300, 200, 100, wooden_log_textures, 11)

    ]

    physical_elements = [
        Obstacle(000, 600, 100, 100, "tiles/bush", 7),
    ]

    enemies_group = pygame.sprite.Group(enemies)
    physical_group = pygame.sprite.Group(physical_elements)
    # Chargement du background
    background_png = pygame.image.load("images/lvl_2_bg.png").convert_alpha()
    background_png = pygame.transform.scale(background_png, (1920, 2080))
    i = 0

    running = True
    while running:
        # Rafraichissement fen^tre
        pygame.sprite.Group(player).draw(screen)
        enemies_group.draw(screen)
        physical_group.draw(screen)
        pygame.display.update()
        clock.tick(60)
        enemies_group.update()

        # Défilmenet
        if start and i >= -1000:
            screen.blit(background_png, (0, i))
            for enemy in enemies_group:
                enemy.rect.y -= 1
            for physical_object in physical_group:
                physical_object.rect.y -= 1
            player.rect.y -= 1
            i -= 1
        elif start and i < -1000:
            screen.blit(background_png, (0, i))
        else:
            screen.blit(background_png, (0, 0))

        # Si en collision avec un obstacle                     OU               Si sors de l'écran
        if pygame.sprite.spritecollide(player, enemies_group, False) or player.rect.y <= -100:
            i = 0
            player.rect.x, player.rect.y = 910, 0
            start = False
            for enemy in enemies_group:
                enemy.rect.x, enemy.rect.y = enemy.init_position[0], enemy.init_position[1]
            for physical_object in physical_group:
                physical_object.rect.x, physical_object.rect.y = physical_object.init_position[0], physical_object.init_position[1]

        # Quitter le jeu
        for event in pygame.event.get():
            if event.type == KEYDOWN and not start:
                start = True
            if (event.type == KEYDOWN and event.key == K_ESCAPE) or event.type == pygame.QUIT:
                pygame.quit()
                running = False
            if event.type == KEYDOWN:
                last_movement = player.move(event)
                print(last_movement)
                if pygame.sprite.spritecollide(player, physical_group, False):
                    print("touché")
                    if last_movement == "left":
                        player.rect.x += 100
                    if last_movement == "right":
                        player.rect.x -= 100
                    if last_movement == "up":
                        player.rect.y += 100
                    if last_movement == "down":
                        player.rect.y -= 100


creation_fenetre("frog27")


pygame.quit()
