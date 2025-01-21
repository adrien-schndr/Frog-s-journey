from constantes import *

class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, length, height, skin, speed):
        super().__init__()
        self.image = pygame.Surface((length, height), pygame.SRCALPHA)
        self.skin = skin
        if type(self.skin) is str:  # Non animé
            self.isAnimated = False
            skin_obstacle = pygame.image.load("images/" + self.skin + ".png").convert_alpha()
            skin_obstacle = pygame.transform.scale(skin_obstacle, (length, height))
            self.image.blit(skin_obstacle, (0, 0))
        if type(self.skin) is list:
            self.index = 0
            self.isAnimated = True
            self.images = []
            for image in skin:
                self.images.append(image)
            self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.init_position = (x, y)
        self.rect.center = (length/2, height/2)
        self.rect.x, self.rect.y = x, y
        self.dimensions = (length, height)
        self.speed = speed

    def update(self):
        self.rect.x += self.speed
        if self.rect.x >= window_length and self.speed > 0:
            self.rect.x = -self.dimensions[0]
        if self.rect.x < 0-self.dimensions[0] and self.speed < 0:
            self.rect.x = 1920
        if self.isAnimated:
            self.index += 1
            if self.index >= len(self.skin):
                self.index = 0
            self.image = self.skin[self.index]
        return
