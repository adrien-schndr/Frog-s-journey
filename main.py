from constantes import *
from pygame.locals import *


class Frog(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        skin_frog = pygame.image.load("images/green_frog.png").convert_alpha()
        skin_frog = pygame.transform.scale(skin_frog, (100, 100))
        self.image = pygame.Surface((100, 100), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.center = (50, 50)
        self.image.blit(skin_frog, (self.rect.x, self.rect.y))
        self.rect.x = 910

    def move(self, event):
        vitesse = 100

        if event.type == KEYDOWN and event.key == K_LEFT:
            if 0 <= self.rect.x - vitesse <= window_length - 100:
                self.rect.x -= vitesse
        if event.type == KEYDOWN and event.key == K_RIGHT:
            if 0 <= self.rect.x + vitesse <= window_length - 100:
                self.rect.x += vitesse
        if event.type == KEYDOWN and event.key == K_UP:
            if 0 <= self.rect.y - vitesse <= window_height - 100:
                self.rect.y -= vitesse
        if event.type == KEYDOWN and event.key == K_DOWN:
            if 0 <= self.rect.y + vitesse <= window_height - 100:
                self.rect.y += vitesse


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, length, height, skin, speed):
        super().__init__()
        self.image = pygame.Surface((length, height), pygame.SRCALPHA)
        self.skin = skin
        if type(self.skin) is str:  # Non animé
            self.isAnimated = False
            skin_obstacle = pygame.image.load("images/" + self.skin + ".png").convert_alpha()
            skin_obstacle = pygame.transform.scale(skin_obstacle, (length, height))
            self.image.blit(skin_obstacle, (0, 0))
            self.rect = self.image.get_rect()
            self.rect.center = (length/2, height/2)
            self.rect.x, self.rect.y = x, y
            self.dimensions = (length, height)
            self.speed = speed
        if type(self.skin) is list:
            self.index = 0
            self.isAnimated = True
            self.images = []
            for image in skin:
                self.images.append(image)
            self.index = 0
            self.image = self.images[self.index]
            self.rect = self.image.get_rect()
            self.rect.center = (length/2, height/2)
            self.rect.x, self.rect.y = x, y
            self.dimensions = (length, height)
            self.speed = speed

    def update(self):
        self.rect.x += self.speed
        if self.rect.x >= window_length:
            self.rect.x = -self.dimensions[0]
        if self.isAnimated:
            self.index += 1

            if self.index >= len(self.skin):
                self.index = 0

            self.image = self.skin[self.index]

        return


pygame.init()
clock = pygame.time.Clock()

player = Frog()

rondin_bois = Obstacle(0, 200, 200, 100, wooden_log_textures, 10)
obsctacle_group = pygame.sprite.Group(rondin_bois)


# Chargement du background
background_png = pygame.image.load("images/background.png").convert_alpha()
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

pygame.quit()
