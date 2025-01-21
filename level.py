from classes.level_class import *

def level():

    with open('save.txt') as load_file:
        data = json.load(load_file)
    frog_skin = data['frog_skin']
    last_unlocked_lvl = data['last_unlocked_lvl']
    chosen_level = data["chosen_level"]

    new_level = Level(chosen_level)

    new_level.build()

    start = False
    running = True

    while running:
        new_level.scroll(start)
        # screen.blit(new_level.background, (0, 0))
        pygame.sprite.Group(new_level.player).draw(screen)
        new_level.ending_sword.draw(screen)
        new_level.enemies_group.draw(screen)
        new_level.physical_group.draw(screen)
        pygame.display.update()
        clock.tick(60)
        new_level.enemies_group.update()

        if 0 < new_level.player.rect.x >= 1920:
            new_level.player.rect.x, new_level.player.rect.y = new_level.spawn

        if new_level.water_zones:
            for water in new_level.water_zones:
                if water[1] <= new_level.player.rect.y < water[3] and water[0] <= new_level.player.rect.x < water[2]:
                    new_level.player.rect.x += water[4]
                    break

        if pygame.sprite.spritecollide(new_level.player, new_level.enemies_group, False)  or new_level.player.rect.y <= -100:
            new_level.scrolled = 0
            new_level.player.rect.x, new_level.player.rect.y = new_level.spawn
            start = False
            for enemy in new_level.enemies_group:
                enemy.rect.x, enemy.rect.y = enemy.init_position[0], enemy.init_position[1]
            for physical_object in new_level.physical_group:
                physical_object.rect.x, physical_object.rect.y = physical_object.init_position[0], physical_object.init_position[1]
            for win_sword in new_level.ending_sword:
                win_sword.rect.x, win_sword.rect.y = win_sword.init_position[0], win_sword.init_position[1]

        for event in pygame.event.get():
            if event.type == KEYDOWN and not start:
                start = True
            if (event.type == KEYDOWN and event.key == K_ESCAPE) or event.type == pygame.QUIT:
                pygame.quit()
                running = False
            if event.type == KEYDOWN:
                last_movement = new_level.player.move(event)
                if pygame.sprite.spritecollide(new_level.player, new_level.physical_group, False):
                    if last_movement == "left":
                        new_level.player.rect.x += 100
                    if last_movement == "right":
                        new_level.player.rect.x -= 100
                    if last_movement == "up":
                        new_level.player.rect.y += 100
                    if last_movement == "down":
                        new_level.player.rect.y -= 100
                new_level.player.rect.x = round(new_level.player.rect.x, -2)

            if pygame.sprite.spritecollide(new_level.player, new_level.ending_sword, False):
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
                    if new_level.level == data['last_unlocked_lvl']:
                        data['last_unlocked_lvl'] += 1
                    with open('save.txt', 'w') as store_data:
                        json.dump(data, store_data)

                    win_screen = pygame.image.load("images/win_screen.Png")
                    win_screen = pygame.transform.scale(win_screen, (1920, 1080))
                    screen.blit(win_screen, (0, 0))
                    pygame.display.update()
                    pygame.time.wait(3000)

                    if new_level.next_scene:
                        if new_level.next_scene == 5:
                            from story.story_final import story_final
                            story_final()
                        else:
                            from story.story_full import story
                            story(new_level.next_scene)
                    else:
                        from select_lvl import select_level
                        select_level()