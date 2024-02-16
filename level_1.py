from constantes import *


def creation_fenetre(frog_skin, screen=screen):

    pygame.init()
    clock = pygame.time.Clock()
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

    enemies_group = pygame.sprite.Group(enemies)
    physical_group = pygame.sprite.Group(physical_elements)

    # Chargement du background
    background_png = pygame.image.load("images/lvl_1_bg.png").convert_alpha()
    scroll = 0

    running = True
    while running:
        # Rafraichissement fen^tre
        screen.blit(background_png, (0, 0))
        pygame.sprite.Group(player).draw(screen)
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
