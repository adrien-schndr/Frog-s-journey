from constantes import *


with open('save.txt') as load_file:
    data = json.load(load_file)
frog_skin = data['frog_skin']
last_unlocked_lvl = data['last_unlocked_lvl']


def level_3():
    start = False

    player = Frog(frog_skin)

    physical_elements = [
        Obstacle(500, 000, 100, 100, "tiles/bush", 7),

        Obstacle(000, 600, 100, 100, "tiles/bush", 7),
        Obstacle(1800, 600, 100, 100, "tiles/bush", 7),
        Obstacle(1200, 600, 100, 100, "tiles/bush", 7),

        Obstacle(300, 1000, 100, 100, "rock", 7),
        Obstacle(1200, 600, 200, 200, "tiles/tree_bob", 7),
    ]

    ending_sword = Obstacle(910, 900, 100, 180, "win_sword", 0)

    physical_group = pygame.sprite.Group(physical_elements)
    ending_sword = pygame.sprite.Group(ending_sword)
    # Chargement du background
    background_png = pygame.image.load("images/lvl_3_bg.png").convert_alpha()
    background_png = pygame.transform.scale(background_png, (1920, 1080))

    running = True
    while running:
        screen.blit(background_png, (0, 0))
        # Rafraichissement fen^tre
        pygame.sprite.Group(player).draw(screen)
        ending_sword.draw(screen)
        physical_group.draw(screen)
        pygame.display.update()
        clock.tick(50)

        for event in pygame.event.get():
            if event.type == KEYDOWN and not start:
                start = True
            if (event.type == KEYDOWN and event.key == K_ESCAPE) or event.type == pygame.QUIT:
                pygame.quit()
                running = False
            if event.type == KEYDOWN:
                last_movement = player.move(event)
                if pygame.sprite.spritecollide(player, physical_group, False):
                    if last_movement == "left":
                        player.rect.x += 100
                    if last_movement == "right":
                        player.rect.x -= 100
                    if last_movement == "up":
                        player.rect.y += 100
                    if last_movement == "down":
                        player.rect.y -= 100

        # Si en collision avec un obstacle                     OU               Si sors de l'écran
        if pygame.sprite.spritecollide(player, "", False):
            player.rect.x, player.rect.y = 910, 0

        if pygame.sprite.spritecollide(player, ending_sword, False):
            running = False
            if last_unlocked_lvl != -1:
                data['last_unlocked_lvl'] = 4
                with open('save.txt', 'w') as store_data:
                    json.dump(data, store_data)
            from select_lvl import select_level
            select_level()
    pygame.quit()
