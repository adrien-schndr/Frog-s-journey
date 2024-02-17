from constantes import *


with open('save.txt') as load_file:
    data = json.load(load_file)
frog_skin = data['frog_skin']
last_unlocked_lvl = data['last_unlocked_lvl']


def level_6():
    start = False

    player = Frog(frog_skin)

    enemies = [
        Obstacle(0, 700, 100, 100, reverse_wooden_log_textures, -10),
        Obstacle(250, 700, 100, 100, reverse_wooden_log_textures, -10),
        Obstacle(600, 700, 100, 100, reverse_wooden_log_textures, -10),
        Obstacle(1300, 700, 100, 100, reverse_wooden_log_textures, -10),

        Obstacle(0, 800, 100, 100, wooden_log_textures, 10),
        Obstacle(250, 800, 100, 100, wooden_log_textures, 10),
        Obstacle(600, 800, 100, 100, wooden_log_textures, 10),
        Obstacle(1300, 800, 100, 100, wooden_log_textures, 10),
    ]

    physical_elements = [
        Obstacle(400, 200, 200, 200, "tiles/tree_bob", 0),
        Obstacle(0, 200, 200, 200, "tiles/tree_bob", 0),
        Obstacle(600, 200, 100, 100, "rock", 0),
        Obstacle(700, 200, 100, 100, "rock", 0),
        Obstacle(800, 200, 100, 100, "rock", 0),
        Obstacle(900, 200, 100, 100, "rock", 0),
        Obstacle(1000, 200, 100, 100, "rock", 0),
        Obstacle(1100, 200, 100, 100, "rock", 0),
        Obstacle(1200, 200, 100, 100, "rock", 0),
        Obstacle(1300, 200, 100, 100, "rock", 0),
        Obstacle(1400, 200, 100, 100, "rock", 0),
        Obstacle(1500, 200, 100, 100, "rock", 0),
        Obstacle(1600, 200, 100, 100, "rock", 0),
        Obstacle(1700, 200, 100, 100, "rock", 0),
        Obstacle(1800, 200, 100, 100, "rock", 0),
        Obstacle(1900, 200, 100, 100, "rock", 0),

        Obstacle(000, 500, 100, 100, "tiles/bush", 0),
        Obstacle(100, 500, 100, 100, "tiles/bush", 0),
        Obstacle(200, 500, 100, 100, "tiles/bush", 0),
        Obstacle(300, 500, 100, 100, "tiles/bush", 0),
        Obstacle(400, 500, 100, 100, "tiles/bush", 0),
        Obstacle(500, 500, 100, 100, "tiles/bush", 0),
        Obstacle(600, 500, 100, 100, "tiles/bush", 0),
        Obstacle(700, 500, 100, 100, "rock", 0),
        Obstacle(800, 500, 100, 100, "tiles/bush", 0),
        Obstacle(900, 500, 100, 100, "tiles/bush", 0),
        Obstacle(1000, 500, 100, 100, "rock", 0),
        Obstacle(1100, 500, 100, 100, "rock", 0),
        Obstacle(1200, 500, 100, 100, "tiles/bush", 0),
        Obstacle(1300, 500, 100, 100, "rock", 0),
        Obstacle(1600, 500, 200, 200, "tiles/tree_bob", 0),
        Obstacle(1800, 500, 100, 100, "rock", 0),
    ]

    ending_sword = Obstacle(900, 900, 100, 180, "win_sword", 0)

    enemies_group = pygame.sprite.Group(enemies)
    physical_group = pygame.sprite.Group(physical_elements)
    ending_sword = pygame.sprite.Group(ending_sword)
    # Chargement du background
    background_png = pygame.image.load("images/lvl_6_bg.png").convert_alpha()
    background_png = pygame.transform.scale(background_png, (1920, 1080))

    running = True
    while running:
        screen.blit(background_png, (0, 0))
        # Rafraichissement fen^tre
        pygame.sprite.Group(player).draw(screen)
        enemies_group.draw(screen)
        ending_sword.draw(screen)
        physical_group.draw(screen)
        pygame.display.update()
        clock.tick(50)
        enemies_group.update()

        if player.rect.x >= 1920 or player.rect.x <= -100:
            player.rect.x, player.rect.y = 910, 0

        if 0 <= player.rect.y < 100:
            player.rect.x = round(player.rect.x, -2)
        if 100 <= player.rect.y < 200:
            player.rect.x += 10
        if 200 <= player.rect.y < 300:
            player.rect.x = round(player.rect.x, -2)
        if (300 <= player.rect.y < 400 and 600 <= player.rect.x) or 400 <= player.rect.y < 500:
            player.rect.x -= 10
        if 300 <= player.rect.y < 400 and 600 > player.rect.x:
            player.rect.x = round(player.rect.x, -2)
        if 500 <= player.rect.y < 1080:
            player.rect.x = round(player.rect.x, -2)

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
            player.rect.x, player.rect.y = 900, 0
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
                data['last_unlocked_lvl'] = 7
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
