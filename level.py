from level_constructor import *

with open('save.txt') as load_file:
    data = json.load(load_file)
frog_skin = data['frog_skin']
last_unlocked_lvl = data['last_unlocked_lvl']


new_level = Level(2)

new_level.load_objects()
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