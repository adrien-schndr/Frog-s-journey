from constantes import *


with open('save.txt') as load_file:
    data = json.load(load_file)
frog_skin = data['frog_skin']
last_unlocked_lvl = data['last_unlocked_lvl']


def level_7():
    start = False

    player = Frog(frog_skin)

    enemies = [
        # Ligne 1
        Obstacle(100, 100, 200, 100, wooden_log_textures, 14),
        Obstacle(550, 100, 200, 100, wooden_log_textures, 14),
        Obstacle(1000, 100, 200, 100, wooden_log_textures, 14),
        Obstacle(1550, 100, 200, 100, wooden_log_textures, 14),

        Obstacle(100, 300, 200, 100, reverse_wooden_log_textures, -15),
        Obstacle(550, 300, 200, 100, reverse_wooden_log_textures, -15),
        Obstacle(1000, 300, 200, 100, reverse_wooden_log_textures, -15),
        Obstacle(1550, 300, 200, 100, reverse_wooden_log_textures, -15),

        Obstacle(50, 500, 200, 100, rabbit_textures, 15),
        Obstacle(150, 500, 200, 100, rabbit_textures, 15),
        Obstacle(250, 500, 200, 100, rabbit_textures, 15),
        Obstacle(350, 500, 200, 100, rabbit_textures, 15),
        Obstacle(450, 500, 200, 100, rabbit_textures, 15),
        Obstacle(550, 500, 200, 100, rabbit_textures, 15),

        Obstacle(300, 700, 200, 100, reverse_wooden_log_textures, 16),
        Obstacle(550, 700, 200, 100, reverse_wooden_log_textures, 16),
        Obstacle(1000, 700, 200, 100, reverse_wooden_log_textures, 16),
        Obstacle(1550, 700, 200, 100, reverse_wooden_log_textures, 16),
        Obstacle(1850, 700, 200, 100, reverse_wooden_log_textures, 16),

        Obstacle(300, 900, 200, 100, reverse_wooden_log_textures, -18),
        Obstacle(550, 900, 200, 100, reverse_wooden_log_textures, -18),
        Obstacle(1000, 900, 200, 100, reverse_wooden_log_textures, -18),
        Obstacle(1550, 900, 200, 100, reverse_wooden_log_textures, -18),
        Obstacle(1850, 900, 200, 100, reverse_wooden_log_textures, -18),

        Obstacle(300, 1100, 200, 100, reverse_wooden_log_textures, 12),
        Obstacle(550, 1100, 200, 100, reverse_wooden_log_textures, 12),
        Obstacle(800, 1100, 200, 100, reverse_wooden_log_textures, 12),
        Obstacle(1000, 1100, 200, 100, reverse_wooden_log_textures, 12),
        Obstacle(1550, 1100, 200, 100, reverse_wooden_log_textures, 12),
        Obstacle(1850, 1100, 200, 100, reverse_wooden_log_textures, 12),

        Obstacle(1050, 1300, 200, 100, rabbit_textures, 13),
        Obstacle(1150, 1300, 200, 100, rabbit_textures, 13),
        Obstacle(1250, 1300, 200, 100, rabbit_textures, 13),
        Obstacle(1350, 1300, 200, 100, rabbit_textures, 13),
        Obstacle(1450, 1300, 200, 100, rabbit_textures, 13),
        Obstacle(1550, 1300, 200, 100, rabbit_textures, 13),

        Obstacle(300, 1500, 200, 100, reverse_wooden_log_textures, 16),
        Obstacle(550, 1500, 200, 100, reverse_wooden_log_textures, 16),
        Obstacle(1000, 1500, 200, 100, reverse_wooden_log_textures, 16),
        Obstacle(1550, 1500, 200, 100, reverse_wooden_log_textures, 16),
        Obstacle(1850, 1500, 200, 100, reverse_wooden_log_textures, 16),

        Obstacle(300, 1700, 200, 100, reverse_wooden_log_textures, 14),
        Obstacle(550, 1700, 200, 100, reverse_wooden_log_textures, 14),
        Obstacle(1550, 1700, 200, 100, reverse_wooden_log_textures, 14),
        Obstacle(1750, 1700, 200, 100, reverse_wooden_log_textures, 14),



    ]

    physical_elements = [
        Obstacle(500, 000, 100, 100, "tiles/bush", 7),

        Obstacle(900, 400, 100, 100, "tiles/bush", 7),

        Obstacle(000, 600, 100, 100, "tiles/bush", 7),
        Obstacle(1800, 600, 100, 100, "tiles/bush", 7),
        Obstacle(1200, 600, 100, 100, "tiles/bush", 7),



        Obstacle(1500, 1200, 100, 100, "tiles/bush", 7),
    ]

    ending_sword = Obstacle(910, 1900, 100, 180, "win_sword", 0)

    enemies_group = pygame.sprite.Group(enemies)
    physical_group = pygame.sprite.Group(physical_elements)
    ending_sword = pygame.sprite.Group(ending_sword)
    # Chargement du background
    background_png = pygame.image.load("images/lvl_7_bg.png").convert_alpha()
    background_png = pygame.transform.scale(background_png, (1920, 2080))
    i = 0

    running = True
    while running:
        # Rafraichissement fen^tre
        pygame.sprite.Group(player).draw(screen)
        enemies_group.draw(screen)
        ending_sword.draw(screen)
        physical_group.draw(screen)
        pygame.display.update()
        clock.tick(50)
        enemies_group.update()

        # Défilmenet
        if start and i > -1000:
            screen.blit(background_png, (0, i))
            for enemy in enemies_group:
                enemy.rect.y -= 5
            for physical_object in physical_group:
                physical_object.rect.y -= 5
            for sword in ending_sword:
                sword.rect.y -= 5
            player.rect.y -= 5
            i -= 5
        elif start and i <= -1000:
            screen.blit(background_png, (0, i))
        else:
            screen.blit(background_png, (0, 0))

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

        # Si en collision avec un obstacle                     OU               Si sors de l'écran
        if pygame.sprite.spritecollide(player, enemies_group, False) or player.rect.y <= -100:
            i = 0
            player.rect.x, player.rect.y = 910, 0
            start = False
            for enemy in enemies_group:
                enemy.rect.x, enemy.rect.y = enemy.init_position[0], enemy.init_position[1]
            for physical_object in physical_group:
                physical_object.rect.x, physical_object.rect.y = physical_object.init_position[0], physical_object.init_position[1]
            for win_sword in ending_sword:
                win_sword.rect.x, win_sword.rect.y = win_sword.init_position[0], win_sword.init_position[1]

        if pygame.sprite.spritecollide(player, ending_sword, False):
            running = False
            if last_unlocked_lvl != -1:
                data['last_unlocked_lvl'] = 8
                with open('save.txt', 'w') as store_data:
                    json.dump(data, store_data)

            win_screen = pygame.image.load("images/win_screen.Png")
            win_screen = pygame.transform.scale(win_screen, (1920, 1080))
            screen.blit(win_screen, (0, 0))
            pygame.display.update()
            pygame.time.wait(3000)

            from select_lvl import select_level
            select_level()
    pygame.quit()
