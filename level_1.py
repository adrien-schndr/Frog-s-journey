from constantes import *


with open('save.txt') as load_file:
    data = json.load(load_file)
frog_skin = data['frog_skin']
last_unlocked_lvl = data['last_unlocked_lvl']


def level_1():

    player = Frog(frog_skin)

    # Chargement objets
    enemies = [
        Obstacle(0, 200, 200, 100, wooden_log_textures, 7.5),
        Obstacle(0, 500, 200, 100, wooden_log_textures, 9),
        Obstacle(300, 500, 200, 100, wooden_log_textures, 9),
        Obstacle(0, 600, 200, 100, wooden_log_textures, 11),
        Obstacle(400, 600, 200, 100, wooden_log_textures, 11),
        Obstacle(0, 800, 200, 100, wooden_log_textures, 5),
        Obstacle(400, 800, 200, 100, wooden_log_textures, 5),
        Obstacle(800, 800, 200, 100, wooden_log_textures, 5),
        Obstacle(1200, 800, 200, 100, wooden_log_textures, 5),
        Obstacle(1600, 800, 200, 100, wooden_log_textures, 5)
    ]

    physical_elements = [
        Obstacle(910, 400, 100, 100, "rock", 0),
        Obstacle(300, 000, 200, 200, "tiles/tree_bob", 0),
        Obstacle(1700, 300, 200, 200, "tiles/tree_bob", 0),
    ]

    ending_sword = Obstacle(910, 900, 100, 180, "win_sword", 0)

    enemies_group = pygame.sprite.Group(enemies)
    physical_group = pygame.sprite.Group(physical_elements)
    ending_sword = pygame.sprite.Group(ending_sword)
    # Chargement du background
    background_png = pygame.image.load("images/lvl_1_bg.png").convert_alpha()

    running = True
    while running:
        # Rafraichissement fen^tre
        screen.blit(background_png, (0, 0))
        pygame.sprite.Group(player).draw(screen)
        ending_sword.draw(screen)
        enemies_group.draw(screen)
        physical_group.draw(screen)
        pygame.display.update()
        clock.tick(60)
        enemies_group.update()

        if pygame.sprite.spritecollide(player, enemies_group, False):
            player.rect.x, player.rect.y = 910, 0

        # Quitter le jeu
        for event in pygame.event.get():
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

        if pygame.sprite.spritecollide(player, ending_sword, False):
            running = False
            if last_unlocked_lvl == -1:

                win_screen = pygame.image.load("images/win_screen.Png")
                win_screen = pygame.transform.scale(win_screen, (1920, 1080))
                screen.blit(win_screen, (0, 0))
                pygame.display.update()
                pygame.time.wait(3000)

                from select_lvl import select_level
                select_level()
            else:
                data['last_unlocked_lvl'] = 2
                with open('save.txt', 'w') as store_data:
                    json.dump(data, store_data)

                win_screen = pygame.image.load("images/win_screen.Png")
                win_screen = pygame.transform.scale(win_screen, (1920, 1080))
                screen.blit(win_screen, (0, 0))
                pygame.display.update()
                pygame.time.wait(3000)

                from story_full import story
                story(3)
    pygame.quit()
